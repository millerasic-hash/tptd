# Pikafish Opening Probe Report

This is a reproducible opening probe, not a game-theoretic proof.

## Configuration

- Start FEN: `rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1`.
- Red opening moves: `44`.
- Depths: `12, 18, 24, 30`.
- MultiPV: `4`.
- Threads: `1`.
- Hash: `128 MB`.
- Clear hash per query: `True`.
- UCI_ShowWDL: `True`.
- Single-pass collection: `True`.
- Go depth per red move: `30`.
- Per-query max seconds: `60.0`.
- Runtime seconds: `1825.079`.

Scores are normalized to Red's point of view. After a red opening move, the side to move is Black, so a negative engine score becomes a positive Red score.

## Depth Summary

| Depth | Positions | Completed | Max seconds | Red score min | Red score median | Red score avg | Red score max |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 12 | 44 | 44 | 0 | -118 | -19.5 | -24.5 | 27 |
| 18 | 44 | 44 | 0 | -119 | -15.5 | -23.86 | 26 |
| 24 | 44 | 44 | 0 | -120 | -14.5 | -25.34 | 17 |
| 30 | 44 | 40 | 4 | -125 | -11.0 | -24.98 | 22 |

## Depth 30 Top Red Moves

| Rank | Red move | Black best reply | Red score | Nodes | Hashfull | PV repeat | PV third-repeat |
|---:|:---|:---|---:|---:|---:|:---:|:---:|
| 1 | c3c4 | g6g5 | 22 | 36302818 | 947 | False | False |
| 2 | b2e2 | h9g7 | 20 | 43435739 | 973 | False | False |
| 3 | h2e2 | h9g7 | 20 | 46741045 | 982 | False | False |
| 4 | g3g4 | c6c5 | 18 | 49119503 | 991 | False | False |
| 5 | b0c2 | c6c5 | 17 | 34979640 | 958 | False | False |
| 6 | c0e2 | c9e7 | 15 | 40013848 | 973 | False | False |
| 7 | g0e2 | g6g5 | 15 | 46178007 | 986 | False | False |
| 8 | h2f2 | b7e7 | 14 | 27935824 | 881 | False | False |
| 9 | h2d2 | h9g7 | 12 | 37304894 | 963 | False | False |
| 10 | h0g2 | g6g5 | 10 | 44365299 | 982 | False | False |

## Depth 30 Bottom Red Moves

| Rank | Red move | Black best reply | Red score | Nodes | Hashfull | PV repeat | PV third-repeat |
|---:|:---|:---|---:|---:|---:|:---:|:---:|
| 1 | b2b5 | c6c5 | -61 | 51253962 | 990 | False | False |
| 2 | i0i2 | h7h0 | -62 | 37460080 | 948 | False | False |
| 3 | h2h5 | g6g5 | -66 | 60325183 | 997 | False | False |
| 4 | a0a2 | b7b0 | -67 | 42263088 | 975 | False | False |
| 5 | i0i1 | h7h0 | -82 | 40248373 | 968 | False | False |
| 6 | a0a1 | b7b0 | -83 | 37177859 | 953 | False | False |
| 7 | e3e4 | b7e7 | -91 | 53481387 | 992 | False | False |
| 8 | e0e1 | h7e7 | -103 | 59472533 | 996 | False | False |
| 9 | b2b9 | a9b9 | -120 | 41810478 | 973 | False | False |
| 10 | h2h9 | i9h9 | -125 | 39441843 | 970 | False | False |

## Full Depth Rows

