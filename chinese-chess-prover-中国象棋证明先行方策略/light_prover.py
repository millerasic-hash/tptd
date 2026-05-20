#!/usr/bin/env python3
"""Lightweight Xiangqi proof search with optional Pikafish move ordering.

This is intentionally small and conservative:
- the built-in verifier is independent of Pikafish;
- Pikafish scores are used only to order moves;
- a WIN/LOSS result is emitted only when the bounded proof tree closes.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


START_FEN = (
    "rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/"
    "P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1"
)

RED = "w"
BLACK = "b"
WIN = "WIN"
LOSS = "LOSS"
UNKNOWN = "UNKNOWN"
INF = 1_000_000_000

FILES = "abcdefghi"
RED_PALACE = {(r, c) for r in range(7, 10) for c in range(3, 6)}
BLACK_PALACE = {(r, c) for r in range(0, 3) for c in range(3, 6)}
ELEPHANT_EYES = {
    (-2, -2): (-1, -1),
    (-2, 2): (-1, 1),
    (2, -2): (1, -1),
    (2, 2): (1, 1),
}
HORSE_LEGS = {
    (-2, -1): (-1, 0),
    (-2, 1): (-1, 0),
    (2, -1): (1, 0),
    (2, 1): (1, 0),
    (-1, -2): (0, -1),
    (1, -2): (0, -1),
    (-1, 2): (0, 1),
    (1, 2): (0, 1),
}


def side_of(piece: str) -> str:
    return RED if piece.isupper() else BLACK


def opposite(side: str) -> str:
    return BLACK if side == RED else RED


def canon_piece(piece: str) -> str:
    table = {"H": "N", "E": "B", "h": "n", "e": "b"}
    return table.get(piece, piece)


def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < 10 and 0 <= c < 9


def coord_to_square(coord: str) -> Tuple[int, int]:
    if len(coord) != 2 or coord[0] not in FILES or coord[1] not in "0123456789":
        raise ValueError(f"bad coordinate: {coord}")
    return 9 - int(coord[1]), FILES.index(coord[0])


def square_to_coord(square: Tuple[int, int]) -> str:
    r, c = square
    return FILES[c] + str(9 - r)


@dataclass(frozen=True)
class Move:
    src: Tuple[int, int]
    dst: Tuple[int, int]

    @classmethod
    def from_uci(cls, text: str) -> "Move":
        if len(text) != 4:
            raise ValueError(f"bad move: {text}")
        return cls(coord_to_square(text[:2]), coord_to_square(text[2:]))

    def uci(self) -> str:
        return square_to_coord(self.src) + square_to_coord(self.dst)


class Board:
    def __init__(self, grid: Sequence[Sequence[str]], side: str):
        self.grid = tuple(tuple(row) for row in grid)
        self.side = side

    @classmethod
    def from_fen(cls, fen: str) -> "Board":
        parts = fen.strip().split()
        if not parts:
            raise ValueError("empty FEN")
        rows = parts[0].split("/")
        if len(rows) != 10:
            raise ValueError("Xiangqi FEN must contain 10 rows")

        grid: List[List[str]] = []
        for raw in rows:
            row: List[str] = []
            for ch in raw:
                if ch.isdigit():
                    row.extend("." for _ in range(int(ch)))
                else:
                    row.append(canon_piece(ch))
            if len(row) != 9:
                raise ValueError(f"bad row width in FEN row {raw!r}")
            grid.append(row)

        side = parts[1] if len(parts) > 1 else RED
        if side not in (RED, BLACK):
            raise ValueError("side to move must be w or b")
        return cls(grid, side)

    def to_fen(self) -> str:
        rows = []
        for row in self.grid:
            out = []
            empty = 0
            for piece in row:
                if piece == ".":
                    empty += 1
                else:
                    if empty:
                        out.append(str(empty))
                        empty = 0
                    out.append(piece)
            if empty:
                out.append(str(empty))
            rows.append("".join(out))
        return "/".join(rows) + f" {self.side} - - 0 1"

    def key(self) -> str:
        return self.to_fen().split(" - - ")[0]

    def piece_at(self, square: Tuple[int, int]) -> str:
        r, c = square
        return self.grid[r][c]

    def locate_king(self, side: str) -> Optional[Tuple[int, int]]:
        target = "K" if side == RED else "k"
        for r in range(10):
            for c in range(9):
                if self.grid[r][c] == target:
                    return r, c
        return None

    def make_move(self, move: Move) -> "Board":
        sr, sc = move.src
        dr, dc = move.dst
        piece = self.grid[sr][sc]
        if piece == ".":
            raise ValueError(f"empty source square: {move.uci()}")
        new_grid = [list(row) for row in self.grid]
        new_grid[dr][dc] = piece
        new_grid[sr][sc] = "."
        return Board(new_grid, opposite(self.side))

    def legal_moves(self, side: Optional[str] = None) -> List[Move]:
        side = side or self.side
        moves: List[Move] = []
        for move in self.pseudo_moves(side):
            child = self.make_move(move)
            if not child.in_check(side):
                moves.append(move)
        return moves

    def in_check(self, side: str) -> bool:
        king = self.locate_king(side)
        if king is None:
            return True
        return self.square_attacked_by(king, opposite(side))

    def is_terminal_loss(self) -> bool:
        return len(self.legal_moves(self.side)) == 0

    def square_attacked_by(self, square: Tuple[int, int], attacker: str) -> bool:
        for move in self.pseudo_moves(attacker, attacks_only=True):
            if move.dst == square:
                return True
        return False

    def pseudo_moves(self, side: str, attacks_only: bool = False) -> Iterable[Move]:
        for r in range(10):
            for c in range(9):
                piece = self.grid[r][c]
                if piece == "." or side_of(piece) != side:
                    continue
                kind = piece.upper()
                if kind == "K":
                    generated = self._king_moves(r, c, side, attacks_only)
                elif kind == "A":
                    generated = self._advisor_moves(r, c, side)
                elif kind == "B":
                    generated = self._elephant_moves(r, c, side)
                elif kind == "N":
                    generated = self._horse_moves(r, c, side)
                elif kind == "R":
                    generated = self._rook_moves(r, c, side)
                elif kind == "C":
                    generated = self._cannon_moves(r, c, side)
                elif kind == "P":
                    generated = self._pawn_moves(r, c, side)
                else:
                    continue

                for move in generated:
                    target = self.piece_at(move.dst)
                    if not attacks_only and target.upper() == "K":
                        continue
                    yield move

    def _can_land(self, r: int, c: int, side: str) -> bool:
        return in_bounds(r, c) and (self.grid[r][c] == "." or side_of(self.grid[r][c]) != side)

    def _king_moves(self, r: int, c: int, side: str, attacks_only: bool) -> Iterable[Move]:
        palace = RED_PALACE if side == RED else BLACK_PALACE
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if (nr, nc) in palace and self._can_land(nr, nc, side):
                yield Move((r, c), (nr, nc))

        # Flying general is an attack relation. It is not emitted as an ordinary
        # legal move because kings are never removed from a proof position.
        if not attacks_only:
            return
        step = -1 if side == RED else 1
        nr = r + step
        while in_bounds(nr, c):
            piece = self.grid[nr][c]
            if piece != ".":
                if piece.upper() == "K" and side_of(piece) != side:
                    yield Move((r, c), (nr, c))
                break
            nr += step

    def _advisor_moves(self, r: int, c: int, side: str) -> Iterable[Move]:
        palace = RED_PALACE if side == RED else BLACK_PALACE
        for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            nr, nc = r + dr, c + dc
            if (nr, nc) in palace and self._can_land(nr, nc, side):
                yield Move((r, c), (nr, nc))

    def _elephant_moves(self, r: int, c: int, side: str) -> Iterable[Move]:
        for (dr, dc), eye in ELEPHANT_EYES.items():
            nr, nc = r + dr, c + dc
            er, ec = r + eye[0], c + eye[1]
            if not in_bounds(nr, nc) or self.grid[er][ec] != ".":
                continue
            if side == RED and nr < 5:
                continue
            if side == BLACK and nr > 4:
                continue
            if self._can_land(nr, nc, side):
                yield Move((r, c), (nr, nc))

    def _horse_moves(self, r: int, c: int, side: str) -> Iterable[Move]:
        for (dr, dc), leg in HORSE_LEGS.items():
            nr, nc = r + dr, c + dc
            lr, lc = r + leg[0], c + leg[1]
            if in_bounds(nr, nc) and self.grid[lr][lc] == "." and self._can_land(nr, nc, side):
                yield Move((r, c), (nr, nc))

    def _rook_moves(self, r: int, c: int, side: str) -> Iterable[Move]:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            while in_bounds(nr, nc):
                piece = self.grid[nr][nc]
                if piece == ".":
                    yield Move((r, c), (nr, nc))
                else:
                    if side_of(piece) != side:
                        yield Move((r, c), (nr, nc))
                    break
                nr += dr
                nc += dc

    def _cannon_moves(self, r: int, c: int, side: str) -> Iterable[Move]:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            seen_screen = False
            while in_bounds(nr, nc):
                piece = self.grid[nr][nc]
                if not seen_screen:
                    if piece == ".":
                        yield Move((r, c), (nr, nc))
                    else:
                        seen_screen = True
                else:
                    if piece != ".":
                        if side_of(piece) != side:
                            yield Move((r, c), (nr, nc))
                        break
                nr += dr
                nc += dc

    def _pawn_moves(self, r: int, c: int, side: str) -> Iterable[Move]:
        steps = [(-1, 0)] if side == RED else [(1, 0)]
        crossed = r <= 4 if side == RED else r >= 5
        if crossed:
            steps.extend([(0, -1), (0, 1)])
        for dr, dc in steps:
            nr, nc = r + dr, c + dc
            if self._can_land(nr, nc, side):
                yield Move((r, c), (nr, nc))


class Pikafish:
    def __init__(
        self,
        path: str,
        movetime_ms: int = 100,
        depth: int = 0,
        cwd: Optional[str] = None,
    ):
        self.path = path
        self.movetime_ms = movetime_ms
        self.depth = depth
        self.path = os.path.abspath(path)
        self.cwd = os.path.abspath(cwd or os.getcwd())
        self.proc = subprocess.Popen(
            [self.path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            bufsize=1,
            cwd=self.cwd,
        )
        self._send("uci")
        self._read_until("uciok", timeout=10)
        self._send("isready")
        self._read_until("readyok", timeout=10)

    def close(self) -> None:
        if self.proc.poll() is None:
            try:
                self._send("quit")
            except BrokenPipeError:
                pass
            self.proc.terminate()

    def _send(self, command: str) -> None:
        assert self.proc.stdin is not None
        self.proc.stdin.write(command + "\n")
        self.proc.stdin.flush()

    def _read_until(self, marker: str, timeout: float) -> List[str]:
        assert self.proc.stdout is not None
        end = time.time() + timeout
        lines: List[str] = []
        while time.time() < end:
            line = self.proc.stdout.readline()
            if not line:
                break
            line = line.strip()
            lines.append(line)
            if line.startswith(marker):
                break
        return lines

    def analyze(self, fen: str) -> Tuple[List[str], Optional[int], Optional[int]]:
        self._send(f"position fen {fen}")
        if self.depth > 0:
            self._send(f"go depth {self.depth}")
        else:
            self._send(f"go movetime {self.movetime_ms}")

        bestmove: Optional[str] = None
        cp: Optional[int] = None
        mate: Optional[int] = None
        lines = self._read_until("bestmove", timeout=max(10, self.movetime_ms / 1000 + 5))
        pv: List[str] = []
        for line in lines:
            parts = line.split()
            if len(parts) >= 2 and parts[0] == "bestmove":
                bestmove = parts[1]
            if parts[:2] == ["info", "depth"] and "score" in parts:
                idx = parts.index("score")
                if idx + 2 < len(parts):
                    if parts[idx + 1] == "cp":
                        cp = int(parts[idx + 2])
                        mate = None
                    elif parts[idx + 1] == "mate":
                        mate = int(parts[idx + 2])
                        cp = None
                if "pv" in parts:
                    pv = parts[parts.index("pv") + 1 :]
        ordered = []
        if bestmove and bestmove != "(none)":
            ordered.append(bestmove)
        ordered.extend(m for m in pv if m not in ordered)
        return ordered, cp, mate


@dataclass
class ProofResult:
    status: str
    node_count: int
    proof: Optional[dict]
    pn: int = 1
    dn: int = 1


class Prover:
    def __init__(self, engine: Optional[Pikafish] = None):
        self.engine = engine
        self.memo: Dict[Tuple[str, int], ProofResult] = {}
        self.nodes = 0

    def prove(self, board: Board, depth: int) -> ProofResult:
        self.nodes += 1
        key = (board.key(), depth)
        if key in self.memo:
            result = self.memo[key]
            return ProofResult(result.status, 1, {"ref": board.key(), "status": result.status})

        legal = board.legal_moves()
        if not legal:
            proof = {
                "fen": board.to_fen(),
                "side": board.side,
                "status": LOSS,
                "terminal": "no_legal_moves",
            }
            result = ProofResult(LOSS, 1, proof)
            self.memo[key] = result
            return result

        if depth <= 0:
            return ProofResult(UNKNOWN, 1, None)

        ordered = self.order_moves(board, legal)
        unknown_seen = False
        child_proofs = []

        for move in ordered:
            child = board.make_move(move)
            child_result = self.prove(child, depth - 1)
            if child_result.status == LOSS:
                proof = {
                    "fen": board.to_fen(),
                    "side": board.side,
                    "status": WIN,
                    "witness": move.uci(),
                    "child": child_result.proof,
                }
                result = ProofResult(WIN, child_result.node_count + 1, proof)
                self.memo[key] = result
                return result
            if child_result.status == UNKNOWN:
                unknown_seen = True
            else:
                child_proofs.append({"move": move.uci(), "child": child_result.proof})

        if unknown_seen:
            return ProofResult(UNKNOWN, 1, None)

        proof = {
            "fen": board.to_fen(),
            "side": board.side,
            "status": LOSS,
            "all_moves": child_proofs,
        }
        result = ProofResult(LOSS, len(child_proofs) + 1, proof)
        self.memo[key] = result
        return result

    def order_moves(self, board: Board, legal: List[Move]) -> List[Move]:
        if not self.engine:
            return sorted(legal, key=lambda m: m.uci())

        try:
            engine_moves, _cp, _mate = self.engine.analyze(board.to_fen())
        except Exception:
            return sorted(legal, key=lambda m: m.uci())

        legal_by_uci = {m.uci(): m for m in legal}
        ordered: List[Move] = []
        for text in engine_moves:
            if text in legal_by_uci and legal_by_uci[text] not in ordered:
                ordered.append(legal_by_uci[text])
        ordered.extend(m for m in sorted(legal, key=lambda x: x.uci()) if m not in ordered)
        return ordered


def legal_nonrepeat_moves(
    board: Board, history: Dict[str, int], repetition_limit: int
) -> Tuple[List[Move], List[Move]]:
    legal = board.legal_moves()
    if repetition_limit <= 0:
        return legal, []

    allowed: List[Move] = []
    blocked: List[Move] = []
    for move in legal:
        child = board.make_move(move)
        if history.get(child.key(), 0) >= repetition_limit:
            blocked.append(move)
        else:
            allowed.append(move)
    return allowed, blocked


def history_signature(history: Dict[str, int], repetition_limit: int) -> Tuple[Tuple[str, int], ...]:
    if repetition_limit <= 0:
        return ()
    return tuple(sorted((key, min(count, repetition_limit)) for key, count in history.items()))


def saturated_sum(values: Iterable[int]) -> int:
    total = 0
    for value in values:
        total += value
        if total >= INF:
            return INF
    return total


def score_to_scalar(cp: Optional[int], mate: Optional[int]) -> Optional[int]:
    if mate is not None:
        return 100_000 if mate > 0 else -100_000
    return cp


def score_to_proof_cost(cp: Optional[int], mate: Optional[int]) -> Tuple[int, int]:
    """Convert an engine score into proof/disproof priors.

    This is only a search-order heuristic. It is not a proof rule.
    Positive scores are treated as easier to prove for side-to-move.
    """

    if mate is not None:
        return (1, INF // 4) if mate > 0 else (INF // 4, 1)
    if cp is None:
        return 1000, 1000

    bounded = max(-3000, min(3000, cp))
    if bounded >= 0:
        return max(1, 1000 - bounded // 2), min(INF // 4, 1000 + bounded // 2)
    return min(INF // 4, 1000 + (-bounded) // 2), max(1, 1000 - (-bounded) // 2)


class DfpnProver:
    """Bounded proof-number search with GHI-safe transpositions.

    The node property is "the side to move is winning".
    For a node N and child C:
    - proving N as WIN requires disproving at least one child C;
    - disproving N requires proving all children C.

    Pikafish, when present, is used only for priors and move ordering.
    """

    def __init__(
        self,
        engine: Optional[Pikafish] = None,
        max_nodes: int = 100_000,
        repetition_limit: int = 2,
    ):
        self.engine = engine
        self.max_nodes = max_nodes
        self.repetition_limit = repetition_limit
        self.nodes = 0
        self.tt: Dict[Tuple[str, int, Tuple[Tuple[str, int], ...]], ProofResult] = {}
        self.tt_hits = 0

    def prove(self, board: Board, depth: int) -> ProofResult:
        history = {board.key(): 1}
        return self._search(board, depth, history)

    def _search(self, board: Board, depth: int, history: Dict[str, int]) -> ProofResult:
        self.nodes += 1
        key = (board.key(), depth, history_signature(history, self.repetition_limit))
        if key in self.tt:
            self.tt_hits += 1
            return self.tt[key]

        allowed, blocked = legal_nonrepeat_moves(board, history, self.repetition_limit)
        if not allowed:
            terminal = "no_legal_moves" if not board.legal_moves() else "no_legal_nonrepeat_moves"
            proof = {
                "fen": board.to_fen(),
                "side": board.side,
                "status": LOSS,
                "terminal": terminal,
            }
            if blocked:
                proof["blocked_repetitions"] = [move.uci() for move in blocked]
            result = ProofResult(LOSS, 1, proof, pn=INF, dn=0)
            self.tt[key] = result
            return result

        if depth <= 0 or self.nodes >= self.max_nodes:
            cp = mate = None
            ordered_uci: List[str] = []
            if self.engine:
                try:
                    ordered_uci, cp, mate = self.engine.analyze(board.to_fen())
                except Exception:
                    ordered_uci = []
            pn, dn = score_to_proof_cost(cp, mate)
            proof = {
                "fen": board.to_fen(),
                "side": board.side,
                "status": UNKNOWN,
                "reason": "depth_limit" if depth <= 0 else "node_limit",
                "engine_score_cp": cp,
                "engine_score_mate": mate,
                "engine_order": ordered_uci[:8],
                "pn": pn,
                "dn": dn,
            }
            return ProofResult(UNKNOWN, 1, proof, pn=pn, dn=dn)

        ordered = self.order_moves(board, allowed)
        child_results: List[Tuple[Move, ProofResult]] = []
        unknown_seen = False

        for move in ordered:
            child = board.make_move(move)
            child_key = child.key()
            history[child_key] = history.get(child_key, 0) + 1
            child_result = self._search(child, depth - 1, history)
            if history[child_key] == 1:
                del history[child_key]
            else:
                history[child_key] -= 1

            child_results.append((move, child_result))

            # OR node: one disproved child is a proof for the current node.
            if child_result.dn == 0:
                proof = {
                    "fen": board.to_fen(),
                    "side": board.side,
                    "status": WIN,
                    "witness": move.uci(),
                    "child": child_result.proof,
                    "pn": 0,
                    "dn": INF,
                }
                result = ProofResult(WIN, child_result.node_count + 1, proof, pn=0, dn=INF)
                self.tt[key] = result
                return result

            if child_result.status == UNKNOWN:
                unknown_seen = True

            if self.nodes >= self.max_nodes:
                unknown_seen = True
                break

        if not unknown_seen and len(child_results) == len(ordered):
            # AND side of the recurrence: every legal child is WIN for opponent.
            if all(child.pn == 0 for _move, child in child_results):
                proof = {
                    "fen": board.to_fen(),
                    "side": board.side,
                    "status": LOSS,
                    "all_moves": [
                        {"move": move.uci(), "child": child.proof} for move, child in child_results
                    ],
                    "pn": INF,
                    "dn": 0,
                }
                result = ProofResult(LOSS, len(child_results) + 1, proof, pn=INF, dn=0)
                self.tt[key] = result
                return result

        pn_candidates = [child.dn for _move, child in child_results]
        dn_terms = [child.pn for _move, child in child_results]
        unexplored = max(0, len(ordered) - len(child_results))
        pn = min(pn_candidates) if pn_candidates else 1
        dn = saturated_sum(dn_terms + [1000] * unexplored)
        proof = {
            "fen": board.to_fen(),
            "side": board.side,
            "status": UNKNOWN,
            "reason": "open_frontier",
            "searched_children": [
                {
                    "move": move.uci(),
                    "status": child.status,
                    "pn": child.pn,
                    "dn": child.dn,
                }
                for move, child in child_results
            ],
            "unsearched_child_count": unexplored,
            "pn": pn,
            "dn": dn,
        }
        result = ProofResult(UNKNOWN, len(child_results) + 1, proof, pn=pn, dn=dn)
        self.tt[key] = result
        return result

    def order_moves(self, board: Board, legal: List[Move]) -> List[Move]:
        legal_by_uci = {move.uci(): move for move in legal}
        ranked: List[Move] = []
        if self.engine:
            try:
                engine_moves, _cp, _mate = self.engine.analyze(board.to_fen())
            except Exception:
                engine_moves = []
            for text in engine_moves:
                move = legal_by_uci.get(text)
                if move and move not in ranked:
                    ranked.append(move)

        captures = []
        quiets = []
        for move in legal:
            if move in ranked:
                continue
            target = board.piece_at(move.dst)
            (captures if target != "." else quiets).append(move)
        captures.sort(key=lambda m: m.uci())
        quiets.sort(key=lambda m: m.uci())
        return ranked + captures + quiets


def verify_proof(
    proof: dict,
    history: Optional[Dict[str, int]] = None,
    repetition_limit: int = 2,
) -> None:
    board = Board.from_fen(proof["fen"])
    status = proof["status"]
    if history is None:
        history = {board.key(): 1}
    allowed, blocked = legal_nonrepeat_moves(board, history, repetition_limit)

    if status == LOSS:
        if "terminal" in proof:
            terminal = proof["terminal"]
            if terminal == "no_legal_moves" and board.legal_moves():
                raise ValueError("terminal LOSS proof has legal moves")
            if terminal == "no_legal_nonrepeat_moves" and allowed:
                raise ValueError("terminal LOSS proof has legal non-repeating moves")
            return
        covered = {item["move"] for item in proof.get("all_moves", [])}
        legal_moves = {m.uci() for m in allowed}
        if covered != legal_moves:
            missing = sorted(legal_moves - covered)
            extra = sorted(covered - legal_moves)
            raise ValueError(f"LOSS proof move coverage mismatch missing={missing} extra={extra}")
        for item in proof["all_moves"]:
            child = board.make_move(Move.from_uci(item["move"]))
            child_proof = item["child"]
            if Board.from_fen(child_proof["fen"]).key() != child.key():
                raise ValueError(f"child FEN mismatch after {item['move']}")
            child_key = child.key()
            history[child_key] = history.get(child_key, 0) + 1
            verify_proof(child_proof, history, repetition_limit)
            if history[child_key] == 1:
                del history[child_key]
            else:
                history[child_key] -= 1
            if child_proof["status"] != WIN:
                raise ValueError("LOSS child must be WIN")
        return

    if status == WIN:
        move = Move.from_uci(proof["witness"])
        if move not in allowed:
            raise ValueError(f"illegal witness move: {move.uci()}")
        child = board.make_move(move)
        child_proof = proof["child"]
        if Board.from_fen(child_proof["fen"]).key() != child.key():
            raise ValueError(f"child FEN mismatch after witness {move.uci()}")
        child_key = child.key()
        history[child_key] = history.get(child_key, 0) + 1
        verify_proof(child_proof, history, repetition_limit)
        if history[child_key] == 1:
            del history[child_key]
        else:
            history[child_key] -= 1
        if child_proof["status"] != LOSS:
            raise ValueError("WIN witness child must be LOSS")
        return

    raise ValueError(f"unsupported proof status: {status}")


def command_prove(args: argparse.Namespace) -> int:
    board = Board.from_fen(args.fen)
    engine = None
    if args.engine:
        engine = Pikafish(
            args.engine,
            movetime_ms=args.movetime,
            depth=args.engine_depth,
            cwd=args.engine_cwd,
        )
    try:
        if args.method == "dfs":
            prover = Prover(engine)
            result = prover.prove(board, args.depth)
            tt_hits = 0
        else:
            prover = DfpnProver(
                engine,
                max_nodes=args.max_nodes,
                repetition_limit=args.repetition_limit,
            )
            result = prover.prove(board, args.depth)
            tt_hits = prover.tt_hits
    finally:
        if engine:
            engine.close()

    output = {
        "fen": board.to_fen(),
        "method": args.method,
        "depth": args.depth,
        "max_nodes": args.max_nodes,
        "repetition_limit": args.repetition_limit,
        "status": result.status,
        "pn": result.pn,
        "dn": result.dn,
        "searched_nodes": prover.nodes,
        "tt_hits": tt_hits,
        "proof": result.proof,
    }
    text = json.dumps(output, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    else:
        print(text)
    return 0


def command_verify(args: argparse.Namespace) -> int:
    with open(args.proof, "r", encoding="utf-8") as f:
        data = json.load(f)
    proof = data.get("proof", data)
    if not proof:
        raise ValueError("no proof found")
    verify_proof(proof, repetition_limit=args.repetition_limit)
    print("OK")
    return 0


def command_moves(args: argparse.Namespace) -> int:
    board = Board.from_fen(args.fen)
    moves = [m.uci() for m in board.legal_moves()]
    print(json.dumps({"fen": board.to_fen(), "legal_count": len(moves), "moves": moves}, indent=2))
    return 0


def threshold_report(records: List[dict], min_samples: int = 1) -> dict:
    usable = [
        r
        for r in records
        if r.get("score_scalar") is not None and r.get("status") in {WIN, LOSS, UNKNOWN}
    ]
    usable.sort(key=lambda r: r["score_scalar"], reverse=True)

    candidates = sorted({r["score_scalar"] for r in usable}, reverse=True)
    threshold = None
    for candidate in candidates:
        above = [r for r in usable if r["score_scalar"] >= candidate]
        if len(above) < min_samples:
            continue
        if all(r["status"] == WIN for r in above):
            threshold = candidate
        else:
            break

    bins = []
    for lower in [-100_000, -2000, -1000, -500, -200, 0, 200, 500, 1000, 2000]:
        upper = lower + 200 if lower < 0 else lower + 500
        if lower == -100_000:
            upper = -2000
        group = [r for r in usable if lower <= r["score_scalar"] < upper]
        if group:
            bins.append(
                {
                    "range": [lower, upper],
                    "count": len(group),
                    "win": sum(1 for r in group if r["status"] == WIN),
                    "loss": sum(1 for r in group if r["status"] == LOSS),
                    "unknown": sum(1 for r in group if r["status"] == UNKNOWN),
                }
            )

    return {
        "sample_count": len(usable),
        "threshold_all_above_proven_win": threshold,
        "min_samples": min_samples,
        "bins": bins,
        "warning": (
            "This threshold is sample/resource bounded. It is not a theorem about all Xiangqi positions."
        ),
    }


def command_calibrate(args: argparse.Namespace) -> int:
    if not args.engine:
        raise ValueError("calibrate requires --engine")
    with open(args.positions, "r", encoding="utf-8") as f:
        positions = [
            line.strip()
            for line in f
            if line.strip() and not line.lstrip().startswith("#")
        ]

    engine = Pikafish(
        args.engine,
        movetime_ms=args.movetime,
        depth=args.engine_depth,
        cwd=args.engine_cwd,
    )
    records = []
    try:
        for index, fen in enumerate(positions, 1):
            board = Board.from_fen(fen)
            _moves, cp, mate = engine.analyze(board.to_fen())
            prover = DfpnProver(
                engine if args.engine_order else None,
                max_nodes=args.max_nodes,
                repetition_limit=args.repetition_limit,
            )
            result = prover.prove(board, args.depth)
            records.append(
                {
                    "index": index,
                    "fen": board.to_fen(),
                    "score_cp": cp,
                    "score_mate": mate,
                    "score_scalar": score_to_scalar(cp, mate),
                    "status": result.status,
                    "pn": result.pn,
                    "dn": result.dn,
                    "searched_nodes": prover.nodes,
                    "tt_hits": prover.tt_hits,
                }
            )
    finally:
        engine.close()

    output = {
        "method": "pikafish-guided-dfpn-calibration",
        "depth": args.depth,
        "max_nodes": args.max_nodes,
        "repetition_limit": args.repetition_limit,
        "engine_depth": args.engine_depth,
        "movetime": args.movetime,
        "report": threshold_report(records, args.min_samples),
        "records": records,
    }
    text = json.dumps(output, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    else:
        print(text)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lightweight Xiangqi proof helper")
    sub = parser.add_subparsers(dest="command", required=True)

    prove = sub.add_parser("prove", help="bounded proof search")
    prove.add_argument("--fen", default=START_FEN)
    prove.add_argument("--depth", type=int, required=True, help="remaining plies to prove")
    prove.add_argument("--method", choices=["dfpn", "dfs"], default="dfpn")
    prove.add_argument("--max-nodes", type=int, default=100_000)
    prove.add_argument("--repetition-limit", type=int, default=2)
    prove.add_argument("--engine", help="optional Pikafish executable path for move ordering")
    prove.add_argument("--engine-cwd", help="working directory for Pikafish, usually where pikafish.nnue lives")
    prove.add_argument("--movetime", type=int, default=100, help="Pikafish movetime in ms")
    prove.add_argument("--engine-depth", type=int, default=0, help="Pikafish depth; overrides movetime")
    prove.add_argument("--output")
    prove.set_defaults(func=command_prove)

    verify = sub.add_parser("verify", help="verify a proof certificate")
    verify.add_argument("proof")
    verify.add_argument("--repetition-limit", type=int, default=2)
    verify.set_defaults(func=command_verify)

    moves = sub.add_parser("moves", help="list legal moves")
    moves.add_argument("--fen", default=START_FEN)
    moves.set_defaults(func=command_moves)

    calibrate = sub.add_parser("calibrate", help="calibrate score threshold on a fixed sample")
    calibrate.add_argument("positions", help="newline-delimited FEN file")
    calibrate.add_argument("--engine", required=True, help="Pikafish executable path")
    calibrate.add_argument("--engine-cwd", help="working directory for Pikafish, usually where pikafish.nnue lives")
    calibrate.add_argument("--depth", type=int, required=True, help="proof depth in plies")
    calibrate.add_argument("--max-nodes", type=int, default=100_000)
    calibrate.add_argument("--repetition-limit", type=int, default=2)
    calibrate.add_argument("--movetime", type=int, default=100)
    calibrate.add_argument("--engine-depth", type=int, default=0)
    calibrate.add_argument("--engine-order", action="store_true", help="use Pikafish inside DF-PN ordering")
    calibrate.add_argument("--min-samples", type=int, default=1)
    calibrate.add_argument("--output")
    calibrate.set_defaults(func=command_calibrate)

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
