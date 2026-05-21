#!/usr/bin/env python3
"""Stateful runner for the 22 -> 33 -> 44 -> 55 -> 66 parameter ladder.

Each invocation runs one small chunk, writes state, and exits. It is designed
for a recurring Codex heartbeat, not for a single huge batch.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


CONTROL_MOVE = "h2e2"
INITIAL_CANDIDATES = ["c3c4", "b2e2", "c0e2", CONTROL_MOVE]


LADDER = [
    {
        "label": "22",
        "description": "depth x MultiPV",
        "depths": [10, 12],
        "multipvs": [1, 2],
        "hashes_mb": [128],
        "threads": [1],
        "clear_hash": [True],
        "show_wdl": [True],
        "max_seconds": 15.0,
        "candidate_limit": 4,
    },
    {
        "label": "33",
        "description": "depth x MultiPV x Hash",
        "depths": [12, 14, 16],
        "multipvs": [1, 2, 4],
        "hashes_mb": [64, 128, 256],
        "threads": [1],
        "clear_hash": [True],
        "show_wdl": [True],
        "max_seconds": 20.0,
        "candidate_limit": 4,
    },
    {
        "label": "44",
        "description": "depth x MultiPV x Hash x ClearHash",
        "depths": [12, 14, 16, 18],
        "multipvs": [1, 2, 3, 4],
        "hashes_mb": [64, 128, 256, 512],
        "threads": [1],
        "clear_hash": [True, False],
        "show_wdl": [True],
        "max_seconds": 25.0,
        "candidate_limit": 3,
    },
    {
        "label": "55",
        "description": "depth x MultiPV x Hash x ClearHash x Threads",
        "depths": [12, 14, 16, 18, 20],
        "multipvs": [1, 2, 3, 4, 6],
        "hashes_mb": [64, 128, 256, 512, 1024],
        "threads": [1, 2],
        "clear_hash": [True, False],
        "show_wdl": [True],
        "max_seconds": 30.0,
        "candidate_limit": 2,
    },
    {
        "label": "66",
        "description": "depth x MultiPV x Hash x ClearHash x Threads x WDL",
        "depths": [12, 14, 16, 18, 20, 22],
        "multipvs": [1, 2, 3, 4, 6, 8],
        "hashes_mb": [64, 128, 256, 512, 1024, 2048],
        "threads": [1, 2],
        "clear_hash": [True, False],
        "show_wdl": [True, False],
        "max_seconds": 30.0,
        "candidate_limit": 2,
    },
]


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def all_configs(stage: dict) -> List[dict]:
    configs = []
    for depth in stage["depths"]:
        for multipv in stage["multipvs"]:
            for hash_mb in stage["hashes_mb"]:
                for threads in stage["threads"]:
                    for clear_hash in stage["clear_hash"]:
                        for show_wdl in stage["show_wdl"]:
                            configs.append(
                                {
                                    "depth": depth,
                                    "multipv": multipv,
                                    "hash_mb": hash_mb,
                                    "threads": threads,
                                    "clear_hash": clear_hash,
                                    "show_wdl": show_wdl,
                                    "max_seconds": stage["max_seconds"],
                                }
                            )
    return configs


def command_for_config(
    candidates: List[str],
    config: dict,
    out_dir: Path,
    engine: str,
    engine_cwd: str,
) -> List[str]:
    return [
        sys.executable,
        "parameter_combo_probe.py",
        "--engine",
        engine,
        "--engine-cwd",
        engine_cwd,
        "--candidates",
        ",".join(candidates),
        "--depths",
        str(config["depth"]),
        "--multipvs",
        str(config["multipv"]),
        "--hashes-mb",
        str(config["hash_mb"]),
        "--threads-list",
        str(config["threads"]),
        "--clear-hash-modes",
        bool_text(config["clear_hash"]),
        "--show-wdl-modes",
        bool_text(config["show_wdl"]),
        "--per-query-max-seconds",
        str(config["max_seconds"]),
        "--out-dir",
        str(out_dir),
    ]


def report_path_for(round_dir: Path) -> Path:
    return round_dir / "parameter_combo_probe_report.json"


def load_rows(report_paths: Iterable[Path]) -> List[dict]:
    rows = []
    for path in report_paths:
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            rows.extend(data.get("rows", []))
    return rows


def score_value(row: dict) -> int | None:
    score = row.get("top_red_score")
    return score if isinstance(score, int) else None


def candidate_stats(rows: List[dict], candidates: List[str]) -> List[dict]:
    config_keys = sorted(
        {
            (
                row["depth"],
                row["multipv"],
                row["hash_mb"],
                row["threads"],
                row["clear_hash"],
                row["show_wdl"],
                row["max_seconds"],
            )
            for row in rows
        }
    )
    top_counts = {candidate: 0 for candidate in candidates}
    ranks = {candidate: [] for candidate in candidates}
    for key in config_keys:
        bucket = [
            row
            for row in rows
            if (
                row["depth"],
                row["multipv"],
                row["hash_mb"],
                row["threads"],
                row["clear_hash"],
                row["show_wdl"],
                row["max_seconds"],
            )
            == key
            and score_value(row) is not None
        ]
        bucket.sort(key=lambda row: (score_value(row), row["red_move"]), reverse=True)
        if not bucket:
            continue
        top_counts[bucket[0]["red_move"]] = top_counts.get(bucket[0]["red_move"], 0) + 1
        for idx, row in enumerate(bucket, start=1):
            ranks.setdefault(row["red_move"], []).append(idx)

    stats = []
    for candidate in candidates:
        items = [row for row in rows if row["red_move"] == candidate and score_value(row) is not None]
        scores = [score_value(row) for row in items]
        replies = sorted({row["best_reply"] for row in items if row.get("best_reply")})
        rank_items = ranks.get(candidate, [])
        stats.append(
            {
                "red_move": candidate,
                "observations": len(items),
                "top_count": top_counts.get(candidate, 0),
                "top_share": round(top_counts.get(candidate, 0) / len(config_keys), 3)
                if config_keys
                else None,
                "score_avg": round(sum(scores) / len(scores), 3) if scores else None,
                "score_min": min(scores) if scores else None,
                "score_max": max(scores) if scores else None,
                "score_range": (max(scores) - min(scores)) if scores else None,
                "rank_avg": round(sum(rank_items) / len(rank_items), 3) if rank_items else None,
                "reply_count": len(replies),
                "replies": replies,
                "pv_repeat_count": sum(1 for row in items if row.get("pv_has_repeat")),
            }
        )
    stats.sort(
        key=lambda item: (
            item["top_count"],
            item["score_avg"] if item["score_avg"] is not None else -math.inf,
            -(item["score_range"] if item["score_range"] is not None else math.inf),
        ),
        reverse=True,
    )
    return stats


def choose_candidates(stats: List[dict], limit: int) -> List[str]:
    chosen = [item["red_move"] for item in stats[:limit]]
    if CONTROL_MOVE not in chosen and len(chosen) < limit:
        chosen.append(CONTROL_MOVE)
    elif CONTROL_MOVE not in chosen and chosen:
        chosen[-1] = CONTROL_MOVE
    return chosen


def stage_report_paths(base_dir: Path, stage_label: str) -> List[Path]:
    return sorted(base_dir.glob(f"round-*/stage-{stage_label}/config-*/parameter_combo_probe_report.json"))


def estimate_configs_to_run(
    state: dict,
    candidate_count: int,
    target_seconds: float,
    remaining_configs: int,
) -> Tuple[int, float]:
    avg_query_seconds = float(state.get("avg_query_seconds") or 1.0)
    estimated_per_config = max(0.2, avg_query_seconds * candidate_count * 1.3)
    count = max(1, int(target_seconds // estimated_per_config))
    return min(count, remaining_configs), estimated_per_config


def interval_for_seconds(seconds: float) -> int:
    if seconds <= 300:
        return 5
    return int(math.ceil(seconds / 300.0) * 5)


def write_markdown_summary(path: Path, summary: dict) -> None:
    lines = [
        "# Combo Auto Runner Summary",
        "",
        f"- Run id: `{summary['run_id']}`.",
        f"- Stage: `{summary['stage_label']}`.",
        f"- Stage description: `{summary['stage_description']}`.",
        f"- Status: `{summary['status']}`.",
        f"- Candidates: `{', '.join(summary['candidates'])}`.",
        f"- Configs run this invocation: `{summary['configs_run']}`.",
        f"- Stage cursor: `{summary['stage_cursor']} / {summary['stage_total_configs']}`.",
        f"- Wall runtime seconds: `{summary['wall_runtime_seconds']}`.",
        f"- Average query seconds: `{summary['avg_query_seconds']}`.",
        f"- Recommended interval minutes: `{summary['recommended_interval_minutes']}`.",
        "",
        "## Candidate Stats",
        "",
        "| Rank | Move | Top count | Top share | Avg score | Score range | Avg rank | Reply variants |",
        "|---:|:---|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, item in enumerate(summary["candidate_stats"], start=1):
        lines.append(
            f"| {idx} | {item['red_move']} | {item['top_count']} | {item['top_share']} | "
            f"{item['score_avg']} | {item['score_range']} | {item['rank_avg']} | {item['reply_count']} |"
        )
    lines.extend(
        [
            "",
            "## Next",
            "",
            f"- Next stage: `{summary['next_stage_label']}`.",
            f"- Next candidates: `{', '.join(summary['next_candidates'])}`.",
            f"- Closure level: `{summary['closure_level']}`.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def default_state() -> dict:
    return {
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "round": 0,
        "stage_index": 0,
        "stage_cursor": 0,
        "candidate_pool": INITIAL_CANDIDATES,
        "avg_query_seconds": 1.0,
        "history": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one scheduled chunk of the parameter ladder")
    parser.add_argument("--base-dir", default="reports/parameter-combo-auto")
    parser.add_argument("--target-seconds", type=float, default=300.0)
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    started = time.time()
    base_dir = Path(args.base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)
    state_path = base_dir / "state.json"
    state = load_json(state_path, default_state())
    if int(state["stage_index"]) >= len(LADDER):
        print(json.dumps({"status": "complete", "state": state}, ensure_ascii=False, indent=2))
        return 0

    stage = LADDER[int(state["stage_index"])]
    stage_configs = all_configs(stage)
    stage_cursor = int(state.get("stage_cursor", 0))
    remaining = len(stage_configs) - stage_cursor
    if remaining <= 0:
        state["stage_index"] = int(state["stage_index"]) + 1
        state["stage_cursor"] = 0
        write_json(state_path, state)
        print(json.dumps({"status": "advanced_stage", "state": state}, ensure_ascii=False, indent=2))
        return 0

    candidates = list(state.get("candidate_pool") or INITIAL_CANDIDATES)
    candidates = candidates[: int(stage["candidate_limit"])]
    if CONTROL_MOVE in state.get("candidate_pool", []) and CONTROL_MOVE not in candidates:
        candidates[-1] = CONTROL_MOVE

    configs_to_run, estimated_per_config = estimate_configs_to_run(
        state, len(candidates), args.target_seconds, remaining
    )
    selected = stage_configs[stage_cursor : stage_cursor + configs_to_run]
    run_id = f"round-{int(state['round']) + 1:04d}"
    stage_dir = base_dir / run_id / f"stage-{stage['label']}"
    generated_reports = []

    if args.dry_run:
        summary = {
            "status": "dry_run",
            "run_id": run_id,
            "stage_label": stage["label"],
            "stage_description": stage["description"],
            "candidates": candidates,
            "configs_run": configs_to_run,
            "stage_cursor": stage_cursor,
            "stage_total_configs": len(stage_configs),
            "estimated_per_config_seconds": round(estimated_per_config, 3),
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    for offset, config in enumerate(selected, start=stage_cursor):
        config_dir = stage_dir / f"config-{offset + 1:04d}"
        command = command_for_config(candidates, config, config_dir, args.engine, args.engine_cwd)
        result = subprocess.run(command, text=True, capture_output=True)
        if result.returncode != 0:
            failure = {
                "status": "failed",
                "run_id": run_id,
                "stage": stage["label"],
                "config": config,
                "returncode": result.returncode,
                "stdout": result.stdout[-4000:],
                "stderr": result.stderr[-4000:],
            }
            failure_path = stage_dir / "failure.json"
            write_json(failure_path, failure)
            print(json.dumps(failure, ensure_ascii=False, indent=2))
            return result.returncode
        report_path = report_path_for(config_dir)
        generated_reports.append(report_path)

    rows = load_rows(generated_reports)
    total_runtime = time.time() - started
    query_count = max(1, len(rows))
    actual_avg_query = total_runtime / query_count
    previous_avg = float(state.get("avg_query_seconds") or actual_avg_query)
    state["avg_query_seconds"] = round((previous_avg * 0.65) + (actual_avg_query * 0.35), 3)
    state["round"] = int(state["round"]) + 1
    state["stage_cursor"] = stage_cursor + configs_to_run
    state["updated_at"] = now_iso()

    stage_complete = state["stage_cursor"] >= len(stage_configs)
    stage_rows = load_rows(stage_report_paths(base_dir, stage["label"]))
    stats = candidate_stats(stage_rows, candidates) if stage_rows else candidate_stats(rows, candidates)
    next_candidates = candidates
    next_stage_label = stage["label"]
    status = "stage_partial"
    if stage_complete:
        next_stage_index = int(state["stage_index"]) + 1
        if next_stage_index < len(LADDER):
            next_stage = LADDER[next_stage_index]
            next_candidates = choose_candidates(stats, int(next_stage["candidate_limit"]))
            state["stage_index"] = next_stage_index
            state["stage_cursor"] = 0
            state["candidate_pool"] = next_candidates
            next_stage_label = next_stage["label"]
            status = "stage_complete_advanced"
        else:
            next_stage_label = "complete"
            status = "complete"

    predicted_next_seconds = (
        float(state.get("avg_query_seconds") or 1.0)
        * max(1, len(state.get("candidate_pool") or candidates))
        * 1.3
    )
    recommended_interval = interval_for_seconds(max(total_runtime, predicted_next_seconds))
    state["history"].append(
        {
            "run_id": run_id,
            "stage": stage["label"],
            "status": status,
            "configs_run": configs_to_run,
            "stage_cursor_after": state["stage_cursor"],
            "wall_runtime_seconds": round(total_runtime, 3),
            "recommended_interval_minutes": recommended_interval,
            "created_at": now_iso(),
        }
    )
    write_json(state_path, state)

    summary = {
        "status": status,
        "run_id": run_id,
        "stage_label": stage["label"],
        "stage_description": stage["description"],
        "candidates": candidates,
        "configs_run": configs_to_run,
        "stage_cursor": state["stage_cursor"] if not stage_complete else len(stage_configs),
        "stage_total_configs": len(stage_configs),
        "wall_runtime_seconds": round(total_runtime, 3),
        "avg_query_seconds": state["avg_query_seconds"],
        "recommended_interval_minutes": recommended_interval,
        "candidate_stats": stats,
        "next_stage_label": next_stage_label,
        "next_candidates": state.get("candidate_pool", next_candidates),
        "closure_level": "L0 Observation",
        "reports": [str(path) for path in generated_reports],
        "state_path": str(state_path),
    }
    summary_path = base_dir / run_id / "combo_auto_summary.json"
    summary_md_path = base_dir / run_id / "combo_auto_summary.md"
    write_json(summary_path, summary)
    write_markdown_summary(summary_md_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