| Red move | Depth | Stop | Best reply | Top red score | Top engine score | Seldepth | Nodes | Time ms | WDL | Top PV |
|:---|---:|:---|:---|---:|:---|---:|---:|---:|:---|:---|
| a0a1 | 12 | completed | b7b0 | -67 | cp 67 | 22 | 89257 | 93 | 241/756/3 | `b7b0 b2e2 h7e7 a1b1 b0a0 e2e6 d9e8 e6e4 h9g7 h2e2 i9h9 b1b0` |
| a0a1 | 18 | completed | b7b0 | -56 | cp 56 | 32 | 1699377 | 1712 | 177/819/4 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0c0 b0c0 h7e7 h0g2 h9g7 i0h0` |
| a0a1 | 24 | completed | b7b0 | -73 | cp 73 | 41 | 9994939 | 10308 | 278/720/2 | `b7b0 b2e2 b9c7 a1b1 b0a0 h2h4 g6g5 h0g2 d9e8 h4c4 h9g7 b1b0` |
| a0a1 | 30 | completed | b7b0 | -83 | cp 83 | 56 | 37177859 | 41084 | 353/645/2 | `b7b0 b2e2 b9c7 a1b1 b0a0 b1b0 a0a1 h2h4 a1h1 h4a4 c9a7 b0b5` |
| a0a2 | 12 | completed | b7b0 | -65 | cp 65 | 20 | 173546 | 180 | 226/771/3 | `b7b0 b2e2 h7e7 a2b2 b0a0 h0g2 h9g7 i0i1 i9h9 i1a1 b9c7 a1a0` |
| a0a2 | 18 | completed | b7b0 | -52 | cp 52 | 35 | 1470358 | 1625 | 154/841/5 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 h9g7 i0i1 h7h5 b2b0 a0c0 b0c0` |
| a0a2 | 24 | completed | b7b0 | -58 | cp 58 | 45 | 9325204 | 10150 | 184/812/4 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 g6g5 b2b0 a0c0 b0c0 a9b9 c3c4` |
| a0a2 | 30 | completed | b7b0 | -67 | cp 67 | 55 | 42263088 | 46048 | 241/756/3 | `b7b0 b2e2 b9c7 a2b2 b0a0 h0g2 g6g5 b2b0 a0c0 b0c0 a9b9 c3c4` |
| a3a4 | 12 | completed | b9c7 | -9 | cp 9 | 22 | 149516 | 147 | 39/939/22 | `b9c7 c3c4 b7a7 b0a2 h7e7 a2b4 e7e3 h0g2` |
| a3a4 | 18 | completed | h7e7 | -10 | cp 10 | 27 | 1822059 | 1830 | 40/939/21 | `h7e7 h0g2 h9g7 i0h0 i9h9 g3g4 h9h3 c3c4 b9c7 b0c2 a9a8 b2b3` |
| a3a4 | 24 | completed | g6g5 | -13 | cp 13 | 28 | 9896027 | 10557 | 45/936/19 | `g6g5 h2g2 h7e7 b2e2 h9g7 b0c2 b7d7 c3c4 b9c7 h0i2 i9h9 i0h0` |
| a3a4 | 30 | completed | g6g5 | -10 | cp 10 | 44 | 49677988 | 57206 | 40/939/21 | `g6g5 h2g2 h7e7 b2e2 h9g7 b0c2 b7d7 a0b0 b9c7 b0b5 i9h9 h0i2` |
| b0a2 | 12 | completed | h7e7 | 3 | cp -3 | 16 | 137701 | 133 | 26/942/32 | `h7e7 h0g2 g6g5 i0h0 h9g7 b2d2 b7b2 d2d7 b2h2 h0h2 i9h9 h2h9` |
| b0a2 | 18 | completed | h7e7 | -12 | cp 12 | 29 | 1323297 | 1339 | 43/937/20 | `h7e7 h0g2 h9g7 i0h0 i9h9 a3a4 c6c5 b2c2 b9c7 a0b0 b7a7 c3c4` |
| b0a2 | 24 | completed | h7e7 | 0 | cp 0 | 35 | 7511771 | 7703 | 29/942/29 | `h7e7 h0g2 h9g7 i0h0 i9h9 h2h6 g6g5 a0a1 b9c7 a1h1 g7f5 h6h7` |
| b0a2 | 30 | completed | h7e7 | 0 | cp 0 | 15 | 32851186 | 35958 | 29/942/29 | `h7e7 h0g2 h9g7 i0h0 i9h9 h2h6 g6g5 a0a1 b9c7 a1h1 g7f5 h6h7` |
| b0c2 | 12 | completed | c6c5 | 16 | cp -16 | 17 | 169685 | 201 | 17/933/50 | `c6c5 b2a2 b9c7 a0b0 a9b9 g3g4 b7b3 h0g2 h7g7 i0i1 h9i7 g2h4` |
| b0c2 | 18 | completed | c6c5 | 12 | cp -12 | 25 | 1316313 | 1489 | 20/937/43 | `c6c5 h2e2 h9g7 h0g2 b9c7 e3e4 i9h9 e4e5 d9e8 c2e3 e6e5 e2e5` |
| b0c2 | 24 | completed | c6c5 | 11 | cp -11 | 44 | 9435267 | 10258 | 20/938/42 | `c6c5 h2e2 h9g7 h0g2 i9h9 i0h0 h7h3 g3g4 b9c7 g2f4 a9a8 g4g5` |
| b0c2 | 30 | completed | c6c5 | 17 | cp -17 | 40 | 34979640 | 41300 | 16/933/51 | `c6c5 h2e2 h9g7 h0g2 i9h9 i0h0 b9c7 g3g4 h7h3 g2f4 g9e7 g4g5` |
| b2a2 | 12 | completed | b9c7 | 13 | cp -13 | 17 | 87828 | 82 | 19/936/45 | `b9c7 b0c2 c6c5 a0b0 a9b9 g3g4 b7b3 h2h4 h7g7 h0g2 h9i7 c3c4` |
| b2a2 | 18 | completed | b9c7 | 7 | cp -7 | 32 | 1050469 | 1328 | 23/940/37 | `b9c7 b0c2 c6c5 a0b0 a9b9 g3g4 b7b3 h0g2 h9i7 h2h4 g9e7 i3i4` |
| b2a2 | 24 | completed | c6c5 | 0 | cp 0 | 46 | 5728762 | 6396 | 29/942/29 | `c6c5 b0c2 b9c7 a0b0 a9b9 g3g4 b7b3 h0g2 h9i7 h2i2 h7h3 c0e2` |
| b2a2 | 30 | completed | c6c5 | 0 | cp 0 | 42 | 28159330 | 32115 | 29/942/29 | `c6c5 b0c2 b9c7 a0b0 a9b9 g3g4 b7b3 h0g2 h9i7 i0i1 h7g7 g2h4` |
| b2b1 | 12 | completed | b7e7 | -46 | cp 46 | 19 | 168125 | 201 | 132/862/6 | `b7e7 h2e2 b9c7 h0g2 a9b9 b1g1 h9i7 i0h0 h7g7 b0c2 g6g5 c3c4` |
| b2b1 | 18 | completed | b7e7 | -44 | cp 44 | 33 | 2108822 | 2261 | 121/873/6 | `b7e7 h0g2 b9c7 a0a2 h9g7 g3g4 i9i8 a2b2 a9a8 c3c4 a8f8 h2i2` |
| b2b1 | 24 | completed | b7e7 | -41 | cp 41 | 39 | 11931712 | 12921 | 111/882/7 | `b7e7 b1e1 b9c7 c3c4 g6g5 b0c2 a9b9 a0b0 b9b0 c2b0 h9g7 b0c2` |
| b2b1 | 30 | max_seconds | b7e7 | -39 | cp 39 | 42 | 51005760 | 58351 | 104/888/8 | `b7e7 h0g2 b9c7 a0a2 g6g5 a2b2 h9g7 h2h4 a9a8 h4c4 c7e8 i0h0` |
| b2b3 | 12 | completed | c6c5 | -33 | cp 33 | 19 | 224177 | 212 | 87/904/9 | `c6c5 h2d2 g6g5 h0g2 h9i7 g0e2 h7g7 b0a2 i9h9 f0e1 b9c7 i0f0` |
| b2b3 | 18 | completed | c6c5 | -36 | cp 36 | 34 | 1803065 | 1883 | 96/896/8 | `c6c5 h2d2 h9g7 h0g2 i9h9 i0h0 h7h3 g3g4 h3g3 b0a2 b9c7 g0e2` |
| b2b3 | 24 | completed | g6g5 | -43 | cp 43 | 32 | 10741548 | 11543 | 120/874/6 | `g6g5 h2e2 h9g7 h0g2 i9h9 c3c4 h7i7 b0c2 d9e8 c2d4 b9a7 b3b4` |
| b2b3 | 30 | max_seconds | c6c5 | -37 | cp 37 | 43 | 52241117 | 59699 | 97/895/8 | `c6c5 h2d2 g6g5 h0g2 h7f7 i0h0 h9g7 h0h4 i9h9 h4f4 b9c7 d0e1` |
| b2b4 | 12 | completed | c6c5 | -21 | cp 21 | 19 | 211702 | 265 | 59/927/14 | `c6c5 h2c2 h9g7 h0g2 i9h9 i0h0 b9c7` |
| b2b4 | 18 | completed | c6c5 | -22 | cp 22 | 31 | 1971840 | 2130 | 60/926/14 | `c6c5 b0c2 b9c7 h0i2 g6g5 h2g2 h9g7 i0h0 i9h9 c0e2 c7d5 g3g4` |
| b2b4 | 24 | completed | c6c5 | -20 | cp 20 | 42 | 9728874 | 10790 | 56/929/15 | `c6c5 b0c2 b9c7 h0i2 g6g5 h2g2 h9g7 i0h0 i9h9 a0a1 a9a8 b4e4` |
| b2b4 | 30 | completed | c6c5 | -26 | cp 26 | 43 | 40724556 | 46011 | 68/920/12 | `c6c5 b0c2 b9c7 h0i2 g6g5 h2g2 h9g7 i0h0 i9h9 c0e2 c7d5 g3g4` |
| b2b5 | 12 | completed | c6c5 | -68 | cp 68 | 18 | 183969 | 200 | 242/755/3 | `c6c5 b0c2 b9c7 b5b1 b7a7 b1c1 a9b9 c3c4 c5c4 c1c4 c7d5` |
| b2b5 | 18 | completed | c6c5 | -70 | cp 70 | 27 | 1871178 | 2035 | 257/740/3 | `c6c5 b0c2 b9c7 b5b1 a9a8 b1c1 c7b5 c0e2 g6g5 h2g2 g9e7 h0i2` |
| b2b5 | 24 | completed | c6c5 | -66 | cp 66 | 34 | 12234012 | 12391 | 234/763/3 | `c6c5 b0c2 b9c7 b5b4 g9e7 h2f2 c7d5 h0i2 h9g7 i0h0 i9h9 h0h4` |
| b2b5 | 30 | max_seconds | c6c5 | -61 | cp 61 | 52 | 51253962 | 58700 | 203/794/3 | `c6c5 b0c2 b9c7 b5b1 g6g5 b1g1 h9g7 a0b0 a9b9 b0b4 b7a7 b4b9` |
| b2b6 | 12 | completed | b9c7 | -28 | cp 28 | 14 | 97611 | 92 | 74/915/11 | `b9c7 g3g4 a9a8 b0c2 a8d8 b6b4 c6c5` |
| b2b6 | 18 | completed | b9c7 | -28 | cp 28 | 25 | 1513128 | 1679 | 74/915/11 | `b9c7 b0c2 g6g5 c3c4 h9g7 h0i2 a9a8 h2h6 e6e5 h6h2 a8d8 h2e2` |
| b2b6 | 24 | completed | c6c5 | -24 | cp 24 | 40 | 7705115 | 9177 | 64/923/13 | `c6c5 h2e2 g9e7 b0c2 a6a5 h0g2 b9c7 i0h0 h9f8 b6b1 i9h9 b1f1` |
| b2b6 | 30 | completed | c6c5 | -22 | cp 22 | 46 | 32743252 | 38379 | 60/926/14 | `c6c5 h2e2 g9e7 b0c2 a6a5 h0g2 h9f8 b6b9 a9b9 a0b0 g6g5 i0h0` |
| b2b9 | 12 | completed | a9b9 | -118 | cp 118 | 15 | 43892 | 32 | 659/341/0 | `a9b9 b0c2 b7e7 h2e2 h9g7 h0g2 b9b3 i0h0 b3c3 a0a2 i9i8 h0h6` |
| b2b9 | 18 | completed | a9b9 | -119 | cp 119 | 28 | 1045030 | 923 | 667/333/0 | `a9b9 b0c2 b7e7 g3g4 h7g7 h0i2 h9i7 i0h0 i6i5 h2e2` |
| b2b9 | 24 | completed | a9b9 | -113 | cp 113 | 38 | 8882689 | 8164 | 618/382/0 | `a9b9 b0c2 b7e7 g0e2 h7f7 a0a1 h9i7 h2h6 e6e5 h0g2 i7g8 i0h0` |
| b2b9 | 30 | completed | a9b9 | -120 | cp 120 | 45 | 41810478 | 39790 | 677/323/0 | `a9b9 b0c2 b7e7 a0a1 h7h5 h0g2 b9b3 g3g4 b3c3 a1c1 h9g7 g0e2` |
| b2c2 | 12 | completed | h7e7 | -14 | cp 14 | 16 | 134973 | 119 | 46/936/18 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9a7 a0b0 a9b9 b0b4 a6a5 a3a4` |
| b2c2 | 18 | completed | h7e7 | -21 | cp 21 | 31 | 1537596 | 1466 | 59/927/14 | `h7e7 h2e2 h9g7 b0a2 b9a7 h0g2 i9h9 a0b0 a9b9 i0i1 h9h3 b0b4` |
| b2c2 | 24 | completed | h7e7 | -21 | cp 21 | 36 | 8256697 | 7906 | 58/928/14 | `h7e7 h2e2 h9g7 h0g2 i9h9 b0a2 b9a7 a0b0 a9b9 b0b6 h9h3 g3g4` |
| b2c2 | 30 | completed | h7e7 | -12 | cp 12 | 46 | 35135439 | 34748 | 44/937/19 | `h7e7 h2e2 h9g7 b0a2 b9a7 h0g2 i9h9 a0b0 a9b9 b0b4 a6a5 a3a4` |
| b2d2 | 12 | completed | h7e7 | 10 | cp -10 | 19 | 140248 | 125 | 21/938/41 | `h7e7 h0g2 h9g7 b0c2 b9a7 a0b0 a9b9 i0h0` |
| b2d2 | 18 | completed | h7e7 | 5 | cp -5 | 33 | 1387645 | 1289 | 24/941/35 | `h7e7 h2e2 h9g7 b0c2 b9a7 h0g2 i9h9 a0b0 a9b9 g3g4 c6c5 i0i1` |
| b2d2 | 24 | completed | h7e7 | 10 | cp -10 | 37 | 6632535 | 6298 | 21/938/41 | `h7e7 h0g2 h9g7 g3g4 i9h9 b0c2 b9a7 i0h0 h9h5 d0e1 a6a5 h2i2` |
| b2d2 | 30 | completed | h7e7 | 9 | cp -9 | 43 | 28704743 | 28184 | 21/940/39 | `h7e7 h0g2 h9g7 g3g4 i9h9 b0c2 b9a7 i0h0 h9h5 d0e1 a6a5 d2f2` |
| b2e2 | 12 | completed | b9c7 | 25 | cp -25 | 20 | 107590 | 92 | 12/922/66 | `b9c7 b0c2 a9b9 a0b0 c6c5 b0b6 h9g7 g3g4 b7a7 b6c6` |
| b2e2 | 18 | completed | b9c7 | 20 | cp -20 | 29 | 1395237 | 1314 | 15/929/56 | `b9c7 c3c4 a9b9 b0c2 g6g5 a0b0 h9g7 h2g2 g9e7 h0i2 g7h5 i0i1` |
| b2e2 | 24 | completed | h9g7 | 17 | cp -17 | 39 | 7834765 | 7521 | 16/933/51 | `h9g7 b0c2 b9c7 a0b0 a9b9 c3c4 g6g5 h2g2 f9e8 h0i2 g7h5 i0i1` |
| b2e2 | 30 | completed | h9g7 | 20 | cp -20 | 45 | 43435739 | 46125 | 15/928/57 | `h9g7 b0c2 b9c7 c3c4 g6g5 a0b0 a9b9 h0i2 i6i5 h2g2 g7h5 i0i1` |
| b2f2 | 12 | completed | c6c5 | 15 | cp -15 | 16 | 187374 | 159 | 17/935/48 | `c6c5 b0c2 b9c7 a0b0 a9b9 h0g2 g6g5 b0b4 b7a7 b4f4 h9g7` |
| b2f2 | 18 | completed | b9c7 | 14 | cp -14 | 28 | 1180957 | 1135 | 18/936/46 | `b9c7 b0c2 a9b9 c3c4 b7a7 h0g2 g6g5 h2h6 h9g7 h6c6 g7h5 a0b0` |
| b2f2 | 24 | completed | b9c7 | 7 | cp -7 | 31 | 7790251 | 7447 | 23/940/37 | `b9c7 b0c2 a9b9 c3c4 g6g5 a0b0 h9g7 g0e2 c9e7 h0g2 b7a7 b0b9` |
| b2f2 | 30 | completed | b9c7 | 8 | cp -8 | 45 | 27597236 | 26871 | 22/940/38 | `b9c7 b0c2 a9b9 c3c4 g6g5 a0b0 h9g7 g0e2 c9e7 h0f1 i9i8 g3g4` |
| b2g2 | 12 | completed | c6c5 | -19 | cp 19 | 18 | 185676 | 165 | 55/930/15 | `c6c5 g2c2 h7e7 h2e2 h9g7 b0a2 b9a7` |
| b2g2 | 18 | completed | b7d7 | -15 | cp 15 | 29 | 1750984 | 1613 | 48/935/17 | `b7d7 b0c2 c6c5 a0b0 b9c7 g3g4 g9e7 g2e2 h9f8 h2f2 c7d5 h0g2` |
| b2g2 | 24 | completed | b7d7 | -9 | cp 9 | 42 | 9719543 | 9160 | 39/939/22 | `b7d7 b0c2 c6c5 a0b0 b9c7 h2h4 g9e7 b0b6 h9f8 h0i2 a9b9 b6b9` |
| b2g2 | 30 | completed | c6c5 | -7 | cp 7 | 42 | 34626675 | 33767 | 37/940/23 | `c6c5 b0c2 b7d7 a0b0 b9c7 g3g4 g9e7 g2e2 h9g7 h0g2 a9a8 b0b6` |
| c0a2 | 12 | completed | b7e7 | -55 | cp 55 | 17 | 152289 | 140 | 172/824/4 | `b7e7 b2e2 b9c7 b0c2 a9b9 h2f2 g6g5 h0i2 h9g7 i0h0 i9h9 h0h6` |
| c0a2 | 18 | completed | b7e7 | -52 | cp 52 | 31 | 1601633 | 1554 | 155/840/5 | `b7e7 b2e2 b9c7 b0c2 a9b9 a0a1 g6g5 a1f1 h9g7 f1f6 i9i7 h2g2` |
| c0a2 | 24 | completed | b7e7 | -51 | cp 51 | 38 | 10567117 | 10401 | 153/842/5 | `b7e7 b2e2 b9c7 b0c2 a9b9 a0a1 h9g7 a1f1 g6g5 h0i2 i9i7 c3c4` |
| c0a2 | 30 | completed | b7e7 | -56 | cp 56 | 57 | 50602212 | 51889 | 173/823/4 | `b7e7 b2e2 b9c7 b0c2 a9b9 a0a1 g6g5 a1f1 h9g7 h0i2 b9b5 f1f6` |
| c0e2 | 12 | completed | c6c5 | 21 | cp -21 | 16 | 143173 | 119 | 14/928/58 | `c6c5 b0d1 c9e7 a0c0 h9i7 c3c4 c5c4 c0c4 i9i8 h0g2 b9c7 g3g4` |
| c0e2 | 18 | completed | b7e7 | 19 | cp -19 | 37 | 1318569 | 1198 | 15/931/54 | `b7e7 b0c2 b9c7 c3c4 h7f7 h0g2 a9b9 a0b0 h9g7 b2b6 i9h9 i0h0` |
| c0e2 | 24 | completed | h7f7 | 16 | cp -16 | 33 | 10661414 | 10049 | 17/934/49 | `h7f7 c3c4 h9g7 h0i2 i9h9 i0h0 g6g5 b0c2 c9e7 b2b1 b9d8 d0e1` |
| c0e2 | 30 | completed | c9e7 | 15 | cp -15 | 44 | 40013848 | 38759 | 17/935/48 | `c9e7 g3g4 h9i7 h0g2 c6c5 i0i1 i9i8 i1d1 b9c7 g2h4 h7h2 b2h2` |
| c3c4 | 12 | completed | b7c7 | 19 | cp -19 | 15 | 159571 | 142 | 15/931/54 | `b7c7 b2e2 h7e7 b0c2 h9g7 h0g2 c6c5 c2d4 c5c4 d4e6 g7e6 e2e6` |
| c3c4 | 18 | completed | b7c7 | 21 | cp -21 | 27 | 1827132 | 1666 | 14/928/58 | `b7c7 h2e2 c9e7 b0a2 i9i8 h0g2 i8d8 a0b0 d9e8 i0h0 h9i7 g3g4` |
| c3c4 | 24 | completed | b7c7 | 17 | cp -17 | 41 | 9586112 | 8996 | 16/933/51 | `b7c7 h2e2 c9e7 h0g2 c6c5 c0a2 c5c4 i0h0 i9i8 e2e6 d9e8 a2c4` |
| c3c4 | 30 | completed | g6g5 | 22 | cp -22 | 43 | 36302818 | 34910 | 14/926/60 | `g6g5 h2g2 c9e7 h0i2 h9g7 i0h0 i9h9 h0h4 h7i7 h4d4 b9c7 b0c2` |
| d0e1 | 12 | completed | b9c7 | -6 | cp 6 | 21 | 106999 | 91 | 35/941/24 | `b9c7 c3c4 b7a7 b0c2 a9b9 a0b0 g6g5 b2b6 h9g7 h2h6 c9e7 h0g2` |
| d0e1 | 18 | completed | b7a7 | -5 | cp 5 | 39 | 1428185 | 1313 | 34/942/24 | `b7a7 c3c4 b9c7 b0c2 a9b9 a0b0 g6g5 b2b6 h9g7 h0i2 i9i8 h2g2` |
| d0e1 | 24 | completed | b7a7 | -6 | cp 6 | 38 | 7034641 | 6596 | 35/941/24 | `b7a7 c3c4 b9c7 b0c2 a9b9 a0b0 g6g5 b2b6 h7h5 h2d2 c6c5 c4c5` |
| d0e1 | 30 | completed | b7a7 | 0 | cp 0 | 39 | 20894396 | 19811 | 29/942/29 | `b7a7 c3c4 b9c7 b0c2 a9b9 a0b0 g6g5 h0i2 b9b3 i0i1 h9g7 i1f1` |
| e0e1 | 12 | completed | h7e7 | -102 | cp 102 | 19 | 141860 | 122 | 516/483/1 | `h7e7 h0g2 h9g7 i0h0 i9h9 b0c2 c6c5 b2a2 b9c7 a0b0 h9h3 b0b4` |
| e0e1 | 18 | completed | h7e7 | -91 | cp 91 | 37 | 2035694 | 1931 | 418/581/1 | `h7e7 h0g2 h9g7 i0h0 i9h9 c3c4 b9a7 b0c2 g6g5 e1e0 b7c7 c2b4` |
| e0e1 | 24 | completed | h7e7 | -99 | cp 99 | 45 | 13304056 | 12755 | 494/505/1 | `h7e7 h0g2 h9g7 i0h0 i9h9 c3c4 h9h5 e1e0 c6c5 c4c5 h5c5 b0c2` |
| e0e1 | 30 | completed | h7e7 | -103 | cp 103 | 58 | 59472533 | 59687 | 522/477/1 | `h7e7 h0g2 h9g7 i0h0 i9h9 c3c4 h9h5 b0c2 c6c5 c4c5 h5c5 e1e0` |
| e3e4 | 12 | completed | b7e7 | -93 | cp 93 | 14 | 172879 | 153 | 441/558/1 | `b7e7 b2e2 e7e4 f0e1 h7e7 h0g2 h9g7 i0h0 i9h9 h2h6 b9c7 b0c2` |
| e3e4 | 18 | completed | h7e7 | -87 | cp 87 | 33 | 1883229 | 1783 | 390/609/1 | `h7e7 h2e2 e7e4 f0e1 b7e7 b0c2 b9c7 a0b0 a9b9 b2b4 h9g7 c3c4` |
| e3e4 | 24 | completed | h7e7 | -86 | cp 86 | 50 | 12039870 | 11494 | 382/617/1 | `h7e7 h2e2 e7e4 f0e1 b7e7 b0c2 b9c7 a0b0 a9b9 b2b4 h9g7 c3c4` |
| e3e4 | 30 | completed | b7e7 | -91 | cp 91 | 53 | 53481387 | 53051 | 424/575/1 | `b7e7 b2e2 e7e4 d0e1 h7e7 h0g2 h9g7 i0h0 i9h9 h2h4 b9c7 g3g4` |
| f0e1 | 12 | completed | h7i7 | -9 | cp 9 | 22 | 107631 | 90 | 39/940/21 | `h7i7 c3c4 h9g7 g0e2 b7c7 b0c2 g6g5 h0f1 b9a7 g3g4` |
| f0e1 | 18 | completed | h9g7 | -4 | cp 4 | 34 | 1348558 | 1225 | 33/942/25 | `h9g7 g3g4 h7i7 h0g2 i9h9 i0h0 c6c5 b0a2 b9c7 h2h6 b7b5 g0e2` |
| f0e1 | 24 | completed | g6g5 | -2 | cp 2 | 44 | 7741970 | 7163 | 31/942/27 | `g6g5 c3c4 b7c7 g0e2 b9a7 b0c2 a9b9 a0b0 h9g7 b2b6 h7h5 h0i2` |
| f0e1 | 30 | completed | h7i7 | 0 | cp 0 | 40 | 23981067 | 22475 | 29/942/29 | `h7i7 g3g4 h9g7 h0g2 i9h9 i0h0 c6c5 h2h6 b9c7 c0e2 b7a7 b0d1` |
| g0e2 | 12 | completed | g6g5 | 21 | cp -21 | 16 | 135472 | 112 | 14/928/58 | `g6g5 b0c2 g9e7 b2a2 b9a7 a0b0 b7c7 c3c4 h9g7 c2d4` |
| g0e2 | 18 | completed | b7d7 | 17 | cp -17 | 31 | 1330573 | 1175 | 16/933/51 | `b7d7 a0a1 b9c7 a1d1 d9e8 d1d6 d7d9 b2d2 a9b9 d2d9 c7d9 b0a2` |
| g0e2 | 24 | completed | b7d7 | 15 | cp -15 | 35 | 8882866 | 8155 | 17/935/48 | `b7d7 g3g4 b9c7 b0a2 a9b9 a0a1 h7f7 a1d1 d9e8 h2f2 h9i7 h0g2` |
| g0e2 | 30 | completed | g6g5 | 15 | cp -15 | 44 | 46178007 | 44594 | 17/935/48 | `g6g5 b0c2 g9e7 c3c4 b9a7 a0a1 a9a8 a1g1 a8d8 h0i2 d8d5 g3g4` |
| g0i2 | 12 | completed | b9c7 | -55 | cp 55 | 23 | 142605 | 124 | 172/824/4 | `b9c7 c3c4 h7e7 h0g2 h9g7 i0h0 i9h9 h2h6 g6g5 b2e2 g7f5` |
| g0i2 | 18 | completed | h7e7 | -48 | cp 48 | 29 | 1913687 | 1838 | 140/855/5 | `h7e7 h2e2 h9g7 h0g2 i9h9 i0i1 b9c7 i1d1 c6c5 b0a2 h9h5 d1d6` |
| g0i2 | 24 | completed | h7e7 | -54 | cp 54 | 42 | 10270055 | 10162 | 165/831/4 | `h7e7 h2e2 h9g7 h0g2 i9h9 i0i1 b9c7 i1d1 c6c5 b0a2 h9h5 d1d6` |
| g0i2 | 30 | completed | h7e7 | -50 | cp 50 | 44 | 58385836 | 59894 | 146/849/5 | `h7e7 h2e2 h9g7 h0g2 i9h9 i0i1 b9c7 i1d1 c6c5 b0a2 f9e8 a0a1` |
| g3g4 | 12 | completed | h7g7 | 17 | cp -17 | 23 | 164366 | 144 | 16/932/52 | `h7g7 b2e2 c9e7 h0i2 h9i7 i0h0 i9h9 h2h6 b9d8 b0c2 g6g5 g4g5` |
| g3g4 | 18 | completed | h7g7 | 26 | cp -26 | 30 | 1773525 | 1637 | 12/920/68 | `h7g7 b2e2 c9e7 h0i2 h9i7 i0h0 i9h9 h2h6 d9e8 b0c2 c6c5 e3e4` |
| g3g4 | 24 | completed | h7g7 | 15 | cp -15 | 37 | 9126254 | 8580 | 17/935/48 | `h7g7 b2e2 g9e7 f0e1 c6c5 b0c2 b9c7 a0b0 a9b9 b0b4 h9i7 h2f2` |
| g3g4 | 30 | completed | c6c5 | 18 | cp -18 | 45 | 49119503 | 48298 | 16/932/52 | `c6c5 h0g2 b9c7 c0e2 g9e7 i0i1 h9f8 b0d1 i9g9 i1f1 a9a8 g2h4` |
| h0g2 | 12 | completed | g6g5 | 16 | cp -16 | 16 | 109225 | 95 | 17/933/50 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 h9g7 b0b4` |
| h0g2 | 18 | completed | g6g5 | 10 | cp -10 | 29 | 1562914 | 1483 | 21/939/40 | `g6g5 h2i2 h9g7 i0h0 i9h9 c3c4 h7h3 b0c2 b9c7 a0a1 b7b3 c2b4` |
| h0g2 | 24 | completed | g6g5 | 3 | cp -3 | 45 | 9845481 | 9391 | 27/941/32 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 b7b3 c3c4 h9g7 h2h6 b3g3 b0b9` |
| h0g2 | 30 | completed | g6g5 | 10 | cp -10 | 46 | 44365299 | 43958 | 21/939/40 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 b7b3 c3c4 h9g7 c2d4 c9e7 c4c5` |
| h0i2 | 12 | completed | b7e7 | -2 | cp 2 | 16 | 145822 | 126 | 30/943/27 | `b7e7 b0c2 b9c7 c3c4 a9b9 a0b0 b9b5 c0e2 h9g7 i0i1 g6g5 i1f1` |
| h0i2 | 18 | completed | b7e7 | -12 | cp 12 | 32 | 1472212 | 1346 | 43/938/19 | `b7e7 b0c2 b9c7 a0b0 a9b9 c3c4 b9b5 i0i1 h9g7 i1f1 g6g5 f1f6` |
| h0i2 | 24 | completed | b7e7 | 0 | cp 0 | 41 | 9388524 | 9120 | 29/942/29 | `b7e7 b0c2 b9c7 a0b0 a9b9 b2b6 c6c5 i0i1 h9g7 i1b1 c7d5 b6b7` |
| h0i2 | 30 | completed | b7e7 | 0 | cp 0 | 39 | 28793738 | 28504 | 29/942/29 | `b7e7 b0c2 b9c7 a0b0 a9b9 b2b6 c6c5 i0i1 i6i5 c0e2 h9g7 i1b1` |
| h2c2 | 12 | completed | c9e7 | -21 | cp 21 | 18 | 184977 | 157 | 59/927/14 | `c9e7 h0g2 i9i8 c2e2 i8d8 f0e1 d8d1 b0a2 d9e8` |
| h2c2 | 18 | completed | i9i8 | -8 | cp 8 | 31 | 1556991 | 1392 | 38/940/22 | `i9i8 h0g2 c9e7 i0h0 i8d8 c2f2 h9i7 d0e1 i6i5 c0e2 d8d5 h0h6` |
| h2c2 | 24 | completed | g6g5 | -4 | cp 4 | 43 | 7756640 | 7145 | 33/942/25 | `g6g5 h0g2 h9g7 i0h0 i9h9 h0h4 h7i7 h4f4 a6a5 c0e2 b9a7 c2d2` |
| h2c2 | 30 | completed | c9e7 | -8 | cp 8 | 38 | 23979041 | 22727 | 38/940/22 | `c9e7 h0g2 i9i8 i0h0 i8d8 c2f2 h9i7 d0e1 i6i5 g3g4 d8d1 b0a2` |
| h2d2 | 12 | completed | h9g7 | 14 | cp -14 | 19 | 151133 | 142 | 18/936/46 | `h9g7 h0g2 i9h9 i0h0 h7h3 g3g4 h3g3 b0c2 h9h0 g2h0` |
| h2d2 | 18 | completed | h9g7 | 8 | cp -8 | 32 | 1341754 | 1259 | 22/940/38 | `h9g7 h0g2 i9h9 b0c2 g6g5 b2a2 b9a7 a0b0 a9b9 i0h0 h7h3 c3c4` |
| h2d2 | 24 | completed | h9g7 | 11 | cp -11 | 40 | 7642483 | 7232 | 20/938/42 | `h9g7 g3g4 i9h9 h0g2 h7i7 c3c4 h9h5 i0h0 h5h0 g2h0 b7e7 b0c2` |
| h2d2 | 30 | completed | h9g7 | 12 | cp -12 | 49 | 37304894 | 36845 | 19/938/43 | `h9g7 h0g2 i9h9 g3g4 c6c5 b0a2 b9c7 i0h0 g9e7 c0e2 h7i7 h0h9` |
| h2e2 | 12 | completed | h9g7 | 27 | cp -27 | 20 | 120480 | 106 | 12/917/71 | `h9g7 g3g4 i9h9 h0g2 c6c5 i0h0 b9c7 b0a2 a9a8 c3c4 c5c4 b2c2` |
| h2e2 | 18 | completed | h9g7 | 25 | cp -25 | 35 | 1493352 | 1407 | 12/921/67 | `h9g7 h0g2 i9h9 i0h0 g6g5 b0c2 b9c7 c3c4 b7b3 g3g4 g5g4 h0h6` |
| h2e2 | 24 | completed | h9g7 | 15 | cp -15 | 45 | 11662301 | 11180 | 17/935/48 | `h9g7 h0g2 i9h9 i0h0 b9c7 c3c4 g6g5 b0c2 b7b3 g3g4 g5g4 h0h6` |
| h2e2 | 30 | completed | h9g7 | 20 | cp -20 | 53 | 46741045 | 46418 | 15/929/56 | `h9g7 h0g2 b9c7 i0h0 i9h9 g3g4 c6c5 b2c2 d9e8 b0a2 c7b5 a0a1` |
| h2f2 | 12 | completed | b7e7 | 16 | cp -16 | 17 | 171603 | 147 | 17/934/49 | `b7e7 b0c2 b9c7 h0g2 h9i7 i0h0 i9h9 a0b0 a9b9 b2b6 c6c5 h0h5` |
| h2f2 | 18 | completed | b7e7 | 10 | cp -10 | 33 | 1756436 | 1663 | 21/939/40 | `b7e7 b0c2 b9c7 h0g2 h9i7 c3c4 a9b9 a0b0 b9b5 g3g4 i9h9 d0e1` |
| h2f2 | 24 | completed | b7e7 | 11 | cp -11 | 38 | 7679170 | 7254 | 20/938/42 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 h9i7 c3c4 b9b5 f0e1 i6i5 b2a2` |
| h2f2 | 30 | completed | b7e7 | 14 | cp -14 | 43 | 27935824 | 27443 | 18/936/46 | `b7e7 b0c2 b9c7 a0b0 a9b9 h0g2 h9i7 c3c4 b9b5 f0e1 i9h9 g0e2` |
| h2g2 | 12 | completed | b7e7 | -20 | cp 20 | 16 | 104702 | 91 | 57/929/14 | `b7e7 b0c2 b9c7 h0i2 h7h2 c0e2 h9i7 i0h0 i9h9 c3c4 a9b9 a0b0` |
| h2g2 | 18 | completed | b7e7 | -24 | cp 24 | 29 | 1508859 | 1392 | 64/923/13 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 a0a1 b9b3 h0h6` |
| h2g2 | 24 | completed | b7e7 | -16 | cp 16 | 40 | 6281365 | 5852 | 50/933/17 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 h0h6 b9b3 c3c4` |
| h2g2 | 30 | completed | b7e7 | -17 | cp 17 | 36 | 33662970 | 33155 | 51/933/16 | `b7e7 b2e2 b9c7 b0c2 a9b9 h0i2 h9i7 i0h0 i9h9 h0h4 i6i5 i3i4` |
| h2h1 | 12 | completed | h7e7 | -42 | cp 42 | 17 | 212211 | 198 | 114/879/7 | `h7e7 h1e1 h9g7 h0g2 i9h9 g3g4 c6c5 b2e2 b9c7 b0c2 a9b9` |
| h2h1 | 18 | completed | h7e7 | -43 | cp 43 | 28 | 1902962 | 1859 | 117/876/7 | `h7e7 b0c2 h9g7 i0i2 b9c7 c3c4 a9a8 i2h2 i9i8 g3g4 a8d8 b2a2` |
| h2h1 | 24 | completed | h7e7 | -42 | cp 42 | 37 | 13140244 | 12995 | 114/879/7 | `h7e7 b0c2 h9g7 i0i2 c6c5 i2h2 b9c7 b2b4 i9i8 b4g4 g7e8 a0b0` |
| h2h1 | 30 | completed | b9c7 | -38 | cp 38 | 49 | 44102800 | 44301 | 100/892/8 | `b9c7 c3c4 h7e7 b0c2 h9g7 h1e1 i9h9 h0g2 g6g5 a0a1 a9a8 a1d1` |
| h2h3 | 12 | completed | g6g5 | -43 | cp 43 | 20 | 174555 | 153 | 117/876/7 | `g6g5 b2e2 h9g7 b0c2 b9a7 a0b0 a9b9 h0i2 b7c7 b0b9 a7b9 i0i1` |
| h2h3 | 18 | completed | g6g5 | -43 | cp 43 | 25 | 1530112 | 1390 | 119/874/7 | `g6g5 b2f2 h9g7 b0c2 b9a7 h0i2 a9a8 a0b0 a8f8 f0e1 a6a5 b0b4` |
| h2h3 | 24 | completed | g6g5 | -45 | cp 45 | 33 | 8553784 | 8072 | 125/869/6 | `g6g5 b2e2 b9c7 b0c2 a9b9 a0b0 h9g7 c3c4 h7h5 b0b6 c9e7 h0i2` |
| h2h3 | 30 | completed | g6g5 | -43 | cp 43 | 45 | 48161352 | 47472 | 118/875/7 | `g6g5 b2f2 c6c5 b0c2 b7d7 a0b0 b9c7 h0i2 g9e7 g3g4 g5g4 b0b4` |
| h2h4 | 12 | completed | g6g5 | -22 | cp 22 | 22 | 172908 | 171 | 61/925/14 | `g6g5 b2e2 h9g7 b0c2 b9a7 a0b0 a9b9 h0g2 c6c5 e3e4 g9e7 c2e3` |
| h2h4 | 18 | completed | g6g5 | -16 | cp 16 | 26 | 1894485 | 1748 | 50/933/17 | `g6g5 h0g2 h9g7 b0a2 c6c5 b2c2 c9e7 a0b0 b9d8 i0i1 g7f5 i1d1` |
| h2h4 | 24 | completed | g6g5 | -16 | cp 16 | 35 | 8364237 | 7951 | 49/934/17 | `g6g5 h0g2 h9g7 b0a2 c6c5 b2c2 b9a7 a0b0 a9b9 a3a4 g9e7 b0b4` |
| h2h4 | 30 | completed | c6c5 | -13 | cp 13 | 44 | 36611917 | 36009 | 45/937/18 | `c6c5 h0g2 g6g5 b2c2 c9e7 h4a4 b9a7 i0h0 i9i8 h0h6 a6a5 a4e4` |
| h2h5 | 12 | completed | g6g5 | -66 | cp 66 | 15 | 146851 | 130 | 234/763/3 | `g6g5 h0g2 h9g7 h5h1 b7e7 c3c4 g7f5 b0c2 b9c7 b2b4 a9b9 a0b0` |
| h2h5 | 18 | completed | g6g5 | -73 | cp 73 | 30 | 2161152 | 2007 | 276/722/2 | `g6g5 h0g2 h9g7 h5h1 i9i8 h1g1 g7h5 g0e2 c6c5 b2c2 c9e7 b0a2` |
| h2h5 | 24 | completed | g6g5 | -67 | cp 67 | 46 | 11318278 | 10770 | 239/758/3 | `g6g5 h0g2 h9g7 h5h1 i9i8 h1g1 g7h5 g0e2 c6c5 b0a2 b9c7 b2c2` |
| h2h5 | 30 | max_seconds | g6g5 | -66 | cp 66 | 51 | 60325183 | 59377 | 233/764/3 | `g6g5 h0g2 h9g7 h5h1 c6c5 h1c1 b9c7 i0h0 i9h9 c3c4 c5c4 h0h4` |
| h2h6 | 12 | completed | h9g7 | -25 | cp 25 | 16 | 116081 | 103 | 67/921/12 | `h9g7 h0g2 i9i8 b0c2 i8d8 g3g4 b9c7 c3c4` |
| h2h6 | 18 | completed | g6g5 | -30 | cp 30 | 33 | 1524817 | 1450 | 79/911/10 | `g6g5 b2e2 c9e7 h0g2 i6i5 e2e6 d9e8 b0c2 b9d8 e6e5 h9g7 h6g6` |
| h2h6 | 24 | completed | g6g5 | -31 | cp 31 | 40 | 7386719 | 7074 | 80/910/10 | `g6g5 b2e2 c9e7 h0g2 i6i5 b0c2 h9g7 i0i1 b9d8 i1d1 i9i6 h6h4` |
| h2h6 | 30 | completed | g6g5 | -32 | cp 32 | 44 | 33262061 | 33212 | 83/907/10 | `g6g5 b2e2 h9g7 h0g2 b9c7 h6g6 c6c5 i0h0 c7d5 h0h4 b7d7 b0c2` |
| h2h9 | 12 | completed | i9h9 | -114 | cp 114 | 19 | 75243 | 59 | 627/373/0 | `i9h9 h0g2 h7e7 b2d2 h9h1 d0e1 b9c7 b0c2 a9b9` |
| h2h9 | 18 | completed | i9h9 | -113 | cp 113 | 30 | 943878 | 828 | 612/388/0 | `i9h9 h0g2 h7e7 c3c4 c6c5 c4c5 h9h5 c5c6 h5c5 c0e2 c5c6 i0h0` |
| h2h9 | 24 | completed | i9h9 | -120 | cp 120 | 42 | 8204231 | 7556 | 675/325/0 | `i9h9 h0g2 h7e7 c3c4 b9a7 b2e2 d9e8 b0c2 h9h4 a0b0 b7c7 e2e6` |
| h2h9 | 30 | completed | i9h9 | -125 | cp 125 | 54 | 39441843 | 39787 | 716/284/0 | `i9h9 h0g2 h7e7 b0c2 c6c5 b2a2 b9c7 a0b0 a9b9 b0b4 c7d5 g3g4` |
| h2i2 | 12 | completed | h9g7 | 11 | cp -11 | 17 | 79452 | 70 | 20/939/41 | `h9g7 h0g2 i9h9 i0h0 g6g5 b2e2 h7h3 b0c2 b9a7 a0b0 a9b9 b0b4` |
| h2i2 | 18 | completed | g6g5 | 4 | cp -4 | 29 | 948233 | 967 | 25/942/33 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4 h7h3 b2b4 b7c7 b0c2 a9a8 a0b0` |
| h2i2 | 24 | completed | g6g5 | -7 | cp 7 | 39 | 7568917 | 7630 | 36/941/23 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4 h7h3 b0c2 b9a7 b2b4 a9a8 a0a1` |
| h2i2 | 30 | completed | g6g5 | 1 | cp -1 | 49 | 30007944 | 30456 | 28/942/30 | `g6g5 h0g2 h9g7 i0h0 i9h9 c3c4 h7h3 b0c2 b9a7 b2a2 b7b3 a0b0` |
| i0i1 | 12 | completed | h7h0 | -83 | cp 83 | 17 | 77246 | 61 | 353/645/2 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0g0 h0g0 b7e7 b0c2 b9c7 a0b0` |
| i0i1 | 18 | completed | h7h0 | -60 | cp 60 | 32 | 1507716 | 1437 | 199/797/4 | `h7h0 h2e2 h9g7 i1h1 h0i0 h1h0 i0g0 h0g0 i9h9 b0c2 b9c7 g0g1` |
| i0i1 | 24 | completed | h7h0 | -71 | cp 71 | 47 | 9750762 | 9415 | 265/733/2 | `h7h0 h2e2 h9g7 i1h1 h0i0 b2b4 b7e7 h1h0 b9c7 b0c2 i0g0 h0g0` |
| i0i1 | 30 | completed | h7h0 | -82 | cp 82 | 53 | 40248373 | 39957 | 343/655/2 | `h7h0 h2e2 h9g7 i1h1 h0i0 b2b4 c6c5 h1h0 i0g0 h0g0 i9h9 b0a2` |
| i0i2 | 12 | completed | h7h0 | -66 | cp 66 | 24 | 113725 | 94 | 230/767/3 | `h7h0 h2e2 b7e7 i2h2 h0i0 h2h8 b9c7 b0c2 a9b9 a0a1 b9b3` |
| i0i2 | 18 | completed | h7h0 | -46 | cp 46 | 35 | 1813397 | 1715 | 132/862/6 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 b9c7 a0a1 b7b5 h2h0 i0g0 h0g0` |
| i0i2 | 24 | completed | h7h0 | -58 | cp 58 | 45 | 9557861 | 9192 | 186/810/4 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 c6c5 h2h0 i0g0 h0g0 i9h9 g3g4` |
| i0i2 | 30 | completed | h7h0 | -62 | cp 62 | 52 | 37460080 | 37038 | 206/791/3 | `h7h0 h2e2 h9g7 i2h2 h0i0 b0c2 c6c5 h2h0 i0g0 h0g0 i9h9 g3g4` |
| i3i4 | 12 | completed | h9g7 | -10 | cp 10 | 18 | 138608 | 130 | 41/939/20 | `h9g7 g3g4 h7i7 h0i2 i9h9 i0h0 b7e7 b2e2 b9c7 b0c2 a9b9 a0a1` |
| i3i4 | 18 | completed | b7e7 | -8 | cp 8 | 30 | 1804915 | 1729 | 38/940/22 | `b7e7 b0c2 b9c7 a0b0 a9b9 c3c4 b9b5 g3g4 g6g5 g4g5 b5g5 h0g2` |
| i3i4 | 24 | completed | h9g7 | -7 | cp 7 | 43 | 8277175 | 7929 | 36/941/23 | `h9g7 g3g4 h7i7 h0i2 b7e7 b2e2 i9h9 i0h0 i6i5 h2g2 h9h0 i2h0` |
| i3i4 | 30 | completed | b7e7 | -10 | cp 10 | 42 | 38902696 | 38928 | 40/939/21 | `b7e7 b0c2 b9c7 a0b0 g6g5 c3c4 h9g7 h0g2 h7i7 i0h0 i9h9 c0e2` |
