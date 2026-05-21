# Pikafish Candidate Opening Probe

This is a reusable Top-k candidate stability probe, not a game-theoretic proof.

## Configuration

- Start FEN: `rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1`.
- Candidates: `h2e2, b2e2, c3c4, g0e2, c0e2, g3g4, b0c2, h0g2, h2f2`.
- Depths: `14, 16, 18, 20, 22, 24`.
- MultiPV: `4`.
- Threads: `1`.
- Hash: `128 MB`.
- Per-query max seconds: `60.0`.
- Wall runtime seconds: `4.793`.
- Cached search runtime seconds: `83.736`.
- Cache hits: `9`.
- Cache misses: `0`.

Each candidate runs one `go depth max(depths)` search and captures intermediate depth snapshots.

## Depth Summary

| Depth | Positions | Completed | Max seconds | Min | Median | Avg | Max | Entropy | Effective candidates | Leader | Score | Reply |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---|---:|:---|
| 14 | 9 | 9 | 0 | 7 | 18 | 16.556 | 22 | 0.994874 | 8.899 | h2e2 | 22 | h9g7 |
| 16 | 9 | 9 | 0 | 6 | 19 | 16.778 | 25 | 0.991791 | 8.839 | h2e2 | 25 | h9g7 |
| 18 | 9 | 9 | 0 | 10 | 19 | 17.778 | 26 | 0.991999 | 8.843 | g3g4 | 26 | h7g7 |
| 20 | 9 | 9 | 0 | 5 | 17 | 15.889 | 28 | 0.985936 | 8.726 | h2e2 | 28 | b9c7 |
| 22 | 9 | 9 | 0 | 8 | 16 | 15 | 22 | 0.995536 | 8.912 | g3g4 | 22 | h7g7 |
| 24 | 9 | 9 | 0 | 3 | 15 | 13.333 | 17 | 0.996098 | 8.923 | c3c4 | 17 | b7c7 |

## Final Depth 24 Ranking

| Rank | Red move | Score | Reply | Avg rank | Score stddev | Reply variants | Frontier | Transposition density | DAG compression | Cost proxy |
|---:|:---|---:|:---|---:|---:|---:|---:|---:|---:|---:|
| 1 | c3c4 | 17 | b7c7 | 3.5 | 2.93 | 1 | 24 | 0.245098 | 1.325 | 39.43 |
| 2 | b2e2 | 17 | h9g7 | 3.5 | 1.067 | 2 | 24 | 0.3125 | 1.455 | 46.567 |
| 3 | c0e2 | 16 | h7f7 | 4.833 | 2.217 | 3 | 24 | 0.226069 | 1.292 | 58.717 |
| 4 | g0e2 | 15 | b7d7 | 4.667 | 1.374 | 2 | 24 | 0.228106 | 1.296 | 47.374 |
| 5 | g3g4 | 15 | h7g7 | 2.833 | 3.902 | 2 | 24 | 0.281124 | 1.391 | 53.402 |
| 6 | h2e2 | 15 | h9g7 | 2.0 | 4.619 | 2 | 24 | 0.300752 | 1.43 | 55.119 |
| 7 | h2f2 | 11 | b7e7 | 8.0 | 1.7 | 1 | 24 | 0.336957 | 1.508 | 35.7 |
| 8 | b0c2 | 11 | c6c5 | 7.333 | 3.236 | 1 | 24 | 0.312115 | 1.454 | 39.736 |
| 9 | h0g2 | 3 | g6g5 | 8.333 | 3.944 | 1 | 24 | 0.247059 | 1.328 | 43.944 |

## Candidate Score Curves

| Red move | d14 | d16 | d18 | d20 | d22 | d24 | Replies |
|:---|---:|---:|---:|---:|---:|---:|:---|
| h2e2 | 22 | 25 | 25 | 28 | 17 | 15 | b9c7, h9g7 |
| b2e2 | 19 | 19 | 20 | 20 | 18 | 17 | b9c7, h9g7 |
| c3c4 | 22 | 15 | 21 | 21 | 15 | 17 | b7c7 |
| g0e2 | 19 | 19 | 17 | 17 | 17 | 15 | b7d7, h7e7 |
| c0e2 | 18 | 21 | 19 | 17 | 14 | 16 | b7e7, c6c5, h7f7 |
| g3g4 | 16 | 23 | 26 | 22 | 22 | 15 | c6c5, h7g7 |
| b0c2 | 11 | 12 | 12 | 5 | 16 | 11 | c6c5 |
| h0g2 | 15 | 11 | 10 | 5 | 8 | 3 | g6g5 |
| h2f2 | 7 | 6 | 10 | 8 | 8 | 11 | b7e7 |

