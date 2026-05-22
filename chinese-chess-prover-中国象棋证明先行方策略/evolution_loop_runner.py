#!/usr/bin/env python3
"""Self-evolution loop for the Chinese chess Pikafish experiment.

Each invocation reads the previous evidence, writes a retrospective, chooses
one small next lens, optionally executes it, and persists the result for the
next invocation.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Iterable


CANDIDATES = ["h2e2", "c3c4"]
MOVE_NAMES = {
    "h2e2": "炮八平五",
    "c3c4": "兵三进一",
}


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def score_value(row: dict) -> int | None:
    score = row.get("top_red_score")
    return score if isinstance(score, int) else None


def config_key(row: dict) -> tuple:
    return (
        row.get("depth"),
        row.get("multipv"),
        row.get("hash_mb"),
        row.get("threads"),
        row.get("clear_hash"),
        row.get("show_wdl"),
        row.get("max_seconds"),
    )


def candidate_stats(rows: list[dict], candidates: list[str]) -> list[dict]:
    keys = sorted({config_key(row) for row in rows})
    top_counts = {candidate: 0 for candidate in candidates}
    ranks: dict[str, list[int]] = {candidate: [] for candidate in candidates}
    for key in keys:
        bucket = [row for row in rows if config_key(row) == key and score_value(row) is not None]
        bucket.sort(key=lambda row: (score_value(row), row.get("red_move", "")), reverse=True)
        if not bucket:
            continue
        top_counts[bucket[0]["red_move"]] = top_counts.get(bucket[0]["red_move"], 0) + 1
        for idx, row in enumerate(bucket, start=1):
            ranks.setdefault(row["red_move"], []).append(idx)

    stats = []
    for candidate in candidates:
        items = [row for row in rows if row.get("red_move") == candidate and score_value(row) is not None]
        scores = [score_value(row) for row in items]
        replies = sorted({row.get("best_reply") for row in items if row.get("best_reply")})
        rank_items = ranks.get(candidate, [])
        stats.append(
            {
                "red_move": candidate,
                "move_name": MOVE_NAMES.get(candidate, ""),
                "observations": len(items),
                "top_count": top_counts.get(candidate, 0),
                "top_share": round(top_counts.get(candidate, 0) / len(keys), 3) if keys else None,
                "score_avg": round(sum(scores) / len(scores), 3) if scores else None,
                "score_min": min(scores) if scores else None,
                "score_max": max(scores) if scores else None,
                "score_range": max(scores) - min(scores) if scores else None,
                "rank_avg": round(sum(rank_items) / len(rank_items), 3) if rank_items else None,
                "reply_count": len(replies),
                "replies": replies,
                "pv_repeat_count": sum(1 for row in items if row.get("pv_has_repeat")),
                "max_seconds_count": sum(1 for row in items if row.get("stop") == "max_seconds"),
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


def latest_combo_summary(reports_dir: Path) -> dict:
    path = reports_dir / "parameter-combo-auto" / "round-0030" / "combo_auto_summary.json"
    return load_json(path, {})


def default_state() -> dict:
    return {
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "round": 0,
        "closure_level": "L0 Observation",
        "candidate_pool": CANDIDATES,
        "history": [],
    }


def choose_action(round_no: int, state: dict, target_seconds: int) -> dict:
    history = state.get("history", [])
    last = history[-1] if history else {}
    last_action = last.get("action", {})
    last_result = last.get("result", {})
    stable = (
        last_result.get("leader") == "h2e2"
        and (last_result.get("score_gap") or 0) >= 2
        and (last_result.get("pv_repeat_total") or 0) == 0
        and (last_result.get("max_seconds_total") or 0) == 0
    )
    recent = history[-3:]
    repeated_c3c4_lens = (
        len(recent) == 3
        and all(item.get("result", {}).get("leader") == "c3c4" for item in recent)
        and all((item.get("result", {}).get("max_seconds_total") or 0) == 0 for item in recent)
        and all((item.get("result", {}).get("pv_repeat_total") or 0) == 0 for item in recent)
        and all(item.get("action", {}).get("depth") == 28 for item in recent)
        and all(item.get("action", {}).get("multipvs") == [8] for item in recent)
        and all(item.get("action", {}).get("hashes_mb") == [1024, 2048] for item in recent)
    )

    if not history:
        depth = 24
        hashes = [512, 1024]
        multipvs = [4, 8]
        reason = "首轮攻击 66 阶段最高 depth 只有 22 的弱点，用 depth 24 做 frontier extension。"
    elif stable:
        depth = min(30, int(last_action.get("depth", 24)) + 2)
        hashes = [1024, 2048] if depth >= 26 else [512, 1024]
        multipvs = [4, 8]
        reason = "上一轮 h2e2 稳定领先，下一轮增加 depth，测试领先是否延续。"
    elif repeated_c3c4_lens:
        depth = 28
        hashes = [512, 1024]
        multipvs = [6]
        reason = "c3c4 已在同一 depth 28 / MultiPV 8 镜头连续复现，下一轮改用 MultiPV 6 和较小 Hash 做交叉复查，避免重复同一证据。"
    else:
        depth = int(last_action.get("depth", 24))
        hashes = [1024, 2048]
        multipvs = [8]
        reason = "上一轮存在反转、超时或重复风险，下一轮不加深，改用更宽 MultiPV 和 Hash 复查。"

    queries = len(CANDIDATES) * len(hashes) * len(multipvs)
    per_query = max(20.0, min(180.0, round((target_seconds / max(1, queries)) * 1.1, 1)))
    return {
        "kind": "frontier_extension",
        "reason": reason,
        "candidates": CANDIDATES,
        "depth": depth,
        "multipvs": multipvs,
        "hashes_mb": hashes,
        "threads": [1],
        "clear_hash": [True],
        "show_wdl": [True],
        "per_query_max_seconds": per_query,
        "target_seconds": target_seconds,
    }


def command_for_action(action: dict, out_dir: Path, engine: str, engine_cwd: str) -> list[str]:
    return [
        sys.executable,
        "parameter_combo_probe.py",
        "--engine",
        engine,
        "--engine-cwd",
        engine_cwd,
        "--candidates",
        ",".join(action["candidates"]),
        "--depths",
        str(action["depth"]),
        "--multipvs",
        ",".join(str(value) for value in action["multipvs"]),
        "--hashes-mb",
        ",".join(str(value) for value in action["hashes_mb"]),
        "--threads-list",
        ",".join(str(value) for value in action["threads"]),
        "--clear-hash-modes",
        ",".join(bool_text(value) for value in action["clear_hash"]),
        "--show-wdl-modes",
        ",".join(bool_text(value) for value in action["show_wdl"]),
        "--per-query-max-seconds",
        str(action["per_query_max_seconds"]),
        "--out-dir",
        str(out_dir),
    ]


def summarize_experiment(report_path: Path) -> dict:
    data = load_json(report_path, {})
    rows = data.get("rows", [])
    stats = candidate_stats(rows, CANDIDATES)
    leader = stats[0]["red_move"] if stats else None
    score_gap = None
    if len(stats) >= 2 and stats[0].get("score_avg") is not None and stats[1].get("score_avg") is not None:
        score_gap = round(stats[0]["score_avg"] - stats[1]["score_avg"], 3)
    return {
        "report_path": str(report_path),
        "rows": len(rows),
        "completed_rows": sum(1 for row in rows if row.get("stop") == "completed"),
        "max_seconds_total": sum(1 for row in rows if row.get("stop") == "max_seconds"),
        "pv_repeat_total": sum(1 for row in rows if row.get("pv_has_repeat")),
        "leader": leader,
        "score_gap": score_gap,
        "candidate_stats": stats,
    }


def table_stats(stats: Iterable[dict]) -> str:
    lines = [
        "| Rank | Move | 象棋记法 | Top count | Top share | Avg score | Score range | Avg rank | Replies | Max seconds |",
        "|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for idx, item in enumerate(stats, start=1):
        lines.append(
            "| {rank} | `{move}` | {name} | `{top}` | `{share}` | `{avg}` | `{rng}` | `{rank_avg}` | `{replies}` | `{max_seconds}` |".format(
                rank=idx,
                move=item["red_move"],
                name=item.get("move_name", ""),
                top=item.get("top_count"),
                share=item.get("top_share"),
                avg=item.get("score_avg"),
                rng=item.get("score_range"),
                rank_avg=item.get("rank_avg"),
                replies=item.get("reply_count"),
                max_seconds=item.get("max_seconds_count"),
            )
        )
    return "\n".join(lines)


def reliability_note(result: dict | None) -> str:
    if not result or not result.get("leader"):
        return "本轮没有新搜索结果，只完成复盘和下一轮策略生成。"
    if (
        result.get("leader") == "h2e2"
        and (result.get("score_gap") or 0) >= 2
        and result.get("pv_repeat_total") == 0
        and result.get("max_seconds_total") == 0
    ):
        return "本轮继续支持 `h2e2` 稳定领先，但仍只能保持 L0，尚未形成证明义务。"
    return "本轮出现反转、差距不足、重复或超时风险；下一轮应优先复查稳定性，而不是升级结论。"


def write_summary(round_dir: Path, round_no: int, action: dict, result: dict | None, combo: dict, executed: bool) -> str:
    stats_md = table_stats(result.get("candidate_stats", [])) if result else ""
    command_path = round_dir / "experiment" / "parameter_combo_probe_report.json"
    md = f"""# Self Evolution Loop Round {round_no:04d}

