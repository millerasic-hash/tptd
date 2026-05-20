#!/usr/bin/env python3
"""Run one bounded Pikafish self-play game at a fixed engine depth."""

from __future__ import annotations

import argparse
import json
import os
import queue
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from light_prover import BLACK, RED, START_FEN, Board, Move, score_to_scalar


RED_WIN = "RED_WIN"
DRAW = "DRAW"
RED_LOSS = "RED_LOSS"


def send(proc: subprocess.Popen[str], command: str) -> None:
    assert proc.stdin is not None
    proc.stdin.write(command + "\n")
    proc.stdin.flush()


def read_until(line_queue: "queue.Queue[str]", marker: str, timeout: float) -> List[str]:
    end = time.time() + timeout
    lines: List[str] = []
    while time.time() < end:
        try:
            line = line_queue.get(timeout=0.2)
        except queue.Empty:
            continue
        lines.append(line)
        if line.startswith(marker):
            break
    return lines


def parse_info(line: str) -> Optional[dict]:
    parts = line.split()
    if not parts or parts[0] != "info" or "depth" not in parts:
        return None
    info: Dict[str, object] = {"raw": line}
    try:
        info["depth"] = int(parts[parts.index("depth") + 1])
    except Exception:
        return None
    for key in ("seldepth", "nodes", "nps", "time"):
        if key in parts:
            try:
                out_key = "time_ms" if key == "time" else key
                info[out_key] = int(parts[parts.index(key) + 1])
            except Exception:
                pass
    if "score" in parts:
        idx = parts.index("score")
        if idx + 2 < len(parts):
            info["score_type"] = parts[idx + 1]
            try:
                info["score"] = int(parts[idx + 2])
            except ValueError:
                info["score"] = parts[idx + 2]
    if "pv" in parts:
        info["pv"] = parts[parts.index("pv") + 1 :]
    return info


class DepthEngine:
    def __init__(self, path: str, cwd: str):
        self.lines: "queue.Queue[str]" = queue.Queue()
        self.proc = subprocess.Popen(
            [os.path.abspath(path)],
            cwd=os.path.abspath(cwd),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            bufsize=1,
        )
        self.reader = threading.Thread(target=self._reader_loop, daemon=True)
        self.reader.start()
        send(self.proc, "uci")
        read_until(self.lines, "uciok", 10)
        send(self.proc, "isready")
        read_until(self.lines, "readyok", 10)

    def _reader_loop(self) -> None:
        assert self.proc.stdout is not None
        for line in self.proc.stdout:
            line = line.strip()
            if line:
                self.lines.put(line)

    def drain(self) -> None:
        while True:
            try:
                self.lines.get_nowait()
            except queue.Empty:
                return

    def close(self) -> None:
        try:
            send(self.proc, "quit")
        except Exception:
            pass
        self.proc.terminate()

    def bestmove(
        self,
        fen: str,
        depth: int,
        max_seconds: float,
        progress_prefix: str,
    ) -> dict:
        self.drain()
        send(self.proc, f"position fen {fen}")
        send(self.proc, f"go depth {depth}")
        started = time.time()
        infos: List[dict] = []
        bestmove = None
        stopped_by = "completed"
        last_reported_depth = 0

        while True:
            elapsed = time.time() - started
            if elapsed >= max_seconds:
                stopped_by = "max_seconds"
                send(self.proc, "stop")
                break

            try:
                line = self.lines.get(timeout=0.2)
            except queue.Empty:
                continue
            if line.startswith("bestmove"):
                parts = line.split()
                bestmove = parts[1] if len(parts) > 1 and parts[1] != "(none)" else None
                break
            info = parse_info(line)
            if info is not None:
                infos.append(info)
                current_depth = int(info["depth"])
                if current_depth > last_reported_depth:
                    last_reported_depth = current_depth
                    score = f"{info.get('score_type')} {info.get('score')}"
                    print(
                        f"{progress_prefix} depth={current_depth}, "
                        f"score={score}, nodes={info.get('nodes')}, "
                        f"elapsed={elapsed:.1f}s",
                        file=sys.stderr,
                        flush=True,
                    )

        if stopped_by == "max_seconds":
            for line in read_until(self.lines, "bestmove", 10):
                if line.startswith("bestmove"):
                    parts = line.split()
                    bestmove = parts[1] if len(parts) > 1 and parts[1] != "(none)" else None
                    break

        last_info = infos[-1] if infos else None
        pv_bestmove = None
        if last_info and last_info.get("pv"):
            pv = last_info["pv"]
            if isinstance(pv, list) and pv:
                pv_bestmove = pv[0]

        return {
            "bestmove": bestmove,
            "bestmove_from_last_pv": pv_bestmove,
            "chosen_move": bestmove or pv_bestmove,
            "stopped_by": stopped_by,
            "runtime_seconds": round(time.time() - started, 3),
            "highest_depth": max((int(info["depth"]) for info in infos), default=0),
            "last_info": last_info,
        }


