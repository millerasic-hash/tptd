#!/usr/bin/env python3
"""Run a fixed 1024 x 12 Pikafish/prover calibration report."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from collections import Counter, deque
from pathlib import Path
from typing import Dict, List

from light_prover import (
    Board,
    DfpnProver,
    Pikafish,
    START_FEN,
    score_to_scalar,
    threshold_report,
)


def generate_samples(count: int, max_source_plies: int) -> List[str]:
    root = Board.from_fen(START_FEN)
    queue = deque([(root, 0)])
    seen = {root.key()}
    samples: List[str] = []

    while queue and len(samples) < count:
        board, ply = queue.popleft()
        if ply > 0:
            samples.append(board.to_fen())
            if len(samples) >= count:
                break
        if ply >= max_source_plies:
            continue
        for move in board.legal_moves():
            child = board.make_move(move)
            key = child.key()
            if key in seen:
                continue
            seen.add(key)
            queue.append((child, ply + 1))

    if len(samples) < count:
        raise RuntimeError(f"only generated {len(samples)} samples")
    return samples


def summarize(records: List[dict]) -> Dict[str, object]:
    counts = Counter(r["status"] for r in records)
    nodes = [r["searched_nodes"] for r in records]
    proven = [r for r in records if r["status"] in {"WIN", "LOSS"}]
    known_scores = [r["score_scalar"] for r in records if r["score_scalar"] is not None]
    return {
        "status_counts": dict(counts),
        "proven_count": len(proven),
        "unknown_count": counts.get("UNKNOWN", 0),
        "avg_nodes": round(statistics.mean(nodes), 2) if nodes else 0,
        "median_nodes": statistics.median(nodes) if nodes else 0,
        "max_nodes_observed": max(nodes) if nodes else 0,
        "min_score": min(known_scores) if known_scores else None,
        "max_score": max(known_scores) if known_scores else None,
    }


def write_markdown(path: Path, output: dict) -> None:
    report = output["threshold_report"]
    summary = output["summary"]
    lines = [
        "# Pikafish Prover 1024x12 Report",
        "",
        "This is a bounded calibration run, not a theorem about Xiangqi.",
        "",
        "## Configuration",
        "",
        f"- Samples: `{output['sample_count']}` generated from standard start positions.",
        f"- Proof depth: `{output['proof_depth']}` plies.",
        f"- Max proof nodes per sample: `{output['max_nodes']}`.",
        f"- Repetition limit: `{output['repetition_limit']}` appearances per state.",
        f"- Pikafish engine: `{output['engine_path']}`.",
        f"- Pikafish engine depth: `{output['engine_depth']}`.",
        f"- Pikafish movetime: `{output['movetime_ms']} ms`.",
        f"- Runtime seconds: `{output['runtime_seconds']}`.",
        "",
        "## Summary",
        "",
        f"- Status counts: `{summary['status_counts']}`.",
        f"- Proven count: `{summary['proven_count']}`.",
        f"- Unknown count: `{summary['unknown_count']}`.",
        f"- Average prover nodes: `{summary['avg_nodes']}`.",
        f"- Median prover nodes: `{summary['median_nodes']}`.",
        f"- Max prover nodes observed: `{summary['max_nodes_observed']}`.",
        f"- Score range: `{summary['min_score']}` to `{summary['max_score']}`.",
        "",
        "## Threshold",
        "",
        f"- `threshold_all_above_proven_win`: `{report['threshold_all_above_proven_win']}`.",
        f"- Warning: {report['warning']}",
        "",
        "## Bins",
        "",
        "| Score range | Count | WIN | LOSS | UNKNOWN |",
        "|---:|---:|---:|---:|---:|",
    ]
    for item in report["bins"]:
        lower, upper = item["range"]
        lines.append(
            f"| [{lower}, {upper}) | {item['count']} | {item['win']} | "
            f"{item['loss']} | {item['unknown']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A score threshold is useful only when a fixed sample, fixed engine setting, "
            "fixed proof depth, and fixed node budget are stated together. A high score "
            "can prioritize proof work, but it cannot replace a closed certificate.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run 1024x12 prover calibration")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--sample-count", type=int, default=1024)
    parser.add_argument("--source-plies", type=int, default=3)
    parser.add_argument("--depth", type=int, default=12)
    parser.add_argument("--max-nodes", type=int, default=1024)
    parser.add_argument("--repetition-limit", type=int, default=2)
    parser.add_argument("--engine-depth", type=int, default=1)
    parser.add_argument("--movetime", type=int, default=20)
    parser.add_argument("--out-dir", default="reports")
    parser.add_argument("--progress-every", type=int, default=64)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "pikafish_prover_1024x12.json"
    md_path = out_dir / "pikafish_prover_1024x12.md"
    samples_path = out_dir / "sample_1024_positions.txt"

    started = time.time()
    samples = generate_samples(args.sample_count, args.source_plies)
    samples_path.write_text("\n".join(samples) + "\n", encoding="utf-8")

    engine = Pikafish(
        args.engine,
        movetime_ms=args.movetime,
        depth=args.engine_depth,
        cwd=args.engine_cwd,
    )
    records: List[dict] = []
    try:
        for index, fen in enumerate(samples, 1):
            board = Board.from_fen(fen)
            _ordered, cp, mate = engine.analyze(board.to_fen())
            prover = DfpnProver(
                engine=None,
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
            if args.progress_every > 0 and (
                index % args.progress_every == 0 or index == len(samples)
            ):
                elapsed = time.time() - started
                print(
                    f"[progress] {index}/{len(samples)} samples, "
                    f"elapsed={elapsed:.1f}s",
                    file=sys.stderr,
                    flush=True,
                )
    finally:
        engine.close()

    output = {
        "sample_count": len(samples),
        "sample_source": "BFS legal positions from standard start",
        "proof_depth": args.depth,
        "max_nodes": args.max_nodes,
        "repetition_limit": args.repetition_limit,
        "engine_path": args.engine,
        "engine_cwd": args.engine_cwd,
        "engine_depth": args.engine_depth,
        "movetime_ms": args.movetime,
        "runtime_seconds": round(time.time() - started, 3),
        "summary": summarize(records),
        "threshold_report": threshold_report(records, min_samples=1),
        "records": records,
    }

    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, output)
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "summary": output["summary"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
