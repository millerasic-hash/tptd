#!/usr/bin/env python3
"""Run one Pikafish depth request with a wall-clock safety cap."""

from __future__ import annotations

import argparse
import json
import os
import select
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional

from light_prover import START_FEN


def parse_info(line: str) -> Optional[dict]:
    parts = line.split()
    if not parts or parts[0] != "info" or "depth" not in parts:
        return None
    info: Dict[str, object] = {"raw": line}
    try:
        info["depth"] = int(parts[parts.index("depth") + 1])
    except Exception:
        return None
    if "seldepth" in parts:
        info["seldepth"] = int(parts[parts.index("seldepth") + 1])
    if "nodes" in parts:
        info["nodes"] = int(parts[parts.index("nodes") + 1])
    if "nps" in parts:
        info["nps"] = int(parts[parts.index("nps") + 1])
    if "time" in parts:
        info["time_ms"] = int(parts[parts.index("time") + 1])
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


def send(proc: subprocess.Popen[str], command: str) -> None:
    assert proc.stdin is not None
    proc.stdin.write(command + "\n")
    proc.stdin.flush()


def read_lines_until(
    proc: subprocess.Popen[str],
    marker: str,
    timeout_seconds: float,
) -> List[str]:
    assert proc.stdout is not None
    fd = proc.stdout.fileno()
    end = time.time() + timeout_seconds
    lines: List[str] = []
    while time.time() < end:
        readable, _, _ = select.select([fd], [], [], 0.2)
        if not readable:
            continue
        line = proc.stdout.readline()
        if not line:
            break
        line = line.strip()
        lines.append(line)
        if line.startswith(marker):
            break
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one bounded Pikafish depth request")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--fen", default=START_FEN)
    parser.add_argument("--depth", type=int, default=256)
    parser.add_argument("--max-seconds", type=float, default=120.0)
    parser.add_argument("--out-dir", default="reports/1x256")
    parser.add_argument("--progress-every-depth", type=int, default=1)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "pikafish_1x_depth.json"
    md_path = out_dir / "pikafish_1x_depth.md"

    proc = subprocess.Popen(
        [os.path.abspath(args.engine)],
        cwd=os.path.abspath(args.engine_cwd),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        bufsize=1,
    )

    started = time.time()
    infos: List[dict] = []
    bestmove = None
    stopped_by = "completed"
    try:
        send(proc, "uci")
        read_lines_until(proc, "uciok", 10)
        send(proc, "isready")
        read_lines_until(proc, "readyok", 10)
        send(proc, f"position fen {args.fen}")
        send(proc, f"go depth {args.depth}")

        assert proc.stdout is not None
        fd = proc.stdout.fileno()
        highest_reported = 0
        while True:
            elapsed = time.time() - started
            if elapsed >= args.max_seconds:
                stopped_by = "max_seconds"
                send(proc, "stop")
                break

            readable, _, _ = select.select([fd], [], [], 0.2)
            if not readable:
                continue
            line = proc.stdout.readline()
            if not line:
                break
            line = line.strip()
            if line.startswith("bestmove"):
                bestmove = line.split()[1] if len(line.split()) > 1 else None
                break
            info = parse_info(line)
            if info is not None:
                infos.append(info)
                depth = int(info["depth"])
                if (
                    args.progress_every_depth > 0
                    and depth >= highest_reported + args.progress_every_depth
                ):
                    highest_reported = depth
                    score = f"{info.get('score_type')} {info.get('score')}"
                    print(
                        f"[progress] depth={depth}, seldepth={info.get('seldepth')}, "
                        f"score={score}, nodes={info.get('nodes')}, "
                        f"elapsed={elapsed:.1f}s",
                        flush=True,
                    )

        if stopped_by == "max_seconds":
            for line in read_lines_until(proc, "bestmove", 10):
                if line.startswith("bestmove"):
                    bestmove = line.split()[1] if len(line.split()) > 1 else None
                    break
    finally:
        try:
            send(proc, "quit")
        except Exception:
            pass
        proc.terminate()

    runtime = round(time.time() - started, 3)
    last_info = infos[-1] if infos else None
    pv_bestmove = None
    if last_info and last_info.get("pv"):
        pv = last_info["pv"]
        if isinstance(pv, list) and pv:
            pv_bestmove = pv[0]
    output = {
        "requested_depth": args.depth,
        "max_seconds": args.max_seconds,
        "stopped_by": stopped_by,
        "runtime_seconds": runtime,
        "fen": args.fen,
        "bestmove": bestmove,
        "bestmove_from_last_pv": pv_bestmove,
        "highest_depth": max((int(info["depth"]) for info in infos), default=0),
        "last_info": last_info,
        "infos": infos,
    }
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        f"# Pikafish 1x{args.depth} Depth Request",
        "",
        "This is one depth request with a wall-clock safety cap.",
        "",
        f"- Requested depth: `{args.depth}`.",
        f"- Max seconds: `{args.max_seconds}`.",
        f"- Stopped by: `{stopped_by}`.",
        f"- Runtime seconds: `{runtime}`.",
        f"- Highest completed/report depth: `{output['highest_depth']}`.",
        f"- Bestmove: `{bestmove}`.",
        f"- Bestmove from last PV: `{pv_bestmove}`.",
    ]
    if last_info:
        lines.extend(
            [
                f"- Last score: `{last_info.get('score_type')} {last_info.get('score')}`.",
                f"- Last seldepth: `{last_info.get('seldepth')}`.",
                f"- Last nodes: `{last_info.get('nodes')}`.",
                f"- Last PV: `{' '.join(last_info.get('pv', []))}`.",
            ]
        )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path), "summary": {k: output[k] for k in ("requested_depth", "stopped_by", "runtime_seconds", "highest_depth", "bestmove", "last_info")}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