## 结论等级

```text
L0 Observation
```

本轮仍然不把 Pikafish 分数、bestmove 或 PV 写成证明。

## 事实复盘

- `66` 阶段最终候选：`{', '.join(combo.get('candidates', CANDIDATES))}`。
- `66` 阶段状态：`{combo.get('status', 'unknown')}`。
- `66` 阶段 cursor：`{combo.get('stage_cursor', 'unknown')} / {combo.get('stage_total_configs', 'unknown')}`。
- 当前闭环目标：在小资源下持续攻击最弱假设，筛出可进入 proof obligation 的候选。

## 自我进化

本轮识别的薄弱点：

- `66` 阶段最高 depth 只有 22，需要 frontier depth 复查。
- 两个候选仍是 cp 级差距，不是胜负证明。
- 还没有固定局面、历史签名和循环判负条件。
- 还没有覆盖黑方应着集合的证明图。

## 优化策略

本轮选择动作：`{action['kind']}`。

理由：{action['reason']}

参数：

- candidates: `{', '.join(action['candidates'])}`
- depth: `{action['depth']}`
- MultiPV: `{', '.join(str(x) for x in action['multipvs'])}`
- Hash MB: `{', '.join(str(x) for x in action['hashes_mb'])}`
- Threads: `{', '.join(str(x) for x in action['threads'])}`
- ClearHash: `{', '.join(bool_text(x) for x in action['clear_hash'])}`
- UCI_ShowWDL: `{', '.join(bool_text(x) for x in action['show_wdl'])}`
- per-query max seconds: `{action['per_query_max_seconds']}`