## Full Rows

| Red move | Depth | Stop | Reply | Red score | Nodes | Time ms | Captured PVs | Top PV |
|:---|---:|:---|:---|---:|---:|---:|---:|:---|
| h2e2 | 14 | completed | h9g7 | 22 | 323421 | 311 | 4 | `h9g7 g3g4 i9h9 c3c4 b7c7 b0a2 b9a7 a0b0 a9b9 b2b6 h7h2 h0g2` |
| h2e2 | 16 | completed | h9g7 | 25 | 634945 | 599 | 4 | `h9g7 h0g2 i9h9 i0h0 g6g5 c3c4 b9c7 b0c2 b7b3 g3g4 g5g4 h0h6` |
| h2e2 | 18 | completed | h9g7 | 25 | 1493352 | 1455 | 4 | `h9g7 h0g2 i9h9 i0h0 g6g5 b0c2 b9c7 c3c4 b7b3 g3g4 g5g4 h0h6` |
| h2e2 | 20 | completed | b9c7 | 28 | 3152805 | 3060 | 4 | `b9c7 h0g2 h9g7 g3g4 c6c5 i0h0 i9h9 b0a2 a6a5 a0a1 a5a4 a3a4` |
| h2e2 | 22 | completed | b9c7 | 17 | 6669072 | 6536 | 4 | `b9c7 h0g2 h9g7 g3g4 c6c5 b0a2 i9h9 i0h0 a6a5 b2c2 c7b5 a0a1` |
| h2e2 | 24 | completed | h9g7 | 15 | 11662301 | 11383 | 4 | `h9g7 h0g2 i9h9 i0h0 b9c7 c3c4 g6g5 b0c2 b7b3 g3g4 g5g4 h0h6` |
| b2e2 | 14 | completed | b9c7 | 19 | 309342 | 282 | 4 | `b9c7 b0c2 c6c5 g3g4 a9b9 a0b0 b7b3 h2h4 h7g7 h0i2 g9e7 i0h0` |
| b2e2 | 16 | completed | b9c7 | 19 | 673077 | 625 | 4 | `b9c7 c3c4 a9b9 b0c2 b7a7 h0g2 g6g5 h2h6 c9e7 h6c6 h9g7 i0h0` |
| b2e2 | 18 | completed | b9c7 | 20 | 1395237 | 1327 | 4 | `b9c7 c3c4 a9b9 b0c2 g6g5 a0b0 h9g7 h2g2 g9e7 h0i2 g7h5 i0i1` |
| b2e2 | 20 | completed | b9c7 | 20 | 2505339 | 2468 | 4 | `b9c7 c3c4 g6g5 b0c2 h9g7 a0b0 a9b9 h0i2 i6i5 i0i1 i5i4 i3i4` |
| b2e2 | 22 | completed | h9g7 | 18 | 4709003 | 4629 | 4 | `h9g7 b0c2 b9c7 a0b0 a9b9 h0i2 g6g5 b0b4 f9e8 h2f2 g7h5 i3i4` |
| b2e2 | 24 | completed | h9g7 | 17 | 7834765 | 7700 | 4 | `h9g7 b0c2 b9c7 a0b0 a9b9 c3c4 g6g5 h2g2 f9e8 h0i2 g7h5 i0i1` |
| c3c4 | 14 | completed | b7c7 | 22 | 423863 | 383 | 4 | `b7c7 h2e2 g9e7 b0c2 c6c5 c4c5 c7c2 e2e6 f9e8 e6e4 h9f8 i0i2` |
| c3c4 | 16 | completed | b7c7 | 15 | 890695 | 819 | 4 | `b7c7 h2e2 h7e7 h0g2 h9g7 b2d2 c6c5 i0h0 b9a7` |
| c3c4 | 18 | completed | b7c7 | 21 | 1827132 | 1701 | 4 | `b7c7 h2e2 c9e7 b0a2 i9i8 h0g2 i8d8 a0b0 d9e8 i0h0 h9i7 g3g4` |
| c3c4 | 20 | completed | b7c7 | 21 | 2978656 | 2832 | 4 | `b7c7 h2e2 c9e7 h0g2 c6c5 c0a2 c5c4 a2c4 i9i8 e2e6 d9e8 i0h0` |
| c3c4 | 22 | completed | b7c7 | 15 | 5171266 | 4954 | 4 | `b7c7 h2e2 c9e7 h0g2 c6c5 c0a2 c5c4 a2c4 i9i8 e2e6 d9e8 i0h0` |
| c3c4 | 24 | completed | b7c7 | 17 | 9586112 | 9498 | 4 | `b7c7 h2e2 c9e7 h0g2 c6c5 c0a2 c5c4 i0h0 i9i8 e2e6 d9e8 a2c4` |
| g0e2 | 14 | completed | b7d7 | 19 | 288528 | 252 | 4 | `b7d7 c3c4 b9c7 b0c2 a9b9 a0b0 h9g7 g3g4 h7i7 h2f2 i9h9 h0g2` |
| g0e2 | 16 | completed | b7d7 | 19 | 622074 | 549 | 4 | `b7d7 g3g4 b9c7 a0a1 a9b9 a1d1 f9e8 h2f2 h9i7 b0a2 i9h9 h0g2` |
| g0e2 | 18 | completed | b7d7 | 17 | 1330573 | 1180 | 4 | `b7d7 a0a1 b9c7 a1d1 d9e8 d1d6 d7d9 b2d2 a9b9 d2d9 c7d9 b0a2` |
| g0e2 | 20 | completed | h7e7 | 17 | 2844614 | 2583 | 4 | `h7e7 g3g4 e7e3 f0e1 e3e4 b0c2 b9c7 h0g2 h9g7 i0h0 c6c5 a0a1` |
| g0e2 | 22 | completed | b7d7 | 17 | 5969609 | 5516 | 4 | `b7d7 g3g4 b9c7 b0a2 a9b9 a0a1 h7f7 a1d1 d9e8 d1d6 d7d9 h2f2` |
| g0e2 | 24 | completed | b7d7 | 15 | 8882866 | 8304 | 4 | `b7d7 g3g4 b9c7 b0a2 a9b9 a0a1 h7f7 a1d1 d9e8 h2f2 h9i7 h0g2` |
| c0e2 | 14 | completed | c6c5 | 18 | 311972 | 302 | 4 | `c6c5 h0g2 c9e7 h2i2 h9i7 i0h0 h7g7 i2i6 i9h9 h0h9 i7h9 i6e6` |
| c0e2 | 16 | completed | c6c5 | 21 | 636515 | 604 | 4 | `c6c5 h0g2 h9i7 h2i2 b9c7 i0h0 i9h9 g3g4 c9e7 b0c2 d9e8 i3i4` |
| c0e2 | 18 | completed | b7e7 | 19 | 1318569 | 1266 | 4 | `b7e7 b0c2 b9c7 c3c4 h7f7 h0g2 a9b9 a0b0 h9g7 b2b6 i9h9 i0h0` |
| c0e2 | 20 | completed | b7e7 | 17 | 2235865 | 2133 | 4 | `b7e7 b0c2 b9c7 c3c4 h7f7 h0g2 a9b9 a0b0 h9g7 i0h0 i9h9 g3g4` |
| c0e2 | 22 | completed | h7f7 | 14 | 4498124 | 4267 | 4 | `h7f7 c3c4 h9g7 h0i2 i9h9 i0h0 g6g5 b0c2 c9e7 c2d4 b9c7 d0e1` |
| c0e2 | 24 | completed | h7f7 | 16 | 10661414 | 10204 | 4 | `h7f7 c3c4 h9g7 h0i2 i9h9 i0h0 g6g5 b0c2 c9e7 b2b1 b9d8 d0e1` |
| g3g4 | 14 | completed | h7g7 | 16 | 367445 | 329 | 4 | `h7g7 b2e2 c9e7 h0i2 h9i7 i0h0 i9h9 h2h6 b9d8 a0a1 d9e8 a1d1` |
| g3g4 | 16 | completed | c6c5 | 23 | 892346 | 818 | 4 | `c6c5 h0g2 b9c7 i0i1 g9e7 c0e2 h9f8 b0d1 i9g9 a0c0 g6g5 g4g5` |
| g3g4 | 18 | completed | h7g7 | 26 | 1773525 | 1670 | 4 | `h7g7 b2e2 c9e7 h0i2 h9i7 i0h0 i9h9 h2h6 d9e8 b0c2 c6c5 e3e4` |
| g3g4 | 20 | completed | h7g7 | 22 | 3500117 | 3347 | 4 | `h7g7 b2e2 g9e7 h0i2 c6c5 b0c2 b9c7 a0b0 a9b9 b0b4 b7a7 e2e6` |
| g3g4 | 22 | completed | h7g7 | 22 | 5694420 | 5429 | 4 | `h7g7 b2e2 g9e7 h0i2 c6c5 b0c2 b9c7 a0b0 a9b9 b0b4 b7a7 e2e6` |
| g3g4 | 24 | completed | h7g7 | 15 | 9126254 | 8657 | 4 | `h7g7 b2e2 g9e7 f0e1 c6c5 b0c2 b9c7 a0b0 a9b9 b0b4 h9i7 h2f2` |
| b0c2 | 14 | completed | c6c5 | 11 | 295841 | 275 | 4 | `c6c5 b2a2 b9c7 a0b0 a9b9 b0b4 g9e7 h0g2 h9f8` |
| b0c2 | 16 | completed | c6c5 | 12 | 655066 | 619 | 4 | `c6c5 h2e2 h9g7 h0g2 b9c7 g3g4 i9h9 i0h0 h7h3 b2b6 h3g3 h0h9` |
| b0c2 | 18 | completed | c6c5 | 12 | 1316313 | 1262 | 4 | `c6c5 h2e2 h9g7 h0g2 b9c7 e3e4 i9h9 e4e5 d9e8 c2e3 e6e5 e2e5` |
| b0c2 | 20 | completed | c6c5 | 5 | 2565752 | 2560 | 4 | `c6c5 b2a2 b9c7 a0b0 a9b9 g3g4 h9g7 h0g2 h7h3 b0b6 h3c3 c0e2` |
| b0c2 | 22 | completed | c6c5 | 16 | 5183842 | 5302 | 4 | `c6c5 h2e2 h9g7 h0g2 i9h9 i0h0 h7h3 g3g4 b9c7 g2f4 a9a8 g4g5` |
| b0c2 | 24 | completed | c6c5 | 11 | 9435267 | 10160 | 4 | `c6c5 h2e2 h9g7 h0g2 i9h9 i0h0 h7h3 g3g4 b9c7 g2f4 a9a8 g4g5` |
| h0g2 | 14 | completed | g6g5 | 15 | 331772 | 330 | 4 | `g6g5 b2e2 b9c7 b0c2 h9g7 a0b0 a9b9 b0b4 b7a7 b4b9 c7b9 e3e4` |
| h0g2 | 16 | completed | g6g5 | 11 | 839654 | 870 | 4 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 h9g7 c3c4 b7b3 h2h6 b3g3 b0b9` |
| h0g2 | 18 | completed | g6g5 | 10 | 1562914 | 1619 | 4 | `g6g5 h2i2 h9g7 i0h0 i9h9 c3c4 h7h3 b0c2 b9c7 a0a1 b7b3 c2b4` |
| h0g2 | 20 | completed | g6g5 | 5 | 2940143 | 3058 | 4 | `g6g5 b2e2 b9c7 b0c2 a9b9 c3c4 h9g7 a0b0 b7b3 h2h6 b3g3 b0b9` |
| h0g2 | 22 | completed | g6g5 | 8 | 5656200 | 5822 | 4 | `g6g5 c3c4 h9g7 b2e2 b9c7 b0c2 a9b9 a0b0 b7b3 h2h6 b3g3 b0b9` |
| h0g2 | 24 | completed | g6g5 | 3 | 9845481 | 10142 | 4 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 b7b3 c3c4 h9g7 h2h6 b3g3 b0b9` |
| h2f2 | 14 | completed | b7e7 | 7 | 365127 | 347 | 4 | `b7e7 b0c2 b9c7 h0g2 h9i7 i0h0 i9h9 a0b0 a9b9 b2b6 c6c5 h0h5` |
| h2f2 | 16 | completed | b7e7 | 6 | 773533 | 757 | 4 | `b7e7 b0c2 b9c7 h0g2 h9i7 a0b0 a9b9 c3c4 b9b5 f0e1 i6i5 g0e2` |
| h2f2 | 18 | completed | b7e7 | 10 | 1756436 | 1754 | 4 | `b7e7 b0c2 b9c7 h0g2 h9i7 c3c4 a9b9 a0b0 b9b5 g3g4 i9h9 d0e1` |
| h2f2 | 20 | completed | b7e7 | 8 | 3053790 | 3059 | 4 | `b7e7 b0c2 b9c7 h0g2 h9i7 c3c4 a9b9 a0b0 b9b5 f0e1 i6i5 b2a2` |
| h2f2 | 22 | completed | b7e7 | 8 | 4854397 | 4872 | 4 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 h9i7 c3c4 b9b5 f0e1 c6c5 c4c5` |
| h2f2 | 24 | completed | b7e7 | 11 | 7679170 | 7686 | 4 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 h9i7 c3c4 b9b5 f0e1 i6i5 b2a2` |
