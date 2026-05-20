# Pikafish Prover 1024x12 Report

This is a bounded calibration run, not a theorem about Xiangqi.

## Configuration

- Samples: `1024` generated from standard start positions.
- Proof depth: `12` plies.
- Max proof nodes per sample: `1024`.
- Repetition limit: `2` appearances per state.
- Pikafish engine: `tools/pikafish/MacOS/pikafish-apple-silicon`.
- Pikafish engine depth: `1`.
- Pikafish movetime: `20 ms`.
- Runtime seconds: `975.034`.

## Summary

- Status counts: `{'UNKNOWN': 1024}`.
- Proven count: `0`.
- Unknown count: `1024`.
- Average prover nodes: `1024`.
- Median prover nodes: `1024.0`.
- Max prover nodes observed: `1024`.
- Score range: `-119` to `428`.

## Threshold

- `threshold_all_above_proven_win`: `None`.
- Warning: This threshold is sample/resource bounded. It is not a theorem about all Xiangqi positions.

## Bins

| Score range | Count | WIN | LOSS | UNKNOWN |
|---:|---:|---:|---:|---:|
| [-200, 0) | 480 | 0 | 0 | 480 |
| [0, 500) | 544 | 0 | 0 | 544 |
| [200, 700) | 83 | 0 | 0 | 83 |

## Interpretation

A score threshold is useful only when a fixed sample, fixed engine setting, fixed proof depth, and fixed node budget are stated together. A high score can prioritize proof work, but it cannot replace a closed certificate.