## 本轮执行

- execute: `{executed}`
- experiment report: `{command_path if executed else 'not executed'}`

"""
    if result:
        md += f"""## 本轮结果

- rows: `{result['rows']}`
- completed rows: `{result['completed_rows']}`
- max_seconds rows: `{result['max_seconds_total']}`
- PV repeat rows: `{result['pv_repeat_total']}`
- leader: `{result['leader']}`
- score gap: `{result['score_gap']}`

{stats_md}

## 复盘输出

{reliability_note(result)}

"""
    else:
        md += f"""## 复盘输出

{reliability_note(result)}

"""
    md += """## 下一轮方向

- 如果 `h2e2` 连续稳定领先，下一轮提高 depth。
- 如果出现反转、超时或重复，下一轮不加深，改为更宽 MultiPV / Hash 复查。
- 连续至少 3 轮稳定后，才考虑把 `h2e2 / c3c4` 转成 L2 proof obligation。
"""
    write_text(round_dir / "evolution_summary.md", md)
    return md


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default="reports/evolution-loop")
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--target-seconds", type=int, default=300)
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    base_dir = Path(args.base_dir)
    reports_dir = Path(args.reports_dir)
    state_path = base_dir / "state.json"
    state = load_json(state_path, default_state())
    round_no = int(state.get("round", 0)) + 1
    round_dir = base_dir / f"round-{round_no:04d}"
    action = choose_action(round_no, state, args.target_seconds)
    combo = latest_combo_summary(reports_dir)

    result = None
    executed = False
    if args.execute:
        engine_path = Path(args.engine)
        if not engine_path.exists():
            result = {
                "blocked": True,
                "reason": f"engine not found: {args.engine}",
                "leader": None,
                "score_gap": None,
                "candidate_stats": [],
                "rows": 0,
                "completed_rows": 0,
                "max_seconds_total": 0,
                "pv_repeat_total": 0,
            }
        else:
            experiment_dir = round_dir / "experiment"
            cmd = command_for_action(action, experiment_dir, args.engine, args.engine_cwd)
            started = now_iso()
            completed = subprocess.run(cmd, text=True, capture_output=True, check=False)
            write_text(round_dir / "command.txt", " ".join(cmd) + "\n")
            write_text(round_dir / "stdout.txt", completed.stdout)
            write_text(round_dir / "stderr.txt", completed.stderr)
            executed = True
            result = summarize_experiment(experiment_dir / "parameter_combo_probe_report.json")
            result["returncode"] = completed.returncode
            result["started_at"] = started
            result["finished_at"] = now_iso()

    summary_md = write_summary(round_dir, round_no, action, result, combo, executed)
    summary_json = {
        "round": round_no,
        "created_at": now_iso(),
        "closure_level": "L0 Observation",
        "action": action,
        "result": result,
        "recommended_interval_minutes": 30,
        "summary_path": str(round_dir / "evolution_summary.md"),
    }
    write_json(round_dir / "evolution_summary.json", summary_json)
    write_text(base_dir / "latest_summary.md", summary_md)

    state["round"] = round_no
    state["updated_at"] = now_iso()
    state["closure_level"] = "L0 Observation"
    state.setdefault("history", []).append(summary_json)
    write_json(state_path, state)
    print(json.dumps(summary_json, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
