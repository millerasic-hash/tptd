#!/usr/bin/env python3
"""Probe a reusable top-k opening candidate set at moderate depth.

This is the first iterative experiment after the dense small grid. It is still
an engine probe, not a proof. It is designed to be cheap to resume: every
candidate move is cached independently under the output directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shlex
import statistics
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from light_prover import START_FEN, Board
from opening_grid_probe import enrich_infos, parse_ints
from opening_probe import MultiPVEngine, apply_uci_if_legal, parse_depths


DEFAULT_CANDIDATES = [
    "h2e2",
    "b2e2",
    "c3c4",
    "g0e2",
    "c0e2",
    "g3g4",
    "b0c2",
    "h0g2",
    "h2f2",
]


def parse_candidates(text: str) -> List[str]:
    moves = []
    for part in text.split(","):
        part = part.strip()
        if part:
            moves.append(part)
    if not moves:
        raise argparse.ArgumentTypeError("at least one candidate move is required")
    return moves


def score_value(row: dict) -> Optional[int]:
    value = row.get("top_red_score")
    return value if isinstance(value, int) else None


def avg(values: List[float]) -> Optional[float]:
    return round(statistics.mean(values), 3) if values else None


def median(values: List[float]) -> Optional[float]:
    return round(statistics.median(values), 3) if values else None


def stddev(values: List[float]) -> Optional[float]:
    return round(statistics.pstdev(values), 3) if len(values) >= 2 else 0.0 if values else None


def softmax_entropy(scores: List[int], temperature: float) -> dict:
    if not scores:
        return {"entropy": None, "normalized_entropy": None, "effective_candidates": None}
    if len(scores) == 1:
        return {"entropy": 0.0, "normalized_entropy": 0.0, "effective_candidates": 1.0}
    scaled = [score / temperature for score in scores]
    max_scaled = max(scaled)
    weights = [math.exp(item - max_scaled) for item in scaled]
    total = sum(weights)
    probs = [weight / total for weight in weights]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return {
        "entropy": round(entropy, 6),
        "normalized_entropy": round(entropy / math.log(len(scores)), 6),
        "effective_candidates": round(math.exp(entropy), 3),
    }


def replay_pv_keys(start_board: Board, pv: Iterable[str]) -> dict:
    board = start_board
    keys = [board.key()]
    illegal_move = None
    for text in pv:
        child = apply_uci_if_legal(board, text)
        if child is None:
            illegal_move = text
            break
        board = child
        keys.append(board.key())
    return {
        "keys": keys,
        "end_key": keys[-1],
        "end_fen": board.to_fen(),
        "illegal_move": illegal_move,
    }


def cache_key(candidate: str, config: dict) -> str:
    identity = {
        "candidate": candidate,
        "start_fen": START_FEN,
        "engine": config["engine"],
        "engine_cwd": config["engine_cwd"],
        "depths": config["depths"],
        "multipv": config["multipv"],
        "threads": config["threads"],
        "hash_mb": config["hash_mb"],
        "clear_hash": config["clear_hash"],
        "show_wdl": config["show_wdl"],
        "go_depth": config["go_depth"],
        "repetition_limit": config["repetition_limit"],
    }
    digest = hashlib.sha256(json.dumps(identity, sort_keys=True).encode("utf-8")).hexdigest()[:16]
    return f"{candidate}_d{config['go_depth']}_mpv{config['multipv']}_{digest}.json"


def build_record(
    candidate: str,
    index: int,
    child: Board,
    analysis: dict,
    depths: List[int],
    repetition_limit: int,
) -> dict:
    record = {
        "index": index,
        "red_move": candidate,
        "fen_after_red_move": child.to_fen(),
        "queries": [],
    }
    go_depth = max(depths)
    for depth in depths:
        snapshot_infos = [dict(info) for info in analysis["snapshots"].get(str(depth), [])]
        if depth == go_depth and not snapshot_infos:
            snapshot_infos = [dict(info) for info in analysis["multipv"]]
        snapshot_infos = enrich_infos(snapshot_infos, child, repetition_limit)
        top = snapshot_infos[0] if snapshot_infos else {}
        query = {
            "depth_requested": depth,
            "source_go_depth": go_depth,
            "highest_depth": analysis["highest_depth"],
            "bestmove": (
                analysis["bestmove"]
                if depth == go_depth
                else ((top.get("pv") or [None])[0] if top else None)
            ),
            "stopped_by": (
                analysis["stopped_by"]
                if depth == go_depth or not snapshot_infos
                else "completed"
            ),
            "runtime_seconds": (
                analysis["runtime_seconds"]
                if depth == go_depth
                else round((top.get("time_ms") or 0) / 1000, 3)
            ),
            "multipv": snapshot_infos,
        }
        record["queries"].append(query)
    return record


def build_rows(records: List[dict]) -> List[dict]:
    rows = []
    for record in records:
        for query in record["queries"]:
            top = query["multipv"][0] if query["multipv"] else {}
            rows.append(
                {
                    "red_move": record["red_move"],
                    "depth": query["depth_requested"],
                    "stop": query["stopped_by"],
                    "best_reply": query["bestmove"],
                    "top_red_score": top.get("red_score"),
                    "top_engine_score_type": top.get("score_type"),
                    "top_engine_score": top.get("score"),
                    "nodes": top.get("nodes"),
                    "time_ms": top.get("time_ms"),
                    "seldepth": top.get("seldepth"),
                    "hashfull": top.get("hashfull"),
                    "wdl": top.get("wdl"),
                    "pv_has_repeat": top.get("pv_has_repeat"),
                    "pv_reaches_repetition_limit": top.get("pv_reaches_repetition_limit"),
                    "pv_first_repeat_at": top.get("pv_first_repeat_at"),
                    "pv": top.get("pv", []),
                    "captured_multipv": len(query["multipv"]),
                }
            )
    return rows


def summarize_by_depth(rows: List[dict], temperature: float) -> Dict[str, dict]:
    summary = {}
    for depth in sorted({row["depth"] for row in rows}):
        bucket = [row for row in rows if row["depth"] == depth]
        scored = [row for row in bucket if score_value(row) is not None]
        scores = [score_value(row) for row in scored]
        ranked = sorted(scored, key=lambda row: (score_value(row), row["red_move"]), reverse=True)
        entropy = softmax_entropy(scores, temperature)
        summary[str(depth)] = {
            "depth": depth,
            "positions": len(bucket),
            "completed": sum(1 for row in bucket if row["stop"] == "completed"),
            "max_seconds": sum(1 for row in bucket if row["stop"] == "max_seconds"),
            "score_min": min(scores) if scores else None,
            "score_median": median(scores),
            "score_avg": avg(scores),
            "score_max": max(scores) if scores else None,
            "candidate_entropy": entropy,
            "pv_repeat": sum(1 for row in bucket if row["pv_has_repeat"]),
            "pv_third_repeat": sum(1 for row in bucket if row["pv_reaches_repetition_limit"]),
            "leader": ranked[0] if ranked else None,
            "top": ranked[: min(5, len(ranked))],
        }
    return summary


def summarize_candidates(records: List[dict], depths: List[int]) -> List[dict]:
    final_depth = max(depths)
    summaries = []
    for record in records:
        rows = []
        all_keys = []
        leaf_keys = []
        child = Board.from_fen(record["fen_after_red_move"])
        for query in record["queries"]:
            top = query["multipv"][0] if query["multipv"] else {}
            row = {
                "depth": query["depth_requested"],
                "reply": query["bestmove"],
                "score": top.get("red_score"),
                "nodes": top.get("nodes"),
                "time_ms": top.get("time_ms"),
                "pv_has_repeat": top.get("pv_has_repeat"),
            }
            rows.append(row)
            for info in query["multipv"]:
                replay = replay_pv_keys(child, info.get("pv", []))
                all_keys.extend(replay["keys"])
                leaf_keys.append(replay["end_key"])

        scores = [row["score"] for row in rows if isinstance(row.get("score"), int)]
        replies = [row["reply"] for row in rows if row.get("reply")]
        final_row = next((row for row in rows if row["depth"] == final_depth), rows[-1] if rows else {})
        unique_keys = set(all_keys)
        raw_nodes = len(all_keys)
        unique_leaf_keys = set(leaf_keys)
        score_std = stddev([float(score) for score in scores])
        reply_count = len(set(replies))
        transposition_density = (
            round(1 - (len(unique_keys) / raw_nodes), 6) if raw_nodes else None
        )
        dag_compression_estimate = (
            round(raw_nodes / len(unique_keys), 3) if unique_keys else None
        )
        proof_cost_proxy = None
        if score_std is not None:
            final_score = final_row.get("score") if isinstance(final_row.get("score"), int) else 0
            score_drop = (max(scores) - final_score) if scores else 0
            proof_cost_proxy = round(
                reply_count * 10
                + score_std
                + max(0, score_drop) * 0.5
                + len(unique_leaf_keys),
                3,
            )
        summaries.append(
            {
                "red_move": record["red_move"],
                "final_depth": final_depth,
                "final_score": final_row.get("score"),
                "final_reply": final_row.get("reply"),
                "score_min": min(scores) if scores else None,
                "score_max": max(scores) if scores else None,
                "score_avg": avg([float(score) for score in scores]),
                "score_stddev": score_std,
                "score_range": (max(scores) - min(scores)) if scores else None,
                "reply_count": reply_count,
                "replies": sorted(set(replies)),
                "pv_repeat_depths": [
                    row["depth"] for row in rows if row.get("pv_has_repeat")
                ],
                "frontier_size": len(unique_leaf_keys),
                "pv_state_occurrences": raw_nodes,
                "pv_unique_states": len(unique_keys),
                "transposition_density": transposition_density,
                "dag_compression_estimate": dag_compression_estimate,
                "proof_cost_proxy": proof_cost_proxy,
                "depth_rows": rows,
            }
        )
    summaries.sort(
        key=lambda item: (
            item["final_score"] if isinstance(item.get("final_score"), int) else -10**9,
            -(item["proof_cost_proxy"] or 10**9),
            item["red_move"],
        ),
        reverse=True,
    )
    return summaries


def add_ranks(candidate_summaries: List[dict], rows: List[dict], depths: List[int]) -> None:
    rank_by_depth: Dict[int, Dict[str, int]] = {}
    for depth in depths:
        bucket = [row for row in rows if row["depth"] == depth and score_value(row) is not None]
        bucket.sort(key=lambda row: (score_value(row), row["red_move"]), reverse=True)
        rank_by_depth[depth] = {row["red_move"]: idx for idx, row in enumerate(bucket, start=1)}
    for item in candidate_summaries:
        ranks = [rank_by_depth.get(depth, {}).get(item["red_move"]) for depth in depths]
        ranks = [rank for rank in ranks if rank is not None]
        item["rank_by_depth"] = {str(depth): rank_by_depth.get(depth, {}).get(item["red_move"]) for depth in depths}
        item["rank_avg"] = avg([float(rank) for rank in ranks])
        item["rank_final"] = rank_by_depth.get(max(depths), {}).get(item["red_move"])


def write_markdown(path: Path, output: dict) -> None:
    config = output["config"]
    lines = [
        "# Pikafish Candidate Opening Probe",
        "",
        "This is a reusable Top-k candidate stability probe, not a game-theoretic proof.",
        "",
        "## Configuration",
        "",
        f"- Start FEN: `{output['start_fen']}`.",
        f"- Candidates: `{', '.join(config['candidates'])}`.",
        f"- Depths: `{', '.join(map(str, config['depths']))}`.",
        f"- MultiPV: `{config['multipv']}`.",
        f"- Threads: `{config['threads']}`.",
        f"- Hash: `{config['hash_mb']} MB`.",
        f"- Per-query max seconds: `{config['per_query_max_seconds']}`.",
        f"- Wall runtime seconds: `{output['wall_runtime_seconds']}`.",
        f"- Cached search runtime seconds: `{output['cached_search_runtime_seconds']}`.",
        f"- Cache hits: `{output['cache']['hits']}`.",
        f"- Cache misses: `{output['cache']['misses']}`.",
        "",
        "Each candidate runs one `go depth max(depths)` search and captures intermediate depth snapshots.",
        "",
        "## Depth Summary",
        "",
        "| Depth | Positions | Completed | Max seconds | Min | Median | Avg | Max | Entropy | Effective candidates | Leader | Score | Reply |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---|---:|:---|",
    ]
    for depth, item in output["depth_summary"].items():
        leader = item["leader"] or {}
        entropy = item["candidate_entropy"]
        lines.append(
            f"| {depth} | {item['positions']} | {item['completed']} | {item['max_seconds']} | "
            f"{item['score_min']} | {item['score_median']} | {item['score_avg']} | {item['score_max']} | "
            f"{entropy['normalized_entropy']} | {entropy['effective_candidates']} | "
            f"{leader.get('red_move')} | {leader.get('top_red_score')} | {leader.get('best_reply')} |"
        )

    lines.extend(
        [
            "",
            f"## Final Depth {max(config['depths'])} Ranking",
            "",
            "| Rank | Red move | Score | Reply | Avg rank | Score stddev | Reply variants | Frontier | Transposition density | DAG compression | Cost proxy |",
            "|---:|:---|---:|:---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for idx, item in enumerate(output["candidate_summary"], start=1):
        lines.append(
            f"| {idx} | {item['red_move']} | {item['final_score']} | {item['final_reply']} | "
            f"{item['rank_avg']} | {item['score_stddev']} | {item['reply_count']} | "
            f"{item['frontier_size']} | {item['transposition_density']} | "
            f"{item['dag_compression_estimate']} | {item['proof_cost_proxy']} |"
        )

    lines.extend(
        [
            "",
            "## Candidate Score Curves",
            "",
            "| Red move | "
            + " | ".join(f"d{depth}" for depth in config["depths"])
            + " | Replies |",
            "|:---|" + "---:|" * len(config["depths"]) + ":---|",
        ]
    )
    summary_by_move = {item["red_move"]: item for item in output["candidate_summary"]}
    for move in config["candidates"]:
        item = summary_by_move[move]
        scores_by_depth = {row["depth"]: row["score"] for row in item["depth_rows"]}
        scores = " | ".join(str(scores_by_depth.get(depth)) for depth in config["depths"])
        lines.append(f"| {move} | {scores} | {', '.join(item['replies'])} |")

    lines.extend(
        [
            "",
            "## Full Rows",
            "",
            "| Red move | Depth | Stop | Reply | Red score | Nodes | Time ms | Captured PVs | Top PV |",
            "|:---|---:|:---|:---|---:|---:|---:|---:|:---|",
        ]
    )
    for row in output["rows"]:
        pv = " ".join(row.get("pv", [])[:12])
        lines.append(
            f"| {row['red_move']} | {row['depth']} | {row['stop']} | {row['best_reply']} | "
            f"{row['top_red_score']} | {row['nodes']} | {row['time_ms']} | "
            f"{row['captured_multipv']} | `{pv}` |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Reusable Top-k candidate opening probe")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--candidates", type=parse_candidates, default=DEFAULT_CANDIDATES)
    parser.add_argument("--depths", type=parse_depths, default=[14, 16, 18, 20, 22, 24])
    parser.add_argument("--multipv", type=int, default=4)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--hash-mb", type=int, default=128)
    parser.add_argument("--per-query-max-seconds", type=float, default=60.0)
    parser.add_argument("--repetition-limit", type=int, default=3)
    parser.add_argument("--entropy-temperature-cp", type=float, default=30.0)
    parser.add_argument("--no-clear-hash", action="store_true")
    parser.add_argument("--no-wdl", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--out-dir", default="reports/opening-candidate-probe")
    args = parser.parse_args()

    started = time.time()
    out_dir = Path(args.out_dir)
    cache_dir = out_dir / "cache"
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "opening_candidate_probe_report.json"
    md_path = out_dir / "opening_candidate_probe_report.md"
    command_path = out_dir / "command.txt"
    command_path.write_text(
        "python3 " + " ".join(shlex.quote(arg) for arg in sys.argv) + "\n",
        encoding="utf-8",
    )

    start_board = Board.from_fen(START_FEN)
    legal = {move.uci(): move for move in start_board.legal_moves()}
    missing = [move for move in args.candidates if move not in legal]
    if missing:
        raise SystemExit(f"candidate moves are not legal from start position: {', '.join(missing)}")

    config = {
        "engine": args.engine,
        "engine_cwd": args.engine_cwd,
        "candidates": args.candidates,
        "depths": args.depths,
        "multipv": args.multipv,
        "threads": args.threads,
        "hash_mb": args.hash_mb,
        "clear_hash": not args.no_clear_hash,
        "show_wdl": not args.no_wdl,
        "go_depth": max(args.depths),
        "per_query_max_seconds": args.per_query_max_seconds,
        "repetition_limit": args.repetition_limit,
        "entropy_temperature_cp": args.entropy_temperature_cp,
    }

    records = []
    cache_hits = 0
    cache_misses = 0
    engine: Optional[MultiPVEngine] = None
    try:
        for index, candidate in enumerate(args.candidates, start=1):
            child = start_board.make_move(legal[candidate])
            candidate_cache = cache_dir / cache_key(candidate, config)
            if candidate_cache.exists() and not args.force:
                record = json.loads(candidate_cache.read_text(encoding="utf-8"))
                cache_hits += 1
                print(f"[cache] {candidate} loaded", file=sys.stderr, flush=True)
            else:
                cache_misses += 1
                if engine is None:
                    engine = MultiPVEngine(
                        args.engine,
                        args.engine_cwd,
                        threads=args.threads,
                        hash_mb=args.hash_mb,
                        multipv=args.multipv,
                        show_wdl=not args.no_wdl,
                    )
                print(
                    f"[run {index}/{len(args.candidates)}] candidate={candidate}",
                    file=sys.stderr,
                    flush=True,
                )
                analysis = engine.analyze(
                    child.to_fen(),
                    max(args.depths),
                    args.per_query_max_seconds,
                    clear_hash=not args.no_clear_hash,
                    progress_prefix=f"[candidate {index}/{len(args.candidates)} {candidate}]",
                    snapshot_depths=args.depths,
                )
                record = build_record(
                    candidate,
                    index,
                    child,
                    analysis,
                    args.depths,
                    args.repetition_limit,
                )
                candidate_cache.write_text(
                    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8",
                )
                final_query = record["queries"][-1]
                top = final_query["multipv"][0] if final_query["multipv"] else {}
                print(
                    f"[done] candidate={candidate} reply={final_query['bestmove']} "
                    f"red_score={top.get('red_score')} stop={final_query['stopped_by']} "
                    f"seconds={final_query['runtime_seconds']}",
                    file=sys.stderr,
                    flush=True,
                )
            records.append(record)
    finally:
        if engine is not None:
            engine.close()

    rows = build_rows(records)
    candidate_summary = summarize_candidates(records, args.depths)
    add_ranks(candidate_summary, rows, args.depths)
    cached_search_runtime_seconds = round(
        sum(
            (record["queries"][-1].get("runtime_seconds") or 0)
            for record in records
            if record.get("queries")
        ),
        3,
    )
    output = {
        "schema": "opening_candidate_probe/v1",
        "start_fen": START_FEN,
        "config": config,
        "wall_runtime_seconds": round(time.time() - started, 3),
        "cached_search_runtime_seconds": cached_search_runtime_seconds,
        "cache": {"hits": cache_hits, "misses": cache_misses},
        "records": records,
        "rows": rows,
        "depth_summary": summarize_by_depth(rows, args.entropy_temperature_cp),
        "candidate_summary": candidate_summary,
    }
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, output)
    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "command": str(command_path),
                "wall_runtime_seconds": output["wall_runtime_seconds"],
                "cached_search_runtime_seconds": output["cached_search_runtime_seconds"],
                "cache": output["cache"],
                "candidate_count": len(args.candidates),
                "depths": args.depths,
                "multipv": args.multipv,
                "leader": output["candidate_summary"][0] if output["candidate_summary"] else None,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
