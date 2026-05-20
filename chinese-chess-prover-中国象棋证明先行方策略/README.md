# 轻量 Pikafish 证明器

这个目录放的是一个外置轻量证明层，不改 Pikafish 核心。目标是做成可以给 Pikafish 上游评估的实验模块：

- 证明器负责闭合证书。
- Pikafish 负责候选着法排序和分数先验。
- 阈值校准只报告“同一资源/同一样本下，多少分以上更接近可证明胜”，不把分数本身当定理。

核心原则：

- Pikafish 只负责给候选着法排序和 proof cost 先验。
- 证明结果只由本地规则生成器和证明树校验器确认。
- 普通 `+800`、`+1500` 分数不会被当成必胜证明。
- 当前版本默认使用 proof-number 风格的有界搜索：证明某个局面在 `N` 个半回合内是 `WIN / LOSS`，否则返回 `UNKNOWN`。

## 方法对应

- Proof-number search：每个节点维护 `pn / dn`。
- Transpositions：内部转置表按 `局面 + 剩余深度 + 历史签名` 缓存。
- GHI：重复相关缓存包含历史计数签名，避免把不同历史下的结论混用。
- Solving Checkers 路线：Pikafish 分数只做启发式，最终仍要证书闭合。
- Proof Cost Network 思路：目前用 Pikafish `cp/mate` 分数映射成 proof cost；以后可以替换成训练网络。
- Retrograde：当前预留接口思路，尚未接残局库。

## 本机 Pikafish

本次实验已下载官方无头引擎到：

```text
tools/pikafish/MacOS/pikafish-apple-silicon
```

NNUE 文件在：

```text
tools/pikafish/pikafish.nnue
```

运行时要让引擎工作目录指向 `tools/pikafish`，否则找不到同目录下的 `pikafish.nnue`：

```bash
python3 light_prover.py prove \
  --fen "3RkR3/3R1R3/4R4/9/9/9/9/9/9/4K4 w - - 0 1" \
  --depth 3 \
  --engine tools/pikafish/MacOS/pikafish-apple-silicon \
  --engine-cwd tools/pikafish \
  --movetime 100
```

## 命令

列出初始局面合法着法：

```bash
python3 light_prover.py moves
```

证明一个局面：

```bash
python3 light_prover.py prove \
  --fen "3RkR3/3R1R3/4R4/9/9/9/9/9/9/4K4 w - - 0 1" \
  --depth 1 \
  --output proof.json
```

校验证书：

```bash
python3 light_prover.py verify proof.json
```

接入 Pikafish，只用它排序：

```bash
python3 light_prover.py prove \
  --fen "3RkR3/3R1R3/4R4/9/9/9/9/9/9/4K4 w - - 0 1" \
  --depth 3 \
  --engine tools/pikafish/MacOS/pikafish-apple-silicon \
  --engine-cwd tools/pikafish \
  --movetime 100
```

做固定资源阈值校准：

```bash
python3 light_prover.py calibrate positions.txt \
  --engine tools/pikafish/MacOS/pikafish-apple-silicon \
  --engine-cwd tools/pikafish \
  --depth 5 \
  --max-nodes 100000 \
  --movetime 100 \
  --engine-order \
  --output calibration.json
```

`calibration.json` 里的 `threshold_all_above_proven_win` 只表示：

```text
在这个 positions.txt 样本、这个深度、这个节点上限、这个 Pikafish 设置下，
分数不低于该阈值的样本全部被证明为 WIN。
```

它不是“中国象棋所有局面大于某分必胜”的证明。

## 1024x12 基线报告

复现本机 1024 个样本、深度 12、每样本最多 1024 个证明节点的基线：

```bash
python3 run_1024x12_report.py \
  --sample-count 1024 \
  --source-plies 2 \
  --depth 12 \
  --max-nodes 1024 \
  --engine-depth 1 \
  --out-dir reports/1024x12
```

本次报告文件：

```text
reports/1024x12/pikafish_prover_1024x12.md
reports/1024x12/pikafish_prover_1024x12.json
reports/1024x12/sample_1024_positions.txt
```

本次结果：

- 1024 个从标准开局 BFS 生成的合法样本。
- 证明深度 12 半回合。
- 每个样本最多 1024 个证明节点。
- Pikafish 根点评分：`engine-depth=1`，`movetime=20 ms`。
- 运行耗时：`975.034` 秒。
- 证明状态：`UNKNOWN: 1024`，`WIN: 0`，`LOSS: 0`。
- 分数范围：`-119` 到 `428`。
- `threshold_all_above_proven_win`：`null`。

解释：在这个资源预算下，开局附近样本没有形成任何闭合胜负证书，所以不能推出“Pikafish 分数大于多少必胜”。它只能作为轻量证明器的第一条资源基线：当前 1024 节点/12 半回合不足以证明这些开局附近局面。

## 1024x48 红方胜平负对局

复现 1024 个样本、每个样本最多继续 48 半回合的 Pikafish 自对弈：

```bash
python3 run_1024x48_games.py \
  --sample-count 1024 \
  --source-plies 2 \
  --max-plies 48 \
  --engine-depth 1 \
  --out-dir reports/1024x48-games \
  --keep-moves
```

本次报告文件：

```text
reports/1024x48-games/pikafish_1024x48_red_wdl.md
reports/1024x48-games/pikafish_1024x48_red_wdl.json
reports/1024x48-games/sample_1024_positions.txt
```

本次结果按“先行方 = 红方”统计：

- 红方胜：`94 / 1024 = 9.18%`。
- 平：`865 / 1024 = 84.47%`。
- 红方负：`65 / 1024 = 6.35%`。
- 终止原因：`black_checkmated: 94`，`red_checkmated: 65`，`max_plies: 782`，`repetition: 83`。
- 平均半回合数：`45.4`。
- 运行耗时：`93.179` 秒。

解释：这里的“平”是实验平局，表示 48 半回合内没有将死，或同一状态第 3 次出现；它不是数学上的必和证明。

## 1x256 单局面深度请求

复现 1 个标准开局局面、向 Pikafish 请求 `go depth 256`，并设置 120 秒安全上限：

```bash
python3 run_1x_depth.py \
  --depth 256 \
  --max-seconds 120 \
  --out-dir reports/1x256
```

本次报告文件：

```text
reports/1x256/pikafish_1x_depth.md
reports/1x256/pikafish_1x_depth.json
```

本次结果：

- 请求深度：`256`。
- 停止原因：`max_seconds`。
- 实际运行：`130.36` 秒。
- 最高报告深度：`42`。
- 最后分数：`cp 23`。
- 最后选择深度：`seldepth 56`。
- 最后节点数：`97104732`。
- 正式 `bestmove`：未返回。
- 从最后 PV 推导的首着：`h2e2`。

解释：这不是“完成 depth 256”的结果，而是一次 `go depth 256` 请求在本机 120 秒上限内实际达到的结果。开局局面直接完成 depth 256 不现实。

## 坐标

走法使用类 UCI 坐标：

- `a0` 是红方左下角。
- `i9` 是黑方右上角。
- FEN 第一行仍是黑方底线。

## 结果含义

- `WIN`：当前行棋方有一步能进入对手 `LOSS`，并且证书闭合。
- `LOSS`：当前行棋方所有合法非重复着法都进入对手 `WIN`，或当前无合法着法。
- `UNKNOWN`：给定深度内没有闭合证明。

这个东西不是完整中国象棋求解器。它是以后接真正 DF-PN 阈值控制、残局库、Pikafish MultiPV、proof-cost 网络的最小可验证骨架。
