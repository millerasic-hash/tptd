# Pikafish Parameter Combination Probe

This is a multi-lens observation report. It is not a proof.

## Configuration

- Candidates: `c3c4, b2e2, c0e2, h2e2`.
- Depths: `10, 12`.
- MultiPV values: `1, 2`.
- Hash values: `128 MB`.
- Threads values: `1`.
- Clear Hash modes: `True`.
- WDL modes: `True`.
- Per-query max seconds: `15.0`.
- Wall runtime seconds: `0.007`.
- Cached search runtime seconds: `0.488`.
- Cache hits: `16`.
- Cache misses: `0`.

## Summary

- Parameter configurations: `4`.
- Observation rows: `16`.
- Completed rows: `16`.
- Max-second rows: `0`.
- Unique leaders: `b2e2, c3c4, h2e2`.
- Score range: `16 .. 30`.

## Candidate Robustness

| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | c3c4 | 2 | 0.5 | 26.75 | 7 | 2.487 | 1.5 | 2 | 0 |
| 2 | h2e2 | 1 | 0.25 | 25 | 7 | 2.739 | 2.25 | 1 | 0 |
| 3 | b2e2 | 1 | 0.25 | 23.5 | 10 | 3.841 | 2.75 | 1 | 0 |
| 4 | c0e2 | 0 | 0.0 | 20 | 10 | 4.243 | 3.5 | 3 | 0 |

## Leaders By Configuration

| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |
|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|
| 10 | 1 | 128 | 1 | True | True | 15.0 | c3c4 | 27 | g6g5 |
| 10 | 2 | 128 | 1 | True | True | 15.0 | b2e2 | 28 | b9c7 |
| 12 | 1 | 128 | 1 | True | True | 15.0 | c3c4 | 30 | b7c7 |
| 12 | 2 | 128 | 1 | True | True | 15.0 | h2e2 | 29 | h9g7 |

## Full Rows

| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |
|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|
| c3c4 | 10 | 1 | 128 | 1 | True | True | completed | g6g5 | 27 | 8628 | 8 | `g6g5 b0c2 h9g7 h2g2 b9c7 h0i2 g7h5 i0i1 h5i3 i1h1` |
| b2e2 | 10 | 1 | 128 | 1 | True | True | completed | b9c7 | 26 | 12483 | 12 | `b9c7 c3c4 a9b9 b0c2 b7a7` |
| c0e2 | 10 | 1 | 128 | 1 | True | True | completed | b7e7 | 16 | 19324 | 16 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 b9b5` |
| h2e2 | 10 | 1 | 128 | 1 | True | True | completed | h9g7 | 26 | 12083 | 11 | `h9g7 g3g4 i9h9 h0g2 h7i7 c3c4 b7c7 b0c2 c6c5 c2d4` |
| c3c4 | 10 | 2 | 128 | 1 | True | True | completed | b7c7 | 27 | 29727 | 26 | `b7c7 h2e2 h7e7 b0c2 c6c5 c2d4 c5c4` |
| b2e2 | 10 | 2 | 128 | 1 | True | True | completed | b9c7 | 28 | 9493 | 8 | `b9c7 b0c2 c6c5 h0g2` |
| c0e2 | 10 | 2 | 128 | 1 | True | True | completed | h7f7 | 22 | 36574 | 27 | `h7f7 g3g4 h9g7 h0g2 i9h9 i0h0 c6c5 b0d1 h9h5 h2i2` |
| h2e2 | 10 | 2 | 128 | 1 | True | True | completed | h9g7 | 22 | 17248 | 13 | `h9g7 h0g2 c6c5 i0h0 i9h9 h0h6 c9e7` |
| c3c4 | 12 | 1 | 128 | 1 | True | True | completed | b7c7 | 30 | 42148 | 41 | `b7c7 c0e2 b9a7 g3g4 h7e7 h0g2` |
| b2e2 | 12 | 1 | 128 | 1 | True | True | completed | b9c7 | 22 | 23258 | 21 | `b9c7 c3c4 g6g5 b0c2 a9b9 h2g2 h9g7` |
| c0e2 | 12 | 1 | 128 | 1 | True | True | completed | c6c5 | 26 | 61857 | 58 | `c6c5 h0g2 c9e7` |
| h2e2 | 12 | 1 | 128 | 1 | True | True | completed | h9g7 | 23 | 25269 | 23 | `h9g7 h0g2 g6g5 i0h0 i9h9 c3c4 h7h3 b2b4` |
| c3c4 | 12 | 2 | 128 | 1 | True | True | completed | b7c7 | 23 | 76211 | 73 | `b7c7 h2e2 h7e7 b0c2 c6c5 c2d4 c5c4 d4e6 h9g7 h0g2` |
| b2e2 | 12 | 2 | 128 | 1 | True | True | completed | b9c7 | 18 | 49538 | 53 | `b9c7 b0c2 c6c5 h0g2 a9b9 h2i2 h9g7 i0h0 i9h9 g3g4` |
| c0e2 | 12 | 2 | 128 | 1 | True | True | completed | b7e7 | 16 | 58528 | 49 | `b7e7 h0g2 b9c7 g3g4 h9i7` |
| h2e2 | 12 | 2 | 128 | 1 | True | True | completed | h9g7 | 29 | 60686 | 51 | `h9g7 h0g2 i9h9 i0h0 c6c5 h0h4 b9c7 b0c2 g6g5 e3e4` |

## Closure Interpretation

All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.
A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.
