# Pikafish Small Grid Opening Probe

This is a dense low-depth parameter probe, not a game-theoretic proof.

## Configuration

- Start FEN: `rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1`.
- Red opening moves: `44`.
- Depths: `4, 6, 8, 10, 12`.
- MultiPV settings: `1, 2, 3, 4`.
- Threads: `1`.
- Hash: `64 MB`.
- Clear hash per query: `True`.
- Per-query max seconds: `15.0`.
- Runtime seconds: `32.766`.

Each MultiPV setting runs one `go depth max(depths)` per red opening move and captures the requested intermediate depths.

Scores are normalized to Red's point of view.

## Grid Summary

| MultiPV | Depth | Positions | Completed | Max seconds | Min | Median | Avg | Max | PV repeat | PV third-repeat | Leader | Score | Reply |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---|---:|:---|
| 1 | 4 | 44 | 44 | 0 | -182 | -26.0 | -40.66 | 32 | 0 | 0 | b2e2 | 32 | b9c7 |
| 1 | 6 | 44 | 44 | 0 | -134 | -13.5 | -27.93 | 30 | 0 | 0 | h2e2 | 30 | b9c7 |
| 1 | 8 | 44 | 44 | 0 | -124 | -18.0 | -25.41 | 29 | 0 | 0 | h2e2 | 29 | h9g7 |
| 1 | 10 | 44 | 44 | 0 | -120 | -17.5 | -22.23 | 31 | 0 | 0 | b2d2 | 31 | h7e7 |
| 1 | 12 | 44 | 44 | 0 | -122 | -19.0 | -22.55 | 30 | 0 | 0 | c3c4 | 30 | b7c7 |
| 2 | 4 | 44 | 44 | 0 | -194 | -34.5 | -47.32 | 41 | 0 | 0 | h2e2 | 41 | b9c7 |
| 2 | 6 | 44 | 44 | 0 | -117 | -19.0 | -28.32 | 41 | 0 | 0 | b2e2 | 41 | b9c7 |
| 2 | 8 | 44 | 44 | 0 | -109 | -14.0 | -23.43 | 33 | 0 | 0 | g3g4 | 33 | c6c5 |
| 2 | 10 | 44 | 44 | 0 | -115 | -18.5 | -22.32 | 32 | 0 | 0 | g3g4 | 32 | h7g7 |
| 2 | 12 | 44 | 44 | 0 | -113 | -21.0 | -23.84 | 29 | 0 | 0 | h2e2 | 29 | h9g7 |
| 3 | 4 | 44 | 44 | 0 | -194 | -30.5 | -49.82 | 31 | 0 | 0 | h0g2 | 31 | b9c7 |
| 3 | 6 | 44 | 44 | 0 | -135 | -16.0 | -29.68 | 30 | 0 | 0 | c3c4 | 30 | b9a7 |
| 3 | 8 | 44 | 44 | 0 | -124 | -13.5 | -23.7 | 33 | 0 | 0 | g3g4 | 33 | c6c5 |
| 3 | 10 | 44 | 44 | 0 | -131 | -14.5 | -22.5 | 30 | 0 | 0 | h2e2 | 30 | h9g7 |
| 3 | 12 | 44 | 44 | 0 | -117 | -17.0 | -23.48 | 24 | 0 | 0 | h2e2 | 24 | h9g7 |
| 4 | 4 | 44 | 44 | 0 | -193 | -31.0 | -48.07 | 33 | 0 | 0 | h2e2 | 33 | h9g7 |
| 4 | 6 | 44 | 44 | 0 | -135 | -16.5 | -27.89 | 40 | 0 | 0 | h2e2 | 40 | b9c7 |
| 4 | 8 | 44 | 44 | 0 | -130 | -14.0 | -23.14 | 33 | 0 | 0 | h2e2 | 33 | h9g7 |
| 4 | 10 | 44 | 44 | 0 | -130 | -16.5 | -23.59 | 31 | 0 | 0 | b2e2 | 31 | b9c7 |
| 4 | 12 | 44 | 44 | 0 | -118 | -19.5 | -24.5 | 27 | 0 | 0 | h2e2 | 27 | h9g7 |

## Leaders By Parameter

| MultiPV | Depth | Red move | Red score | Black reply |
|---:|---:|:---|---:|:---|
| 1 | 4 | b2e2 | 32 | b9c7 |
| 1 | 6 | h2e2 | 30 | b9c7 |
| 1 | 8 | h2e2 | 29 | h9g7 |
| 1 | 10 | b2d2 | 31 | h7e7 |
| 1 | 12 | c3c4 | 30 | b7c7 |
| 2 | 4 | h2e2 | 41 | b9c7 |
| 2 | 6 | b2e2 | 41 | b9c7 |
| 2 | 8 | g3g4 | 33 | c6c5 |
| 2 | 10 | g3g4 | 32 | h7g7 |
| 2 | 12 | h2e2 | 29 | h9g7 |
| 3 | 4 | h0g2 | 31 | b9c7 |
| 3 | 6 | c3c4 | 30 | b9a7 |
| 3 | 8 | g3g4 | 33 | c6c5 |
| 3 | 10 | h2e2 | 30 | h9g7 |
| 3 | 12 | h2e2 | 24 | h9g7 |
| 4 | 4 | h2e2 | 33 | h9g7 |
| 4 | 6 | h2e2 | 40 | b9c7 |
| 4 | 8 | h2e2 | 33 | h9g7 |
| 4 | 10 | b2e2 | 31 | b9c7 |
| 4 | 12 | h2e2 | 27 | h9g7 |

## Depth 12 MultiPV 4 Top Red Moves

| Rank | Red move | Reply | Red score | Nodes | Time ms | PV repeat |
|---:|:---|:---|---:|---:|---:|:---:|
| 1 | h2e2 | h9g7 | 27 | 120480 | 108 | False |
| 2 | b2e2 | b9c7 | 25 | 107590 | 93 | False |
| 3 | g0e2 | g6g5 | 21 | 135472 | 114 | False |
| 4 | c0e2 | c6c5 | 21 | 143173 | 122 | False |
| 5 | c3c4 | b7c7 | 19 | 159571 | 142 | False |
| 6 | g3g4 | h7g7 | 17 | 164366 | 148 | False |
| 7 | h2f2 | b7e7 | 16 | 171603 | 152 | False |
| 8 | h0g2 | g6g5 | 16 | 109225 | 97 | False |
| 9 | b0c2 | c6c5 | 16 | 169685 | 158 | False |
| 10 | b2f2 | c6c5 | 15 | 187374 | 160 | False |

## Depth 12 MultiPV 4 Bottom Red Moves

| Rank | Red move | Reply | Red score | Nodes | Time ms | PV repeat |
|---:|:---|:---|---:|---:|---:|:---:|
| 1 | b2b9 | a9b9 | -118 | 43892 | 32 | False |
| 2 | h2h9 | i9h9 | -114 | 75243 | 61 | False |
| 3 | e0e1 | h7e7 | -102 | 141860 | 123 | False |
| 4 | e3e4 | b7e7 | -93 | 172879 | 147 | False |
| 5 | i0i1 | h7h0 | -83 | 77246 | 62 | False |
| 6 | b2b5 | c6c5 | -68 | 183969 | 167 | False |
| 7 | a0a1 | b7b0 | -67 | 89257 | 74 | False |
| 8 | h2h5 | g6g5 | -66 | 146851 | 134 | False |
| 9 | i0i2 | h7h0 | -66 | 113725 | 94 | False |
| 10 | a0a2 | b7b0 | -65 | 173546 | 152 | False |

## Most Sensitive Moves At Depth 12

Reference is MultiPV `4`. `Score range` is the spread across MultiPV settings at the final depth.

| Red move | Reference score | Reference reply | Score range | Reply variants |
|:---|---:|:---|---:|:---|
| i0i1 | -83 | h7h0 | 28 | h7h0 |
| a0a1 | -67 | b7b0 | 19 | b7b0 |
| g0i2 | -55 | b9c7 | 18 | b9c7, c6c5, h7e7 |
| b2d2 | 10 | h7e7 | 18 | h7e7 |
| e0e1 | -102 | h7e7 | 17 | b9c7, g6g5, h7e7 |
| h2g2 | -20 | b7e7 | 17 | b7e7 |
| b0a2 | 3 | h7e7 | 16 | h7e7 |
| a0a2 | -65 | b7b0 | 14 | b7b0 |
| h2f2 | 16 | b7e7 | 14 | b7e7 |
| b2b3 | -33 | c6c5 | 13 | c6c5 |

## Full Rows

