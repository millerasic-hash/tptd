# Pikafish Parameter Combination Probe

This is a multi-lens observation report. It is not a proof.

## Configuration

- Candidates: `c3c4, b2e2, c0e2, h2e2`.
- Depths: `10`.
- MultiPV values: `2`.
- Hash values: `128 MB`.
- Threads values: `1`.
- Clear Hash modes: `True`.
- WDL modes: `True`.
- Per-query max seconds: `15.0`.
- Wall runtime seconds: `0.336`.
- Cached search runtime seconds: `0.082`.
- Cache hits: `0`.
- Cache misses: `4`.

## Summary

- Parameter configurations: `1`.
- Observation rows: `4`.
- Completed rows: `4`.
- Max-second rows: `0`.
- Unique leaders: `b2e2`.
- Score range: `22 .. 28`.

## Candidate Robustness

| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | b2e2 | 1 | 1.0 | 28 | 0 | 0.0 | 1 | 1 | 0 |
| 2 | c3c4 | 0 | 0.0 | 27 | 0 | 0.0 | 2 | 1 | 0 |
| 3 | c0e2 | 0 | 0.0 | 22 | 0 | 0.0 | 4 | 1 | 0 |
| 4 | h2e2 | 0 | 0.0 | 22 | 0 | 0.0 | 3 | 1 | 0 |

## Leaders By Configuration

| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |
|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|
| 10 | 2 | 128 | 1 | True | True | 15.0 | b2e2 | 28 | b9c7 |

## Full Rows

| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |
|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|
| c3c4 | 10 | 2 | 128 | 1 | True | True | completed | b7c7 | 27 | 29727 | 27 | `b7c7 h2e2 h7e7 b0c2 c6c5 c2d4 c5c4` |
| b2e2 | 10 | 2 | 128 | 1 | True | True | completed | b9c7 | 28 | 9493 | 9 | `b9c7 b0c2 c6c5 h0g2` |
| c0e2 | 10 | 2 | 128 | 1 | True | True | completed | h7f7 | 22 | 36574 | 31 | `h7f7 g3g4 h9g7 h0g2 i9h9 i0h0 c6c5 b0d1 h9h5 h2i2` |
| h2e2 | 10 | 2 | 128 | 1 | True | True | completed | h9g7 | 22 | 17248 | 15 | `h9g7 h0g2 c6c5 i0h0 i9h9 h0h6 c9e7` |

## Closure Interpretation

All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.
A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.
