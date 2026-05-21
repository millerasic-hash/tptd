# Pikafish Parameter Combination Probe

This is a multi-lens observation report. It is not a proof.

## Configuration

- Candidates: `c3c4, b2e2, c0e2, h2e2`.
- Depths: `12`.
- MultiPV values: `2`.
- Hash values: `128 MB`.
- Threads values: `1`.
- Clear Hash modes: `True`.
- WDL modes: `True`.
- Per-query max seconds: `15.0`.
- Wall runtime seconds: `0.535`.
- Cached search runtime seconds: `0.236`.
- Cache hits: `0`.
- Cache misses: `4`.

## Summary

- Parameter configurations: `1`.
- Observation rows: `4`.
- Completed rows: `4`.
- Max-second rows: `0`.
- Unique leaders: `h2e2`.
- Score range: `16 .. 29`.

## Candidate Robustness

| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | h2e2 | 1 | 1.0 | 29 | 0 | 0.0 | 1 | 1 | 0 |
| 2 | c3c4 | 0 | 0.0 | 23 | 0 | 0.0 | 2 | 1 | 0 |
| 3 | b2e2 | 0 | 0.0 | 18 | 0 | 0.0 | 3 | 1 | 0 |
| 4 | c0e2 | 0 | 0.0 | 16 | 0 | 0.0 | 4 | 1 | 0 |

## Leaders By Configuration

| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |
|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|
| 12 | 2 | 128 | 1 | True | True | 15.0 | h2e2 | 29 | h9g7 |

## Full Rows

| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |
|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|
| c3c4 | 12 | 2 | 128 | 1 | True | True | completed | b7c7 | 23 | 76211 | 76 | `b7c7 h2e2 h7e7 b0c2 c6c5 c2d4 c5c4 d4e6 h9g7 h0g2` |
| b2e2 | 12 | 2 | 128 | 1 | True | True | completed | b9c7 | 18 | 49538 | 47 | `b9c7 b0c2 c6c5 h0g2 a9b9 h2i2 h9g7 i0h0 i9h9 g3g4` |
| c0e2 | 12 | 2 | 128 | 1 | True | True | completed | b7e7 | 16 | 58528 | 53 | `b7e7 h0g2 b9c7 g3g4 h9i7` |
| h2e2 | 12 | 2 | 128 | 1 | True | True | completed | h9g7 | 29 | 60686 | 59 | `h9g7 h0g2 i9h9 i0h0 c6c5 h0h4 b9c7 b0c2 g6g5 e3e4` |

## Closure Interpretation

All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.
A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.