| MultiPV | Red move | Depth | Stop | Reply | Red score | Nodes | Time ms | Captured PVs | Top PV |
|---:|:---|---:|:---|:---|---:|---:|---:|---:|:---|
| 1 | a0a1 | 4 | completed | c6c5 | -95 | 660 | 1 | 1 | `c6c5 c3c4 b7b0 c4c5` |
| 1 | a0a1 | 6 | completed | b7b0 | -100 | 1732 | 2 | 1 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0` |
| 1 | a0a1 | 8 | completed | b7b0 | -110 | 2676 | 3 | 1 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0` |
| 1 | a0a1 | 10 | completed | b7b0 | -69 | 18065 | 17 | 1 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0a1 h2h4 g9e7 h0g2` |
| 1 | a0a1 | 12 | completed | b7b0 | -79 | 36676 | 35 | 1 | `b7b0 b2e2 h7e7 a1b1 b0a0 e2e6 d9e8 e6e4 h9g7 h2e2` |
| 1 | a0a2 | 4 | completed | b7b0 | -182 | 404 | 1 | 1 | `b7b0 a2a0 h7b7` |
| 1 | a0a2 | 6 | completed | b7b0 | -83 | 1958 | 2 | 1 | `b7b0 b2e2 b9c7 a2b2 a9b9 b2b9 c7b9 e2e6` |
| 1 | a0a2 | 8 | completed | b7b0 | -54 | 21592 | 20 | 1 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 h7e7 b2b0 a0c0 b0c0` |
| 1 | a0a2 | 10 | completed | b7b0 | -51 | 38961 | 35 | 1 | `b7b0 b2e2 h9g7 a2b2 b0a0 b2b0` |
| 1 | a0a2 | 12 | completed | b7b0 | -58 | 89020 | 84 | 1 | `b7b0 b2e2 h9g7 a2b2 b0a0 h0g2 b9c7 i0i1` |
| 1 | a3a4 | 4 | completed | b7e7 | -27 | 575 | 1 | 1 | `b7e7` |
| 1 | a3a4 | 6 | completed | c6c5 | -14 | 2379 | 3 | 1 | `c6c5 h0g2 g6g5 h2i2 b9c7 i0h0` |
| 1 | a3a4 | 8 | completed | h7e7 | -10 | 5053 | 6 | 1 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0a2 h9h4` |
| 1 | a3a4 | 10 | completed | b9c7 | -8 | 18135 | 19 | 1 | `b9c7 h0g2 g6g5 b0a2 c6c5 b2c2 h9g7 a0b0 g7f5 g0e2` |
| 1 | a3a4 | 12 | completed | b9c7 | -10 | 41237 | 43 | 1 | `b9c7 h2e2 c6c5 h0g2 h9g7 g3g4` |
| 1 | b0a2 | 4 | completed | g6g5 | -8 | 504 | 1 | 1 | `g6g5 h2i2 h7e7` |
| 1 | b0a2 | 6 | completed | h7e7 | 9 | 2421 | 3 | 1 | `h7e7 h0g2 h9g7 g3g4 i9h9 i0h0` |
| 1 | b0a2 | 8 | completed | h7e7 | 5 | 9610 | 10 | 1 | `h7e7 b2e2 b9c7` |
| 1 | b0a2 | 10 | completed | h7e7 | 5 | 16354 | 16 | 1 | `h7e7 h2e2 h9g7 h0g2 i9h9 g3g4 h9h5 a0a1 b9c7 a1d1` |
| 1 | b0a2 | 12 | completed | h7e7 | 2 | 26960 | 25 | 1 | `h7e7 h2e2 h9g7 h0g2 i9h9 g3g4 a6a5 a0a1 b9c7 a1d1` |
| 1 | b0c2 | 4 | completed | c6c5 | -9 | 440 | 1 | 1 | `c6c5` |
| 1 | b0c2 | 6 | completed | c6c5 | 12 | 2983 | 3 | 1 | `c6c5 h2e2 h9g7 g3g4 i9h9` |
| 1 | b0c2 | 8 | completed | c6c5 | 24 | 8781 | 9 | 1 | `c6c5 b2a2 b9c7 a0b0 a9b9 g3g4 g9e7 h2f2 h9f8 h0g2` |
| 1 | b0c2 | 10 | completed | c6c5 | 23 | 9718 | 10 | 1 | `c6c5 b2a2 b9c7 a0b0 a9b9 b0b4 g9e7 h2f2 h9f8 h0g2` |
| 1 | b0c2 | 12 | completed | c6c5 | 20 | 18341 | 18 | 1 | `c6c5 b2a2 b9c7 a0b0 a9b9 g3g4 h9g7 c0e2 b7b3 h0g2` |
| 1 | b2a2 | 4 | completed | b7e7 | -9 | 493 | 1 | 1 | `b7e7 h0g2 b9c7` |
| 1 | b2a2 | 6 | completed | c6c5 | 10 | 2461 | 3 | 1 | `c6c5 g3g4 b9c7 b0c2 c7b5` |
| 1 | b2a2 | 8 | completed | h7e7 | 20 | 7318 | 7 | 1 | `h7e7 b0c2 b9c7 a0b0` |
| 1 | b2a2 | 10 | completed | c6c5 | 16 | 12982 | 12 | 1 | `c6c5 b0c2 b9c7 a0b0 a9b9 g3g4 b7b3 h2h4 h9g7` |
| 1 | b2a2 | 12 | completed | c6c5 | 12 | 23440 | 23 | 1 | `c6c5 b0c2 b9c7 h2e2 a9b9 h0g2 h9g7 a0b0 b7b3 i0h0` |
| 1 | b2b1 | 4 | completed | h7e7 | -51 | 1431 | 1 | 1 | `h7e7 h0g2 h9g7 i0h0` |
| 1 | b2b1 | 6 | completed | b7e7 | -39 | 4864 | 4 | 1 | `b7e7 h0g2 b9c7 b1e1 a9b9` |
| 1 | b2b1 | 8 | completed | b7e7 | -48 | 8615 | 7 | 1 | `b7e7 b1e1 b9c7 g3g4 h7g7 b0c2 a9b9 c3c4 g6g5` |
| 1 | b2b1 | 10 | completed | b7e7 | -38 | 18883 | 17 | 1 | `b7e7 h0g2 g6g5 b1g1 h7g7 b0c2 a9a8 a0b0 b9c7 b0b4` |
| 1 | b2b1 | 12 | completed | b7e7 | -39 | 28343 | 26 | 1 | `b7e7 h0g2 b9c7 b1g1 a9a8 a0a2 h7h5 d0e1 h9i7 a2f2` |
| 1 | b2b3 | 4 | completed | c6c5 | -55 | 670 | 1 | 1 | `c6c5` |
| 1 | b2b3 | 6 | completed | h7e7 | -41 | 6390 | 6 | 1 | `h7e7 h0g2 h9g7 g3g4 i9h9` |
| 1 | b2b3 | 8 | completed | c6c5 | -51 | 9749 | 9 | 1 | `c6c5 g3g4 h9i7 h0g2 h7g7 i0h0 i9h9` |
| 1 | b2b3 | 10 | completed | c6c5 | -48 | 29059 | 27 | 1 | `c6c5 h2e2 b9c7 h0g2 h9g7 g3g4` |
| 1 | b2b3 | 12 | completed | c6c5 | -46 | 41554 | 38 | 1 | `c6c5 h2e2 b9c7 h0g2 h9i7 i0h0 i9h9 b0c2 c9e7 b3b6` |
| 1 | b2b4 | 4 | completed | h9g7 | -24 | 630 | 1 | 1 | `h9g7 b0c2` |
| 1 | b2b4 | 6 | completed | c6c5 | -30 | 3250 | 4 | 1 | `c6c5 b0c2 g6g5 b4i4 h9i7 a0b0 b9c7 h2e2` |
| 1 | b2b4 | 8 | completed | c6c5 | -26 | 7872 | 8 | 1 | `c6c5 b0c2 b9c7 c0e2 g6g5 h0i2 c9e7 h2f2 h9g7 i0h0` |
| 1 | b2b4 | 10 | completed | c6c5 | -23 | 14029 | 14 | 1 | `c6c5 b0c2 g6g5 h0i2 b9c7 c0e2 h9g7 b4i4 h7i7 a0b0` |
| 1 | b2b4 | 12 | completed | c6c5 | -23 | 28790 | 27 | 1 | `c6c5 h0i2 b9c7 b0c2 g6g5 c0e2 h9g7 b4i4 h7i7` |
| 1 | b2b5 | 4 | completed | h9g7 | -71 | 1303 | 2 | 1 | `h9g7 b0c2 c6c5` |
| 1 | b2b5 | 6 | completed | c6c5 | -65 | 3161 | 3 | 1 | `c6c5 b0c2 b9c7 b5b4 g6g5 b4i4 h9i7` |
| 1 | b2b5 | 8 | completed | c6c5 | -65 | 4519 | 5 | 1 | `c6c5 b0c2 h7e7 b5b4 h9g7 b4h4 b9c7 a0b0` |
| 1 | b2b5 | 10 | completed | c6c5 | -67 | 21770 | 19 | 1 | `c6c5 b0c2 b9c7 b5b4 g6g5 h0i2 h9g7 b4i4 g9i7 a0b0` |
| 1 | b2b5 | 12 | completed | c6c5 | -66 | 32253 | 29 | 1 | `c6c5 b0c2 b9c7 b5b1 b7a7 g3g4 h9i7 a0b0 a9b9 h0g2` |
| 1 | b2b6 | 4 | completed | b9c7 | -42 | 707 | 1 | 1 | `b9c7 b0c2` |
| 1 | b2b6 | 6 | completed | b9c7 | -26 | 2192 | 2 | 1 | `b9c7 g3g4 c6c5 h2e2 h9g7 b0c2` |
| 1 | b2b6 | 8 | completed | b9c7 | -21 | 5213 | 5 | 1 | `b9c7 b0c2 c6c5 b6c6 g6g5` |
| 1 | b2b6 | 10 | completed | b9c7 | -24 | 17717 | 16 | 1 | `b9c7 c3c4 h7e7 h0g2 h9g7 i0h0 a9a8 b0c2 a8d8 g3g4` |
| 1 | b2b6 | 12 | completed | b9c7 | -24 | 25236 | 23 | 1 | `b9c7 b0c2 g6g5 h2e2 h9g7 h0g2 i9h9 c3c4 a9a8 i0h0` |
| 1 | b2b9 | 4 | completed | a9b9 | -94 | 766 | 1 | 1 | `a9b9 h2e2 b7e7 b0c2` |
| 1 | b2b9 | 6 | completed | a9b9 | -115 | 2018 | 2 | 1 | `a9b9 b0c2 b7e7 h2e2` |
| 1 | b2b9 | 8 | completed | a9b9 | -123 | 3847 | 3 | 1 | `a9b9 h2e2 b7e7 b0c2 h9g7 h0g2 i9h9 i0h0` |
| 1 | b2b9 | 10 | completed | a9b9 | -120 | 9011 | 8 | 1 | `a9b9 b0c2 b7c7 g3g4 h7e7 h0g2 h9g7 i0h0` |
| 1 | b2b9 | 12 | completed | a9b9 | -122 | 36657 | 33 | 1 | `a9b9 b0c2 b7e7 h0g2 h9i7 a0a1 h7g7 i0h0 i9h9 h2i2` |
| 1 | b2c2 | 4 | completed | h7e7 | -38 | 491 | 1 | 1 | `h7e7 f0e1 h9g7 g3g4` |
| 1 | b2c2 | 6 | completed | h7e7 | -16 | 2381 | 2 | 1 | `h7e7 h0g2 h9g7 b0a2 b9a7 a0b0` |
| 1 | b2c2 | 8 | completed | h7e7 | -21 | 4712 | 5 | 1 | `h7e7 g0e2 b9a7 b0a2 a9b9 a3a4 h9g7` |
| 1 | b2c2 | 10 | completed | h7e7 | -21 | 16975 | 19 | 1 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0a2 b7b2 g0e2 b9a7` |
| 1 | b2c2 | 12 | completed | h7e7 | -25 | 31838 | 34 | 1 | `h7e7 h2e2 h9g7 b0a2 b9a7 a0b0 a9b9 h0g2 i9h9 b0b4` |
| 1 | b2d2 | 4 | completed | b9c7 | 5 | 1769 | 2 | 1 | `b9c7` |
| 1 | b2d2 | 6 | completed | c6c5 | 3 | 2020 | 2 | 1 | `c6c5 h0g2 b9c7 g3g4 a9b9` |
| 1 | b2d2 | 8 | completed | g6g5 | 13 | 4591 | 5 | 1 | `g6g5 b0c2 b9a7 a0b0 a9b9 c3c4 h9g7 g3g4 g5g4` |
| 1 | b2d2 | 10 | completed | h7e7 | 31 | 18628 | 20 | 1 | `h7e7 h0g2 b9c7 b0c2` |
| 1 | b2d2 | 12 | completed | h7e7 | 28 | 56209 | 62 | 1 | `h7e7 h0g2 h9g7 b0c2 b9a7 i0h0 i9h9 a0b0 b7c7 h2h6` |
| 1 | b2e2 | 4 | completed | b9c7 | 32 | 1059 | 1 | 1 | `b9c7 b0c2 c6c5 a0b0` |
| 1 | b2e2 | 6 | completed | b9c7 | 30 | 1241 | 1 | 1 | `b9c7 c3c4 g6g5 b0c2 a9b9 a0b0` |
| 1 | b2e2 | 8 | completed | b9c7 | 27 | 2662 | 3 | 1 | `b9c7 c3c4 b7a7 b0c2 a9b9 g3g4 b9b5 a0b0 b5b0 c2b0` |
| 1 | b2e2 | 10 | completed | b9c7 | 26 | 12483 | 13 | 1 | `b9c7 c3c4 a9b9 b0c2 b7a7` |
| 1 | b2e2 | 12 | completed | b9c7 | 22 | 23258 | 23 | 1 | `b9c7 c3c4 g6g5 b0c2 a9b9 h2g2 h9g7` |
| 1 | b2f2 | 4 | completed | b9c7 | -6 | 1854 | 2 | 1 | `b9c7 b0c2 a9b9 g3g4` |
| 1 | b2f2 | 6 | completed | c6c5 | 9 | 5740 | 5 | 1 | `c6c5 g3g4 b9c7 b0c2 a9b9` |
| 1 | b2f2 | 8 | completed | c6c5 | 22 | 16400 | 14 | 1 | `c6c5 b0c2 b9c7 g3g4 a9b9 a0b0 h9i7 b0b4 h7f7 h0g2` |
| 1 | b2f2 | 10 | completed | c6c5 | 27 | 21849 | 18 | 1 | `c6c5 b0c2 b9c7 a0b0 a9b9 g3g4 b7b3 h0g2 c9e7 g2f4` |
| 1 | b2f2 | 12 | completed | c6c5 | 19 | 32787 | 27 | 1 | `c6c5 b0c2 b9c7 g3g4 a9b9 h0g2 h9i7 g0e2 h7f7 h2h7` |
| 1 | b2g2 | 4 | completed | g9e7 | -7 | 1825 | 2 | 1 | `g9e7 b0c2 a9a8 a0b0` |
| 1 | b2g2 | 6 | completed | c6c5 | -13 | 3206 | 3 | 1 | `c6c5 b0c2 b7d7 a0b0 b9c7` |
| 1 | b2g2 | 8 | completed | b7d7 | -20 | 5802 | 5 | 1 | `b7d7 b0c2 c6c5 a0b0 b9c7` |
| 1 | b2g2 | 10 | completed | c6c5 | -11 | 11188 | 11 | 1 | `c6c5 g2c2 h7e7 g0e2 b9a7 c3c4 a9b9` |
| 1 | b2g2 | 12 | completed | c6c5 | -15 | 20311 | 19 | 1 | `c6c5 g2c2 b7e7 h2e2 b9c7 h0g2 c7d5 i0h0 h9g7 g3g4` |
| 1 | c0a2 | 4 | completed | b7e7 | -72 | 855 | 1 | 1 | `b7e7 d0e1 h9g7` |
| 1 | c0a2 | 6 | completed | b7e7 | -64 | 1859 | 2 | 1 | `b7e7 b0d1 b9c7 g3g4 a9b9` |
| 1 | c0a2 | 8 | completed | b7e7 | -49 | 9103 | 9 | 1 | `b7e7 h2e2 b9c7 h0g2 h9i7` |
| 1 | c0a2 | 10 | completed | b7e7 | -54 | 15239 | 15 | 1 | `b7e7 b2e2 b9c7 b0c2 a9b9 h2f2 i6i5 h0g2 h9i7 i0h0` |
| 1 | c0a2 | 12 | completed | b7e7 | -53 | 19000 | 18 | 1 | `b7e7 h2e2 b9c7 h0g2 h9i7 b2d2 a9b9 b0c2 h7g7 i0h0` |
| 1 | c0e2 | 4 | completed | g6g5 | -3 | 875 | 1 | 1 | `g6g5 h0g2 b7a7 c3c4` |
| 1 | c0e2 | 6 | completed | b7e7 | 1 | 2307 | 3 | 1 | `b7e7 g3g4 h9i7 i3i4 h7f7` |
| 1 | c0e2 | 8 | completed | b7e7 | 11 | 8546 | 8 | 1 | `b7e7 b0c2 b9c7 a0b0 g6g5 h2g2 a9b9 g3g4` |
| 1 | c0e2 | 10 | completed | b7e7 | 16 | 19324 | 18 | 1 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 b9b5` |
| 1 | c0e2 | 12 | completed | c6c5 | 26 | 61857 | 55 | 1 | `c6c5 h0g2 c9e7` |
| 1 | c3c4 | 4 | completed | g6g5 | 10 | 692 | 1 | 1 | `g6g5 b0c2 h9g7 c2d4` |
| 1 | c3c4 | 6 | completed | c9e7 | 23 | 2078 | 2 | 1 | `c9e7 b0c2 b9d8 c2d4 g6g5` |
| 1 | c3c4 | 8 | completed | b9a7 | 22 | 5200 | 5 | 1 | `b9a7 b0c2 g6g5 g0e2 b7c7 a0b0 a9b9 g3g4 g5g4` |
| 1 | c3c4 | 10 | completed | g6g5 | 27 | 8628 | 8 | 1 | `g6g5 b0c2 h9g7 h2g2 b9c7 h0i2 g7h5 i0i1 h5i3 i1h1` |
| 1 | c3c4 | 12 | completed | b7c7 | 30 | 42148 | 40 | 1 | `b7c7 c0e2 b9a7 g3g4 h7e7 h0g2` |
| 1 | d0e1 | 4 | completed | g9e7 | -10 | 580 | 1 | 1 | `g9e7 g3g4` |
| 1 | d0e1 | 6 | completed | c6c5 | -13 | 3982 | 4 | 1 | `c6c5 h0i2` |
| 1 | d0e1 | 8 | completed | b7a7 | -5 | 10087 | 9 | 1 | `b7a7 c3c4 b9c7 b0c2 g6g5` |
| 1 | d0e1 | 10 | completed | b7e7 | -6 | 13439 | 12 | 1 | `b7e7 b0c2 c6c5 g3g4 b9c7 h0g2 a9b9` |
| 1 | d0e1 | 12 | completed | b9c7 | -12 | 32389 | 30 | 1 | `b9c7 h2f2 b7a7 h0i2 a9b9 c0e2 h9g7 i0h0 i9h9 h0h6` |
| 1 | e0e1 | 4 | completed | c6c5 | -102 | 1353 | 1 | 1 | `c6c5` |
| 1 | e0e1 | 6 | completed | b7e7 | -109 | 1761 | 1 | 1 | `b7e7 b0c2 b9c7 e1e0 a9b9 a0b0` |
| 1 | e0e1 | 8 | completed | b7e7 | -102 | 5298 | 5 | 1 | `b7e7 b0c2 b9c7 a0b0 a9b9 c3c4` |
| 1 | e0e1 | 10 | completed | c6c5 | -93 | 18729 | 16 | 1 | `c6c5 g3g4 h7g7 e1e0` |
| 1 | e0e1 | 12 | completed | g6g5 | -89 | 27687 | 25 | 1 | `g6g5 e1e0 b7e7 b0c2 c6c5 a0b0 h9g7 b2a2 b9c7` |
| 1 | e3e4 | 4 | completed | h7e7 | -99 | 1113 | 1 | 1 | `h7e7 g0e2 h9g7` |
| 1 | e3e4 | 6 | completed | h7e7 | -93 | 2056 | 2 | 1 | `h7e7 h2e2 h9g7 f0e1 i9h9 h0g2` |
| 1 | e3e4 | 8 | completed | h7e7 | -89 | 11251 | 10 | 1 | `h7e7 f0e1 e7e4 g0e2 b7e7 b0c2 h9g7` |
| 1 | e3e4 | 10 | completed | h7e7 | -92 | 13639 | 11 | 1 | `h7e7 f0e1 e7e4 g0e2 h9g7 h0f1 b7e7 b0c2 b9c7 a0b0` |
| 1 | e3e4 | 12 | completed | b7e7 | -85 | 54056 | 48 | 1 | `b7e7 f0e1 e7e4 h2e2 b9c7 b0c2 a9b9 a0b0 h7e7` |
| 1 | f0e1 | 4 | completed | c6c5 | -17 | 637 | 1 | 1 | `c6c5 g3g4` |
| 1 | f0e1 | 6 | completed | h7f7 | -10 | 3192 | 3 | 1 | `h7f7 c3c4 h9g7 g3g4 i9h9 h0g2 h9h5` |
| 1 | f0e1 | 8 | completed | h9g7 | -1 | 9560 | 9 | 1 | `h9g7 c3c4 h7i7 h2f2 i9h9` |
| 1 | f0e1 | 10 | completed | g6g5 | 2 | 17872 | 16 | 1 | `g6g5 b0a2 h9g7 b2d2 b9c7` |
| 1 | f0e1 | 12 | completed | g6g5 | -3 | 38769 | 35 | 1 | `g6g5 g0e2 h9g7 b2d2 b9c7 b0a2 h7i7` |
| 1 | g0e2 | 4 | completed | g6g5 | -5 | 526 | 1 | 1 | `g6g5` |
| 1 | g0e2 | 6 | completed | g9e7 | 14 | 3021 | 3 | 1 | `g9e7 g3g4 h9f8 h0g2` |
| 1 | g0e2 | 8 | completed | h7f7 | 18 | 7800 | 7 | 1 | `h7f7 c3c4 h9g7 b0c2 i9h9 c2d4 h9h5 d4c6 b9c7` |
| 1 | g0e2 | 10 | completed | h7e7 | 21 | 20078 | 19 | 1 | `h7e7 g3g4 h9g7 h0g2 i9h9 i0h0 b9a7 b0c2` |
| 1 | g0e2 | 12 | completed | h7e7 | 18 | 30355 | 28 | 1 | `h7e7 b0c2 h9g7 h2f2 i9h9 h0g2 b7c7` |
| 1 | g0i2 | 4 | completed | h7e7 | -75 | 1145 | 2 | 1 | `h7e7 h0g2 h9g7 g3g4` |
| 1 | g0i2 | 6 | completed | c6c5 | -42 | 4744 | 5 | 1 | `c6c5 b2e2 b9c7 b0c2 h9g7` |
| 1 | g0i2 | 8 | completed | c6c5 | -41 | 8130 | 7 | 1 | `c6c5 b2e2 b9c7 b0a2 h9g7 a0b0 c7d5 h0f1` |
| 1 | g0i2 | 10 | completed | c6c5 | -38 | 16722 | 15 | 1 | `c6c5 b2e2 b9c7 b0c2 h9g7 a0b0 c7d5 g3g4 a9a8` |
| 1 | g0i2 | 12 | completed | h7e7 | -46 | 27233 | 25 | 1 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 h9h5 i0h0 h5h0 g2h0` |
| 1 | g3g4 | 4 | completed | g9e7 | 16 | 1184 | 1 | 1 | `g9e7 h2i2` |
| 1 | g3g4 | 6 | completed | g9e7 | 26 | 3477 | 3 | 1 | `g9e7 h2i2 b9c7` |
| 1 | g3g4 | 8 | completed | h7g7 | 26 | 6749 | 6 | 1 | `h7g7 b0c2 h9i7 h0g2 i9h9 g2f4` |
| 1 | g3g4 | 10 | completed | h7g7 | 23 | 14556 | 13 | 1 | `h7g7 g0e2 h9i7 h0g2 i9h9 i0h0 b9c7` |
| 1 | g3g4 | 12 | completed | h7g7 | 18 | 27661 | 26 | 1 | `h7g7 c3c4 g6g5 g0e2 g5g4 b0c2 b9c7 h0f1 h9i7 c2d4` |
| 1 | h0g2 | 4 | completed | g6g5 | -4 | 577 | 1 | 1 | `g6g5 h2h1` |
| 1 | h0g2 | 6 | completed | g6g5 | 16 | 3208 | 3 | 1 | `g6g5 c3c4 h9g7 b2d2 i9i8` |
| 1 | h0g2 | 8 | completed | g6g5 | 23 | 5936 | 6 | 1 | `g6g5 c3c4 h9g7 b2d2 c9e7 b0c2 b9d8 a0b0` |
| 1 | h0g2 | 10 | completed | g6g5 | 19 | 11434 | 10 | 1 | `g6g5 c3c4 h9g7 b0c2 c9e7 c2d4 b9a7 b2d2 a9b9` |
| 1 | h0g2 | 12 | completed | g6g5 | 15 | 27115 | 25 | 1 | `g6g5 b2e2 h9g7 b0c2 b9c7 a0b0 a9b9 i0i1 g9e7 c3c4` |
| 1 | h0i2 | 4 | completed | c6c5 | -1 | 1661 | 1 | 1 | `c6c5 h2c2 b9c7 i0h0` |
| 1 | h0i2 | 6 | completed | c6c5 | -7 | 2840 | 2 | 1 | `c6c5 h2c2 b9c7 i0h0` |
| 1 | h0i2 | 8 | completed | b7e7 | -4 | 5053 | 5 | 1 | `b7e7 b2e2 b9c7 b0c2 a9b9 h2f2` |
| 1 | h0i2 | 10 | completed | b7e7 | -9 | 19781 | 18 | 1 | `b7e7 b2e2 b9c7 b0c2 a9b9 i0i1 h9g7` |
| 1 | h0i2 | 12 | completed | b7e7 | -4 | 40547 | 37 | 1 | `b7e7 b0c2 b9c7 i3i4 a9b9 i2h4 g6g5 h2h7 h9g7` |
| 1 | h2c2 | 4 | completed | c9e7 | -5 | 1964 | 2 | 1 | `c9e7` |
| 1 | h2c2 | 6 | completed | g6g5 | -11 | 2432 | 2 | 1 | `g6g5 c0e2 h9g7 h0g2 i9h9` |
| 1 | h2c2 | 8 | completed | g6g5 | -15 | 11421 | 11 | 1 | `g6g5 h0g2 h9g7 b0a2 i9h9 i0h0 c9e7 a0a1` |
| 1 | h2c2 | 10 | completed | g6g5 | -15 | 22161 | 21 | 1 | `g6g5 h0g2 h7f7 c2e2 b9c7 i0h0 c9e7` |
| 1 | h2c2 | 12 | completed | g6g5 | -14 | 36651 | 34 | 1 | `g6g5 h0g2 h9g7 b0a2 i9h9 i0h0 c9e7 a0a1 c6c5 a1f1` |
| 1 | h2d2 | 4 | completed | i9i8 | 1 | 1551 | 2 | 1 | `i9i8 h0g2 i8d8 f0e1` |
| 1 | h2d2 | 6 | completed | b7a7 | 12 | 6331 | 6 | 1 | `b7a7 b0c2` |
| 1 | h2d2 | 8 | completed | h9g7 | 16 | 8582 | 8 | 1 | `h9g7 h0g2 g6g5 i0h0 i9h9 h0h4 b9a7 g3g4` |
| 1 | h2d2 | 10 | completed | h9g7 | 23 | 18461 | 16 | 1 | `h9g7 c3c4 b7c7 b0a2 g6g5 h0g2 b9a7 a0b0` |
| 1 | h2d2 | 12 | completed | g6g5 | 16 | 40567 | 35 | 1 | `g6g5 c3c4 b7c7 b0a2 b9a7` |
| 1 | h2e2 | 4 | completed | h9g7 | 22 | 954 | 1 | 1 | `h9g7` |
| 1 | h2e2 | 6 | completed | b9c7 | 30 | 1777 | 1 | 1 | `b9c7 h0g2 h9g7 c3c4 i9h9 i0h0` |
| 1 | h2e2 | 8 | completed | h9g7 | 29 | 3162 | 3 | 1 | `h9g7 b0c2 c6c5 h0g2 i9h9 i0h0` |
| 1 | h2e2 | 10 | completed | h9g7 | 26 | 12083 | 11 | 1 | `h9g7 g3g4 i9h9 h0g2 h7i7 c3c4 b7c7 b0c2 c6c5 c2d4` |
| 1 | h2e2 | 12 | completed | h9g7 | 23 | 25269 | 23 | 1 | `h9g7 h0g2 g6g5 i0h0 i9h9 c3c4 h7h3 b2b4` |
| 1 | h2f2 | 4 | completed | b7e7 | -14 | 525 | 1 | 1 | `b7e7 d0e1 h9g7 g3g4` |
| 1 | h2f2 | 6 | completed | h7e7 | 20 | 5269 | 4 | 1 | `h7e7 b2e2 e7e3 f0e1 e3e5 h0g2` |
| 1 | h2f2 | 8 | completed | b7e7 | 28 | 11535 | 10 | 1 | `b7e7 b0c2 b9c7 h0g2 h9i7 c3c4` |
| 1 | h2f2 | 10 | completed | b7e7 | 28 | 24750 | 22 | 1 | `b7e7 b0c2 b9c7 h0g2 h9i7 i0h0 h7g7 c3c4 a9b9 a0b0` |
| 1 | h2f2 | 12 | completed | b7e7 | 22 | 45817 | 42 | 1 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0g2 h9i7 i0h0 i9h9 f2f7` |
| 1 | h2g2 | 4 | completed | b7e7 | -25 | 1362 | 2 | 1 | `b7e7 b0c2 b9c7 c3c4` |
| 1 | h2g2 | 6 | completed | c6c5 | -4 | 5024 | 5 | 1 | `c6c5 b0c2 h9i7 h0i2 b9c7` |
| 1 | h2g2 | 8 | completed | b7e7 | -1 | 7210 | 7 | 1 | `b7e7 b0c2 h9i7 b2a2 i9h9 a0b0 b9c7 c3c4` |
| 1 | h2g2 | 10 | completed | b7e7 | -16 | 18590 | 17 | 1 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 h0h4` |
| 1 | h2g2 | 12 | completed | b7e7 | -26 | 37978 | 34 | 1 | `b7e7 b0c2 b9c7 h0i2 h9i7 i0h0 i9h9 h0h4 a9b9` |
| 1 | h2h1 | 4 | completed | b7e7 | -61 | 1373 | 1 | 1 | `b7e7 c0e2 h9i7` |
| 1 | h2h1 | 6 | completed | b7e7 | -40 | 3400 | 3 | 1 | `b7e7 h1e1 b9c7 h0g2 a9b9 a0a2` |
| 1 | h2h1 | 8 | completed | h7e7 | -34 | 10013 | 9 | 1 | `h7e7 b2e2 h9g7 i0i2 b9c7 b0c2 c6c5` |
| 1 | h2h1 | 10 | completed | h7e7 | -32 | 19565 | 18 | 1 | `h7e7 h1e1 h9g7 h0g2 i9i8 b2e2 b9c7 i0h0 i8d8` |
| 1 | h2h1 | 12 | completed | h7e7 | -41 | 51882 | 48 | 1 | `h7e7 b2e2 h9g7 h1e1 b9c7 b0c2 a9b9 a0b0` |
| 1 | h2h3 | 4 | completed | g6g5 | -49 | 593 | 1 | 1 | `g6g5 a3a4 i6i5` |
| 1 | h2h3 | 6 | completed | b7e7 | -39 | 4202 | 4 | 1 | `b7e7 c3c4` |
| 1 | h2h3 | 8 | completed | g6g5 | -44 | 7093 | 7 | 1 | `g6g5 b2g2 a9a8 b0c2 h9g7 a0b0 a8f8` |
| 1 | h2h3 | 10 | completed | g6g5 | -54 | 14145 | 13 | 1 | `g6g5 h0i2 g9e7 b2e2 b9c7 c3c4` |
| 1 | h2h3 | 12 | completed | g6g5 | -40 | 53325 | 53 | 1 | `g6g5 h0i2 g9e7 c0e2 b7d7 b0d1 b9c7 a0b0 a9b9 d1f2` |
| 1 | h2h4 | 4 | completed | b9c7 | -32 | 698 | 1 | 1 | `b9c7 h4e4 h7e7` |
| 1 | h2h4 | 6 | completed | g6g5 | -13 | 4022 | 5 | 1 | `g6g5 h0g2 h9g7 h4a4 b9a7 i0h0 h7i7` |
| 1 | h2h4 | 8 | completed | g6g5 | -34 | 5854 | 7 | 1 | `g6g5 h0g2 h9g7 h4a4` |
| 1 | h2h4 | 10 | completed | g6g5 | -24 | 18706 | 21 | 1 | `g6g5 b2g2 g9e7 b0c2 a9a8 a0b0 a8f8 g2e2 h9i7 h0i2` |
| 1 | h2h4 | 12 | completed | g6g5 | -22 | 40036 | 44 | 1 | `g6g5 b2e2 h9g7 b0c2 b9a7 h0g2 g9e7 h4f4 a9a8 a0b0` |
| 1 | h2h5 | 4 | completed | b7e7 | -107 | 576 | 1 | 1 | `b7e7` |
| 1 | h2h5 | 6 | completed | g6g5 | -81 | 2596 | 3 | 1 | `g6g5 h5h4 c6c5 h0g2 h9g7 h4e4 b7e7` |
| 1 | h2h5 | 8 | completed | g6g5 | -75 | 8365 | 8 | 1 | `g6g5 h0g2 h9g7 h5h1 b7e7 b0c2` |
| 1 | h2h5 | 10 | completed | g6g5 | -63 | 15594 | 16 | 1 | `g6g5 h0g2 h9g7 h5h1 i9i8 c3c4 b9a7 h1g1 b7c7 c0e2` |
| 1 | h2h5 | 12 | completed | g6g5 | -64 | 30399 | 32 | 1 | `g6g5 h0g2 h9g7 h5h1 i9i8 c3c4 i8d8 b2e2 b7c7 b0a2` |
| 1 | h2h6 | 4 | completed | g6g5 | -51 | 523 | 1 | 1 | `g6g5 h0g2` |
| 1 | h2h6 | 6 | completed | b9c7 | -29 | 3691 | 3 | 1 | `b9c7 g3g4 h9g7 b0a2 c6c5` |
| 1 | h2h6 | 8 | completed | h9g7 | -26 | 7998 | 7 | 1 | `h9g7 b2e2 c6c5 b0c2 b9c7 a0b0 a9b9 h0g2 g6g5 h6g6` |
| 1 | h2h6 | 10 | completed | h9g7 | -27 | 11729 | 11 | 1 | `h9g7 c3c4 g6g5 h0g2 g9e7` |
| 1 | h2h6 | 12 | completed | h9g7 | -26 | 34902 | 34 | 1 | `h9g7 b2e2 b9c7 b0c2 c6c5 a0b0 a9b9 h0g2` |
| 1 | h2h9 | 4 | completed | i9h9 | -96 | 706 | 1 | 1 | `i9h9 b2e2 c6c5 e2e6` |
| 1 | h2h9 | 6 | completed | i9h9 | -105 | 1630 | 1 | 1 | `i9h9 h0g2` |
| 1 | h2h9 | 8 | completed | i9h9 | -124 | 5030 | 4 | 1 | `i9h9 b2e2 h7g7 h0g2 b7e7 b0c2 b9c7` |
| 1 | h2h9 | 10 | completed | i9h9 | -118 | 14203 | 12 | 1 | `i9h9 h0g2 h7e7 b0c2 b7c7 a0b0 b9a7 b2a2 a9a8 c0e2` |
| 1 | h2h9 | 12 | completed | i9h9 | -112 | 49593 | 46 | 1 | `i9h9 h0g2 h7f7 b0c2 c6c5 b2a2 b9a7 a0b0` |
| 1 | h2i2 | 4 | completed | h9g7 | -2 | 605 | 1 | 1 | `h9g7 h0g2 i9h9` |
| 1 | h2i2 | 6 | completed | g6g5 | 4 | 2224 | 2 | 1 | `g6g5 c3c4 h9g7 h0g2 i9h9 i0h0` |
| 1 | h2i2 | 8 | completed | b9c7 | 15 | 9302 | 9 | 1 | `b9c7 b0c2 b7a7 h0g2 a9b9 a0b0` |
| 1 | h2i2 | 10 | completed | g6g5 | 16 | 18544 | 18 | 1 | `g6g5 b2e2 h9g7 h0g2 b9c7 i0h0 i9h9 b0c2 c6c5 a0b0` |
| 1 | h2i2 | 12 | completed | g6g5 | 16 | 37898 | 36 | 1 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4 h7h3 b0c2` |
| 1 | i0i1 | 4 | completed | h7h0 | -122 | 624 | 1 | 1 | `h7h0 h2e2 h9g7 i1h1` |
| 1 | i0i1 | 6 | completed | h7h0 | -134 | 1395 | 1 | 1 | `h7h0 h2e2 h9g7 i1h1` |
| 1 | i0i1 | 8 | completed | h7h0 | -99 | 9648 | 9 | 1 | `h7h0 h2e2 h9g7 i1h1 h0i0` |
| 1 | i0i1 | 10 | completed | h7h0 | -99 | 10039 | 9 | 1 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0i1 b0c2 i1c1 b2b4` |
| 1 | i0i1 | 12 | completed | h7h0 | -55 | 49503 | 43 | 1 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0i1 b2b4 i1b1 b4i4` |
| 1 | i0i2 | 4 | completed | h7h0 | -154 | 235 | 1 | 1 | `h7h0 b0c2 b9c7 c3c4` |
| 1 | i0i2 | 6 | completed | h7h0 | -97 | 1926 | 2 | 1 | `h7h0 h2e2 h9g7 i2h2 h0i0` |
| 1 | i0i2 | 8 | completed | h7h0 | -109 | 4061 | 3 | 1 | `h7h0 h2e2 h9g7 i2h2 h0i0 h2h0` |
| 1 | i0i2 | 10 | completed | h7h0 | -68 | 22758 | 19 | 1 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b9c7 h2h0 i0i1 a0a1` |
| 1 | i0i2 | 12 | completed | h7h0 | -64 | 36182 | 30 | 1 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b9c7 h2h0 i0g0 h0g0` |
| 1 | i3i4 | 4 | completed | h7e7 | -51 | 763 | 1 | 1 | `h7e7` |
| 1 | i3i4 | 6 | completed | b9c7 | -15 | 4069 | 4 | 1 | `b9c7 b0c2 c6c5 h0i2` |
| 1 | i3i4 | 8 | completed | b7e7 | -16 | 5487 | 5 | 1 | `b7e7 b0c2 b9c7 a0b0 g6g5 c3c4 a9b9 h0i2 h9g7` |
| 1 | i3i4 | 10 | completed | b7e7 | -19 | 13158 | 13 | 1 | `b7e7 b2e2 b9c7 g3g4 a9b9 b0c2 h9g7 a0b0 b9b0 c2b0` |
| 1 | i3i4 | 12 | completed | b7e7 | -16 | 16028 | 15 | 1 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0i2 g6g5 i2h4 h7h2 b2h2` |
| 2 | a0a1 | 4 | completed | b7b0 | -132 | 1321 | 1 | 2 | `b7b0 h0g2 h9g7 g3g4` |
| 2 | a0a1 | 6 | completed | b7b0 | -115 | 5493 | 5 | 2 | `b7b0 b2e2 b9c7 a1b1` |
| 2 | a0a1 | 8 | completed | b7b0 | -106 | 10817 | 9 | 2 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0a1 h0g2 a1g1` |
| 2 | a0a1 | 10 | completed | b7b0 | -106 | 15668 | 14 | 2 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0a1 h0g2 a1g1 g3g4` |
| 2 | a0a1 | 12 | completed | b7b0 | -60 | 76308 | 69 | 2 | `b7b0 b2e2 h7e7 a1b1 b0a0 e2e6 f9e8 e6e4 h9g7 b1b0` |
| 2 | a0a2 | 4 | completed | b7b0 | -194 | 943 | 1 | 2 | `b7b0 a3a4` |
| 2 | a0a2 | 6 | completed | b7b0 | -53 | 5303 | 4 | 2 | `b7b0 b2e2 b9c7 a2b2 a9b9 b2b9 c7b9 e2e6 b9c7` |
| 2 | a0a2 | 8 | completed | b7b0 | -107 | 8036 | 7 | 2 | `b7b0 b2e2 b9c7 a2b2 b0a0 b2b0` |
| 2 | a0a2 | 10 | completed | b7b0 | -49 | 45486 | 38 | 2 | `b7b0 b2e2 g9e7 a2b2 b0a0 h0g2` |
| 2 | a0a2 | 12 | completed | b7b0 | -51 | 86662 | 77 | 2 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 h9g7 b2b0 a0c0 b0c0` |
| 2 | a3a4 | 4 | completed | h9g7 | -26 | 1487 | 1 | 2 | `h9g7 h0g2 g6g5` |
| 2 | a3a4 | 6 | completed | g6g5 | -18 | 6007 | 6 | 2 | `g6g5 h0g2 h7f7 b0a2` |
| 2 | a3a4 | 8 | completed | b9c7 | -9 | 15366 | 14 | 2 | `b9c7 g0e2 h7e7 c3c4 h9g7 h0f1 i9h9` |
| 2 | a3a4 | 10 | completed | b9c7 | -10 | 33787 | 31 | 2 | `b9c7 g0e2 h7e7 c3c4 b7a7 b0a2 a9b9` |
| 2 | a3a4 | 12 | completed | b9c7 | -12 | 82886 | 81 | 2 | `b9c7 c3c4 b7a7 b2c2 h7e7 h0g2 e6e5 h2h6 h9g7 b0a2` |
| 2 | b0a2 | 4 | completed | h7e7 | -34 | 835 | 1 | 2 | `h7e7` |
| 2 | b0a2 | 6 | completed | b7e7 | -2 | 5784 | 4 | 2 | `b7e7 h0g2 b9c7 g3g4` |
| 2 | b0a2 | 8 | completed | h7e7 | -2 | 14268 | 11 | 2 | `h7e7 h0g2 h9g7 b2d2 b7b2 g0e2 b9c7 a0b0` |
| 2 | b0a2 | 10 | completed | h7e7 | -6 | 48299 | 43 | 2 | `h7e7 h0g2 h9g7 i0h0 i9h9 g3g4 b9c7` |
| 2 | b0a2 | 12 | completed | h7e7 | -12 | 112466 | 104 | 2 | `h7e7 h2e2 h9g7 b2d2 b9a7 a0b0` |
| 2 | b0c2 | 4 | completed | c6c5 | -37 | 862 | 1 | 2 | `c6c5` |
| 2 | b0c2 | 6 | completed | c6c5 | 8 | 6089 | 5 | 2 | `c6c5 h2e2 b9c7 h0g2 h9g7 i0h0 i9h9 h0h4` |
| 2 | b0c2 | 8 | completed | c6c5 | 25 | 12630 | 11 | 2 | `c6c5 h2e2 c9e7 h0g2 h9g7 i0h0 i9h9 h0h4 b9c7 c3c4` |
| 2 | b0c2 | 10 | completed | c6c5 | 20 | 29483 | 27 | 2 | `c6c5 g3g4 b9c7 h2f2 h9i7 h0g2 i9h9 i0h0 a9a8 c0e2` |
| 2 | b0c2 | 12 | completed | c6c5 | 17 | 71932 | 68 | 2 | `c6c5 h2e2 b9c7 g3g4 h9i7 h0g2 i9h9 i0h0` |
| 2 | b2a2 | 4 | completed | b9c7 | 7 | 2094 | 1 | 2 | `b9c7 b0c2 a9b9 a0b0` |
| 2 | b2a2 | 6 | completed | c6c5 | 15 | 6633 | 5 | 2 | `c6c5 b0c2 b9c7 a0b0 a9b9 h0g2` |
| 2 | b2a2 | 8 | completed | c6c5 | 17 | 13222 | 10 | 2 | `c6c5 g3g4 b9c7 b0c2 a9b9 a0b0 b7b3 h0g2 h7h3 g2f4` |
| 2 | b2a2 | 10 | completed | b9c7 | 15 | 22710 | 19 | 2 | `b9c7 b0c2 c6c5 h2e2 a9b9 h0g2` |
| 2 | b2a2 | 12 | completed | c6c5 | 9 | 52716 | 47 | 2 | `c6c5 b0c2 b9c7 h2e2 h9g7 a0b0 c7d5 h0g2 i9h9 i0h0` |
| 2 | b2b1 | 4 | completed | h9g7 | -33 | 3066 | 2 | 2 | `h9g7` |
| 2 | b2b1 | 6 | completed | h7e7 | -34 | 6550 | 5 | 2 | `h7e7 h0g2 h9g7 g3g4 i9h9 h2h4 b9c7 c3c4` |
| 2 | b2b1 | 8 | completed | b7e7 | -24 | 20540 | 18 | 2 | `b7e7 h0g2 b9c7 g3g4 a9b9 b1g1 h9i7 b0c2 i9i8 g0e2` |
| 2 | b2b1 | 10 | completed | h9g7 | -35 | 32364 | 30 | 2 | `h9g7 g3g4 b7e7 h0g2 b9c7 a0a2 i9i8 a2b2 i8f8 c3c4` |
| 2 | b2b1 | 12 | completed | b7e7 | -36 | 82596 | 78 | 2 | `b7e7 h2e2 h9i7 h0g2 b9c7 b1c1 i9h9 b0a2 h7g7 a0b0` |
| 2 | b2b3 | 4 | completed | g6g5 | -89 | 1166 | 2 | 2 | `g6g5 h2c2` |
| 2 | b2b3 | 6 | completed | h7e7 | -50 | 5684 | 6 | 2 | `h7e7 g3g4 c6c5 b0a2 h9g7` |
| 2 | b2b3 | 8 | completed | c6c5 | -48 | 15491 | 14 | 2 | `c6c5 h2c2 c9e7 h0g2 i9i8 i0h0` |
| 2 | b2b3 | 10 | completed | c6c5 | -39 | 45441 | 42 | 2 | `c6c5 h2c2 h7f7 h0g2 i9i8 i0h0 h9g7 h0h4` |
| 2 | b2b3 | 12 | completed | c6c5 | -42 | 82860 | 78 | 2 | `c6c5 b0a2 c9e7 a0a1 b9c7 g3g4` |
| 2 | b2b4 | 4 | completed | c6c5 | -35 | 765 | 1 | 2 | `c6c5 b4e4 h7e7` |
| 2 | b2b4 | 6 | completed | g6g5 | -26 | 5050 | 5 | 2 | `g6g5 b0c2 c6c5 b4e4 f9e8 a0b0` |
| 2 | b2b4 | 8 | completed | g6g5 | -19 | 15336 | 15 | 2 | `g6g5 h2e2 h9g7 h0g2 i9h9 i0h0 b9c7` |
| 2 | b2b4 | 10 | completed | c6c5 | -28 | 31493 | 30 | 2 | `c6c5 b0a2 b9c7 h2c2 h9i7 h0g2 c9e7 i0h0 i9h9` |
| 2 | b2b4 | 12 | completed | c6c5 | -25 | 92097 | 89 | 2 | `c6c5 b0c2 b9c7 h0i2 g6g5 h2f2 h7h2` |
| 2 | b2b5 | 4 | completed | h7e7 | -121 | 2344 | 2 | 2 | `h7e7 h2e2` |
| 2 | b2b5 | 6 | completed | h7e7 | -71 | 6751 | 5 | 2 | `h7e7 h0g2 h9g7 i0h0 c6c5 b0c2 b9c7 b5b1` |
| 2 | b2b5 | 8 | completed | h7e7 | -65 | 13691 | 12 | 2 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0c2 c6c5` |
| 2 | b2b5 | 10 | completed | c6c5 | -66 | 63585 | 59 | 2 | `c6c5 b0c2 b9c7 b5b1 g6g5 g0e2 h9g7 b1g1 b7b3` |
| 2 | b2b5 | 12 | completed | c6c5 | -65 | 129010 | 122 | 2 | `c6c5 b0c2 b9c7 b5b4 g6g5 h0i2 h9g7 b4i4 g9i7 h2f2` |
| 2 | b2b6 | 4 | completed | c6c5 | -12 | 900 | 1 | 2 | `c6c5` |
| 2 | b2b6 | 6 | completed | c6c5 | -25 | 2640 | 2 | 2 | `c6c5 g3g4 b9c7 b6c6 c9e7` |
| 2 | b2b6 | 8 | completed | b9c7 | -23 | 12485 | 12 | 2 | `b9c7 c3c4 a9a8 h2e2 h9g7 h0g2 a8d8 i0h0 i9h9 b0c2` |
| 2 | b2b6 | 10 | completed | b9c7 | -24 | 18238 | 17 | 2 | `b9c7 h2e2 h9g7 b0c2 i9h9 g3g4 h7i7` |
| 2 | b2b6 | 12 | completed | h9g7 | -30 | 41830 | 41 | 2 | `h9g7 g3g4 h7i7 h0g2 i9h9 i0h0 h9h5 b6b4 g6g5 g2f4` |
| 2 | b2b9 | 4 | completed | a9b9 | -117 | 1392 | 1 | 2 | `a9b9 c0e2 g6g5 b0c2` |
| 2 | b2b9 | 6 | completed | a9b9 | -117 | 2257 | 1 | 2 | `a9b9 c0e2 g6g5 b0c2 b7d7 h0i2` |
| 2 | b2b9 | 8 | completed | a9b9 | -109 | 5894 | 4 | 2 | `a9b9 b0c2 b7d7 h2e2 h9g7 a0b0 b9b0 c2b0` |
| 2 | b2b9 | 10 | completed | a9b9 | -110 | 17791 | 14 | 2 | `a9b9 b0c2 b7e7 h2e2 h9g7 h0g2 h7h3 a0b0 b9b0 c2b0` |
| 2 | b2b9 | 12 | completed | a9b9 | -113 | 25743 | 22 | 2 | `a9b9 b0c2 b7e7 h2e2 h9g7 h0g2 h7h3 a0b0 b9b0 c2b0` |
| 2 | b2c2 | 4 | completed | b7e7 | -15 | 1996 | 2 | 2 | `b7e7` |
| 2 | b2c2 | 6 | completed | h9g7 | -5 | 5561 | 5 | 2 | `h9g7 b0a2 b9a7 h0g2` |
| 2 | b2c2 | 8 | completed | h7e7 | -10 | 13332 | 12 | 2 | `h7e7 h0g2 h9g7 b0a2 b9a7 a0b0 a9b9` |
| 2 | b2c2 | 10 | completed | h7e7 | -18 | 23245 | 21 | 2 | `h7e7 h2e2 h9g7 b0a2 b9a7 h0g2` |
| 2 | b2c2 | 12 | completed | h7e7 | -24 | 80436 | 75 | 2 | `h7e7 h2e2 h9g7 b0a2 b9a7 h0g2 i9h9 a0b0 a9b9 a3a4` |
| 2 | b2d2 | 4 | completed | b7e7 | -60 | 682 | 1 | 2 | `b7e7` |
| 2 | b2d2 | 6 | completed | h7e7 | 8 | 7779 | 7 | 2 | `h7e7 g0e2 e7e3 f0e1 b7e7 h0g2` |
| 2 | b2d2 | 8 | completed | b9a7 | 21 | 18278 | 15 | 2 | `b9a7 b0c2 a9b9 g3g4 h7e7 h0g2` |
| 2 | b2d2 | 10 | completed | h7e7 | 19 | 32964 | 28 | 2 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0c2 b9a7 a0b0 b7c7 g3g4` |
| 2 | b2d2 | 12 | completed | h7e7 | 19 | 69003 | 68 | 2 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0c2 b9a7 a0b0 a9b9 h2h6` |
| 2 | b2e2 | 4 | completed | c9e7 | 36 | 1013 | 1 | 2 | `c9e7 b0c2 b9c7 c3c4` |
| 2 | b2e2 | 6 | completed | b9c7 | 41 | 1998 | 1 | 2 | `b9c7 b0c2 h9g7 a0b0` |
| 2 | b2e2 | 8 | completed | b9c7 | 28 | 4448 | 3 | 2 | `b9c7 b0c2 c6c5 a0b0 a9b9 b0b6` |
| 2 | b2e2 | 10 | completed | b9c7 | 28 | 9493 | 8 | 2 | `b9c7 b0c2 c6c5 h0g2` |
| 2 | b2e2 | 12 | completed | b9c7 | 18 | 49538 | 46 | 2 | `b9c7 b0c2 c6c5 h0g2 a9b9 h2i2 h9g7 i0h0 i9h9 g3g4` |
| 2 | b2f2 | 4 | completed | a9a8 | -10 | 2288 | 2 | 2 | `a9a8 b0c2 a8f8 f0e1 h9g7 g3g4` |
| 2 | b2f2 | 6 | completed | a9a8 | -9 | 3170 | 3 | 2 | `a9a8 b0c2 a8f8 f0e1 h9g7 g3g4` |
| 2 | b2f2 | 8 | completed | g6g5 | 8 | 23930 | 20 | 2 | `g6g5 b0c2 b9c7 h0i2` |
| 2 | b2f2 | 10 | completed | g6g5 | 22 | 42385 | 36 | 2 | `g6g5 b0c2 b9c7 a0b0 a9b9 c3c4 h9g7 g0e2 h7i7 h0f1` |
| 2 | b2f2 | 12 | completed | b9c7 | 21 | 83437 | 76 | 2 | `b9c7 b0c2 g6g5 a0b0 a9b9 c3c4 h9g7 g0e2 i9i8 h0i2` |
| 2 | b2g2 | 4 | completed | h9i7 | -17 | 2156 | 2 | 2 | `h9i7` |
| 2 | b2g2 | 6 | completed | c6c5 | -13 | 5409 | 4 | 2 | `c6c5 g3g4 h9i7 b0c2 b9c7 a0b0 a9b9` |
| 2 | b2g2 | 8 | completed | b9c7 | -16 | 9853 | 8 | 2 | `b9c7 g3g4 a9b9` |
| 2 | b2g2 | 10 | completed | c6c5 | -18 | 28259 | 25 | 2 | `c6c5 b0c2 b9c7 a0b0 a9b9 b0b6 b7a7 b6b9 c7b9 g3g4` |
| 2 | b2g2 | 12 | completed | c6c5 | -20 | 50370 | 46 | 2 | `c6c5 b0c2 b9c7 a0b0 a9b9 g2g1 g9e7 h2e2 b7b3 h0g2` |
| 2 | c0a2 | 4 | completed | b9c7 | -53 | 2284 | 2 | 2 | `b9c7` |
| 2 | c0a2 | 6 | completed | g6g5 | -53 | 5542 | 5 | 2 | `g6g5 b0d1 h9g7 h0i2 b9c7 c3c4` |
| 2 | c0a2 | 8 | completed | b7e7 | -48 | 14566 | 13 | 2 | `b7e7 h2e2 b9c7 h0g2 h9i7 i0h0 a9b9 b0d1` |
| 2 | c0a2 | 10 | completed | g6g5 | -46 | 20915 | 19 | 2 | `g6g5 h0i2 h9g7 h2e2 b7e7 i0h0 b9c7 h0h6 a9b9 b0d1` |
| 2 | c0a2 | 12 | completed | b7e7 | -58 | 69926 | 67 | 2 | `b7e7 b2e2 b9c7 b0c2 a9b9 c3c4 g6g5 a0a1 h9g7 a1f1` |
| 2 | c0e2 | 4 | completed | h7e7 | -5 | 2346 | 2 | 2 | `h7e7 c3c4 e7e3 f0e1` |
| 2 | c0e2 | 6 | completed | b9c7 | 5 | 5148 | 4 | 2 | `b9c7 c3c4 g6g5 h0g2 h9g7` |
| 2 | c0e2 | 8 | completed | g6g5 | 19 | 21092 | 17 | 2 | `g6g5 b0d1 b9c7 h0i2 h9g7` |
| 2 | c0e2 | 10 | completed | h7f7 | 22 | 36574 | 31 | 2 | `h7f7 g3g4 h9g7 h0g2 i9h9 i0h0 c6c5 b0d1 h9h5 h2i2` |
| 2 | c0e2 | 12 | completed | b7e7 | 16 | 58528 | 51 | 2 | `b7e7 h0g2 b9c7 g3g4 h9i7` |
| 2 | c3c4 | 4 | completed | g6g5 | 0 | 1840 | 1 | 2 | `g6g5 h0g2` |
| 2 | c3c4 | 6 | completed | g6g5 | 27 | 3728 | 3 | 2 | `g6g5 b0c2 h9g7 h0g2 c9e7` |
| 2 | c3c4 | 8 | completed | g6g5 | 29 | 8730 | 8 | 2 | `g6g5 g0e2 h9g7 b0c2 c9e7 a0a1 i9i8` |
| 2 | c3c4 | 10 | completed | b7c7 | 27 | 29727 | 28 | 2 | `b7c7 h2e2 h7e7 b0c2 c6c5 c2d4 c5c4` |
| 2 | c3c4 | 12 | completed | b7c7 | 23 | 76211 | 74 | 2 | `b7c7 h2e2 h7e7 b0c2 c6c5 c2d4 c5c4 d4e6 h9g7 h0g2` |
| 2 | d0e1 | 4 | completed | g6g5 | -34 | 824 | 1 | 2 | `g6g5` |
| 2 | d0e1 | 6 | completed | c6c5 | -14 | 7191 | 6 | 2 | `c6c5 b0a2 h9g7 g3g4 b9c7 h0g2` |
| 2 | d0e1 | 8 | completed | b7e7 | -11 | 11544 | 10 | 2 | `b7e7 c3c4 b9c7 b0c2 a9b9` |
| 2 | d0e1 | 10 | completed | b9c7 | -11 | 30100 | 26 | 2 | `b9c7 c0e2 g6g5 h0i2 h9g7 c3c4 b7a7` |
| 2 | d0e1 | 12 | completed | b9c7 | -9 | 66540 | 61 | 2 | `b9c7 h2f2 b7a7 b0c2 a9b9 h0g2 g6g5 i0h0 h7g7 c3c4` |
| 2 | e0e1 | 4 | completed | c6c5 | -103 | 1871 | 1 | 2 | `c6c5` |
| 2 | e0e1 | 6 | completed | b7e7 | -107 | 3543 | 3 | 2 | `b7e7 b0c2 h9g7 e1e0` |
| 2 | e0e1 | 8 | completed | g6g5 | -95 | 15763 | 13 | 2 | `g6g5 e1e0 h9g7 c3c4 b9a7 b0c2` |
| 2 | e0e1 | 10 | completed | h7e7 | -94 | 53656 | 49 | 2 | `h7e7 h0g2 h9g7 i0h0 i9h9 g3g4 b9c7 e1e0 h9h3` |
| 2 | e0e1 | 12 | completed | b9c7 | -85 | 83498 | 78 | 2 | `b9c7 e1e0 h7e7 h0g2 h9g7 i0h0 b7a7` |
| 2 | e3e4 | 4 | completed | h7e7 | -96 | 2204 | 1 | 2 | `h7e7 f0e1 h9g7 h2e2 i9h9` |
| 2 | e3e4 | 6 | completed | h7e7 | -89 | 4517 | 3 | 2 | `h7e7 f0e1 e7e4 h2e2 b7e7 h0g2 h9g7 i0h0` |
| 2 | e3e4 | 8 | completed | b7e7 | -96 | 11694 | 9 | 2 | `b7e7 b2e2 e7e4 d0e1 h7e7 h0g2` |
| 2 | e3e4 | 10 | completed | b7e7 | -97 | 28995 | 25 | 2 | `b7e7 f0e1 e7e4 b2e2 h7e7 b0c2 h9g7 h0g2 i9h9 i0h0` |
| 2 | e3e4 | 12 | completed | b7e7 | -95 | 56603 | 51 | 2 | `b7e7 d0e1 e7e4 h2e2 b9c7 b0c2 a9b9 a0b0 b9b3 h0g2` |
| 2 | f0e1 | 4 | completed | h7i7 | -21 | 1073 | 1 | 2 | `h7i7 b0a2` |
| 2 | f0e1 | 6 | completed | c9e7 | -17 | 6182 | 5 | 2 | `c9e7 g3g4 b9d8 b0c2 c6c5 b2a2` |
| 2 | f0e1 | 8 | completed | h7i7 | -11 | 12813 | 11 | 2 | `h7i7 c3c4 h9g7 h0g2 g6g5` |
| 2 | f0e1 | 10 | completed | h9g7 | -7 | 35415 | 30 | 2 | `h9g7 c3c4 b7c7 g0e2 h7i7 b0c2 i9h9` |
| 2 | f0e1 | 12 | completed | g6g5 | -5 | 66923 | 59 | 2 | `g6g5 g0e2 h9g7 b0a2 b9c7 b2d2 a9b9 a0b0 c6c5` |
| 2 | g0e2 | 4 | completed | b7e7 | -12 | 967 | 1 | 2 | `b7e7 c3c4` |
| 2 | g0e2 | 6 | completed | h9i7 | 2 | 7246 | 6 | 2 | `h9i7 c3c4 h7f7 h0g2 i9h9 i0h0` |
| 2 | g0e2 | 8 | completed | h7f7 | 14 | 20120 | 16 | 2 | `h7f7 c3c4 h9g7 h0g2 i9h9` |
| 2 | g0e2 | 10 | completed | h7e7 | 18 | 48273 | 41 | 2 | `h7e7 h0g2 h9g7 b2d2 i9h9 i0h0 g6g5 b0c2 b9a7 a0b0` |
| 2 | g0e2 | 12 | completed | h7e7 | 15 | 91620 | 79 | 2 | `h7e7 h0g2 h9g7 b0c2 i9h9 i0h0 c6c5 g3g4 b9c7 h2h6` |
| 2 | g0i2 | 4 | completed | h7e7 | -74 | 1951 | 2 | 2 | `h7e7 f0e1 h9g7` |
| 2 | g0i2 | 6 | completed | h7e7 | -46 | 6016 | 5 | 2 | `h7e7 b2e2 h9g7 b0c2 i9h9 a0b0 h9h2 b0b7` |
| 2 | g0i2 | 8 | completed | b9c7 | -46 | 14401 | 13 | 2 | `b9c7 c3c4 h7e7 b0c2 h9g7 h0g2` |
| 2 | g0i2 | 10 | completed | h7e7 | -56 | 26893 | 24 | 2 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9c7` |
| 2 | g0i2 | 12 | completed | h7e7 | -64 | 82231 | 75 | 2 | `h7e7 h2e2 h9g7 h0g2 i9h9 b2d2 b9a7 b0c2 a9b9 a0b0` |
| 2 | g3g4 | 4 | completed | g9e7 | 20 | 1600 | 1 | 2 | `g9e7` |
| 2 | g3g4 | 6 | completed | c6c5 | 23 | 5908 | 5 | 2 | `c6c5 b2e2 b9c7 b0c2 a9b9` |
| 2 | g3g4 | 8 | completed | c6c5 | 33 | 14256 | 13 | 2 | `c6c5 c0e2 g9e7 b0d1 h9f8 h0g2` |
| 2 | g3g4 | 10 | completed | h7g7 | 32 | 22248 | 21 | 2 | `h7g7 h2e2 b9c7 h0g2 h9i7 i0h0` |
| 2 | g3g4 | 12 | completed | h7g7 | 23 | 53748 | 50 | 2 | `h7g7 g0e2 b7e7 b2d2 b9c7 b0c2 a9b9` |
| 2 | h0g2 | 4 | completed | g6g5 | 19 | 1821 | 2 | 2 | `g6g5 b2e2 b9c7 b0c2` |
| 2 | h0g2 | 6 | completed | g6g5 | 29 | 3121 | 3 | 2 | `g6g5 b2e2 b9c7 b0c2 c6c5 a0b0 a9b9 b0b4` |
| 2 | h0g2 | 8 | completed | g6g5 | 24 | 5724 | 5 | 2 | `g6g5 b2e2 b9c7 b0c2 c6c5 a0b0 a9b9` |
| 2 | h0g2 | 10 | completed | g6g5 | 20 | 13364 | 13 | 2 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 c6c5 e3e4 h7e7` |
| 2 | h0g2 | 12 | completed | g6g5 | 22 | 63137 | 61 | 2 | `g6g5 b2e2 b9c7 b0c2 a9b9 h2i2 b7a7 i0h0 h9i7 e3e4` |
| 2 | h0i2 | 4 | completed | b7e7 | -63 | 712 | 1 | 2 | `b7e7` |
| 2 | h0i2 | 6 | completed | b7e7 | -12 | 7698 | 6 | 2 | `b7e7 b0c2 b9c7 a0b0 a9b9` |
| 2 | h0i2 | 8 | completed | b7e7 | -2 | 23240 | 19 | 2 | `b7e7 b2e2 b9c7 b0c2 a9b9 c3c4 h9g7` |
| 2 | h0i2 | 10 | completed | b7e7 | 6 | 42139 | 36 | 2 | `b7e7 b2e2 b9c7 b0c2 a9b9 h2g2 h9i7 i0h0 i9h9 h0h4` |
| 2 | h0i2 | 12 | completed | b7e7 | 1 | 73682 | 65 | 2 | `b7e7 b2e2 b9c7 b0c2 a9b9 a0a1 b9b3 c3c4 b3c3 h2f2` |
| 2 | h2c2 | 4 | completed | h9g7 | -10 | 2201 | 1 | 2 | `h9g7 h0g2 i9h9 i0h0` |
| 2 | h2c2 | 6 | completed | h9g7 | -20 | 3317 | 2 | 2 | `h9g7 h0g2 g6g5` |
| 2 | h2c2 | 8 | completed | g6g5 | -18 | 12111 | 10 | 2 | `g6g5 h0g2 h9g7 i0h0 i9h9 h0h4 h7i7 h4h9 g7h9` |
| 2 | h2c2 | 10 | completed | g6g5 | -19 | 31659 | 27 | 2 | `g6g5 h0g2 h9g7 c0e2 i9h9 i0h0 h7h3 b0d1 b9a7 g3g4` |
| 2 | h2c2 | 12 | completed | g6g5 | -19 | 73512 | 66 | 2 | `g6g5 h0g2 h9g7 i0h0 i9h9 h0h4 h7i7 h4h9 g7h9 c0e2` |
| 2 | h2d2 | 4 | completed | h9i7 | -6 | 1751 | 2 | 2 | `h9i7 a3a4` |
| 2 | h2d2 | 6 | completed | g6g5 | 6 | 11102 | 8 | 2 | `g6g5 h0g2 h9g7 i0h0 i9h9 b0c2` |
| 2 | h2d2 | 8 | completed | g6g5 | 8 | 21029 | 16 | 2 | `g6g5 h0g2 h9g7 c0e2 c6c5 i0h0 i9h9 h0h4` |
| 2 | h2d2 | 10 | completed | g6g5 | 14 | 45799 | 36 | 2 | `g6g5 h0g2 h9g7 c3c4 b9a7 i0h0 i9h9 h0h4 b7c7` |
| 2 | h2d2 | 12 | completed | h9g7 | 10 | 74638 | 63 | 2 | `h9g7 g3g4 i9h9 h0g2 h7i7 c3c4 b9a7 b0c2 a9a8 a3a4` |
| 2 | h2e2 | 4 | completed | b9c7 | 41 | 1590 | 1 | 2 | `b9c7 h0g2 h9g7 i0h0` |
| 2 | h2e2 | 6 | completed | h9g7 | 36 | 2081 | 1 | 2 | `h9g7 h0g2 i9h9 g3g4 c6c5` |
| 2 | h2e2 | 8 | completed | h9g7 | 21 | 4638 | 4 | 2 | `h9g7 h0g2 c6c5 i0h0 i9h9 g3g4` |
| 2 | h2e2 | 10 | completed | h9g7 | 22 | 17248 | 14 | 2 | `h9g7 h0g2 c6c5 i0h0 i9h9 h0h6 c9e7` |
| 2 | h2e2 | 12 | completed | h9g7 | 29 | 60686 | 54 | 2 | `h9g7 h0g2 i9h9 i0h0 c6c5 h0h4 b9c7 b0c2 g6g5 e3e4` |
| 2 | h2f2 | 4 | completed | h9i7 | -2 | 2018 | 2 | 2 | `h9i7 h0g2 i9h9 c3c4` |
| 2 | h2f2 | 6 | completed | c6c5 | 20 | 8491 | 7 | 2 | `c6c5 h0g2 b9c7 g3g4` |
| 2 | h2f2 | 8 | completed | b7e7 | 27 | 14682 | 12 | 2 | `b7e7 b0c2 h9i7 h0g2 i9h9` |
| 2 | h2f2 | 10 | completed | b7f7 | 25 | 32797 | 29 | 2 | `b7f7 h0g2 h9i7 i0h0 i9h9 g3g4` |
| 2 | h2f2 | 12 | completed | b7e7 | 8 | 73507 | 66 | 2 | `b7e7 b0c2 b9c7 h0g2 h9i7 a0b0 i9h9` |
| 2 | h2g2 | 4 | completed | b7e7 | -55 | 1545 | 1 | 2 | `b7e7 b0c2 h9i7 a3a4` |
| 2 | h2g2 | 6 | completed | b7e7 | -17 | 5483 | 4 | 2 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0i2` |
| 2 | h2g2 | 8 | completed | b7e7 | -11 | 12015 | 9 | 2 | `b7e7 b0c2 b9c7 a0b0 a9b9 c3c4 b9b3 g0e2 i6i5 h0f1` |
| 2 | h2g2 | 10 | completed | b7e7 | -19 | 35492 | 30 | 2 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0i2 h9i7 i3i4` |
| 2 | h2g2 | 12 | completed | b7e7 | -32 | 85156 | 74 | 2 | `b7e7 b0c2 b9c7 h0i2 h7h2 g0e2 h9i7 i0h0 i9h9 b2b4` |
| 2 | h2h1 | 4 | completed | b9c7 | -45 | 2364 | 2 | 2 | `b9c7 b0c2 h7e7 h1c1` |
| 2 | h2h1 | 6 | completed | h7e7 | -28 | 6673 | 5 | 2 | `h7e7 h1e1 h9g7 h0g2 i9h9 g3g4 h9h5` |
| 2 | h2h1 | 8 | completed | h7e7 | -31 | 12847 | 11 | 2 | `h7e7 h1e1 h9g7 h0g2 i9h9 c0e2` |
| 2 | h2h1 | 10 | completed | h7e7 | -41 | 27125 | 23 | 2 | `h7e7 h1e1 h9g7 h0g2 i9h9 g3g4 c6c5 i0h0 h9h0 g2h0` |
| 2 | h2h1 | 12 | completed | h7e7 | -44 | 98070 | 93 | 2 | `h7e7 c0e2 h9g7 b0c2 c6c5 h1c1 i9i8 i0i1` |
| 2 | h2h3 | 4 | completed | h9g7 | -64 | 895 | 1 | 2 | `h9g7 g3g4 c6c5` |
| 2 | h2h3 | 6 | completed | g6g5 | -49 | 7022 | 5 | 2 | `g6g5 c3c4 b9a7 b0c2 b7c7 c2b4 h9g7 h0i2 i6i5 c0e2` |
| 2 | h2h3 | 8 | completed | g6g5 | -49 | 10505 | 9 | 2 | `g6g5 c3c4 b9a7 b0c2 h9g7 h0i2 b7c7 c2b4` |
| 2 | h2h3 | 10 | completed | g6g5 | -44 | 47436 | 41 | 2 | `g6g5 b2g2 g9e7 b0c2 a9a8 g0e2 b9a7 a0b0 a8f8 h0i2` |
| 2 | h2h3 | 12 | completed | g6g5 | -45 | 86485 | 76 | 2 | `g6g5 b2g2 g9e7 b0c2 a9a8 g0e2 a8f8 a0b0 b9a7 b0b4` |
| 2 | h2h4 | 4 | completed | h9g7 | -25 | 1099 | 1 | 2 | `h9g7 g3g4` |
| 2 | h2h4 | 6 | completed | g6g5 | -23 | 5202 | 5 | 2 | `g6g5 h0g2 h9g7 b2e2 c6c5` |
| 2 | h2h4 | 8 | completed | c6c5 | -18 | 11650 | 10 | 2 | `c6c5 b2c2 g6g5 b0a2 h9g7` |
| 2 | h2h4 | 10 | completed | g6g5 | -22 | 23528 | 21 | 2 | `g6g5 h0g2 c6c5 h4i4 h7i7 b0a2 b9c7 i4a4` |
| 2 | h2h4 | 12 | completed | g6g5 | -22 | 73589 | 69 | 2 | `g6g5 c3c4 c9e7 h0g2 h9g7 b0c2 g7f5 a0a1 f5g3 g0e2` |
| 2 | h2h5 | 4 | completed | b7e7 | -96 | 897 | 1 | 2 | `b7e7` |
| 2 | h2h5 | 6 | completed | b7e7 | -82 | 7425 | 6 | 2 | `b7e7 b0c2 b9c7 h0g2 g6g5 h5h4 a9b9` |
| 2 | h2h5 | 8 | completed | g6g5 | -57 | 17051 | 14 | 2 | `g6g5 h0g2 h9g7 h5h1 c9e7 c0e2 c6c5 b0d1 b9c7` |
| 2 | h2h5 | 10 | completed | b7e7 | -57 | 31135 | 27 | 2 | `b7e7 h0g2 b9c7 h5b5 c6c5 b5b4 h9i7 c0e2 i9h9` |
| 2 | h2h5 | 12 | completed | g6g5 | -58 | 66992 | 60 | 2 | `g6g5 h0g2 h9g7 h5h1 c9e7 b0a2 b9c7 h1c1 i9h9` |
| 2 | h2h6 | 4 | completed | g6g5 | -41 | 1180 | 1 | 2 | `g6g5 h0g2 c6c5` |
| 2 | h2h6 | 6 | completed | g6g5 | -31 | 2880 | 2 | 2 | `g6g5 c3c4 h9g7` |
| 2 | h2h6 | 8 | completed | h9g7 | -25 | 13834 | 12 | 2 | `h9g7 h0g2 c6c5 g3g4 b9c7 b0a2` |
| 2 | h2h6 | 10 | completed | b9c7 | -29 | 32753 | 29 | 2 | `b9c7 b2e2 a9b9 b0c2 h9g7 a0b0 c6c5 h0g2 i9i8` |
| 2 | h2h6 | 12 | completed | h9g7 | -28 | 91794 | 86 | 2 | `h9g7 h0g2 c6c5 g3g4 b9c7 g0e2 i9i8 b0c2 i8f8` |
| 2 | h2h9 | 4 | completed | i9h9 | -121 | 1211 | 1 | 2 | `i9h9 h0g2 h7e7 c3c4` |
| 2 | h2h9 | 6 | completed | i9h9 | -102 | 3015 | 2 | 2 | `i9h9 h0g2 b9c7` |
| 2 | h2h9 | 8 | completed | i9h9 | -109 | 7248 | 6 | 2 | `i9h9 h0g2 h7e7 b2e2 b9c7 b0c2 c6c5 a0b0` |
| 2 | h2h9 | 10 | completed | i9h9 | -115 | 14962 | 12 | 2 | `i9h9 h0g2 h7e7 c3c4 b9a7 b2e2 a9b9 b0c2` |
| 2 | h2h9 | 12 | completed | i9h9 | -113 | 42255 | 36 | 2 | `i9h9 h0g2 h7e7 b0c2 b7c7 a0b0 c7c3 c0e2 b9c7 g3g4` |
| 2 | h2i2 | 4 | completed | h7h2 | 14 | 2118 | 2 | 2 | `h7h2 h0g2 h2b2 i2b2` |
| 2 | h2i2 | 6 | completed | g6g5 | 1 | 3314 | 3 | 2 | `g6g5 h0g2 h9g7 i0h0` |
| 2 | h2i2 | 8 | completed | g6g5 | 13 | 13836 | 12 | 2 | `g6g5 b2g2 h9i7 b0c2 i9h9 a0b0 c9e7` |
| 2 | h2i2 | 10 | completed | g6g5 | 13 | 23256 | 20 | 2 | `g6g5 h0g2 h9g7 i0h0 i9h9 b2e2 h7h3 b0c2 b9c7 a0b0` |
| 2 | h2i2 | 12 | completed | g6g5 | 9 | 52948 | 48 | 2 | `g6g5 h0g2 h9g7 i0h0 i9h9 b0c2 c6c5 b2a2 b9c7 a0b0` |
| 2 | i0i1 | 4 | completed | h7h0 | -170 | 1119 | 1 | 2 | `h7h0 b0c2 h9g7` |
| 2 | i0i1 | 6 | completed | h7h0 | -111 | 4292 | 3 | 2 | `h7h0 b2b4 a6a5 b4i4 b7i7 i4e4 i7e7` |
| 2 | i0i1 | 8 | completed | h7h0 | -61 | 27917 | 21 | 2 | `h7h0 h2e2 b7e7 i1h1 h0i0 b0c2 b9c7 h1h0 i0g0 h0g0` |
| 2 | i0i1 | 10 | completed | h7h0 | -58 | 39813 | 31 | 2 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0i1 b2b4 i1b1 b4i4` |
| 2 | i0i1 | 12 | completed | h7h0 | -58 | 54809 | 44 | 2 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0i1 b2b4 i1b1 b4i4` |
| 2 | i0i2 | 4 | completed | h7h0 | -154 | 1256 | 1 | 2 | `h7h0 b0c2 b7e7 c3c4` |
| 2 | i0i2 | 6 | completed | h7h0 | -100 | 5122 | 3 | 2 | `h7h0 h2e2 h9g7 i2h2 h0i0 h2h0` |
| 2 | i0i2 | 8 | completed | h7h0 | -80 | 15116 | 11 | 2 | `h7h0 h2e2 b7e7 i2h2 h0i0 h2h0 i0g0 h0g0 b9c7` |
| 2 | i0i2 | 10 | completed | h7h0 | -52 | 50298 | 40 | 2 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b7e7 a0a1 b9c7 a1i1` |
| 2 | i0i2 | 12 | completed | h7h0 | -55 | 87078 | 74 | 2 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b9c7 h2h0 i0g0 h0g0` |
| 2 | i3i4 | 4 | completed | c6c5 | -37 | 728 | 1 | 2 | `c6c5` |
| 2 | i3i4 | 6 | completed | h7e7 | -28 | 4681 | 4 | 2 | `h7e7 b0c2 c6c5 g3g4` |
| 2 | i3i4 | 8 | completed | h9g7 | -12 | 11667 | 10 | 2 | `h9g7 b2e2 b9c7 b0c2 a9b9 a0b0` |
| 2 | i3i4 | 10 | completed | b7e7 | -9 | 35995 | 32 | 2 | `b7e7 b0c2 b9c7 a0b0 h9g7 b2a2 g6g5 h0g2 a9a8` |
| 2 | i3i4 | 12 | completed | b7e7 | -9 | 65922 | 61 | 2 | `b7e7 b0c2 b9c7 a0b0 a9b9 b2b6 c6c5 g3g4 h9i7` |
| 3 | a0a1 | 4 | completed | b7b0 | -181 | 2662 | 2 | 3 | `b7b0 g3g4` |
| 3 | a0a1 | 6 | completed | b7b0 | -118 | 7648 | 5 | 3 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0` |
| 3 | a0a1 | 8 | completed | b7b0 | -48 | 31391 | 23 | 3 | `b7b0 b2e2 h7e7 a1b1 b0a0 h0g2 h9g7 b1b0` |
| 3 | a0a1 | 10 | completed | b7b0 | -68 | 58064 | 45 | 3 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0a1 h2h4 g9e7 i0i1` |
| 3 | a0a1 | 12 | completed | b7b0 | -75 | 91819 | 75 | 3 | `b7b0 b2e2 h7e7 a1b1 b0a0 e2e6 d9e8 e6e4 h9g7 h2e2` |
| 3 | a0a2 | 4 | completed | b7b0 | -194 | 1169 | 1 | 3 | `b7b0 a3a4` |
| 3 | a0a2 | 6 | completed | b7b0 | -113 | 6496 | 5 | 3 | `b7b0 a2a0 b0d0 e0d0 b9c7 d0e0` |
| 3 | a0a2 | 8 | completed | b7b0 | -124 | 15026 | 12 | 3 | `b7b0 b2e2 b9c7 a2b2 b0a0 b2b0 a0a1 h0g2` |
| 3 | a0a2 | 10 | completed | b7b0 | -60 | 60643 | 51 | 3 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 h7e7 i0i1 h9g7 i1a1` |
| 3 | a0a2 | 12 | completed | b7b0 | -58 | 131716 | 118 | 3 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 h7e7 i0i1 h9g7 i1a1` |
| 3 | a3a4 | 4 | completed | b7e7 | -69 | 965 | 1 | 3 | `b7e7` |
| 3 | a3a4 | 6 | completed | b7e7 | -20 | 6306 | 5 | 3 | `b7e7 f0e1 b9c7 h0g2 g6g5` |
| 3 | a3a4 | 8 | completed | h7e7 | -14 | 14753 | 12 | 3 | `h7e7 h0g2 h9g7 b0a2` |
| 3 | a3a4 | 10 | completed | g6g5 | -15 | 43682 | 39 | 3 | `g6g5 g0e2 h9g7 h0f1 b9c7 b2c2` |
| 3 | a3a4 | 12 | completed | h7e7 | -12 | 125743 | 117 | 3 | `h7e7 h0g2 h9g7 i0h0 i9h9 g3g4 h9h3 b0c2 c6c5 h2i2` |
| 3 | b0a2 | 4 | completed | g6g5 | -7 | 1746 | 1 | 3 | `g6g5 a0a1` |
| 3 | b0a2 | 6 | completed | h7e7 | 0 | 7440 | 6 | 3 | `h7e7 h0g2 h9g7 i0h0 g6g5 a0a1` |
| 3 | b0a2 | 8 | completed | h7e7 | 4 | 16601 | 14 | 3 | `h7e7 h0g2 g6g5 b2e2 h9g7 a0b0 b9c7 i0h0` |
| 3 | b0a2 | 10 | completed | h9g7 | 5 | 51772 | 45 | 3 | `h9g7 b2d2 h7i7 a0b0 i9h9 h0g2 g6g5` |
| 3 | b0a2 | 12 | completed | h7e7 | 4 | 132336 | 120 | 3 | `h7e7 h0g2 h9g7 i0h0 i9h9 g3g4 h9h5 a0a1 c6c5` |
| 3 | b0c2 | 4 | completed | g6g5 | 8 | 1329 | 1 | 3 | `g6g5 g0e2 c6c5` |
| 3 | b0c2 | 6 | completed | c6c5 | 15 | 5175 | 4 | 3 | `c6c5 b2a2 b9c7 a0b0 a9b9` |
| 3 | b0c2 | 8 | completed | c6c5 | 21 | 12420 | 10 | 3 | `c6c5 b2a2 b9c7 a0b0 a9b9 g3g4 g9e7 h0g2 h9f8` |
| 3 | b0c2 | 10 | completed | c6c5 | 16 | 36603 | 32 | 3 | `c6c5 b2a2 b9c7 a0b0 g6g5 b0b4 a9b9 g3g4 g5g4` |
| 3 | b0c2 | 12 | completed | c6c5 | 17 | 118321 | 109 | 3 | `c6c5 h2f2 h9i7 h0g2 i9h9 b2a2 b9c7 a0b0 a9b9 i0h0` |
| 3 | b2a2 | 4 | completed | h7e7 | 9 | 2087 | 1 | 3 | `h7e7` |
| 3 | b2a2 | 6 | completed | b9c7 | 13 | 5059 | 4 | 3 | `b9c7 b0c2 c6c5 a0b0 a9b9 h0g2` |
| 3 | b2a2 | 8 | completed | c6c5 | 11 | 15807 | 13 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 h0g2 g6g5 b0b4` |
| 3 | b2a2 | 10 | completed | c6c5 | 9 | 32483 | 28 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 h2e2 h9g7 h0g2 i9h9 i0h0` |
| 3 | b2a2 | 12 | completed | c6c5 | 7 | 64967 | 57 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 b0b4 h9g7 g3g4 b7a7 b4b9` |
| 3 | b2b1 | 4 | completed | h9i7 | -30 | 2873 | 2 | 3 | `h9i7` |
| 3 | b2b1 | 6 | completed | b7e7 | -50 | 6463 | 5 | 3 | `b7e7 h2e2 b9c7 h0g2 a9b9 b1g1` |
| 3 | b2b1 | 8 | completed | b7e7 | -34 | 26296 | 23 | 3 | `b7e7 h0g2 b9c7 c3c4 g6g5 b1g1 a9a8 b0c2` |
| 3 | b2b1 | 10 | completed | b7e7 | -34 | 44095 | 39 | 3 | `b7e7 h0g2 b9c7 a0a2 h7g7 i0h0 h9i7 a2b2 i9h9 h2h4` |
| 3 | b2b1 | 12 | completed | b7e7 | -35 | 109175 | 101 | 3 | `b7e7 h0g2 h9i7 a0a2 h7g7 h2h4` |
| 3 | b2b3 | 4 | completed | c6c5 | -73 | 1224 | 2 | 3 | `c6c5` |
| 3 | b2b3 | 6 | completed | c6c5 | -56 | 6491 | 5 | 3 | `c6c5 g3g4 h9i7 b0a2` |
| 3 | b2b3 | 8 | completed | c6c5 | -40 | 26654 | 22 | 3 | `c6c5 h2c2 c9e7 h0g2 h9i7 b0a2 b9c7` |
| 3 | b2b3 | 10 | completed | c6c5 | -48 | 54476 | 46 | 3 | `c6c5 g3g4 b9c7 h0g2 h7g7 g2f4` |
| 3 | b2b3 | 12 | completed | c6c5 | -46 | 131735 | 115 | 3 | `c6c5 b0a2 g6g5 a0a1 h7f7 h2e2 b9c7 h0g2 h9g7` |
| 3 | b2b4 | 4 | completed | g9e7 | -29 | 2356 | 2 | 3 | `g9e7` |
| 3 | b2b4 | 6 | completed | c6c5 | -18 | 7970 | 7 | 3 | `c6c5 g3g4 b9c7 b0c2 h9i7` |
| 3 | b2b4 | 8 | completed | c6c5 | -20 | 21641 | 19 | 3 | `c6c5 g3g4 g9e7 h0g2 b9c7 b0c2 a9a8 c0e2 c7d5` |
| 3 | b2b4 | 10 | completed | c6c5 | -20 | 43161 | 38 | 3 | `c6c5 g3g4 b9c7 h0g2 a9a8 c0e2 g9e7 b0c2 h9f8 i0i1` |
| 3 | b2b4 | 12 | completed | c6c5 | -24 | 141537 | 129 | 3 | `c6c5 g3g4 b9c7 h0g2 g9e7 c0e2` |
| 3 | b2b5 | 4 | completed | b9c7 | -125 | 832 | 1 | 3 | `b9c7` |
| 3 | b2b5 | 6 | completed | h7e7 | -96 | 5599 | 4 | 3 | `h7e7 b0c2` |
| 3 | b2b5 | 8 | completed | c6c5 | -76 | 23613 | 21 | 3 | `c6c5 b0c2 b9c7 b5b4 g6g5 h0i2 c7d5 b4i4` |
| 3 | b2b5 | 10 | completed | h7e7 | -61 | 46818 | 42 | 3 | `h7e7 b0c2 c6c5 g3g4 h9g7 h0g2 i9h9 i0h0 h9h3 h2i2` |
| 3 | b2b5 | 12 | completed | c6c5 | -62 | 136212 | 141 | 3 | `c6c5 b5b4 b9c7 b0c2 c9e7 g3g4 h7g7 g0e2 h9i7 h0g2` |
| 3 | b2b6 | 4 | completed | b9c7 | -36 | 1180 | 2 | 3 | `b9c7 c3c4 g6g5 b0c2` |
| 3 | b2b6 | 6 | completed | c6c5 | -14 | 4445 | 4 | 3 | `c6c5 g3g4 b9c7 h0g2 a9a8` |
| 3 | b2b6 | 8 | completed | h9g7 | -25 | 12768 | 12 | 3 | `h9g7 h0i2 h7i7 b0c2 i9h9 i0h0 h9h5 h2e2` |
| 3 | b2b6 | 10 | completed | h9g7 | -29 | 22868 | 22 | 3 | `h9g7 h0i2 g6g5 c3c4 b9c7 b0c2 c9e7 c0e2 i6i5 i0i1` |
| 3 | b2b6 | 12 | completed | b9c7 | -28 | 109455 | 108 | 3 | `b9c7 b0c2 h9g7 g3g4 h7h5 b6b4 c9e7 h0g2 h5a5 c0a2` |
| 3 | b2b9 | 4 | completed | a9b9 | -67 | 2087 | 1 | 3 | `a9b9 b0c2 g6g5 a0b0` |
| 3 | b2b9 | 6 | completed | a9b9 | -53 | 4652 | 2 | 3 | `a9b9 b0c2 g6g5 a0b0 b9b8` |
| 3 | b2b9 | 8 | completed | a9b9 | -123 | 8130 | 5 | 3 | `a9b9 b0c2 b7e7 h2e2 b9b3 h0g2 h9g7 i0h0` |
| 3 | b2b9 | 10 | completed | a9b9 | -131 | 13986 | 9 | 3 | `a9b9 b0c2 b7e7 g0e2 h9g7 a0b0 b9b0 c2b0` |
| 3 | b2b9 | 12 | completed | a9b9 | -117 | 60629 | 52 | 3 | `a9b9 b0c2 b7e7 h2f2 h7h2 g0e2 h9g7 h0f1 h2h3 c3c4` |
| 3 | b2c2 | 4 | completed | g6g5 | -21 | 2727 | 2 | 3 | `g6g5 g0e2` |
| 3 | b2c2 | 6 | completed | g6g5 | -12 | 4550 | 3 | 3 | `g6g5 h2e2 h9g7 h0g2 i9h9 i0h0` |
| 3 | b2c2 | 8 | completed | h7e7 | -10 | 12291 | 10 | 3 | `h7e7 h0g2 h9g7 b0a2` |
| 3 | b2c2 | 10 | completed | h7e7 | -2 | 36528 | 31 | 3 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9a7 a0b0 a9b9 a3a4` |
| 3 | b2c2 | 12 | completed | h7e7 | -19 | 87588 | 80 | 3 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0a2 b7b2 c0e2 b9a7 g3g4` |
| 3 | b2d2 | 4 | completed | b9c7 | 3 | 2106 | 2 | 3 | `b9c7 b0c2` |
| 3 | b2d2 | 6 | completed | b7e7 | 16 | 9369 | 7 | 3 | `b7e7 h0g2 b9c7 b0c2 a9b9 c3c4` |
| 3 | b2d2 | 8 | completed | b7e7 | 27 | 18378 | 15 | 3 | `b7e7 h0g2 b9c7 b0c2 a9b9 g3g4 c6c5 g0e2` |
| 3 | b2d2 | 10 | completed | h7e7 | 20 | 39032 | 35 | 3 | `h7e7 h0g2 h9g7 b0c2 b9a7 i0h0 i9h9 a0b0 b7c7 g3g4` |
| 3 | b2d2 | 12 | completed | h7e7 | 12 | 74732 | 70 | 3 | `h7e7 h0g2 h9g7 b0c2 b9a7 a0b0 a9b9 i0h0 i9h9 g0e2` |
| 3 | b2e2 | 4 | completed | b9c7 | 25 | 2186 | 2 | 3 | `b9c7 b0c2 a9b9 a0b0` |
| 3 | b2e2 | 6 | completed | b9c7 | 26 | 4010 | 3 | 3 | `b9c7 b0c2 a9b9 h0g2 h9g7 a0b0` |
| 3 | b2e2 | 8 | completed | b9c7 | 31 | 10671 | 8 | 3 | `b9c7 b0c2 c6c5 h0g2 h9g7` |
| 3 | b2e2 | 10 | completed | b9c7 | 23 | 35087 | 30 | 3 | `b9c7 b0c2 c6c5 a0b0 a9b9 h0g2 h9g7 h2i2 g6g5 i0h0` |
| 3 | b2e2 | 12 | completed | b9c7 | 19 | 122265 | 116 | 3 | `b9c7 b0c2 a9b9 a0b0 c6c5 b0b4 h9g7 e3e4` |
| 3 | b2f2 | 4 | completed | b9c7 | 2 | 2472 | 2 | 3 | `b9c7` |
| 3 | b2f2 | 6 | completed | b9c7 | 6 | 9146 | 7 | 3 | `b9c7 b0c2 c6c5 g3g4` |
| 3 | b2f2 | 8 | completed | c6c5 | 18 | 29256 | 24 | 3 | `c6c5 g3g4 h9i7 h0g2 h7g7 b0c2 i9h9 i0h0 b9c7` |
| 3 | b2f2 | 10 | completed | c6c5 | 11 | 51131 | 42 | 3 | `c6c5 g3g4 h7g7 h0i2 h9i7 b0c2 i9h9 i0h0 b9c7` |
| 3 | b2f2 | 12 | completed | b7e7 | 13 | 108077 | 95 | 3 | `b7e7 b0c2 b9c7 a0b0 h9g7 g3g4 a9a8 h0g2 a8f8 d0e1` |
| 3 | b2g2 | 4 | completed | h7e7 | -82 | 2694 | 2 | 3 | `h7e7` |
| 3 | b2g2 | 6 | completed | c6c5 | -21 | 7095 | 5 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 i3i4` |
| 3 | b2g2 | 8 | completed | c6c5 | -22 | 13133 | 11 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 i3i4 g9e7 b0b4 f9e8 g3g4` |
| 3 | b2g2 | 10 | completed | c6c5 | -20 | 37939 | 33 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 i3i4 b7b3 h0i2` |
| 3 | b2g2 | 12 | completed | c6c5 | -18 | 101379 | 92 | 3 | `c6c5 b0c2 b9c7 a0b0 a9b9 b0b6 g9e7 g0e2 g6g5 h0f1` |
| 3 | c0a2 | 4 | completed | b7e7 | -73 | 2109 | 2 | 3 | `b7e7 b0c2 b9c7 c3c4` |
| 3 | c0a2 | 6 | completed | g6g5 | -57 | 5899 | 4 | 3 | `g6g5 b0c2 b7e7 h2e2 b9c7 h0g2 a9b9` |
| 3 | c0a2 | 8 | completed | g6g5 | -46 | 20428 | 17 | 3 | `g6g5 h2e2 h9g7 h0g2 b9c7 i0h0 g7f5 c3c4` |
| 3 | c0a2 | 10 | completed | b7e7 | -54 | 58631 | 53 | 3 | `b7e7 h2e2 b9c7 h0g2 h9g7 i0h0 a9b9 b0d1 i9i8 a0b0` |
| 3 | c0a2 | 12 | completed | g6g5 | -48 | 133402 | 128 | 3 | `g6g5 b2e2 b9c7 b0d1 a9b9 a0b0 h9g7 b0b4 g7f5` |
| 3 | c0e2 | 4 | completed | g6g5 | -5 | 2612 | 2 | 3 | `g6g5 c3c4 h9g7` |
| 3 | c0e2 | 6 | completed | b7e7 | 16 | 11327 | 9 | 3 | `b7e7 g3g4 b9c7 h0g2 a9b9` |
| 3 | c0e2 | 8 | completed | h7f7 | 24 | 20951 | 16 | 3 | `h7f7 h0i2 h9g7 g3g4 i9h9 h2g2 c6c5` |
| 3 | c0e2 | 10 | completed | b7e7 | 18 | 46603 | 40 | 3 | `b7e7 g3g4 b9c7 h0g2 a9b9` |
| 3 | c0e2 | 12 | completed | h7f7 | 20 | 168129 | 155 | 3 | `h7f7 h0g2 g6g5 c3c4 h9g7 b0c2 i9h9 i0h0 c9e7 c2d4` |
| 3 | c3c4 | 4 | completed | g6g5 | -2 | 1961 | 1 | 3 | `g6g5 b0c2 b9a7` |
| 3 | c3c4 | 6 | completed | b9a7 | 30 | 8007 | 7 | 3 | `b9a7 b0c2 g9e7 c2d4` |
| 3 | c3c4 | 8 | completed | b7c7 | 16 | 17488 | 15 | 3 | `b7c7 c0e2 b9a7 b0c2 a9b9 c2d4 h7e7 d4e6` |
| 3 | c3c4 | 10 | completed | b7c7 | 19 | 52795 | 47 | 3 | `b7c7 b2e2 h7e7 b0c2 h9g7 c2d4 i9h9 h0g2 g6g5` |
| 3 | c3c4 | 12 | completed | b7c7 | 19 | 138858 | 131 | 3 | `b7c7 h0g2 g6g5 b0c2 h9g7 c2d4 i9i8 b2e2` |
| 3 | d0e1 | 4 | completed | g6g5 | -26 | 1109 | 1 | 3 | `g6g5` |
| 3 | d0e1 | 6 | completed | b7a7 | -11 | 5791 | 5 | 3 | `b7a7 c3c4 b9c7 g3g4` |
| 3 | d0e1 | 8 | completed | b9c7 | -3 | 12982 | 11 | 3 | `b9c7 g3g4 b7a7 h2f2 a9b9 c0e2 h9g7` |
| 3 | d0e1 | 10 | completed | b9c7 | -3 | 25157 | 22 | 3 | `b9c7 c3c4 h9g7 b2d2` |
| 3 | d0e1 | 12 | completed | b9c7 | -3 | 70191 | 66 | 3 | `b9c7 h2f2 b7a7 h0g2 a9b9 b2d2 h9i7 i0h0 i9h9 b0c2` |
| 3 | e0e1 | 4 | completed | h9g7 | -115 | 2054 | 2 | 3 | `h9g7 e1e0 b7e7 b0c2 b9c7 c3c4` |
| 3 | e0e1 | 6 | completed | b9c7 | -117 | 3212 | 3 | 3 | `b9c7 b0c2` |
| 3 | e0e1 | 8 | completed | b7e7 | -91 | 19597 | 17 | 3 | `b7e7 b0c2 b9c7 a0b0` |
| 3 | e0e1 | 10 | completed | g6g5 | -99 | 36246 | 32 | 3 | `g6g5 e1e0 h7e7 h0g2 h9g7 i0h0 i9h9 c3c4 b9a7 c0e2` |
| 3 | e0e1 | 12 | completed | h7e7 | -96 | 101193 | 96 | 3 | `h7e7 h0g2 h9g7 g3g4 i9h9 i0h0 h9h3 e1e0 c6c5 c0e2` |
| 3 | e3e4 | 4 | completed | h7e7 | -100 | 2348 | 2 | 3 | `h7e7 c0e2 h9g7` |
| 3 | e3e4 | 6 | completed | b7e7 | -79 | 7313 | 6 | 3 | `b7e7 b2e2 h9g7 d0e1 b9c7 h0g2 a9b9` |
| 3 | e3e4 | 8 | completed | b7e7 | -87 | 12423 | 10 | 3 | `b7e7 d0e1 e7e4 c0e2 h9g7` |
| 3 | e3e4 | 10 | completed | h7e7 | -98 | 40037 | 34 | 3 | `h7e7 d0e1 e7e4 c0e2 h9g7 h0g2 i9h9` |
| 3 | e3e4 | 12 | completed | h7e7 | -97 | 109117 | 97 | 3 | `h7e7 d0e1 e7e4 b2e2 h9g7 h0g2 i9h9 i0h0 h9h3 b0c2` |
| 3 | f0e1 | 4 | completed | c6c5 | -31 | 1062 | 1 | 3 | `c6c5 a3a4` |
| 3 | f0e1 | 6 | completed | h7i7 | -10 | 6690 | 5 | 3 | `h7i7 g3g4 h9g7 h0g2 i9h9` |
| 3 | f0e1 | 8 | completed | g6g5 | -3 | 22306 | 18 | 3 | `g6g5 c3c4 b7c7 g0e2 b9a7 b0c2 a9b9 c2d4 h9g7` |
| 3 | f0e1 | 10 | completed | g6g5 | -2 | 49240 | 43 | 3 | `g6g5 b2d2 b9a7 b0a2 a6a5 a0b0 a9b9 b0b4 b7c7 b4f4` |
| 3 | f0e1 | 12 | completed | h9g7 | -7 | 109712 | 99 | 3 | `h9g7 g3g4 h7i7 h0g2 i9h9 i0h0 c6c5 h2h6 b9c7 b2b6` |
| 3 | g0e2 | 4 | completed | h7e7 | -12 | 2109 | 2 | 3 | `h7e7 g3g4 c6c5` |
| 3 | g0e2 | 6 | completed | b7e7 | 6 | 8369 | 6 | 3 | `b7e7 h0g2 b9c7 g3g4 a9b9 b2c2 b9b1` |
| 3 | g0e2 | 8 | completed | h7f7 | 16 | 21823 | 18 | 3 | `h7f7 g3g4 h9i7 h0g2 i9h9 i0h0 h9h5 c3c4` |
| 3 | g0e2 | 10 | completed | h7f7 | 19 | 54705 | 47 | 3 | `h7f7 b2d2 b9a7 b0c2 h9g7 a0b0 a9b9` |
| 3 | g0e2 | 12 | completed | g6g5 | 21 | 142282 | 126 | 3 | `g6g5 c3c4 b9a7 a3a4 g9e7 b0a2 h9g7` |
| 3 | g0i2 | 4 | completed | h9g7 | -64 | 2205 | 2 | 3 | `h9g7 b0c2 c6c5 g3g4` |
| 3 | g0i2 | 6 | completed | h7e7 | -55 | 7446 | 6 | 3 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0c2` |
| 3 | g0i2 | 8 | completed | h7e7 | -46 | 19475 | 16 | 3 | `h7e7 b2e2 h9g7 b0c2 i9h9 a0b0 h9h2 b0b7` |
| 3 | g0i2 | 10 | completed | h7e7 | -48 | 53467 | 46 | 3 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0c2 c6c5 a0a1 b7a7 a1d1` |
| 3 | g0i2 | 12 | completed | c6c5 | -50 | 109651 | 102 | 3 | `c6c5 b2e2 h9g7 b0a2 b9c7 a0b0 c7d5 b0b4 b7d7 g3g4` |
| 3 | g3g4 | 4 | completed | b7e7 | 3 | 1830 | 1 | 3 | `b7e7 h0g2 h9i7 i3i4` |
| 3 | g3g4 | 6 | completed | g9e7 | 21 | 5387 | 4 | 3 | `g9e7 h2e2 b9c7 c3c4` |
| 3 | g3g4 | 8 | completed | c6c5 | 33 | 17495 | 15 | 3 | `c6c5 b0a2 b9c7 h0g2 g9e7 a0a1` |
| 3 | g3g4 | 10 | completed | c6c5 | 29 | 30422 | 26 | 3 | `c6c5 b2c2 g9e7 b0a2 b9c7 h0g2` |
| 3 | g3g4 | 12 | completed | h7g7 | 23 | 90217 | 84 | 3 | `h7g7 g0e2 h9i7 c3c4 i9h9 b2d2 b7e7 b0c2 b9c7` |
| 3 | h0g2 | 4 | completed | b9c7 | 31 | 2351 | 2 | 3 | `b9c7 g3g4 g9e7` |
| 3 | h0g2 | 6 | completed | g6g5 | 27 | 4733 | 4 | 3 | `g6g5 h2i2 h9g7 i0h0` |
| 3 | h0g2 | 8 | completed | g6g5 | 25 | 10047 | 10 | 3 | `g6g5 h2i2 c6c5 b2c2` |
| 3 | h0g2 | 10 | completed | g6g5 | 23 | 35475 | 33 | 3 | `g6g5 c3c4 c9e7 i0i1` |
| 3 | h0g2 | 12 | completed | g6g5 | 20 | 116655 | 109 | 3 | `g6g5 h2i2 h9g7 i0h0 i9h9 c3c4 c9e7 b2d2 h7h3 b0c2` |
| 3 | h0i2 | 4 | completed | b9c7 | -9 | 2276 | 2 | 3 | `b9c7 h2g2 h9i7 i0h0` |
| 3 | h0i2 | 6 | completed | b7e7 | 3 | 6853 | 6 | 3 | `b7e7 b0c2 b9c7 a0b0 c6c5 h2g2` |
| 3 | h0i2 | 8 | completed | b7e7 | 6 | 18106 | 16 | 3 | `b7e7 b2e2 b9c7 b0c2 a9b9 i0i1 b9b5 i1f1 h9g7` |
| 3 | h0i2 | 10 | completed | b7e7 | 1 | 48282 | 43 | 3 | `b7e7 b0c2 b9c7 a0b0 a9b9 c0e2 c6c5` |
| 3 | h0i2 | 12 | completed | b7e7 | 1 | 128001 | 117 | 3 | `b7e7 b2e2 b9c7 b0c2 a9b9 a0a1 i6i5 a1f1 b9b3 c3c4` |
| 3 | h2c2 | 4 | completed | h7e7 | -88 | 2693 | 3 | 3 | `h7e7` |
| 3 | h2c2 | 6 | completed | g6g5 | -15 | 10758 | 8 | 3 | `g6g5 h0g2 h9g7 i0h0 b9a7 h0h6` |
| 3 | h2c2 | 8 | completed | g6g5 | -13 | 24074 | 20 | 3 | `g6g5 h0g2 h9g7 i0h0 i9h9 h0h6 c9e7 c0e2 h7i7 h6h9` |
| 3 | h2c2 | 10 | completed | c9e7 | -14 | 41088 | 35 | 3 | `c9e7 c2i2 h9i7 h0g2 i9h9 i0h0 b9c7` |
| 3 | h2c2 | 12 | completed | g6g5 | -18 | 121241 | 110 | 3 | `g6g5 c0e2 h9g7 h0g2 i9h9 i0i1 c9e7 b0d1 h7i7 a3a4` |
| 3 | h2d2 | 4 | completed | c6c5 | -10 | 2378 | 3 | 3 | `c6c5` |
| 3 | h2d2 | 6 | completed | g6g5 | 9 | 10898 | 9 | 3 | `g6g5 h0g2 h9g7 i0h0` |
| 3 | h2d2 | 8 | completed | h9g7 | 11 | 35717 | 29 | 3 | `h9g7 g3g4 c6c5 h0g2 b9c7 i0h0 i9h9 b0a2` |
| 3 | h2d2 | 10 | completed | h9g7 | 9 | 71294 | 60 | 3 | `h9g7 c3c4 g6g5 b0c2 b9a7 b2a2` |
| 3 | h2d2 | 12 | completed | h9g7 | 10 | 163858 | 145 | 3 | `h9g7 c3c4 b7c7 h0g2 i9h9 c0e2 g6g5 i0h0 h7h3 b0c2` |
| 3 | h2e2 | 4 | completed | h9g7 | 21 | 1579 | 1 | 3 | `h9g7 h0g2 i9h9 i0h0 g6g5` |
| 3 | h2e2 | 6 | completed | h9g7 | 27 | 3432 | 3 | 3 | `h9g7 h0g2 i9h9 i0h0 g6g5 b0c2` |
| 3 | h2e2 | 8 | completed | h9g7 | 30 | 12879 | 10 | 3 | `h9g7 h0g2 i9h9 i0h0 c6c5 h0h4 b9c7 c3c4 c5c4` |
| 3 | h2e2 | 10 | completed | h9g7 | 30 | 40422 | 37 | 3 | `h9g7 g3g4 c6c5 h0g2 b9c7` |
| 3 | h2e2 | 12 | completed | h9g7 | 24 | 79716 | 74 | 3 | `h9g7 g3g4 i9h9 h0g2 c6c5 i0h0 b9c7 b0a2 h7h3 a0a1` |
| 3 | h2f2 | 4 | completed | b7e7 | -7 | 2585 | 3 | 3 | `b7e7 b0c2 c6c5 h0i2` |
| 3 | h2f2 | 6 | completed | h9g7 | 12 | 5644 | 5 | 3 | `h9g7 h0g2 i9h9 i0h0 c6c5 g3g4` |
| 3 | h2f2 | 8 | completed | h9g7 | 22 | 16912 | 14 | 3 | `h9g7 c3c4 g6g5 b0c2 i9h9 h0g2 b7c7 i0h0 h7h3 a0b0` |
| 3 | h2f2 | 10 | completed | b7e7 | 19 | 41250 | 38 | 3 | `b7e7 b0c2 h9i7` |
| 3 | h2f2 | 12 | completed | b7e7 | 20 | 109964 | 105 | 3 | `b7e7 b0c2 b9c7 h0g2 h9i7 i0h0 i9h9 a0b0 a9b9 b2b6` |
| 3 | h2g2 | 4 | completed | h7e7 | -19 | 2311 | 2 | 3 | `h7e7` |
| 3 | h2g2 | 6 | completed | b7e7 | -12 | 6630 | 5 | 3 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0i2` |
| 3 | h2g2 | 8 | completed | b7e7 | -6 | 14797 | 12 | 3 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 i3i4` |
| 3 | h2g2 | 10 | completed | b7e7 | -10 | 37575 | 35 | 3 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 a0a1` |
| 3 | h2g2 | 12 | completed | b7e7 | -15 | 74075 | 69 | 3 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 h0h4` |
| 3 | h2h1 | 4 | completed | h7e7 | -59 | 2125 | 2 | 3 | `h7e7 h1e1 h9g7` |
| 3 | h2h1 | 6 | completed | b7e7 | -41 | 7382 | 5 | 3 | `b7e7 b0c2 b9c7 a0b0 a9b9 h1e1` |
| 3 | h2h1 | 8 | completed | h7e7 | -36 | 20323 | 17 | 3 | `h7e7 b0c2 h9g7 h1c1 i9h9` |
| 3 | h2h1 | 10 | completed | h7e7 | -34 | 51929 | 46 | 3 | `h7e7 h1e1 h9g7 h0g2 i9h9 b2e2 b9c7` |
| 3 | h2h1 | 12 | completed | h7e7 | -38 | 81453 | 73 | 3 | `h7e7 h1e1 h9g7 h0g2 i9h9 g3g4 c6c5 i0h0 h9h0 g2h0` |
| 3 | h2h3 | 4 | completed | g6g5 | -65 | 2121 | 2 | 3 | `g6g5 c3c4` |
| 3 | h2h3 | 6 | completed | h7i7 | -48 | 7214 | 6 | 3 | `h7i7 h0g2` |
| 3 | h2h3 | 8 | completed | b7d7 | -41 | 23707 | 21 | 3 | `b7d7 b2e2 h9g7 g3g4 b9c7 b0c2 a9b9 h0g2` |
| 3 | h2h3 | 10 | completed | g6g5 | -42 | 49101 | 44 | 3 | `g6g5 h0i2 b7d7 b2e2 b9c7 b0c2 h9g7` |
| 3 | h2h3 | 12 | completed | g6g5 | -42 | 125398 | 114 | 3 | `g6g5 b2g2 a9a8 b0c2 g9e7 d0e1 a8f8 g2f2 f8f4 c0e2` |
| 3 | h2h4 | 4 | completed | b9c7 | -34 | 2256 | 2 | 3 | `b9c7 h4e4 h7e7` |
| 3 | h2h4 | 6 | completed | g6g5 | -17 | 6355 | 5 | 3 | `g6g5 h0g2` |
| 3 | h2h4 | 8 | completed | g6g5 | -22 | 20332 | 18 | 3 | `g6g5 b2e2 h9g7 b0c2 b9c7 c3c4 g7f5` |
| 3 | h2h4 | 10 | completed | g6g5 | -27 | 59097 | 54 | 3 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 h9g7 c3c4` |
| 3 | h2h4 | 12 | completed | g6g5 | -16 | 142935 | 130 | 3 | `g6g5 h0g2 h9g7 c3c4 i9i8 g0e2 i8c8 f0e1 c9e7 i0f0` |
| 3 | h2h5 | 4 | completed | g6g5 | -119 | 1667 | 2 | 3 | `g6g5` |
| 3 | h2h5 | 6 | completed | b7e7 | -96 | 4068 | 3 | 3 | `b7e7 h0g2 b9c7` |
| 3 | h2h5 | 8 | completed | g6g5 | -69 | 22475 | 19 | 3 | `g6g5 h5h4 h9g7 c3c4 b9a7 h0g2 b7c7` |
| 3 | h2h5 | 10 | completed | g6g5 | -65 | 58373 | 51 | 3 | `g6g5 h0g2 h9g7 h5h1 b7e7 a0a2 g7f5 c3c4 b9c7 b0c2` |
| 3 | h2h5 | 12 | completed | g6g5 | -67 | 137238 | 123 | 3 | `g6g5 h0g2 h9g7 h5h1 g7f5 h1g1 h7g7 i0h0 c6c5 h0h4` |
| 3 | h2h6 | 4 | completed | h9g7 | -20 | 1184 | 1 | 3 | `h9g7` |
| 3 | h2h6 | 6 | completed | g6g5 | -36 | 4136 | 3 | 3 | `g6g5 b2e2 h9g7 h0g2` |
| 3 | h2h6 | 8 | completed | h9g7 | -26 | 17221 | 15 | 3 | `h9g7 b2e2 b9c7 b0c2 a9b9 a0b0 c6c5` |
| 3 | h2h6 | 10 | completed | h9g7 | -29 | 28787 | 25 | 3 | `h9g7 g3g4 b9c7 h0g2 b7a7 b0a2 a9b9 a0b0 b9b5` |
| 3 | h2h6 | 12 | completed | b9c7 | -26 | 115196 | 105 | 3 | `b9c7 h0g2 b7a7 b0c2 a9b9 a0b0 b9b5` |
| 3 | h2h9 | 4 | completed | i9h9 | -135 | 1720 | 1 | 3 | `i9h9 h0g2` |
| 3 | h2h9 | 6 | completed | i9h9 | -135 | 3345 | 1 | 3 | `i9h9 h0g2 h7e7 b0c2 b9c7 i0h0 h9h0 g2h0` |
| 3 | h2h9 | 8 | completed | i9h9 | -111 | 7629 | 4 | 3 | `i9h9 h0g2 h7e7 b2e2 b9c7 i0h0 h9h0 g2h0 e7e3 f0e1` |
| 3 | h2h9 | 10 | completed | i9h9 | -111 | 17119 | 12 | 3 | `i9h9 h0g2 h7e7 c3c4 b9c7 b0c2 a9a8 i0h0 h9h0 g2h0` |
| 3 | h2h9 | 12 | completed | i9h9 | -117 | 38049 | 29 | 3 | `i9h9 h0g2 h7g7 i0h0 h9h0 g2h0 c6c5 b2e2 b9c7 b0c2` |
| 3 | h2i2 | 4 | completed | g6g5 | -21 | 1277 | 1 | 3 | `g6g5 c3c4` |
| 3 | h2i2 | 6 | completed | g6g5 | -2 | 7812 | 5 | 3 | `g6g5 b2e2 b9c7 h0g2 h9g7 i0h0` |
| 3 | h2i2 | 8 | completed | g6g5 | 10 | 18752 | 14 | 3 | `g6g5 h0g2 h9g7 i0h0 i9h9 h0h4 h7i7 h4h9 g7h9 b2e2` |
| 3 | h2i2 | 10 | completed | g6g5 | 12 | 31508 | 24 | 3 | `g6g5 h0g2 h9g7 i0h0 i9h9 b2e2 b9c7 b0c2 a9b9 a0b0` |
| 3 | h2i2 | 12 | completed | g6g5 | 14 | 89978 | 80 | 3 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4 h7h3 b0c2 b7b3 g0e2` |
| 3 | i0i1 | 4 | completed | h7h0 | -145 | 1884 | 1 | 3 | `h7h0 h2e2 b9c7` |
| 3 | i0i1 | 6 | completed | h7h0 | -111 | 4940 | 3 | 3 | `h7h0 i1i0 h0f0 e0f0 h9g7 h2e2` |
| 3 | i0i1 | 8 | completed | h7h0 | -84 | 17175 | 13 | 3 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0i1 b2b4 b9c7` |
| 3 | i0i1 | 10 | completed | h7h0 | -69 | 37952 | 30 | 3 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0g0 h0g0 i9h9 b0c2` |
| 3 | i0i1 | 12 | completed | h7h0 | -62 | 97925 | 85 | 3 | `h7h0 h2e2 b7e7 i1h1 h0i0 b0c2 b9c7 b2b4 h9g7 b4g4` |
| 3 | i0i2 | 4 | completed | h7h0 | -176 | 1653 | 1 | 3 | `h7h0 c3c4` |
| 3 | i0i2 | 6 | completed | h7h0 | -101 | 7591 | 5 | 3 | `h7h0 h2e2 h9g7 i2h2 h0i0 h2h0` |
| 3 | i0i2 | 8 | completed | h7h0 | -119 | 13662 | 9 | 3 | `h7h0 h2e2 h9g7 i2h2 h0i0 h2h0 i0i1` |
| 3 | i0i2 | 10 | completed | h7h0 | -49 | 69490 | 57 | 3 | `h7h0 h2e2 b9c7 i2h2 h0i0 b0c2 h9g7 h2h0 i0i1` |
| 3 | i0i2 | 12 | completed | h7h0 | -68 | 133736 | 115 | 3 | `h7h0 h2e2 b7e7 i2h2 h0i0 b0c2 b9c7 h2i2 h9g7 i2i0` |
| 3 | i3i4 | 4 | completed | b9c7 | -45 | 1555 | 1 | 3 | `b9c7` |
| 3 | i3i4 | 6 | completed | h7e7 | -19 | 6845 | 5 | 3 | `h7e7 b0c2 h9g7 h0i2 i9h9 c3c4` |
| 3 | i3i4 | 8 | completed | c6c5 | -9 | 24231 | 20 | 3 | `c6c5 b0c2 h9g7 h0i2 i6i5 i2h4 i5i4 h2h7 b7h7` |
| 3 | i3i4 | 10 | completed | b7e7 | -11 | 46494 | 41 | 3 | `b7e7 b0c2 b9c7 g3g4 h9g7 c3c4 a9b9 a0b0 h7i7 h0g2` |
| 3 | i3i4 | 12 | completed | b7e7 | -13 | 103852 | 94 | 3 | `b7e7 b0c2 b9c7 h0i2 a9b9 i2h4 g6g5 h2h7 b9b2 a0a2` |
| 4 | a0a1 | 4 | completed | b7b0 | -4 | 3643 | 2 | 4 | `b7b0 b2e2 b0b5 e2e6 b5e5 h2e2 e5e2 g0e2` |
| 4 | a0a1 | 6 | completed | b7b0 | -125 | 5434 | 4 | 4 | `b7b0 h2e2` |
| 4 | a0a1 | 8 | completed | b7b0 | -72 | 29397 | 23 | 4 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0c0 b0c0 h7e7 h0g2` |
| 4 | a0a1 | 10 | completed | b7b0 | -72 | 42783 | 34 | 4 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0c0 b0c0 h7e7 h0g2` |
| 4 | a0a1 | 12 | completed | b7b0 | -67 | 89257 | 74 | 4 | `b7b0 b2e2 h7e7 a1b1 b0a0 e2e6 d9e8 e6e4 h9g7 h2e2` |
| 4 | a0a2 | 4 | completed | b7b0 | -193 | 1967 | 2 | 4 | `b7b0 a3a4` |
| 4 | a0a2 | 6 | completed | b7b0 | -122 | 6975 | 4 | 4 | `b7b0 b2e2 b9c7 a2b2 b0a0 b2b0` |
| 4 | a0a2 | 8 | completed | b7b0 | -74 | 27646 | 21 | 4 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 h9g7 b2b0 a0c0 b0c0` |
| 4 | a0a2 | 10 | completed | b7b0 | -58 | 73607 | 60 | 4 | `b7b0 b2e2 h7e7 a2b2 b0a0 b2b0 a0c0 b0c0 h9g7 h0g2` |
| 4 | a0a2 | 12 | completed | b7b0 | -65 | 173546 | 152 | 4 | `b7b0 b2e2 h7e7 a2b2 b0a0 h0g2 h9g7 i0i1 i9h9 i1a1` |
| 4 | a3a4 | 4 | completed | c6c5 | -60 | 2121 | 2 | 4 | `c6c5` |
| 4 | a3a4 | 6 | completed | b9c7 | -13 | 10767 | 8 | 4 | `b9c7 b0a2` |
| 4 | a3a4 | 8 | completed | h7e7 | -10 | 20719 | 17 | 4 | `h7e7 h2e2 h9g7 h0g2 i9h9` |
| 4 | a3a4 | 10 | completed | h7f7 | -9 | 59244 | 54 | 4 | `h7f7 h0g2 h9g7 g3g4 i9h9 i0h0 b9c7 h2h6 c6c5` |
| 4 | a3a4 | 12 | completed | b9c7 | -9 | 149516 | 142 | 4 | `b9c7 c3c4 b7a7 b0a2 h7e7 a2b4 e7e3 h0g2` |
| 4 | b0a2 | 4 | completed | g9e7 | 0 | 2666 | 2 | 4 | `g9e7` |
| 4 | b0a2 | 6 | completed | h7e7 | 6 | 8635 | 6 | 4 | `h7e7 h0g2 h9g7 i0h0 i9h9 b2c2` |
| 4 | b0a2 | 8 | completed | h7e7 | 4 | 22610 | 18 | 4 | `h7e7 h0g2 h9g7 i0h0 i9h9 b2d2 b7b2` |
| 4 | b0a2 | 10 | completed | h7e7 | 6 | 60182 | 52 | 4 | `h7e7 h0g2 h9g7 g3g4 i9h9 i0h0 h9h5 b2c2 b7b2 g0e2` |
| 4 | b0a2 | 12 | completed | h7e7 | 3 | 137701 | 124 | 4 | `h7e7 h0g2 g6g5 i0h0 h9g7 b2d2 b7b2 d2d7 b2h2 h0h2` |
| 4 | b0c2 | 4 | completed | c6c5 | -8 | 1883 | 1 | 4 | `c6c5` |
| 4 | b0c2 | 6 | completed | c6c5 | 6 | 6657 | 4 | 4 | `c6c5 h2e2 b9c7 h0g2 h9g7 i0h0` |
| 4 | b0c2 | 8 | completed | c6c5 | 17 | 18126 | 13 | 4 | `c6c5 g3g4 b9c7 h2f2 h9i7 h0g2 i9h9` |
| 4 | b0c2 | 10 | completed | c6c5 | 18 | 47322 | 41 | 4 | `c6c5 h2e2 h9g7 h0g2 i9h9 i0h0 g6g5` |
| 4 | b0c2 | 12 | completed | c6c5 | 16 | 169685 | 158 | 4 | `c6c5 b2a2 b9c7 a0b0 a9b9 g3g4 b7b3 h0g2 h7g7 i0i1` |
| 4 | b2a2 | 4 | completed | b9c7 | 12 | 3028 | 2 | 4 | `b9c7 b0c2 h9g7 a0b0` |
| 4 | b2a2 | 6 | completed | c6c5 | 14 | 9898 | 7 | 4 | `c6c5 b0c2 b9c7 a0b0 a9b9 g3g4 g9e7 h0g2 h9f8 g2f4` |
| 4 | b2a2 | 8 | completed | c6c5 | 16 | 18182 | 14 | 4 | `c6c5 b0c2 b9c7 a0b0 a9b9 b0b4 g9e7` |
| 4 | b2a2 | 10 | completed | b9c7 | 12 | 37706 | 30 | 4 | `b9c7 b0c2 c6c5 a0b0 a9b9 b0b4 b7a7 b4b9 c7b9 g3g4` |
| 4 | b2a2 | 12 | completed | b9c7 | 13 | 87828 | 75 | 4 | `b9c7 b0c2 c6c5 a0b0 a9b9 g3g4 b7b3 h2h4 h7g7 h0g2` |
| 4 | b2b1 | 4 | completed | b7b5 | -47 | 3456 | 2 | 4 | `b7b5 b1g1` |
| 4 | b2b1 | 6 | completed | b7e7 | -33 | 7977 | 5 | 4 | `b7e7 b1e1 b9c7 b0c2 a9b9 g3g4` |
| 4 | b2b1 | 8 | completed | b7e7 | -37 | 24428 | 20 | 4 | `b7e7 b1e1 b9c7 b0c2 a9b9 h2e2 h9g7 h0g2 g6g5` |
| 4 | b2b1 | 10 | completed | b7e7 | -37 | 53264 | 46 | 4 | `b7e7 b1e1 b9c7 b0c2 a9b9 h2e2 h9g7 h0g2 g6g5` |
| 4 | b2b1 | 12 | completed | b7e7 | -46 | 168125 | 155 | 4 | `b7e7 h2e2 b9c7 h0g2 a9b9 b1g1 h9i7 i0h0 h7g7 b0c2` |
| 4 | b2b3 | 4 | completed | g6g5 | -76 | 1641 | 2 | 4 | `g6g5` |
| 4 | b2b3 | 6 | completed | h7e7 | -58 | 9036 | 8 | 4 | `h7e7 h0i2 h9g7 c0e2 i9h9 i0h0 c6c5` |
| 4 | b2b3 | 8 | completed | g9e7 | -42 | 26925 | 22 | 4 | `g9e7 b0c2 c6c5 h0g2 b9c7` |
| 4 | b2b3 | 10 | completed | c6c5 | -47 | 54579 | 47 | 4 | `c6c5 h2c2 c9e7 h0g2 i9i8 i0h0 i8d8 c0e2 d8d4` |
| 4 | b2b3 | 12 | completed | c6c5 | -33 | 224177 | 205 | 4 | `c6c5 h2d2 g6g5 h0g2 h9i7 g0e2 h7g7 b0a2 i9h9 f0e1` |
| 4 | b2b4 | 4 | completed | g6g5 | -36 | 1281 | 1 | 4 | `g6g5` |
| 4 | b2b4 | 6 | completed | c6c5 | -24 | 10591 | 9 | 4 | `c6c5 b0c2 b9c7 h2e2 g6g5 b4i4` |
| 4 | b2b4 | 8 | completed | c6c5 | -20 | 25995 | 23 | 4 | `c6c5 h0i2 b9c7 b0c2 h9i7 h2e2 i6i5` |
| 4 | b2b4 | 10 | completed | c6c5 | -18 | 57349 | 51 | 4 | `c6c5 c0e2 g6g5 h0i2 b9c7 b0c2` |
| 4 | b2b4 | 12 | completed | c6c5 | -21 | 211702 | 196 | 4 | `c6c5 h2c2 h9g7 h0g2 i9h9 i0h0 b9c7` |
| 4 | b2b5 | 4 | completed | b7e7 | -123 | 3162 | 2 | 4 | `b7e7` |
| 4 | b2b5 | 6 | completed | h7e7 | -102 | 7005 | 5 | 4 | `h7e7 b0c2` |
| 4 | b2b5 | 8 | completed | b7e7 | -68 | 25567 | 21 | 4 | `b7e7 b0c2 c6c5 b5b8 i9i8 a0b0 a9a8 b8b7` |
| 4 | b2b5 | 10 | completed | c6c5 | -72 | 81575 | 74 | 4 | `c6c5 b0c2 b9c7 b5b4 g6g5 g0e2 c9e7 h0f1 h9g7` |
| 4 | b2b5 | 12 | completed | c6c5 | -68 | 183969 | 167 | 4 | `c6c5 b0c2 b9c7 b5b1 b7a7 b1c1 a9b9 c3c4 c5c4 c1c4` |
| 4 | b2b6 | 4 | completed | c6c5 | -72 | 1747 | 1 | 4 | `c6c5 b6g6` |
| 4 | b2b6 | 6 | completed | d9e8 | -30 | 4590 | 3 | 4 | `d9e8 b6e6 h7e7 e6e4` |
| 4 | b2b6 | 8 | completed | b9c7 | -23 | 15414 | 13 | 4 | `b9c7 c3c4 a9a8 b0c2 a8d8 h0i2 d8d5 b6b1 h9g7` |
| 4 | b2b6 | 10 | completed | b9c7 | -22 | 50897 | 47 | 4 | `b9c7 h2e2 c6c5 b0c2 h9g7 h0g2` |
| 4 | b2b6 | 12 | completed | b9c7 | -28 | 97611 | 89 | 4 | `b9c7 g3g4 a9a8 b0c2 a8d8 b6b4 c6c5` |
| 4 | b2b9 | 4 | completed | a9b9 | -69 | 2426 | 1 | 4 | `a9b9 b0c2 g6g5 a0b0` |
| 4 | b2b9 | 6 | completed | a9b9 | -53 | 4833 | 3 | 4 | `a9b9 b0c2 g6g5 a0b0 b9b8` |
| 4 | b2b9 | 8 | completed | a9b9 | -130 | 10016 | 6 | 4 | `a9b9 c3c4 b7e7 b0c2 b9b1` |
| 4 | b2b9 | 10 | completed | a9b9 | -118 | 26884 | 19 | 4 | `a9b9 b0c2 b7e7 h2e2 h9g7 h0g2 b9b3 i0h0 b3c3 a0a2` |
| 4 | b2b9 | 12 | completed | a9b9 | -118 | 43892 | 32 | 4 | `a9b9 b0c2 b7e7 h2e2 h9g7 h0g2 b9b3 i0h0 b3c3 a0a2` |
| 4 | b2c2 | 4 | completed | h7e7 | -78 | 3069 | 2 | 4 | `h7e7` |
| 4 | b2c2 | 6 | completed | h7e7 | -5 | 10713 | 8 | 4 | `h7e7 h0g2` |
| 4 | b2c2 | 8 | completed | h7e7 | -7 | 20187 | 15 | 4 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9a7` |
| 4 | b2c2 | 10 | completed | h7e7 | -14 | 67865 | 59 | 4 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9a7 a0b0 a9b9 b0b4` |
| 4 | b2c2 | 12 | completed | h7e7 | -14 | 134973 | 120 | 4 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9a7 a0b0 a9b9 b0b4` |
| 4 | b2d2 | 4 | completed | b9c7 | -2 | 2609 | 2 | 4 | `b9c7 c3c4 a9b9 h0g2` |
| 4 | b2d2 | 6 | completed | b7e7 | 22 | 9093 | 6 | 4 | `b7e7 h2e2 b9c7 h0g2 a9b9 b0c2` |
| 4 | b2d2 | 8 | completed | g6g5 | 20 | 25901 | 20 | 4 | `g6g5 b0c2 b9c7 a0b0 a9b9 h2e2 h9g7 h0g2 g7f5 i0h0` |
| 4 | b2d2 | 10 | completed | b9c7 | 24 | 55277 | 47 | 4 | `b9c7 b0c2 g6g5 a0b0 a9b9 c3c4 h9g7 g0e2 i9i8 f0e1` |
| 4 | b2d2 | 12 | completed | h7e7 | 10 | 140248 | 127 | 4 | `h7e7 h0g2 h9g7 b0c2 b9a7 a0b0 a9b9 i0h0` |
| 4 | b2e2 | 4 | completed | b9c7 | 8 | 1675 | 1 | 4 | `b9c7 b0c2` |
| 4 | b2e2 | 6 | completed | b9c7 | 27 | 6355 | 4 | 4 | `b9c7 b0c2 a9b9 h0g2 h9g7 g3g4 c6c5 a0b0` |
| 4 | b2e2 | 8 | completed | b9c7 | 27 | 18518 | 14 | 4 | `b9c7 b0c2 a9b9 a0b0 c6c5 h0g2` |
| 4 | b2e2 | 10 | completed | b9c7 | 31 | 52820 | 43 | 4 | `b9c7 b0c2 c6c5 a0b0 a9b9 b0b4 g9e7` |
| 4 | b2e2 | 12 | completed | b9c7 | 25 | 107590 | 93 | 4 | `b9c7 b0c2 a9b9 a0b0 c6c5 b0b6 h9g7 g3g4 b7a7 b6c6` |
| 4 | b2f2 | 4 | completed | a9a8 | -2 | 2950 | 2 | 4 | `a9a8 b0c2 a8f8 h0g2 f8f3` |
| 4 | b2f2 | 6 | completed | g6g5 | -1 | 12244 | 9 | 4 | `g6g5 b0c2 b9c7 h0i2 c6c5` |
| 4 | b2f2 | 8 | completed | g6g5 | 19 | 30293 | 23 | 4 | `g6g5 b0c2 b9c7 c3c4 a9b9 h0i2 h9g7 a0b0 i9i8 i3i4` |
| 4 | b2f2 | 10 | completed | b9c7 | 13 | 67826 | 55 | 4 | `b9c7 b0c2 a9b9 a0b0 g6g5 h0i2 h9g7 c3c4 i9i8 g0e2` |
| 4 | b2f2 | 12 | completed | c6c5 | 15 | 187374 | 160 | 4 | `c6c5 b0c2 b9c7 a0b0 a9b9 h0g2 g6g5 b0b4 b7a7 b4f4` |
| 4 | b2g2 | 4 | completed | c9e7 | -14 | 2811 | 2 | 4 | `c9e7 b0c2 b9d8 a0b0` |
| 4 | b2g2 | 6 | completed | c6c5 | -12 | 8792 | 6 | 4 | `c6c5 g3g4 b7d7 b0c2 b9c7 a0b0` |
| 4 | b2g2 | 8 | completed | g9e7 | -11 | 19320 | 16 | 4 | `g9e7 i3i4 a9a8 b0c2 a8f8` |
| 4 | b2g2 | 10 | completed | c6c5 | -21 | 40922 | 34 | 4 | `c6c5 b0c2 b9c7 a0b0 a9b9 g3g4 h9i7 b0b6` |
| 4 | b2g2 | 12 | completed | c6c5 | -19 | 185676 | 168 | 4 | `c6c5 g2c2 h7e7 h2e2 h9g7 b0a2 b9a7` |
| 4 | c0a2 | 4 | completed | b7e7 | -128 | 2731 | 2 | 4 | `b7e7` |
| 4 | c0a2 | 6 | completed | h7e7 | -48 | 10111 | 7 | 4 | `h7e7 h2e2 h9g7 h0g2 i9h9 g3g4` |
| 4 | c0a2 | 8 | completed | h9g7 | -45 | 24658 | 20 | 4 | `h9g7 g3g4 b7e7 b2e2 h7i7 h0g2` |
| 4 | c0a2 | 10 | completed | b7e7 | -56 | 59705 | 49 | 4 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9g7` |
| 4 | c0a2 | 12 | completed | b7e7 | -55 | 152289 | 136 | 4 | `b7e7 b2e2 b9c7 b0c2 a9b9 h2f2 g6g5 h0i2 h9g7 i0h0` |
| 4 | c0e2 | 4 | completed | b9c7 | -1 | 1844 | 1 | 4 | `b9c7 c3c4 g6g5 b0c2` |
| 4 | c0e2 | 6 | completed | h7f7 | 6 | 8189 | 6 | 4 | `h7f7 c3c4 h9g7 b0c2 i9h9 h2g2 h9h1` |
| 4 | c0e2 | 8 | completed | c6c5 | 16 | 27745 | 22 | 4 | `c6c5 g3g4 h9i7 h0g2 b9c7 b0d1` |
| 4 | c0e2 | 10 | completed | b7d7 | 19 | 73487 | 61 | 4 | `b7d7 h2f2 g6g5 h0g2 h9g7 i0h0 b9c7 h0h4 a9b9 b0a2` |
| 4 | c0e2 | 12 | completed | c6c5 | 21 | 143173 | 122 | 4 | `c6c5 b0d1 c9e7 a0c0 h9i7 c3c4 c5c4 c0c4 i9i8 h0g2` |
| 4 | c3c4 | 4 | completed | h7e7 | 11 | 2757 | 2 | 4 | `h7e7 b0c2 g6g5 a3a4` |
| 4 | c3c4 | 6 | completed | g6g5 | 23 | 6457 | 5 | 4 | `g6g5 b0c2 h9g7 h2e2 i9h9` |
| 4 | c3c4 | 8 | completed | g6g5 | 18 | 18766 | 15 | 4 | `g6g5 h0i2 h9g7 i0i1 h7i7 b0c2` |
| 4 | c3c4 | 10 | completed | b7c7 | 17 | 49647 | 41 | 4 | `b7c7 c0e2 b9a7 b0c2 a9b9 c2d4 h7e7 d4e6` |
| 4 | c3c4 | 12 | completed | b7c7 | 19 | 159571 | 142 | 4 | `b7c7 b2e2 h7e7 b0c2 h9g7 h0g2 c6c5 c2d4 c5c4 d4e6` |
| 4 | d0e1 | 4 | completed | c6c5 | -17 | 1590 | 1 | 4 | `c6c5 h0i2` |
| 4 | d0e1 | 6 | completed | c6c5 | -18 | 8147 | 6 | 4 | `c6c5 b2e2 b9c7 b0c2 a9b9` |
| 4 | d0e1 | 8 | completed | b9c7 | -8 | 26570 | 22 | 4 | `b9c7 c3c4 b7a7 b2d2 a9b9 b0c2` |
| 4 | d0e1 | 10 | completed | c6c5 | -4 | 52952 | 45 | 4 | `c6c5 h0i2 b9c7 c0e2 h9g7 h2g2 c7d5` |
| 4 | d0e1 | 12 | completed | b9c7 | -6 | 106999 | 92 | 4 | `b9c7 c3c4 b7a7 b0c2 a9b9 a0b0 g6g5 b2b6 h9g7 h2h6` |
| 4 | e0e1 | 4 | completed | b7e7 | -177 | 2180 | 1 | 4 | `b7e7 b0c2 b9c7 h0i2` |
| 4 | e0e1 | 6 | completed | h7e7 | -118 | 9153 | 6 | 4 | `h7e7 h0g2 h9g7` |
| 4 | e0e1 | 8 | completed | h9g7 | -100 | 22858 | 17 | 4 | `h9g7 b0c2 b7e7 e1e0 b9c7 a0b0 a9b9 g3g4` |
| 4 | e0e1 | 10 | completed | h7e7 | -101 | 59585 | 50 | 4 | `h7e7 h0g2 h9g7 g3g4 i9h9 i0h0 b9c7 e1e0 h9h3` |
| 4 | e0e1 | 12 | completed | h7e7 | -102 | 141860 | 123 | 4 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0c2 c6c5 b2a2 b9c7 a0b0` |
| 4 | e3e4 | 4 | completed | b7e7 | -137 | 3422 | 3 | 4 | `b7e7 c0e2 b9c7 b0d1 e7e4 d1e3` |
| 4 | e3e4 | 6 | completed | h7e7 | -98 | 10463 | 7 | 4 | `h7e7 f0e1 h9g7 h2e2 i9h9` |
| 4 | e3e4 | 8 | completed | b7e7 | -93 | 28907 | 21 | 4 | `b7e7 b2e2 e7e4 d0e1 h7e7 h0g2 h9g7 h2h6 b9c7` |
| 4 | e3e4 | 10 | completed | h7e7 | -95 | 70103 | 57 | 4 | `h7e7 h2e2 e7e4 f0e1 b7e7 h0g2` |
| 4 | e3e4 | 12 | completed | b7e7 | -93 | 172879 | 147 | 4 | `b7e7 b2e2 e7e4 f0e1 h7e7 h0g2 h9g7 i0h0 i9h9 h2h6` |
| 4 | f0e1 | 4 | completed | b9c7 | -75 | 1754 | 1 | 4 | `b9c7` |
| 4 | f0e1 | 6 | completed | c6c5 | -11 | 9108 | 7 | 4 | `c6c5 b0a2 g6g5 h0i2 h9g7` |
| 4 | f0e1 | 8 | completed | h7e7 | -7 | 20801 | 16 | 4 | `h7e7 g0e2 h9g7 h0g2 i9h9 i0h0 h9h3 c3c4` |
| 4 | f0e1 | 10 | completed | g6g5 | -12 | 47568 | 38 | 4 | `g6g5 c3c4 b7c7 b0c2 c6c5 c2d4 c5c4 d4e6 g9e7 g0e2` |
| 4 | f0e1 | 12 | completed | h7i7 | -9 | 107631 | 90 | 4 | `h7i7 c3c4 h9g7 g0e2 b7c7 b0c2 g6g5 h0f1 b9a7 g3g4` |
| 4 | g0e2 | 4 | completed | h7f7 | 2 | 3153 | 2 | 4 | `h7f7 g3g4 h9g7 b2d2` |
| 4 | g0e2 | 6 | completed | c6c5 | 18 | 11359 | 8 | 4 | `c6c5 h0f1 b9c7` |
| 4 | g0e2 | 8 | completed | b7d7 | 24 | 30171 | 23 | 4 | `b7d7 c3c4 b9a7 b0c2 a9b9 a0b0 g6g5 h0f1 b9b5 b2a2` |
| 4 | g0e2 | 10 | completed | g6g5 | 19 | 62603 | 51 | 4 | `g6g5 b0c2 b9a7 b2a2 a9b9 a0b0 h9g7 h0f1` |
| 4 | g0e2 | 12 | completed | g6g5 | 21 | 135472 | 114 | 4 | `g6g5 b0c2 g9e7 b2a2 b9a7 a0b0 b7c7 c3c4 h9g7 c2d4` |
| 4 | g0i2 | 4 | completed | b9c7 | -55 | 2853 | 2 | 4 | `b9c7 b0c2 h7e7` |
| 4 | g0i2 | 6 | completed | c6c5 | -50 | 6012 | 5 | 4 | `c6c5 b2e2 b9c7 g3g4 a9b9 b0c2` |
| 4 | g0i2 | 8 | completed | h7e7 | -47 | 20735 | 16 | 4 | `h7e7 b2e2 h9g7 b0c2 i9h9 a0b0 h9h2 b0b7` |
| 4 | g0i2 | 10 | completed | h7e7 | -50 | 41345 | 34 | 4 | `h7e7 b2e2 h9g7 b0c2 b9a7 a0b0 b7c7 h0f1` |
| 4 | g0i2 | 12 | completed | b9c7 | -55 | 142605 | 127 | 4 | `b9c7 c3c4 h7e7 h0g2 h9g7 i0h0 i9h9 h2h6 g6g5 b2e2` |
| 4 | g3g4 | 4 | completed | b7e7 | 14 | 3018 | 2 | 4 | `b7e7 h0g2 b9c7 b0c2` |
| 4 | g3g4 | 6 | completed | c6c5 | 27 | 9309 | 7 | 4 | `c6c5 c0e2 h9i7 h0g2 b9c7 c3c4 c5c4` |
| 4 | g3g4 | 8 | completed | c6c5 | 29 | 22660 | 19 | 4 | `c6c5 h0g2 b9c7 b2e2 g9e7 b0c2 a9b9 a0b0 h9f8 b0b4` |
| 4 | g3g4 | 10 | completed | h7g7 | 22 | 52146 | 47 | 4 | `h7g7 b2e2 b7e7 b0c2 b9c7 a0b0 h9i7 h2f2 i9h9` |
| 4 | g3g4 | 12 | completed | h7g7 | 17 | 164366 | 148 | 4 | `h7g7 b2e2 c9e7 h0i2 h9i7 i0h0 i9h9 h2h6 b9d8 b0c2` |
| 4 | h0g2 | 4 | completed | c6c5 | -20 | 1875 | 1 | 4 | `c6c5` |
| 4 | h0g2 | 6 | completed | b7a7 | 22 | 7912 | 5 | 4 | `b7a7 b0c2 c6c5 g3g4 b9c7` |
| 4 | h0g2 | 8 | completed | g6g5 | 23 | 19359 | 15 | 4 | `g6g5 b2e2 h9g7 b0c2 b9c7 a0b0 a9b9` |
| 4 | h0g2 | 10 | completed | b7e7 | 26 | 44746 | 38 | 4 | `b7e7 h2i2 b9c7 i0h0 h9g7 b0c2` |
| 4 | h0g2 | 12 | completed | g6g5 | 16 | 109225 | 97 | 4 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 h9g7 b0b4` |
| 4 | h0i2 | 4 | completed | b7e7 | -11 | 2724 | 2 | 4 | `b7e7 b0c2 b9c7 a0b0` |
| 4 | h0i2 | 6 | completed | b7e7 | 3 | 11371 | 8 | 4 | `b7e7 b0c2 b9c7 a0b0 a9b9 b2b6` |
| 4 | h0i2 | 8 | completed | c6c5 | 17 | 28928 | 22 | 4 | `c6c5 b2e2 b9c7 h2g2 h9g7 i0h0 i9h9 b0c2 c7d5` |
| 4 | h0i2 | 10 | completed | b7e7 | 13 | 71115 | 59 | 4 | `b7e7 b0c2 c6c5 h2g2` |
| 4 | h0i2 | 12 | completed | b7e7 | -2 | 145822 | 127 | 4 | `b7e7 b0c2 b9c7 c3c4 a9b9 a0b0 b9b5 c0e2 h9g7 i0i1` |
| 4 | h2c2 | 4 | completed | b7e7 | -75 | 2634 | 2 | 4 | `b7e7` |
| 4 | h2c2 | 6 | completed | g6g5 | -21 | 10259 | 8 | 4 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4` |
| 4 | h2c2 | 8 | completed | g6g5 | -20 | 22838 | 18 | 4 | `g6g5 c0e2 h9g7 h0g2 h7h3` |
| 4 | h2c2 | 10 | completed | h9i7 | -22 | 75072 | 65 | 4 | `h9i7 c2e2 b7e7 e2e6 d9e8 b2e2 b9c7` |
| 4 | h2c2 | 12 | completed | c9e7 | -21 | 184977 | 163 | 4 | `c9e7 h0g2 i9i8 c2e2 i8d8 f0e1 d8d1 b0a2 d9e8` |
| 4 | h2d2 | 4 | completed | c6c5 | -13 | 3194 | 2 | 4 | `c6c5 h0g2 g6g5 i0h0` |
| 4 | h2d2 | 6 | completed | c6c5 | 23 | 16169 | 12 | 4 | `c6c5 h0g2 h7f7` |
| 4 | h2d2 | 8 | completed | h9g7 | 14 | 32698 | 26 | 4 | `h9g7 h0g2 i9h9 i0h0 g6g5 c3c4` |
| 4 | h2d2 | 10 | completed | g6g5 | 20 | 64358 | 54 | 4 | `g6g5 c0e2 h9g7 h0g2 i9h9 i0h0` |
| 4 | h2d2 | 12 | completed | h9g7 | 14 | 151133 | 133 | 4 | `h9g7 h0g2 i9h9 i0h0 h7h3 g3g4 h3g3 b0c2 h9h0 g2h0` |
| 4 | h2e2 | 4 | completed | h9g7 | 33 | 1770 | 1 | 4 | `h9g7 h0g2 i9h9` |
| 4 | h2e2 | 6 | completed | b9c7 | 40 | 3576 | 2 | 4 | `b9c7 b0c2 h7e7 h0g2 h9g7 i0h0` |
| 4 | h2e2 | 8 | completed | h9g7 | 33 | 10950 | 9 | 4 | `h9g7 c3c4 c9e7 h0g2 g6g5 i0h0` |
| 4 | h2e2 | 10 | completed | h9g7 | 27 | 46219 | 38 | 4 | `h9g7 g3g4 c6c5 h0g2 i9h9 i0h0 b9c7 b0a2 h7h3 b2d2` |
| 4 | h2e2 | 12 | completed | h9g7 | 27 | 120480 | 108 | 4 | `h9g7 g3g4 i9h9 h0g2 c6c5 i0h0 b9c7 b0a2 a9a8 c3c4` |
| 4 | h2f2 | 4 | completed | h9g7 | 2 | 2875 | 2 | 4 | `h9g7 h0g2 i9h9 c3c4` |
| 4 | h2f2 | 6 | completed | g6g5 | 16 | 9647 | 6 | 4 | `g6g5 b0c2 h9g7` |
| 4 | h2f2 | 8 | completed | b7e7 | 23 | 27067 | 21 | 4 | `b7e7 b0c2 b9c7 h0g2 h9i7 i0h0` |
| 4 | h2f2 | 10 | completed | g6g5 | 17 | 59236 | 50 | 4 | `g6g5 h0g2 h9g7 i0h0 i9h9 b2e2 b9c7 b0c2 c6c5 a0b0` |
| 4 | h2f2 | 12 | completed | b7e7 | 16 | 171603 | 152 | 4 | `b7e7 b0c2 b9c7 h0g2 h9i7 i0h0 i9h9 a0b0 a9b9 b2b6` |
| 4 | h2g2 | 4 | completed | c6c5 | -20 | 3906 | 2 | 4 | `c6c5 b2e2 b9c7 b0c2 a9b9` |
| 4 | h2g2 | 6 | completed | b7e7 | -16 | 7893 | 5 | 4 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0` |
| 4 | h2g2 | 8 | completed | b7e7 | -16 | 15149 | 11 | 4 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0` |
| 4 | h2g2 | 10 | completed | b7e7 | -15 | 48404 | 41 | 4 | `b7e7 b0c2 b9c7 a0b0 c6c5` |
| 4 | h2g2 | 12 | completed | b7e7 | -20 | 104702 | 92 | 4 | `b7e7 b0c2 b9c7 h0i2 h7h2 c0e2 h9i7 i0h0 i9h9 c3c4` |
| 4 | h2h1 | 4 | completed | b7e7 | -35 | 2922 | 2 | 4 | `b7e7 b0c2` |
| 4 | h2h1 | 6 | completed | h7e7 | -32 | 7170 | 6 | 4 | `h7e7 h1e1 h9g7 c3c4` |
| 4 | h2h1 | 8 | completed | h7e7 | -39 | 28023 | 24 | 4 | `h7e7 b0c2 h9g7 h1e1 i9h9 h0g2` |
| 4 | h2h1 | 10 | completed | h7e7 | -38 | 79180 | 72 | 4 | `h7e7 b0c2 c6c5 h1c1 i9i8 c0e2 i8d8` |
| 4 | h2h1 | 12 | completed | h7e7 | -42 | 212211 | 202 | 4 | `h7e7 h1e1 h9g7 h0g2 i9h9 g3g4 c6c5 b2e2 b9c7 b0c2` |
| 4 | h2h3 | 4 | completed | g6g5 | -65 | 2034 | 2 | 4 | `g6g5 c3c4` |
| 4 | h2h3 | 6 | completed | b7e7 | -53 | 10806 | 9 | 4 | `b7e7 b0a2` |
| 4 | h2h3 | 8 | completed | b7d7 | -46 | 41298 | 36 | 4 | `b7d7 b0a2 g6g5 a0b0 b9c7 b2d2 h9g7 h0g2` |
| 4 | h2h3 | 10 | completed | g6g5 | -44 | 76928 | 67 | 4 | `g6g5 b2e2 b9c7 b0c2 c6c5` |
| 4 | h2h3 | 12 | completed | g6g5 | -43 | 174555 | 156 | 4 | `g6g5 b2e2 h9g7 b0c2 b9a7 a0b0 a9b9 h0i2 b7c7 b0b9` |
| 4 | h2h4 | 4 | completed | i6i5 | -42 | 2032 | 2 | 4 | `i6i5 b2g2` |
| 4 | h2h4 | 6 | completed | h9g7 | -17 | 6880 | 7 | 4 | `h9g7 h0g2 b9a7 h4e4 g9e7 i0h0 i9h9` |
| 4 | h2h4 | 8 | completed | g6g5 | -15 | 26969 | 24 | 4 | `g6g5 h4i4 h9i7 h0g2 i6i5 i0h0 i9h9 i4a4` |
| 4 | h2h4 | 10 | completed | g6g5 | -21 | 69486 | 64 | 4 | `g6g5 b2e2 h9g7 b0c2 c6c5 a0b0 b9a7` |
| 4 | h2h4 | 12 | completed | g6g5 | -22 | 172908 | 160 | 4 | `g6g5 b2e2 h9g7 b0c2 b9a7 a0b0 a9b9 h0g2 c6c5 e3e4` |
| 4 | h2h5 | 4 | completed | b7e7 | -83 | 2200 | 2 | 4 | `b7e7 b0c2 g6g5 c3c4` |
| 4 | h2h5 | 6 | completed | g6g5 | -71 | 4815 | 4 | 4 | `g6g5 h0g2 h9g7 h5h4 b7e7` |
| 4 | h2h5 | 8 | completed | b7e7 | -60 | 23121 | 20 | 4 | `b7e7 b0c2 b9c7 c3c4 g6g5 h0g2 a9b9 a0b0 h9g7` |
| 4 | h2h5 | 10 | completed | g6g5 | -62 | 59639 | 53 | 4 | `g6g5 h0g2 h9g7 h5h1 i9i8 c3c4 g7f5 b0c2 c9e7 h1e1` |
| 4 | h2h5 | 12 | completed | g6g5 | -66 | 146851 | 134 | 4 | `g6g5 h0g2 h9g7 h5h1 b7e7 c3c4 g7f5 b0c2 b9c7 b2b4` |
| 4 | h2h6 | 4 | completed | b9c7 | -16 | 2060 | 1 | 4 | `b9c7` |
| 4 | h2h6 | 6 | completed | h9g7 | -32 | 5413 | 3 | 4 | `h9g7 b2e2 c6c5 b0c2 b9c7` |
| 4 | h2h6 | 8 | completed | h9g7 | -32 | 14887 | 12 | 4 | `h9g7 b2e2 b9c7 b0c2 g6g5` |
| 4 | h2h6 | 10 | completed | b9c7 | -31 | 39796 | 34 | 4 | `b9c7 b0a2 b7a7 b2c2 a9b9 a0b0 b9b0 a2b0 a7a3` |
| 4 | h2h6 | 12 | completed | h9g7 | -25 | 116081 | 104 | 4 | `h9g7 h0g2 i9i8 b0c2 i8d8 g3g4 b9c7 c3c4` |
| 4 | h2h9 | 4 | completed | i9h9 | -126 | 2261 | 1 | 4 | `i9h9 h0g2` |
| 4 | h2h9 | 6 | completed | i9h9 | -135 | 4912 | 3 | 4 | `i9h9 h0g2 h7e7 g3g4 b9c7` |
| 4 | h2h9 | 8 | completed | i9h9 | -118 | 14651 | 11 | 4 | `i9h9 h0g2 h7e7 c3c4 h9h5 b0c2` |
| 4 | h2h9 | 10 | completed | i9h9 | -130 | 26177 | 19 | 4 | `i9h9 h0g2 h7e7 b0c2 c6c5 i0i1` |
| 4 | h2h9 | 12 | completed | i9h9 | -114 | 75243 | 61 | 4 | `i9h9 h0g2 h7e7 b2d2 h9h1 d0e1 b9c7 b0c2 a9b9` |
| 4 | h2i2 | 4 | completed | g6g5 | 4 | 2674 | 2 | 4 | `g6g5 h0g2 h9g7` |
| 4 | h2i2 | 6 | completed | g6g5 | 7 | 8870 | 6 | 4 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4` |
| 4 | h2i2 | 8 | completed | h9g7 | 15 | 20043 | 16 | 4 | `h9g7 h0g2 i9h9 i0h0 g6g5 c3c4 h7h3 b0c2 b9c7 c2d4` |
| 4 | h2i2 | 10 | completed | h9g7 | 12 | 39986 | 33 | 4 | `h9g7 h0g2 i9h9 i0h0 g6g5 c3c4 h7h3 b0c2 c9e7 a0a1` |
| 4 | h2i2 | 12 | completed | h9g7 | 11 | 79452 | 66 | 4 | `h9g7 h0g2 i9h9 i0h0 g6g5 b2e2 h7h3 b0c2 b9a7 a0b0` |
| 4 | i0i1 | 4 | completed | h7h0 | -118 | 2521 | 2 | 4 | `h7h0 h2e2` |
| 4 | i0i1 | 6 | completed | h7h0 | -82 | 8166 | 5 | 4 | `h7h0` |
| 4 | i0i1 | 8 | completed | h7h0 | -125 | 20757 | 16 | 4 | `h7h0 h2e2 b9c7 i1h1 h0i0 h1h0 i0i1 a0a1 b7b0 a1i1` |
| 4 | i0i1 | 10 | completed | h7h0 | -81 | 44891 | 34 | 4 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0g0 h0g0 i9h9 b0c2` |
| 4 | i0i1 | 12 | completed | h7h0 | -83 | 77246 | 62 | 4 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0g0 h0g0 b7e7 b0c2` |
| 4 | i0i2 | 4 | completed | h7h0 | -176 | 2109 | 1 | 4 | `h7h0 c3c4` |
| 4 | i0i2 | 6 | completed | h7h0 | -94 | 6710 | 4 | 4 | `h7h0 h2e2 h9g7 i2h2 h0i0 h2h0` |
| 4 | i0i2 | 8 | completed | h7h0 | -55 | 27491 | 21 | 4 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b9c7 a0a1 b7b5 h2h0` |
| 4 | i0i2 | 10 | completed | h7h0 | -75 | 42057 | 32 | 4 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b9c7 a0a1 b7b5 h2h0` |
| 4 | i0i2 | 12 | completed | h7h0 | -66 | 113725 | 94 | 4 | `h7h0 h2e2 b7e7 i2h2 h0i0 h2h8 b9c7 b0c2 a9b9 a0a1` |
| 4 | i3i4 | 4 | completed | g6g5 | -27 | 1635 | 1 | 4 | `g6g5 b0c2 h9g7` |
| 4 | i3i4 | 6 | completed | c6c5 | -13 | 5598 | 4 | 4 | `c6c5 g3g4 b9c7 h0g2 h7e7 b0c2` |
| 4 | i3i4 | 8 | completed | h9g7 | -13 | 22256 | 19 | 4 | `h9g7 g3g4 h7i7 h0i2 i9h9 i0h0 c6c5` |
| 4 | i3i4 | 10 | completed | b7e7 | -9 | 47427 | 42 | 4 | `b7e7 b0c2 b9c7 a0b0 a9b9 g3g4 c6c5 h0g2 h9g7 c0e2` |
| 4 | i3i4 | 12 | completed | h9g7 | -10 | 138608 | 129 | 4 | `h9g7 g3g4 h7i7 h0i2 i9h9 i0h0 b7e7 b2e2 b9c7 b0c2` |