def terminal_result(board: Board) -> Optional[Tuple[str, str]]:
    if board.legal_moves():
        return None
    if not board.in_check(board.side):
        return DRAW, "no_legal_moves_not_in_check"
    if board.side == BLACK:
        return RED_WIN, "black_checkmated"
    return RED_LOSS, "red_checkmated"


def legal_move(board: Board, text: Optional[str]) -> Optional[Move]:
    if not text:
        return None
    legal = {move.uci(): move for move in board.legal_moves()}
    return legal.get(text)


def write_markdown(path: Path, output: dict) -> None:
    lines = [
        f"# Pikafish 1 Game Depth {output['engine_depth']}",
        "",
        "This is one bounded self-play game from the standard Xiangqi start position.",
        "",
        "## Result",
        "",
        f"- Outcome: `{output['outcome']}`.",
        f"- Reason: `{output['reason']}`.",
        f"- Plies played: `{output['plies_played']}`.",
        f"- Runtime seconds: `{output['runtime_seconds']}`.",
        f"- Engine depth requested per move: `{output['engine_depth']}`.",
        f"- Per-move max seconds: `{output['per_move_max_seconds']}`.",
        f"- Max plies: `{output['max_plies']}`.",
        f"- Final FEN: `{output['final_fen']}`.",
        "",
        "## Moves",
        "",
        "| Ply | Side | Move | Reached depth | Score | Nodes | Seconds | Stop |",
        "|---:|:---:|:---|---:|:---|---:|---:|:---|",
    ]
    for item in output["moves"]:
        info = item.get("last_info") or {}
        score = ""
        if info:
            score = f"{info.get('score_type')} {info.get('score')}"
        lines.append(
            f"| {item['ply']} | {item['side']} | {item['move']} | "
            f"{item['highest_depth']} | {score} | {info.get('nodes', '')} | "
            f"{item['runtime_seconds']} | {item['stopped_by']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one Pikafish fixed-depth game")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--depth", type=int, default=42)
    parser.add_argument("--per-move-max-seconds", type=float, default=180.0)
    parser.add_argument("--max-plies", type=int, default=256)
    parser.add_argument("--repetition-limit", type=int, default=3)
    parser.add_argument("--out-dir", default="reports/1-game-depth42")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "pikafish_1_game_depth42.json"
    md_path = out_dir / "pikafish_1_game_depth42.md"

    board = Board.from_fen(START_FEN)
    history: Dict[str, int] = {board.key(): 1}
    moves: List[dict] = []
    started = time.time()
    outcome = DRAW
    reason = "max_plies"

    engine = DepthEngine(args.engine, args.engine_cwd)
    try:
        for ply in range(1, args.max_plies + 1):
            terminal = terminal_result(board)
            if terminal is not None:
                outcome, reason = terminal
                break

            side = board.side
            analysis = engine.bestmove(
                board.to_fen(),
                args.depth,
                args.per_move_max_seconds,
                progress_prefix=f"[ply {ply} {side}]",
            )
            move = legal_move(board, analysis["chosen_move"])
            if move is None:
                outcome = DRAW
                reason = "engine_no_legal_bestmove"
                moves.append({"ply": ply, "side": side, "move": None, **analysis})
                break

            board = board.make_move(move)
            key = board.key()
            history[key] = history.get(key, 0) + 1
            moves.append({"ply": ply, "side": side, "move": move.uci(), **analysis})
            print(
                f"[move] ply={ply}, side={side}, move={move.uci()}, "
                f"reached_depth={analysis['highest_depth']}, "
                f"runtime={analysis['runtime_seconds']}s",
                file=sys.stderr,
                flush=True,
            )

            if history[key] >= args.repetition_limit:
                outcome = DRAW
                reason = "repetition"
                break
        else:
            outcome = DRAW
            reason = "max_plies"
    finally:
        engine.close()

    terminal = terminal_result(board)
    if terminal is not None and reason not in {"repetition", "engine_no_legal_bestmove"}:
        outcome, reason = terminal

    output = {
        "engine_depth": args.depth,
        "per_move_max_seconds": args.per_move_max_seconds,
        "max_plies": args.max_plies,
        "repetition_limit": args.repetition_limit,
        "outcome": outcome,
        "reason": reason,
        "plies_played": len([m for m in moves if m.get("move")]),
        "runtime_seconds": round(time.time() - started, 3),
        "final_fen": board.to_fen(),
        "moves": moves,
    }
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, output)
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "summary": {k: output[k] for k in ("outcome", "reason", "plies_played", "runtime_seconds", "final_fen")}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
