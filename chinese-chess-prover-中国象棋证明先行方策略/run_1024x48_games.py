#!/usr/bin/env python3
"""Run bounded Pikafish self-play playouts and score red W/D/L.

This is not a solution proof. It resumes from generated legal samples and lets
Pikafish choose moves for both sides for at most N plies. A red win/loss is
recorded only when the opponent/current red side has no legal move while in
check. Repetition and horizon exits are recorded as draws.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from light_prover import BLACK, RED, Board, Move, Pikafish, opposite, score_to_scalar
from run_1024x12_report import generate_samples


RED_WIN = "RED_WIN"
DRAW = "DRAW"
RED_LOSS = "RED_LOSS"


def red_score_from_side_score(score: Optional[int], side: str) -> Optional[int]:
    if score is None:
        return None
    return score if side == RED else -score


def legal_move_by_uci(board: Board) -> Dict[str, Move]:
    return {move.uci(): move for move in board.legal_moves()}


def choose_engine_move(engine: Pikafish, board: Board) -> Tuple[Optional[Move], dict]:
    legal_by_uci = legal_move_by_uci(board)
    if not legal_by_uci:
        return None, {"score_cp": None, "score_mate": None, "bestmove": None, "fallback": False}

    ordered, cp, mate = engine.analyze(board.to_fen())
    for text in ordered:
        move = legal_by_uci.get(text)
        if move is not None:
            return move, {
                "score_cp": cp,
                "score_mate": mate,
                "score_scalar": score_to_scalar(cp, mate),
                "bestmove": text,
                "fallback": False,
            }

    fallback = sorted(legal_by_uci)[0]
    return legal_by_uci[fallback], {
        "score_cp": cp,
        "score_mate": mate,
        "score_scalar": score_to_scalar(cp, mate),
        "bestmove": fallback,
        "fallback": True,
    }


def terminal_result(board: Board) -> Optional[Tuple[str, str]]:
    legal = board.legal_moves()
    if legal:
        return None
    if not board.in_check(board.side):
        return DRAW, "no_legal_moves_not_in_check"
    if board.side == BLACK:
        return RED_WIN, "black_checkmated"
    return RED_LOSS, "red_checkmated"


def play_game(
    index: int,
    start_fen: str,
    engine: Pikafish,
    max_plies: int,
    repetition_limit: int,
    keep_moves: bool,
) -> dict:
    board = Board.from_fen(start_fen)
    initial_side = board.side
    initial_ordered, initial_cp, initial_mate = engine.analyze(board.to_fen())
    initial_score = score_to_scalar(initial_cp, initial_mate)
    initial_red_score = red_score_from_side_score(initial_score, initial_side)

    history: Dict[str, int] = {board.key(): 1}
    moves: List[dict] = []

    for ply in range(max_plies + 1):
        terminal = terminal_result(board)
        if terminal is not None:
            outcome, reason = terminal
            return {
                "index": index,
                "start_fen": start_fen,
                "initial_side": initial_side,
                "initial_score_cp": initial_cp,
                "initial_score_mate": initial_mate,
                "initial_score_scalar": initial_score,
                "initial_red_score": initial_red_score,
                "initial_pv": initial_ordered[:8],
                "outcome": outcome,
                "reason": reason,
                "plies_played": ply,
                "end_fen": board.to_fen(),
                "moves": moves if keep_moves else None,
            }

        if ply >= max_plies:
            return {
                "index": index,
                "start_fen": start_fen,
                "initial_side": initial_side,
                "initial_score_cp": initial_cp,
                "initial_score_mate": initial_mate,
                "initial_score_scalar": initial_score,
                "initial_red_score": initial_red_score,
                "initial_pv": initial_ordered[:8],
                "outcome": DRAW,
                "reason": "max_plies",
                "plies_played": ply,
                "end_fen": board.to_fen(),
                "moves": moves if keep_moves else None,
            }

        side = board.side
        move, info = choose_engine_move(engine, board)
        if move is None:
            return {
                "index": index,
                "start_fen": start_fen,
                "initial_side": initial_side,
                "initial_score_cp": initial_cp,
                "initial_score_mate": initial_mate,
                "initial_score_scalar": initial_score,
                "initial_red_score": initial_red_score,
                "initial_pv": initial_ordered[:8],
                "outcome": DRAW,
                "reason": "no_legal_moves_not_in_check",
                "plies_played": ply,
                "end_fen": board.to_fen(),
                "moves": moves if keep_moves else None,
            }

        next_board = board.make_move(move)
        next_key = next_board.key()
        moves.append(
            {
                "ply": ply + 1,
                "side": side,
                "move": move.uci(),
                "score_cp": info.get("score_cp"),
                "score_mate": info.get("score_mate"),
                "score_scalar": info.get("score_scalar"),
                "fallback": info.get("fallback", False),
            }
        )
        history[next_key] = history.get(next_key, 0) + 1
        board = next_board

        if history[next_key] >= repetition_limit:
            return {
                "index": index,
                "start_fen": start_fen,
                "initial_side": initial_side,
                "initial_score_cp": initial_cp,
                "initial_score_mate": initial_mate,
                "initial_score_scalar": initial_score,
                "initial_red_score": initial_red_score,
                "initial_pv": initial_ordered[:8],
                "outcome": DRAW,
                "reason": "repetition",
                "plies_played": ply + 1,
                "end_fen": board.to_fen(),
                "moves": moves if keep_moves else None,
            }

    raise AssertionError("unreachable")


def summarize(records: List[dict]) -> dict:
    outcome_counts = Counter(record["outcome"] for record in records)
    reason_counts = Counter(record["reason"] for record in records)
    plies = [record["plies_played"] for record in records]
    red_scores = [
        record["initial_red_score"]
        for record in records
        if record["initial_red_score"] is not None
    ]
    by_initial_side: Dict[str, Dict[str, int]] = {}
    for record in records:
        side = record["initial_side"]
        by_initial_side.setdefault(side, {RED_WIN: 0, DRAW: 0, RED_LOSS: 0})
        by_initial_side[side][record["outcome"]] += 1

    return {
        "outcome_counts": {
            RED_WIN: outcome_counts.get(RED_WIN, 0),
            DRAW: outcome_counts.get(DRAW, 0),
            RED_LOSS: outcome_counts.get(RED_LOSS, 0),
        },
        "reason_counts": dict(reason_counts),
        "by_initial_side": by_initial_side,
        "avg_plies": round(statistics.mean(plies), 2) if plies else 0,
        "median_plies": statistics.median(plies) if plies else 0,
        "max_plies_observed": max(plies) if plies else 0,
        "red_initial_score_min": min(red_scores) if red_scores else None,
        "red_initial_score_max": max(red_scores) if red_scores else None,
        "red_initial_score_avg": round(statistics.mean(red_scores), 2) if red_scores else None,
    }


def write_markdown(path: Path, output: dict) -> None:
    summary = output["summary"]
    counts = summary["outcome_counts"]
    lines = [
        "# Pikafish 1024x48 Red WDL Playout Report",
        "",
        "This is bounded engine self-play from generated legal samples, not a game-theoretic solution.",
        "",
        "## Configuration",
        "",
        f"- Samples: `{output['sample_count']}`.",
        f"- Sample source: `{output['sample_source']}`.",
        f"- Max plies per sample: `{output['max_plies']}`.",
        f"- Repetition limit: `{output['repetition_limit']}` appearances per state.",
        f"- Pikafish engine: `{output['engine_path']}`.",
        f"- Pikafish engine depth: `{output['engine_depth']}`.",
        f"- Pikafish movetime: `{output['movetime_ms']} ms`.",
        f"- Runtime seconds: `{output['runtime_seconds']}`.",
        "",
        "## Red WDL",
        "",
        f"- Red wins: `{counts[RED_WIN]}`.",
        f"- Draws: `{counts[DRAW]}`.",
        f"- Red losses: `{counts[RED_LOSS]}`.",
        "",
        "## Termination Reasons",
        "",
    ]
    for reason, count in sorted(summary["reason_counts"].items()):
        lines.append(f"- `{reason}`: `{count}`.")
    lines.extend(
        [
            "",
            "## Plies",
            "",
            f"- Average plies: `{summary['avg_plies']}`.",
            f"- Median plies: `{summary['median_plies']}`.",
            f"- Max plies observed: `{summary['max_plies_observed']}`.",
            "",
            "## Red Initial Score",
            "",
            f"- Min: `{summary['red_initial_score_min']}`.",
            f"- Max: `{summary['red_initial_score_max']}`.",
            f"- Average: `{summary['red_initial_score_avg']}`.",
            "",
            "## Interpretation",
            "",
            "A draw here means the playout did not reach checkmate inside the fixed 48-ply horizon, "
            "or repeated a state under this experiment's repetition rule. It is not a formal draw proof.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run 1024x48 Pikafish red WDL playouts")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--sample-count", type=int, default=1024)
    parser.add_argument("--source-plies", type=int, default=2)
    parser.add_argument("--max-plies", type=int, default=48)
    parser.add_argument("--repetition-limit", type=int, default=3)
    parser.add_argument("--engine-depth", type=int, default=1)
    parser.add_argument("--movetime", type=int, default=20)
    parser.add_argument("--out-dir", default="reports/1024x48-games")
    parser.add_argument("--progress-every", type=int, default=32)
    parser.add_argument("--keep-moves", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "pikafish_1024x48_red_wdl.json"
    md_path = out_dir / "pikafish_1024x48_red_wdl.md"
    samples_path = out_dir / "sample_1024_positions.txt"

    started = time.time()
    samples = generate_samples(args.sample_count, args.source_plies)
    samples_path.write_text("\n".join(samples) + "\n", encoding="utf-8")

    records: List[dict] = []
    engine = Pikafish(
        args.engine,
        movetime_ms=args.movetime,
        depth=args.engine_depth,
        cwd=args.engine_cwd,
    )
    try:
        for index, fen in enumerate(samples, 1):
            record = play_game(
                index=index,
                start_fen=fen,
                engine=engine,
                max_plies=args.max_plies,
                repetition_limit=args.repetition_limit,
                keep_moves=args.keep_moves,
            )
            records.append(record)
            if args.progress_every > 0 and (
                index % args.progress_every == 0 or index == len(samples)
            ):
                elapsed = time.time() - started
                counts = Counter(r["outcome"] for r in records)
                print(
                    f"[progress] {index}/{len(samples)} games, "
                    f"red_win={counts.get(RED_WIN, 0)}, "
                    f"draw={counts.get(DRAW, 0)}, "
                    f"red_loss={counts.get(RED_LOSS, 0)}, "
                    f"elapsed={elapsed:.1f}s",
                    file=sys.stderr,
                    flush=True,
                )
    finally:
        engine.close()

    output = {
        "sample_count": len(samples),
        "sample_source": f"BFS legal positions from standard start, source_plies={args.source_plies}",
        "max_plies": args.max_plies,
        "repetition_limit": args.repetition_limit,
        "engine_path": args.engine,
        "engine_cwd": args.engine_cwd,
        "engine_depth": args.engine_depth,
        "movetime_ms": args.movetime,
        "runtime_seconds": round(time.time() - started, 3),
        "summary": summarize(records),
        "records": records,
    }
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, output)
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "summary": output["summary"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
