# Pikafish Parameter Combination Probe

This is a multi-lens observation report. It is not a proof.

## Configuration

- Candidates: `h2e2, c3c4`.
- Depths: `24`.
- MultiPV values: `4, 8`.
- Hash values: `512, 1024 MB`.
- Threads values: `1`.
- Clear Hash modes: `True`.
- WDL modes: `True`.
- Per-query max seconds: `41.2`.
- Wall runtime seconds: `125.329`.
- Cached search runtime seconds: `122.774`.
- Cache hits: `0`.
- Cache misses: `8`.

## Summary

- Parameter configurations: `4`.
- Observation rows: `8`.
- Completed rows: `8`.
- Max-second rows: `0`.
- Unique leaders: `c3c4, h2e2`.
- Score range: `12 .. 20`.

## Candidate Robustness

| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | h2e2 | 3 | 0.75 | 18.75 | 2 | 0.829 | 1.25 | 2 | 0 |
| 2 | c3c4 | 1 | 0.25 | 15.25 | 7 | 2.861 | 1.75 | 1 | 0 |

## Leaders By Configuration

| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |
|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|
| 24 | 4 | 512 | 1 | True | True | 41.2 | c3c4 | 19 | b7c7 |
| 24 | 4 | 1024 | 1 | True | True | 41.2 | h2e2 | 18 | h9g7 |
| 24 | 8 | 512 | 1 | True | True | 41.2 | h2e2 | 19 | h9g7 |
| 24 | 8 | 1024 | 1 | True | True | 41.2 | h2e2 | 20 | b9c7 |

## Full Rows

| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |
|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|
| h2e2 | 24 | 4 | 512 | 1 | True | True | completed | b9c7 | 18 | 9755838 | 10047 | `b9c7 h0g2 h9g7 i0h0 i9h9 g3g4 c6c5 b2c2 d9e8 b0a2` |
| c3c4 | 24 | 4 | 512 | 1 | True | True | completed | b7c7 | 19 | 8795769 | 9331 | `b7c7 h2e2 c9e7 c0a2 g6g5 h0g2 h9g7 b2d2 i9h9 b0c2` |
| h2e2 | 24 | 4 | 1024 | 1 | True | True | completed | h9g7 | 18 | 8270170 | 8539 | `h9g7 h0g2 i9h9 i0h0 g6g5 h0h6 b9c7 b0c2 g7f5 c3c4` |
| c3c4 | 24 | 4 | 1024 | 1 | True | True | completed | b7c7 | 17 | 9400992 | 8822 | `b7c7 h2e2 c9e7 h0g2 c6c5 c0a2 c5c4 a2c4 i9i8 e2e6` |
| h2e2 | 24 | 8 | 512 | 1 | True | True | completed | h9g7 | 19 | 21736910 | 21723 | `h9g7 g3g4 i9h9 h0g2 c6c5 i0h0 b9c7 b0a2 a6a5 b2c2` |
| c3c4 | 24 | 8 | 512 | 1 | True | True | completed | b7c7 | 13 | 21128947 | 20854 | `b7c7 h2e2 c9e7 h0g2 c6c5 b0a2 c5c4 i0h0 i9i8 h0h4` |
| h2e2 | 24 | 8 | 1024 | 1 | True | True | completed | b9c7 | 20 | 18914563 | 19055 | `b9c7 h0g2 h9g7 i0h0 i9h9 g3g4 c6c5 b2c2 d9e8 b0a2` |
| c3c4 | 24 | 8 | 1024 | 1 | True | True | completed | b7c7 | 12 | 22820476 | 24403 | `b7c7 h2e2 c9e7 h0g2 c6c5 i0h0 c5c4 b2c2 i9i8 h0h4` |

## Closure Interpretation

All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.
A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.
