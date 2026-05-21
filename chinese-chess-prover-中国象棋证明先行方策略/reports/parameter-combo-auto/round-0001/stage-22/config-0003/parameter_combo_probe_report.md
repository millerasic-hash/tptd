# Pikafish Parameter Combination Probe

This is a multi-lens observation report. It is not a proof.

## Configuration

- Candidates: `c3c4, b2e2, c0e2, h2e2`.
- Depths: `12`.
- MultiPV values: `1`.
- Hash values: `128 MB`.
- Threads values: `1`.
- Clear Hash modes: `True`.
- WDL modes: `True`.
- Per-query max seconds: `15.0`.
- Wall runtime seconds: `0.392`.
- Cached search runtime seconds: `0.172`.
- Cache hits: `0`.
- Cache misses: `4`.

## Summary

- Parameter configurations: `1`.
- Observation rows: `4`.
- Completed rows: `4`.
- Max-second rows: `0`.
- Unique leaders: `c3c4`.
- Score range: `22 .. 30`.

## Candidate Robustness

| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | c3c4 | 1 | 1.0 | 30 | 0 | 0.0 | 1 | 1 | 0 |
| 2 | c0e2 | 0 | 0.0 | 26 | 0 | 0.0 | 2 | 1 | 0 |
| 3 | h2e2 | 0 | 0.0 | 23 | 0 | 0.0 | 3 | 1 | 0 |
| 4 | b2e2 | 0 | 0.0 | 22 | 0 | 0.0 | 4 | 1 | 0 |

## Leaders By Configuration

| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |
|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|
| 12 | 1 | 128 | 1 | True | True | 15.0 | c3c4 | 30 | b7c7 |

## Full Rows

| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |
|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|
| c3c4 | 12 | 1 | 128 | 1 | True | True | completed | b7c7 | 30 | 42148 | 44 | `b7c7 c0e2 b9a7 g3g4 h7e7 h0g2` |
| b2e2 | 12 | 1 | 128 | 1 | True | True | completed | b9c7 | 22 | 23258 | 26 | `b9c7 c3c4 g6g5 b0c2 a9b9 h2g2 h9g7` |
| c0e2 | 12 | 1 | 128 | 1 | True | True | completed | c6c5 | 26 | 61857 | 71 | `c6c5 h0g2 c9e7` |
| h2e2 | 12 | 1 | 128 | 1 | True | True | completed | h9g7 | 23 | 25269 | 30 | `h9g7 h0g2 g6g5 i0h0 i9h9 c3c4 h7h3 b2b4` |

## Closure Interpretation

All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.
A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.
