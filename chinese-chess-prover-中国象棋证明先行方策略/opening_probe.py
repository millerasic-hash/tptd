#!/usr/bin/env python3
"""Probe every legal red opening move with fixed-depth Pikafish MultiPV.

This is an experiment collector, not a proof. It asks Pikafish to analyze the
position after each legal red first move, then records Black's MultiPV replies
at several fixed depths. Scores are kept both in engine side-to-move form and
normalized to Red's point of view.
"""

from __future__ import annotations

import argparse
import json
import os
import queue
import statistics
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from light_prover import BLACK, RED, START_FEN, Board, Move


def send(proc: subprocess.Popen[str], command: str) -> None:
    assert proc.stdin is not None
    proc.stdin.write(command + "\n")
    proc.stdin.flush()


def parse_int(parts: List[str], key: str) -> Optional[int]:
    if key not in parts:
        return None
    idx = parts.index(key)
    if idx + 1 >= len(parts):
        return None
    try:
        return int(parts[idx + 1])
    except ValueError:
        return None


def parse_info(line: str) -> Optional[dict]:
    parts = line.split()
    if not parts or parts[0] != "info" or "depth" not in parts:
        return None

    info: Dict[str, object] = {"raw": line}
    depth = parse_int(parts, "depth")
    if depth is None:
        return None
    info["depth"] = depth

    for key in ("seldepth", "multipv", "nodes", "nps", "hashfull", "tbhits"):
        value = parse_int(parts, key)
        if value is not None:
            info[key] = value

    time_ms = parse_int(parts, "time")
    if time_ms is not None:
        info["time_ms"] = time_ms

    if "score" in parts:
        idx = parts.index("score")
        if idx + 2 < len(parts):
            info["score_type"] = parts[idx + 1]
            try:
                info["score"] = int(parts[idx + 2])
            except ValueError:
                info["score"] = parts[idx + 2]

    if "wdl" in parts:
        idx = parts.index("wdl")
        if idx + 3 < len(parts):
            try:
                info["wdl"] = [int(parts[idx + 1]), int(parts[idx + 2]), int(parts[idx + 3])]
            except ValueError:
                pass

    if "pv" in parts:
        info["pv"] = parts[parts.index("pv") + 1 :]
    return info


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


class MultiPVEngine:
    def __init__(
        self,
        path: str,
        cwd: str,
        threads: int,
        hash_mb: int,
        multipv: int,
        show_wdl: bool,
    ):
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
        for command in (
            f"setoption name Threads value {threads}",
            f"setoption name Hash value {hash_mb}",
            f"setoption name MultiPV value {multipv}",
            f"setoption name UCI_ShowWDL value {'true' if show_wdl else 'false'}",
        ):
            send(self.proc, command)
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

    def analyze(
        self,
        fen: str,
        depth: int,
        max_seconds: float,
        clear_hash: bool,
        progress_prefix: str,
        snapshot_depths: Optional[Iterable[int]] = None,
    ) -> dict:
        self.drain()
        if clear_hash:
            send(self.proc, "setoption name Clear Hash")
            send(self.proc, "isready")
            read_until(self.lines, "readyok", 30)
        send(self.proc, f"position fen {fen}")
        send(self.proc, f"go depth {depth}")

        started = time.time()
        stopped_by = "completed"
        bestmove = None
        infos_by_mpv: Dict[int, dict] = {}
        snapshots: Dict[int, Dict[int, dict]] = {
            int(item): {} for item in (snapshot_depths or [])
        }
        highest_depth = 0

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
            if info is None:
                continue
            current_depth = int(info["depth"])
            if current_depth > highest_depth:
                highest_depth = current_depth
                display_mpv = int(info.get("multipv", 1))
                print(
                    f"{progress_prefix} depth={current_depth}, "
                    f"mpv={display_mpv}, score={info.get('score_type')} {info.get('score')}, "
                    f"nodes={info.get('nodes')}, elapsed={elapsed:.1f}s",
                    file=sys.stderr,
                    flush=True,
                )
            if "pv" not in info:
                continue
            mpv = int(info.get("multipv", 1))
            infos_by_mpv[mpv] = info
            if current_depth in snapshots:
                snapshots[current_depth][mpv] = dict(info)

        if stopped_by == "max_seconds":
            for line in read_until(self.lines, "bestmove", 10):
                if line.startswith("bestmove"):
                    parts = line.split()
                    bestmove = parts[1] if len(parts) > 1 and parts[1] != "(none)" else None
                    break

        return {
            "depth_requested": depth,
            "highest_depth": highest_depth,
            "bestmove": bestmove,
            "stopped_by": stopped_by,
            "runtime_seconds": round(time.time() - started, 3),
            "multipv": [infos_by_mpv[k] for k in sorted(infos_by_mpv)],
            "snapshots": {
                str(depth_key): [
                    mpv_infos[k] for k in sorted(mpv_infos)
                ]
                for depth_key, mpv_infos in sorted(snapshots.items())
            },
        }


