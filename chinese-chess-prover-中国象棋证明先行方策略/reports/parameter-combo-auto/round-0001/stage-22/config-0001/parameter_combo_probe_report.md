# Pikafish Parameter Combination Probe

This is a multi-lens observation report. It is not a proof.

## Configuration

- Candidates: `c3c4, b2e2, c0e2, h2e2`.
- Depths: `10`.
- MultiPV values: `1`.
- Hash values: `128 MB`.
- Threads values: `1`.
- Clear Hash modes: `True`.
- WDL modes: `True`.
- Per-query max seconds: `15.0`.
- Wall runtime seconds: `0.297`.
- Cached search runtime seconds: `0.054`.
- Cache hits: `0`.
- Cache misses: `4`.

## Summary

- Parameter configurations: `1`.
- Observation rows: `4`.
- Completed rows: `4`.
- Max-second rows: `0`.
- Unique leaders: `c3c4`.
- Score range: `16 .. 27`.

## Candidate Robustness

| Rank | Red move | Top count | Top share | Avg score | Score range | Score stddev | Avg rank | Reply variants | PV repeats |
|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | c3c4 | 1 | 1.0 | 27 | 0 | 0.0 | 1 | 1 | 0 |
| 2 | b2e2 | 0 | 0.0 | 26 | 0 | 0.0 | 3 | 1 | 0 |
| 3 | h2e2 | 0 | 0.0 | 26 | 0 | 0.0 | 2 | 1 | 0 |
| 4 | c0e2 | 0 | 0.0 | 16 | 0 | 0.0 | 4 | 1 | 0 |

## Leaders By Configuration

| Depth | MultiPV | Hash | Threads | Clear Hash | WDL | Max seconds | Leader | Score | Reply |
|---:|---:|---:|---:|:---:|:---:|---:|:---|---:|:---|
| 10 | 1 | 128 | 1 | True | True | 15.0 | c3c4 | 27 | g6g5 |

## Full Rows

| Move | Depth | MultiPV | Hash | Threads | Clear | WDL | Stop | Reply | Score | Nodes | Time ms | Top PV |
|:---|---:|---:|---:|---:|:---:|:---:|:---|:---|---:|---:|---:|:---|
| c3c4 | 10 | 1 | 128 | 1 | True | True | completed | g6g5 | 27 | 8628 | 9 | `g6g5 b0c2 h9g7 h2g2 b9c7 h0i2 g7h5 i0i1 h5i3 i1h1` |
| b2e2 | 10 | 1 | 128 | 1 | True | True | completed | b9c7 | 26 | 12483 | 13 | `b9c7 c3c4 a9b9 b0c2 b7a7` |
| c0e2 | 10 | 1 | 128 | 1 | True | True | completed | b7e7 | 16 | 19324 | 19 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 b9b5` |
| h2e2 | 10 | 1 | 128 | 1 | True | True | completed | h9g7 | 26 | 12083 | 12 | `h9g7 g3g4 i9h9 h0g2 h7i7 c3c4 b7c7 b0c2 c6c5 c2d4` |

## Closure Interpretation

All rows in this report are `L0 Observation` under `docs/proof_closure_protocol.md`.
A candidate may be promoted to `L1 Hypothesis` only after it remains robust when additional parameter dimensions are added.
