#!/usr/bin/env python3
"""Dense low-depth opening probe across depth and MultiPV settings.

This collector is for parameter sensitivity, not proof. It runs every legal red
opening move under several small depth and MultiPV settings, then reports score
spread, top-move stability, PV repetition, and resource use.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from light_prover import START_FEN, Board
from opening_probe import MultiPVEngine, parse_depths, replay_pv, score_from_red_view


def parse_ints(text: str) -> List[int]:
    values = []
    for part in text.split(","):
        part = part.strip()
        if part:
            values.append(int(part))
    if not values:
        raise argparse.ArgumentTypeError("at least one integer is required")
    return values


def enrich_infos(infos: Iterable[dict], board: Board, repetition_limit: int) -> List[dict]:
    enriched = []
    for info in infos:
        item = dict(info)
        item["red_score"] = score_from_red_view(item, board.side)
        item.update(replay_pv(board, item.get("pv", []), repetition_limit))
        enriched.append(item)
    return enriched


def score_value(row: dict) -> Optional[int]:
    value = row.get("top_red_score")
    return value if isinstance(value, int) else None


def median(values: List[int]) -> Optional[float]:
    return statistics.median(values) if values else None


def avg(values: List[int]) -> Optional[float]:
    return round(statistics.mean(values), 2) if values else None


def build_rows(runs: List[dict]) -> List[dict]:
    rows = []
    for run in runs:
        multipv_setting = run["multipv"]
        for record in run["records"]:
            for query in record["queries"]:
                top = query["multipv"][0] if query["multipv"] else {}
                pv = top.get("pv", []) if top else []
                rows.append(
                    {
                        "multipv": multipv_setting,
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
                        "pv": pv,
                        "captured_multipv": len(query["multipv"]),
                    }
                )
    return rows


def summarize_rows(rows: List[dict]) -> dict:
    summary = {}
    keys = sorted({(row["multipv"], row["depth"]) for row in rows})
    for multipv, depth in keys:
        bucket = [row for row in rows if row["multipv"] == multipv and row["depth"] == depth]
        scores = [score_value(row) for row in bucket]
        scores = [score for score in scores if score is not None]
        ranked = sorted(
            [row for row in bucket if score_value(row) is not None],
            key=lambda row: (score_value(row), row["red_move"]),
            reverse=True,
        )
        summary[f"mpv{multipv}_d{depth}"] = {
            "multipv": multipv,
            "depth": depth,
            "positions": len(bucket),
            "completed": sum(1 for row in bucket if row["stop"] == "completed"),
            "max_seconds": sum(1 for row in bucket if row["stop"] == "max_seconds"),
            "score_min": min(scores) if scores else None,
            "score_median": median(scores),
            "score_avg": avg(scores),
            "score_max": max(scores) if scores else None,
            "pv_repeat": sum(1 for row in bucket if row["pv_has_repeat"]),
            "pv_third_repeat": sum(1 for row in bucket if row["pv_reaches_repetition_limit"]),
            "leader": ranked[0] if ranked else None,
            "top5": ranked[:5],
        }
    return summary


def build_stability(rows: List[dict], depths: List[int], multipvs: List[int]) -> dict:
    final_depth = max(depths)
    final_rows = [row for row in rows if row["depth"] == final_depth]
    by_mpv: Dict[int, Dict[str, dict]] = {}
    for multipv in multipvs:
        by_mpv[multipv] = {
            row["red_move"]: row for row in final_rows if row["multipv"] == multipv
        }

    reference_mpv = max(multipvs)
    reference = by_mpv.get(reference_mpv, {})
    move_stability = []
    for red_move in sorted(reference):
        ref = reference[red_move]
        scores = []
        replies = []
        for multipv in multipvs:
            row = by_mpv.get(multipv, {}).get(red_move)
            if not row:
                continue
            if score_value(row) is not None:
                scores.append(score_value(row))
            if row.get("best_reply"):
                replies.append(row["best_reply"])
        move_stability.append(
            {
                "red_move": red_move,
                "reference_score": ref.get("top_red_score"),
                "reference_reply": ref.get("best_reply"),
                "score_range": (max(scores) - min(scores)) if scores else None,
                "reply_count": len(set(replies)),
                "replies": sorted(set(replies)),
            }
        )
    move_stability.sort(
        key=lambda item: (
            item["score_range"] if item["score_range"] is not None else -1,
            item["reply_count"],
        ),
        reverse=True,
    )

    leaders = []
    for multipv in multipvs:
        for depth in depths:
            bucket = [
                row
                for row in rows
                if row["multipv"] == multipv
                and row["depth"] == depth
                and score_value(row) is not None
            ]
            bucket.sort(key=lambda row: (score_value(row), row["red_move"]), reverse=True)
            if bucket:
                leaders.append(
                    {
                        "multipv": multipv,
                        "depth": depth,
                        "red_move": bucket[0]["red_move"],
                        "score": bucket[0]["top_red_score"],
                        "best_reply": bucket[0]["best_reply"],
                    }
                )

    return {
        "final_depth": final_depth,
        "reference_multipv": reference_mpv,
        "leaders": leaders,
        "most_sensitive_final_depth_moves": move_stability[:10],
    }


def write_markdown(path: Path, output: dict) -> None:
    config = output["config"]
    summary = output["summary"]
    stability = output["stability"]
    final_depth = stability["final_depth"]
    reference_mpv = stability["reference_multipv"]

    lines = [
        "# Pikafish Small Grid Opening Probe",
        "",
        "This is a dense low-depth parameter probe, not a game-theoretic proof.",
        "",
        "## Configuration",
        "",
        f"- Start FEN: `{output['start_fen']}`.",
        f"- Red opening moves: `{output['red_move_count']}`.",
        f"- Depths: `{', '.join(map(str, config['depths']))}`.",
        f"- MultiPV settings: `{', '.join(map(str, config['multipvs']))}`.",
        f"- Threads: `{config['threads']}`.",
        f"- Hash: `{config['hash_mb']} MB`.",
        f"- Clear hash per query: `{config['clear_hash']}`.",
        f"- Per-query max seconds: `{config['per_query_max_seconds']}`.",
        f"- Runtime seconds: `{output['runtime_seconds']}`.",
        "",
        "Each MultiPV setting runs one `go depth max(depths)` per red opening move and captures the requested intermediate depths.",
        "",
        "Scores are normalized to Red's point of view.",
        "",
        "## Grid Summary",
        "",
        "| MultiPV | Depth | Positions | Completed | Max seconds | Min | Median | Avg | Max | PV repeat | PV third-repeat | Leader | Score | Reply |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---|---:|:---|",
    ]
    for key in sorted(summary, key=lambda k: (summary[k]["multipv"], summary[k]["depth"])):
        item = summary[key]
        leader = item["leader"] or {}
        lines.append(
            f"| {item['multipv']} | {item['depth']} | {item['positions']} | "
            f"{item['completed']} | {item['max_seconds']} | {item['score_min']} | "
            f"{item['score_median']} | {item['score_avg']} | {item['score_max']} | "
            f"{item['pv_repeat']} | {item['pv_third_repeat']} | "
            f"{leader.get('red_move')} | {leader.get('top_red_score')} | {leader.get('best_reply')} |"
        )

    lines.extend(
        [
            "",
            "## Leaders By Parameter",
            "",
            "| MultiPV | Depth | Red move | Red score | Black reply |",
            "|---:|---:|:---|---:|:---|",
        ]
    )
    for item in stability["leaders"]:
        lines.append(
            f"| {item['multipv']} | {item['depth']} | {item['red_move']} | "
            f"{item['score']} | {item['best_reply']} |"
        )

    reference_rows = [
        row
        for row in output["rows"]
        if row["multipv"] == reference_mpv
        and row["depth"] == final_depth
        and score_value(row) is not None
    ]
    reference_rows.sort(key=lambda row: (score_value(row), row["red_move"]), reverse=True)
    lines.extend(
        [
            "",
            f"## Depth {final_depth} MultiPV {reference_mpv} Top Red Moves",
            "",
            "| Rank | Red move | Reply | Red score | Nodes | Time ms | PV repeat |",
            "|---:|:---|:---|---:|---:|---:|:---:|",
        ]
    )
    for idx, row in enumerate(reference_rows[:10], start=1):
        lines.append(
            f"| {idx} | {row['red_move']} | {row['best_reply']} | {row['top_red_score']} | "
            f"{row['nodes']} | {row['time_ms']} | {row['pv_has_repeat']} |"
        )

    lines.extend(
        [
            "",
            f"## Depth {final_depth} MultiPV {reference_mpv} Bottom Red Moves",
            "",
            "| Rank | Red move | Reply | Red score | Nodes | Time ms | PV repeat |",
            "|---:|:---|:---|---:|---:|---:|:---:|",
        ]
    )
    for idx, row in enumerate(list(reversed(reference_rows[-10:])), start=1):
        lines.append(
            f"| {idx} | {row['red_move']} | {row['best_reply']} | {row['top_red_score']} | "
            f"{row['nodes']} | {row['time_ms']} | {row['pv_has_repeat']} |"
        )

    lines.extend(
        [
            "",
            f"## Most Sensitive Moves At Depth {final_depth}",
            "",
            f"Reference is MultiPV `{reference_mpv}`. `Score range` is the spread across MultiPV settings at the final depth.",
            "",
            "| Red move | Reference score | Reference reply | Score range | Reply variants |",
            "|:---|---:|:---|---:|:---|",
        ]
    )
    for item in stability["most_sensitive_final_depth_moves"]:
        lines.append(
            f"| {item['red_move']} | {item['reference_score']} | {item['reference_reply']} | "
            f"{item['score_range']} | {', '.join(item['replies'])} |"
        )

    lines.extend(
        [
            "",
            "## Full Rows",
            "",
            "| MultiPV | Red move | Depth | Stop | Reply | Red score | Nodes | Time ms | Captured PVs | Top PV |",
            "|---:|:---|---:|:---|:---|---:|---:|---:|---:|:---|",
        ]
    )
    for row in output["rows"]:
        pv = " ".join(row.get("pv", [])[:10])
        lines.append(
            f"| {row['multipv']} | {row['red_move']} | {row['depth']} | {row['stop']} | "
            f"{row['best_reply']} | {row['top_red_score']} | {row['nodes']} | "
            f"{row['time_ms']} | {row['captured_multipv']} | `{pv}` |"
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Dense small opening probe over depth and MultiPV")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--depths", type=parse_depths, default=[4, 6, 8, 10, 12])
    parser.add_argument("--multipvs", type=parse_ints, default=[1, 2, 3, 4])
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--hash-mb", type=int, default=64)
    parser.add_argument("--per-query-max-seconds", type=float, default=15.0)
    parser.add_argument("--repetition-limit", type=int, default=3)
    parser.add_argument("--no-clear-hash", action="store_true")
    parser.add_argument("--no-wdl", action="store_true")
    parser.add_argument("--out-dir", default="reports/opening-grid-small")
    args = parser.parse_args()

    started = time.time()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "opening_grid_small_report.json"
    md_path = out_dir / "opening_grid_small_report.md"

    start_board = Board.from_fen(START_FEN)
    red_moves = sorted(start_board.legal_moves(), key=lambda move: move.uci())
    go_depth = max(args.depths)
    runs = []

    for multipv_index, multipv in enumerate(args.multipvs, start=1):
        print(
            f"[multipv {multipv_index}/{len(args.multipvs)}] MultiPV={multipv}",
            file=sys.stderr,
            flush=True,
        )
        engine = MultiPVEngine(
            args.engine,
            args.engine_cwd,
            threads=args.threads,
            hash_mb=args.hash_mb,
            multipv=multipv,
            show_wdl=not args.no_wdl,
        )
        records = []
        try:
            for index, red_move in enumerate(red_moves, start=1):
                child = start_board.make_move(red_move)
                analysis = engine.analyze(
                    child.to_fen(),
                    go_depth,
                    args.per_query_max_seconds,
                    clear_hash=not args.no_clear_hash,
                    progress_prefix=f"[mpv {multipv} {index}/{len(red_moves)} {red_move.uci()}]",
                    snapshot_depths=args.depths,
                )
                record = {
                    "index": index,
                    "red_move": red_move.uci(),
                    "fen_after_red_move": child.to_fen(),
                    "queries": [],
                }
                for depth in args.depths:
                    snapshot_infos = [
                        dict(info) for info in analysis["snapshots"].get(str(depth), [])
                    ]
                    if depth == go_depth and not snapshot_infos:
                        snapshot_infos = [dict(info) for info in analysis["multipv"]]
                    snapshot_infos = enrich_infos(snapshot_infos, child, args.repetition_limit)
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
                final_top = record["queries"][-1]["multipv"][0] if record["queries"][-1]["multipv"] else {}
                print(
                    f"[done] MultiPV={multipv} red={red_move.uci()} "
                    f"reply={record['queries'][-1]['bestmove']} "
                    f"red_score={final_top.get('red_score')} "
                    f"seconds={analysis['runtime_seconds']}",
                    file=sys.stderr,
                    flush=True,
                )
                records.append(record)
        finally:
            engine.close()
        runs.append({"multipv": multipv, "records": records})

    rows = build_rows(runs)
    output = {
        "start_fen": START_FEN,
        "red_move_count": len(red_moves),
        "config": {
            "engine": args.engine,
            "engine_cwd": args.engine_cwd,
            "depths": args.depths,
            "multipvs": args.multipvs,
            "threads": args.threads,
            "hash_mb": args.hash_mb,
            "clear_hash": not args.no_clear_hash,
            "show_wdl": not args.no_wdl,
            "go_depth": go_depth,
            "per_query_max_seconds": args.per_query_max_seconds,
            "repetition_limit": args.repetition_limit,
        },
        "runtime_seconds": round(time.time() - started, 3),
        "runs": runs,
        "rows": rows,
        "summary": summarize_rows(rows),
        "stability": build_stability(rows, args.depths, args.multipvs),
    }
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, output)
    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "red_move_count": output["red_move_count"],
                "runtime_seconds": output["runtime_seconds"],
                "depths": args.depths,
                "multipvs": args.multipvs,
                "final_depth": output["stability"]["final_depth"],
                "reference_multipv": output["stability"]["reference_multipv"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