def score_from_red_view(info: dict, side_to_move: str) -> Optional[int]:
    score = info.get("score")
    if not isinstance(score, int):
        return None
    if info.get("score_type") == "mate":
        score = 100000 if score > 0 else -100000
    return score if side_to_move == RED else -score


def apply_uci_if_legal(board: Board, move_text: str) -> Optional[Board]:
    legal = {move.uci(): move for move in board.legal_moves()}
    move = legal.get(move_text)
    if move is None:
        return None
    return board.make_move(move)


def replay_pv(start_board: Board, pv: Iterable[str], repetition_limit: int) -> dict:
    board = start_board
    history: Dict[str, int] = {board.key(): 1}
    legal_plies = 0
    first_repeat_at = None
    reaches_repetition_limit_at = None
    illegal_move = None

    for text in pv:
        child = apply_uci_if_legal(board, text)
        if child is None:
            illegal_move = text
            break
        legal_plies += 1
        board = child
        key = board.key()
        history[key] = history.get(key, 0) + 1
        if history[key] == 2 and first_repeat_at is None:
            first_repeat_at = legal_plies
        if history[key] >= repetition_limit and reaches_repetition_limit_at is None:
            reaches_repetition_limit_at = legal_plies

    return {
        "pv_legal_plies": legal_plies,
        "pv_has_repeat": first_repeat_at is not None,
        "pv_first_repeat_at": first_repeat_at,
        "pv_reaches_repetition_limit": reaches_repetition_limit_at is not None,
        "pv_repetition_limit_at": reaches_repetition_limit_at,
        "pv_illegal_move": illegal_move,
        "pv_end_fen": board.to_fen(),
    }


def summarize(records: List[dict]) -> dict:
    depth_summary: Dict[str, dict] = {}
    for depth in sorted({q["depth_requested"] for r in records for q in r["queries"]}):
        top_infos = [
            q["multipv"][0]
            for r in records
            for q in r["queries"]
            if q["depth_requested"] == depth and q["multipv"]
        ]
        red_scores = [
            info["red_score"]
            for info in top_infos
            if isinstance(info.get("red_score"), int)
        ]
        depth_summary[str(depth)] = {
            "positions": len(top_infos),
            "red_score_min": min(red_scores) if red_scores else None,
            "red_score_max": max(red_scores) if red_scores else None,
            "red_score_avg": round(statistics.mean(red_scores), 2) if red_scores else None,
            "red_score_median": statistics.median(red_scores) if red_scores else None,
            "completed": sum(
                1
                for r in records
                for q in r["queries"]
                if q["depth_requested"] == depth and q["stopped_by"] == "completed"
            ),
            "max_seconds": sum(
                1
                for r in records
                for q in r["queries"]
                if q["depth_requested"] == depth and q["stopped_by"] == "max_seconds"
            ),
        }

    final_depth = max(int(d) for d in depth_summary) if depth_summary else None
    ranked = []
    if final_depth is not None:
        for record in records:
            query = next(
                (q for q in record["queries"] if q["depth_requested"] == final_depth),
                None,
            )
            if not query or not query["multipv"]:
                continue
            top = query["multipv"][0]
            if isinstance(top.get("red_score"), int):
                ranked.append(
                    {
                        "red_move": record["red_move"],
                        "black_bestmove": query["bestmove"],
                        "red_score": top["red_score"],
                        "nodes": top.get("nodes"),
                        "hashfull": top.get("hashfull"),
                        "pv_has_repeat": top.get("pv_has_repeat"),
                        "pv_reaches_repetition_limit": top.get("pv_reaches_repetition_limit"),
                    }
                )
        ranked.sort(key=lambda item: item["red_score"], reverse=True)

    return {
        "depth_summary": depth_summary,
        "final_depth": final_depth,
        "top_final_depth": ranked[:10],
        "bottom_final_depth": ranked[-10:],
    }


