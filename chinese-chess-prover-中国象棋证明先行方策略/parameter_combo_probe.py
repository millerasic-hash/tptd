#!/usr/bin/env python3
"""Run a resumable Pikafish parameter-combination probe.

This is a multi-lens experiment collector. It varies a small set of engine
parameters over a fixed candidate pool and records observations only. It does
not produce proof claims.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import shlex
import statistics
import sys
import time
from pathlib import Path
from typing import Iterable, List, Optional

from light_prover import START_FEN, Board
from opening_candidate_probe import parse_candidates
from opening_grid_probe import enrich_infos
from opening_probe import MultiPVEngine, apply_uci_if_legal, parse_depths


DEFAULT_CANDIDATES = ["c3c4", "b2e2", "c0e2", "h2e2"]


def parse_ints(text: str) -> List[int]:
    values = []
    for part in text.split(","):
        part = part.strip()
        if part:
            values.append(int(part))
    if not values:
        raise argparse.ArgumentTypeError("at least one integer is required")
    return values


def parse_bools(text: str) -> List[bool]:
    values = []
    for part in text.split(","):
        item = part.strip().lower()
        if not item:
            continue
        if item in {"1", "true", "yes", "y", "on"}:
            values.append(True)
        elif item in {"0", "false", "no", "n", "off"}:
            values.append(False)
        else:
            raise argparse.ArgumentTypeError(f"invalid bool value: {part}")
    if not values:
        raise argparse.ArgumentTypeError("at least one bool is required")
    return values


def mean(values: Iterable[float]) -> Optional[float]:
    items = list(values)
    return round(statistics.mean(items), 3) if items else None


def median(values: Iterable[float]) -> Optional[float]:
    items = list(values)
    return round(statistics.median(items), 3) if items else None


def pstdev(values: Iterable[float]) -> Optional[float]:
    items = list(values)
    if not items:
        return None
    return round(statistics.pstdev(items), 3) if len(items) > 1 else 0.0


def score_value(row: dict) -> Optional[int]:
    value = row.get("top_red_score")
    return value if isinstance(value, int) else None


def cache_name(candidate: str, config: dict) -> str:
    identity = {
        "candidate": candidate,
        "start_fen": START_FEN,
        "engine": config["engine"],
        "engine_cwd": config["engine_cwd"],
        "depth": config["depth"],
        "multipv": config["multipv"],
        "threads": config["threads"],
        "hash_mb": config["hash_mb"],
        "clear_hash": config["clear_hash"],
        "show_wdl": config["show_wdl"],
        "max_seconds": config["max_seconds"],
        "repetition_limit": config["repetition_limit"],
    }
    digest = hashlib.sha256(json.dumps(identity, sort_keys=True).encode("utf-8")).hexdigest()[:16]
    return (
        f"{candidate}_d{config['depth']}_mpv{config['multipv']}_"
        f"h{config['hash_mb']}_t{config['threads']}_{digest}.json"
    )


def build_record(candidate: str, child: Board, config: dict, analysis: dict) -> dict:
    infos = [dict(info) for info in analysis["multipv"]]
    infos = enrich_infos(infos, child, config["repetition_limit"])
    top = infos[0] if infos else {}
    return {
        "red_move": candidate,
        "fen_after_red_move": child.to_fen(),
        "config": config,
        "query": {
            "depth_requested": config["depth"],
            "highest_depth": analysis["highest_depth"],
            "bestmove": analysis["bestmove"],
            "stopped_by": analysis["stopped_by"],
            "runtime_seconds": analysis["runtime_seconds"],
            "multipv": infos,
        },
        "top": {
            "best_reply": analysis["bestmove"],
            "red_score": top.get("red_score"),
            "engine_score_type": top.get("score_type"),
            "engine_score": top.get("score"),
            "nodes": top.get("nodes"),
            "time_ms": top.get("time_ms"),
            "seldepth": top.get("seldepth"),
            "hashfull": top.get("hashfull"),
            "wdl": top.get("wdl"),
            "pv": top.get("pv", []),
            "pv_has_repeat": top.get("pv_has_repeat"),
            "pv_reaches_repetition_limit": top.get("pv_reaches_repetition_limit"),
        },
    }


def build_rows(records: List[dict]) -> List[dict]:
    rows = []
    for record in records:
        config = record["config"]
        top = record["top"]
        query = record["query"]
        rows.append(
            {
                "red_move": record["red_move"],
                "depth": config["depth"],
                "multipv": config["multipv"],
                "hash_mb": config["hash_mb"],
                "threads": config["threads"],
                "clear_hash": config["clear_hash"],
                "show_wdl": config["show_wdl"],
                "max_seconds": config["max_seconds"],
                "stop": query["stopped_by"],
                "highest_depth": query["highest_depth"],
                "best_reply": top["best_reply"],
                "top_red_score": top["red_score"],
                "top_engine_score_type": top["engine_score_type"],
                "top_engine_score": top["engine_score"],
                "nodes": top["nodes"],
                "time_ms": top["time_ms"],
                "seldepth": top["seldepth"],
                "hashfull": top["hashfull"],
                "wdl": top["wdl"],
                "pv_has_repeat": top["pv_has_repeat"],
                "pv_reaches_repetition_limit": top["pv_reaches_repetition_limit"],
                "captured_multipv": len(query["multipv"]),
                "pv": top["pv"],
            }
        )
    return rows


def config_key(row: dict) -> tuple:
    return (
        row["depth"],
        row["multipv"],
        row["hash_mb"],
        row["threads"],
        row["clear_hash"],
        row["show_wdl"],
        row["max_seconds"],
    )


def summarize(rows: List[dict], candidates: List[str]) -> dict:
    config_keys = sorted({config_key(row) for row in rows})
    leaders = []
    rank_by_candidate = {candidate: [] for candidate in candidates}
    top_counts = {candidate: 0 for candidate in candidates}

    for key in config_keys:
        bucket = [row for row in rows if config_key(row) == key and score_value(row) is not None]
        bucket.sort(key=lambda row: (score_value(row), row["red_move"]), reverse=True)
        if not bucket:
            continue
        leader = bucket[0]
        top_counts[leader["red_move"]] += 1
        leaders.append(
            {
                "depth": key[0],
                "multipv": key[1],
                "hash_mb": key[2],
                "threads": key[3],
                "clear_hash": key[4],
                "show_wdl": key[5],
                "max_seconds": key[6],
                "leader": leader["red_move"],
                "score": leader["top_red_score"],
                "reply": leader["best_reply"],
            }
        )
        for rank, row in enumerate(bucket, start=1):
            rank_by_candidate[row["red_move"]].append(rank)

    candidate_stats = []
    for candidate in candidates:
        candidate_rows = [
            row for row in rows if row["red_move"] == candidate and score_value(row) is not None
        ]
        scores = [score_value(row) for row in candidate_rows]
        replies = sorted({row["best_reply"] for row in candidate_rows if row["best_reply"]})
        ranks = rank_by_candidate[candidate]
        candidate_stats.append(
            {
                "red_move": candidate,
                "observations": len(candidate_rows),
                "top_count": top_counts[candidate],
                "top_share": round(top_counts[candidate] / len(config_keys), 3) if config_keys else None,
                "score_min": min(scores) if scores else None,
                "score_median": median(scores),
                "score_avg": mean(scores),
                "score_max": max(scores) if scores else None,
                "score_range": (max(scores) - min(scores)) if scores else None,
                "score_stddev": pstdev(scores),
                "rank_avg": mean(ranks),
                "rank_stddev": pstdev(ranks),
                "reply_count": len(replies),
                "replies": replies,
                "pv_repeat_count": sum(1 for row in candidate_rows if row["pv_has_repeat"]),
                "third_repeat_count": sum(
                    1 for row in candidate_rows if row["pv_reaches_repetition_limit"]
                ),
            }
        )
    candidate_stats.sort(
        key=lambda item: (
            item["top_count"],
            item["score_avg"] if item["score_avg"] is not None else -math.inf,
            -(item["score_stddev"] if item["score_stddev"] is not None else math.inf),
        ),
        reverse=True,
    )

    all_scores = [score_value(row) for row in rows if score_value(row) is not None]
    unique_leaders = sorted({item["leader"] for item in leaders})
    return {
        "config_count": len(config_keys),
        "row_count": len(rows),
        "completed": sum(1 for row in rows if row["stop"] == "completed"),
        "max_seconds": sum(1 for row in rows if row["stop"] == "max_seconds"),
        "score_min": min(all_scores) if all_scores else None,
        "score_median": median(all_scores),
        "score_avg": mean(all_scores),
        "score_max": max(all_scores) if all_scores else None,
        "leader_count": len(unique_leaders),
        "leaders": leaders,
        "unique_leaders": unique_leaders,
        "candidate_stats": candidate_stats,
    }


def write_markdown(path: Path, output: dict) -> None:
    config = output["config"]
    summary = output["summary"]
    lines = [
        "# Pikafish Parameter Combination Probe",
        "",
        "This is a multi-lens observation report. It is not a proof.",
        "",
        "## Configuration",
        "",
        f"- Candidates: `{', '.join(config['candidates'])}`.",
        f"- Depths: `{', '.join(map(str, config['depths']))}`.",
        f"- MultiPV values: `{', '.join(map(str, config['multipvs']))}`.",
        f"- Hash values: `{', '.join(map(str, config['hashes_mb']))} MB`.",
        f"- Threads values: `{', '.join(map(str, config['threads_list']))}`.",
        f"- Clear Hash modes: `{', '.join(map(str, config['clear_hash_modes']))}`.",
        f"- WDL modes: `{', '.join(map(str, config['show_wdl_modes']))}`.",
        f"- Per-query max seconds: `{config['per_query_max_seconds']}`.",
        f"- Wall runtime seconds: `{output['wall_runtime_seconds']}`.",
        f"- Cached search runtime seconds: `{output['cached_search_runtime_seconds']}`.",
        f"- Cache hits: `{output['cache']['hits']}`.",
        f"- Cache misses: `{output['cache']['misses']}`.",
        "",
        "## Summary",
        "",
        f"- Parameter configurations: `{summary['config_count']}`.",
        f"- Observation rows: `{summary['row_count']}`.",
        f"- Completed rows: `{summary['completed']}`.",
        f"- Max-second rows: `{summary['max_seconds']}`.",
        f"- Unique leaders: `{', '.join(summary['unique_leaders'])}`.",
        f"- Score range: `{summary['score_min']} .. {summary['score_max']}`.",
        "",
        "## Candidate Robustness",
        "",
        "| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |",
        "|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, item in enumerate(summary["candidate_stats"], start=1):
        lines.append(
            f"| {idx} | {item['red_move']} | {item['top_count']} | {item['top_share']} | "
            f"{item['score_avg']} | {item['score_range']} | {item['score_stddev']} | "
            f"{item['rank_avg']} | {item['reply_count']} | {item['pv_repeat_count']} |"
        )

    lines.extend(
        [
            "",
            "## Leaders By Configuration",
            "",
            "| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |",
            "|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|",
        ]
    )
    for item in summary["leaders"]:
        lines.append(
            f"| {item['depth']} | {item['multipv']} | {item['hash_mb']} | {item['threads']} | "
            f"{item['clear_hash']} | {item['show_wdl']} | {item['max_seconds']} | "
            f"{item['leader']} | {item['score']} | {item['reply']} |"
        )

    lines.extend(
        [
            "",
            "## Full Rows",
            "",
            "| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |",
            "|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|",
        ]
    )
    for row in output["rows"]:
        pv = " ".join(row.get("pv", [])[:10])
        lines.append(
            f"| {row['red_move']} | {row['depth']} | {row['multipv']} | {row['hash_mb']} | "
            f"{row['threads']} | {row['clear_hash']} | {row['show_wdl']} | {row['stop']} | "
            f"{row['best_reply']} | {row['top_red_score']} | {row['nodes']} | {row['time_ms']} | `{pv}` |"
        )

    lines.extend(
        [
            "",
            "## Closure Interpretation",
            "",
            "All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.",
            "A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Pikafish parameter-combination probe")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--candidates", type=parse_candidates, default=DEFAULT_CANDIDATES)
    parser.add_argument("--depths", type=parse_depths, default=[10, 12])
    parser.add_argument("--multipvs", type=parse_ints, default=[1, 2])
    parser.add_argument("--hashes-mb", type=parse_ints, default=[128])
    parser.add_argument("--threads-list", type=parse_ints, default=[1])
    parser.add_argument("--clear-hash-modes", type=parse_bools, default=[True])
    parser.add_argument("--show-wdl-modes", type=parse_bools, default=[True])
    parser.add_argument("--per-query-max-seconds", type=float, default=15.0)
    parser.add_argument("--repetition-limit", type=int, default=3)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--out-dir", default="reports/parameter-combo-pilot")
    args = parser.parse_args()

    started = time.time()
    out_dir = Path(args.out_dir)
    cache_dir = out_dir / "cache"
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    start_board = Board.from_fen(START_FEN)
    candidates = [str(item) for item in args.candidates]
    children = {}
    for candidate in candidates:
        child = apply_uci_if_legal(start_board, candidate)
        if child is None:
            raise SystemExit(f"illegal candidate move from start position: {candidate}")
        children[candidate] = child

    command_path = out_dir / "command.txt"
    command_path.write_text(" ".join(shlex.quote(item) for item in sys.argv) + "\n", encoding="utf-8")

    records = []
    cache_hits = 0
    cache_misses = 0
    for depth, multipv, hash_mb, threads, clear_hash, show_wdl in itertools.product(
        args.depths,
        args.multipvs,
        args.hashes_mb,
        args.threads_list,
        args.clear_hash_modes,
        args.show_wdl_modes,
    ):
        base_config = {
            "engine": args.engine,
            "engine_cwd": args.engine_cwd,
            "depth": depth,
            "multipv": multipv,
            "threads": threads,
            "hash_mb": hash_mb,
            "clear_hash": clear_hash,
            "show_wdl": show_wdl,
            "max_seconds": args.per_query_max_seconds,
            "repetition_limit": args.repetition_limit,
        }
        pending = [
            candidate
            for candidate in candidates
            if args.force or not (cache_dir / cache_name(candidate, base_config)).exists()
        ]
        engine = None
        try:
            if pending:
                engine = MultiPVEngine(
                    args.engine,
                    args.engine_cwd,
                    threads=threads,
                    hash_mb=hash_mb,
                    multipv=multipv,
                    show_wdl=show_wdl,
                )
            for candidate in candidates:
                config = dict(base_config)
                cache_path = cache_dir / cache_name(candidate, config)
                if cache_path.exists() and not args.force:
                    cache_hits += 1
                    record = json.loads(cache_path.read_text(encoding="utf-8"))
                    print(
                        f"[cache] d={depth} mpv={multipv} hash={hash_mb} "
                        f"threads={threads} clear={clear_hash} wdl={show_wdl} move={candidate}",
                        file=sys.stderr,
                        flush=True,
                    )
                else:
                    cache_misses += 1
                    assert engine is not None
                    child = children[candidate]
                    progress = (
                        f"[d {depth} mpv {multipv} h {hash_mb} t {threads} "
                        f"clear {clear_hash} wdl {show_wdl} {candidate}]"
                    )
                    analysis = engine.analyze(
                        child.to_fen(),
                        depth,
                        args.per_query_max_seconds,
                        clear_hash=clear_hash,
                        progress_prefix=progress,
                    )
                    record = build_record(candidate, child, config, analysis)
                    cache_path.write_text(
                        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8",
                    )
                    print(
                        f"[done] d={depth} mpv={multipv} hash={hash_mb} "
                        f"move={candidate} score={record['top']['red_score']} "
                        f"reply={record['top']['best_reply']} seconds={analysis['runtime_seconds']}",
                        file=sys.stderr,
                        flush=True,
                    )
                records.append(record)
        finally:
            if engine is not None:
                engine.close()

    rows = build_rows(records)
    output = {
        "start_fen": START_FEN,
        "config": {
            "engine": args.engine,
            "engine_cwd": args.engine_cwd,
            "candidates": candidates,
            "depths": args.depths,
            "multipvs": args.multipvs,
            "hashes_mb": args.hashes_mb,
            "threads_list": args.threads_list,
            "clear_hash_modes": args.clear_hash_modes,
            "show_wdl_modes": args.show_wdl_modes,
            "per_query_max_seconds": args.per_query_max_seconds,
            "repetition_limit": args.repetition_limit,
        },
        "wall_runtime_seconds": round(time.time() - started, 3),
        "cached_search_runtime_seconds": round(
            sum(record["query"]["runtime_seconds"] for record in records), 3
        ),
        "cache": {"hits": cache_hits, "misses": cache_misses},
        "records": records,
        "rows": rows,
        "summary": summarize(rows, candidates),
        "closure_level": "L0 Observation",
    }
    json_path = out_dir / "parameter_combo_probe_report.json"
    md_path = out_dir / "parameter_combo_probe_report.md"
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
                "summary": output["summary"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