def write_markdown(path: Path, output: dict) -> None:
    config = output["config"]
    summary = output["summary"]
    lines = [
        "# Pikafish Opening Probe Report",
        "",
        "This is a reproducible opening probe, not a game-theoretic proof.",
        "",
        "## Configuration",
        "",
        f"- Start FEN: `{output['start_fen']}`.",
        f"- Red opening moves: `{output['red_move_count']}`.",
        f"- Depths: `{', '.join(map(str, config['depths']))}`.",
        f"- MultiPV: `{config['multipv']}`.",
        f"- Threads: `{config['threads']}`.",
        f"- Hash: `{config['hash_mb']} MB`.",
        f"- Clear hash per query: `{config['clear_hash']}`.",
        f"- UCI_ShowWDL: `{config['show_wdl']}`.",
        f"- Single-pass collection: `{config['single_pass']}`.",
        f"- Go depth per red move: `{config['go_depth']}`.",
        f"- Per-query max seconds: `{config['per_query_max_seconds']}`.",
        f"- Runtime seconds: `{output['runtime_seconds']}`.",
        "",
        "Scores are normalized to Red's point of view. After a red opening move, the side to move is Black, so a negative engine score becomes a positive Red score.",
        "",
        "## Depth Summary",
        "",
        "| Depth | Positions | Completed | Max seconds | Red score min | Red score median | Red score avg | Red score max |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for depth, row in summary["depth_summary"].items():
        lines.append(
            f"| {depth} | {row['positions']} | {row['completed']} | {row['max_seconds']} | "
            f"{row['red_score_min']} | {row['red_score_median']} | {row['red_score_avg']} | {row['red_score_max']} |"
        )

    final_depth = summary["final_depth"]
    lines.extend(
        [
            "",
            f"## Depth {final_depth} Top Red Moves",
            "",
            "| Rank | Red move | Black best reply | Red score | Nodes | Hashfull | PV repeat | PV third-repeat |",
            "|---:|:---|:---|---:|---:|---:|:---:|:---:|",
        ]
    )
    for idx, item in enumerate(summary["top_final_depth"], start=1):
        lines.append(
            f"| {idx} | {item['red_move']} | {item['black_bestmove']} | {item['red_score']} | "
            f"{item['nodes']} | {item['hashfull']} | {item['pv_has_repeat']} | {item['pv_reaches_repetition_limit']} |"
        )

    lines.extend(
        [
            "",
            f"## Depth {final_depth} Bottom Red Moves",
            "",
            "| Rank | Red move | Black best reply | Red score | Nodes | Hashfull | PV repeat | PV third-repeat |",
            "|---:|:---|:---|---:|---:|---:|:---:|:---:|",
        ]
    )
    for idx, item in enumerate(summary["bottom_final_depth"], start=1):
        lines.append(
            f"| {idx} | {item['red_move']} | {item['black_bestmove']} | {item['red_score']} | "
            f"{item['nodes']} | {item['hashfull']} | {item['pv_has_repeat']} | {item['pv_reaches_repetition_limit']} |"
        )

    lines.extend(
        [
            "",
            "## Full Depth Rows",
            "",
            "| Red move | Depth | Stop | Best reply | Top red score | Top engine score | Seldepth | Nodes | Time ms | WDL | Top PV |",
            "|:---|---:|:---|:---|---:|:---|---:|---:|---:|:---|:---|",
        ]
    )
    for record in output["records"]:
        for query in record["queries"]:
            top = query["multipv"][0] if query["multipv"] else {}
            engine_score = ""
            if top:
                engine_score = f"{top.get('score_type')} {top.get('score')}"
            pv = " ".join(top.get("pv", [])[:12]) if top else ""
            wdl = "/".join(map(str, top.get("wdl", []))) if top.get("wdl") else ""
            lines.append(
                f"| {record['red_move']} | {query['depth_requested']} | {query['stopped_by']} | "
                f"{query['bestmove']} | {top.get('red_score')} | {engine_score} | "
                f"{top.get('seldepth')} | {top.get('nodes')} | {top.get('time_ms')} | {wdl} | `{pv}` |"
            )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_depths(text: str) -> List[int]:
    depths = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        depths.append(int(part))
    if not depths:
        raise argparse.ArgumentTypeError("at least one depth is required")
    return depths


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe every legal red opening move with Pikafish")
    parser.add_argument("--engine", default="tools/pikafish/MacOS/pikafish-apple-silicon")
    parser.add_argument("--engine-cwd", default="tools/pikafish")
    parser.add_argument("--depths", type=parse_depths, default=[12, 18, 24, 30])
    parser.add_argument("--multipv", type=int, default=4)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--hash-mb", type=int, default=128)
    parser.add_argument("--per-query-max-seconds", type=float, default=60.0)
    parser.add_argument("--repetition-limit", type=int, default=3)
    parser.add_argument("--no-clear-hash", action="store_true")
    parser.add_argument("--no-wdl", action="store_true")
    parser.add_argument(
        "--separate-depth-queries",
        action="store_true",
        help="Run one engine search per requested depth. Default is one max-depth search per red move and snapshot intermediate depths.",
    )
    parser.add_argument("--out-dir", default="reports/opening-probe")
    args = parser.parse_args()

    started = time.time()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "opening_probe_report.json"
    md_path = out_dir / "opening_probe_report.md"

    start_board = Board.from_fen(START_FEN)
    red_moves = sorted(start_board.legal_moves(), key=lambda move: move.uci())
    records: List[dict] = []

    engine = MultiPVEngine(
        args.engine,
        args.engine_cwd,
        threads=args.threads,
        hash_mb=args.hash_mb,
        multipv=args.multipv,
        show_wdl=not args.no_wdl,
    )
    try:
        for index, red_move in enumerate(red_moves, start=1):
            child = start_board.make_move(red_move)
            record = {
                "index": index,
                "red_move": red_move.uci(),
                "fen_after_red_move": child.to_fen(),
                "queries": [],
            }
            print(
                f"[move {index}/{len(red_moves)}] red={red_move.uci()}",
                file=sys.stderr,
                flush=True,
            )
            if args.separate_depth_queries:
                for depth in args.depths:
                    query = engine.analyze(
                        child.to_fen(),
                        depth,
                        args.per_query_max_seconds,
                        clear_hash=not args.no_clear_hash,
                        progress_prefix=f"[{index}/{len(red_moves)} {red_move.uci()} d{depth}]",
                    )
                    for info in query["multipv"]:
                        info["red_score"] = score_from_red_view(info, child.side)
                        info.update(replay_pv(child, info.get("pv", []), args.repetition_limit))
                    record["queries"].append(query)
                    top = query["multipv"][0] if query["multipv"] else {}
                    print(
                        f"[done] red={red_move.uci()} depth={depth} best={query['bestmove']} "
                        f"red_score={top.get('red_score')} stop={query['stopped_by']} "
                        f"seconds={query['runtime_seconds']}",
                        file=sys.stderr,
                        flush=True,
                    )
            else:
                go_depth = max(args.depths)
                analysis = engine.analyze(
                    child.to_fen(),
                    go_depth,
                    args.per_query_max_seconds,
                    clear_hash=not args.no_clear_hash,
                    progress_prefix=f"[{index}/{len(red_moves)} {red_move.uci()} d{go_depth}]",
                    snapshot_depths=args.depths,
                )
                for depth in args.depths:
                    snapshot_infos = [dict(info) for info in analysis["snapshots"].get(str(depth), [])]
                    if depth == go_depth and not snapshot_infos:
                        snapshot_infos = [dict(info) for info in analysis["multipv"]]
                    for info in snapshot_infos:
                        info["red_score"] = score_from_red_view(info, child.side)
                        info.update(replay_pv(child, info.get("pv", []), args.repetition_limit))
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
                    print(
                        f"[snapshot] red={red_move.uci()} depth={depth} best={query['bestmove']} "
                        f"red_score={top.get('red_score')} stop={query['stopped_by']} "
                        f"seconds={query['runtime_seconds']}",
                        file=sys.stderr,
                        flush=True,
                    )
                top = analysis["multipv"][0] if analysis["multipv"] else {}
                final_red_score = score_from_red_view(top, child.side) if top else None
                print(
                    f"[done] red={red_move.uci()} go_depth={go_depth} best={analysis['bestmove']} "
                    f"red_score={final_red_score} stop={analysis['stopped_by']} "
                    f"seconds={analysis['runtime_seconds']}",
                    file=sys.stderr,
                    flush=True,
                )
            records.append(record)
    finally:
        engine.close()

    output = {
        "start_fen": START_FEN,
        "red_move_count": len(red_moves),
        "config": {
            "engine": args.engine,
            "engine_cwd": args.engine_cwd,
            "depths": args.depths,
            "multipv": args.multipv,
            "threads": args.threads,
            "hash_mb": args.hash_mb,
            "clear_hash": not args.no_clear_hash,
            "show_wdl": not args.no_wdl,
            "single_pass": not args.separate_depth_queries,
            "go_depth": max(args.depths),
            "per_query_max_seconds": args.per_query_max_seconds,
            "repetition_limit": args.repetition_limit,
        },
        "runtime_seconds": round(time.time() - started, 3),
        "summary": summarize(records),
        "records": records,
    }
    json_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(md_path, output)
    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "summary": {
                    "red_move_count": output["red_move_count"],
                    "runtime_seconds": output["runtime_seconds"],
                    "final_depth": output["summary"]["final_depth"],
                    "depth_summary": output["summary"]["depth_summary"],
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
