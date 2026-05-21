# 参数组合阶梯实验

这份文档规定 Pikafish 主要参数如何进入多镜头闭环。目标不是一次性跑满所有组合，而是按维度逐层增加，观察结论是否稳定。

核心原则：

```text
先小维度高密度，再高维度低密度。
先 Observation，再 Hypothesis。
任何参数矩阵都不能直接生成 proof。
```

## 1. 固定候选池

第一轮参数组合不再扫 44 个首着，固定为：

```text
c3c4
b2e2
c0e2
h2e2
```

其中 `h2e2` 是对照组。

## 2. 参数维度顺序

按这个顺序增加维度：

| 维度 | 参数 | 作用 | 是否用于首轮 |
|---:|:---|:---|:---:|
| 1 | `depth` | 最重要的搜索深度镜头 | 是 |
| 2 | `MultiPV` | 观察候选是否依赖单一主线 | 是 |
| 3 | `Hash` | 观察内存/置换表敏感性 | 第二轮 |
| 4 | `Clear Hash` | 区分干净搜索和热缓存污染 | 第三轮 |
| 5 | `Threads` | 观察硬件并行敏感性 | 第四轮 |
| 6 | `UCI_ShowWDL / max_seconds` | 报告镜头和资源上限镜头 | 第五轮 |

`EvalFile` 固定为当前 `pikafish.nnue`，不作为实验变量。`Move Overhead` 和 `nodestime` 主要服务时间控制，固定深度实验暂不纳入。

## 3. 二参数组合

目标：

```text
depth x MultiPV
```

建议首轮：

```text
depth = 10,12
MultiPV = 1,2
Hash = 128 MB
Threads = 1
Clear Hash = true
UCI_ShowWDL = true
```

输出：

```text
reports/parameter-combo-pilot/
```

命令：

```bash
python3 parameter_combo_probe.py \
  --candidates c3c4,b2e2,c0e2,h2e2 \
  --depths 10,12 \
  --multipvs 1,2 \
  --hashes-mb 128 \
  --threads-list 1 \
  --clear-hash-modes true \
  --show-wdl-modes true \
  --per-query-max-seconds 15 \
  --out-dir reports/parameter-combo-pilot
```

判断：

- 如果 leader 在 `depth x MultiPV` 下频繁切换，只能保持 L0 Observation。
- 如果某候选持续领先，可升级为 L1 Hypothesis。

## 4. 三参数组合

目标：

```text
depth x MultiPV x Hash
```

建议：

```text
depth = 12,14
MultiPV = 1,2,4
Hash = 64,128,256
```

判断：

- 如果某候选只在大 Hash 下领先，说明它依赖资源，不应过早进入证明。
- 如果 Hash 变化不影响排序，说明候选更稳。

## 5. 四参数组合

目标：

```text
depth x MultiPV x Hash x ClearHash
```

注意：

```text
ClearHash=false 是热缓存诊断，不是证明口径。
```

证明相关报告默认以 `ClearHash=true` 为主。

## 6. 五参数组合

目标：

```text
depth x MultiPV x Hash x ClearHash x Threads
```

线程数会引入非确定性和硬件差异，因此只做稳定性检查，不作为证明必要条件。

建议：

```text
Threads = 1,2
```

如果 `Threads=2` 反转排序，而 `Threads=1` 稳定，则证明入口仍以 `Threads=1` 为准。

## 7. 六参数组合

目标：

```text
depth x MultiPV x Hash x ClearHash x Threads x ResourceLens
```

`ResourceLens` 可以是：

```text
UCI_ShowWDL = true,false
max_seconds = 15,60,180
```

首选把 `max_seconds` 当第六维，因为它直接决定是否完整达到 depth。

六参数不做全笛卡尔积，采用小样本：

```text
只保留 L1 候选
只跑 2 个 depth
只跑 2 个 Hash
只跑 1-2 个 MultiPV
```

## 8. 闭合协议映射

参数组合报告默认只产生：

```text
L0 Observation
```

升级到 `L1 Hypothesis` 的条件：

- top_count 明显领先。
- score_stddev 较低。
- rank_avg 较低。
- reply_count 少。
- PV 无重复污染。
- 增加参数维度后不反转。

升级到 `L2 Proof Obligation` 还需要：

```text
明确 fen
明确 side_to_move
明确 history_signature
明确 WIN / LOSS claim
明确 prover budget
```

## 9. 第一轮实验问题

第一轮只问：

```text
在 depth x MultiPV 两参数组合下，
c3c4 / b2e2 / c0e2 / h2e2 谁最稳定？
```

不问：

```text
谁能证明红方必胜？
```

如果第一轮 leader 不稳定，下一轮优先加密 `depth`，而不是直接加参数维度。

## 10. 首轮 2D Pilot 结果

已完成第一轮：

```text
reports/parameter-combo-pilot/parameter_combo_probe_report.md
reports/parameter-combo-pilot/parameter_combo_probe_report.json
```

参数：

```text
candidates = c3c4,b2e2,c0e2,h2e2
depth = 10,12
MultiPV = 1,2
Hash = 128 MB
Threads = 1
Clear Hash = true
UCI_ShowWDL = true
per-query-max-seconds = 15
```

结果：

```text
configs = 4
rows = 16
completed = 16
max_seconds = 0
first_compute_wall_runtime = 1.383 seconds
cache_rerun_wall_runtime = 0.007 seconds
cache_hits = 16
cache_misses = 0
```

leader：

| Depth | MultiPV | Leader | Score | Reply |
|---:|---:|:---|---:|:---|
| 10 | 1 | `c3c4` | `27` | `g6g5` |
| 10 | 2 | `b2e2` | `28` | `b9c7` |
| 12 | 1 | `c3c4` | `30` | `b7c7` |
| 12 | 2 | `h2e2` | `29` | `h9g7` |

解释：

- `c3c4` 领先 `2 / 4`，是 2D pilot 中最强观察。
- leader 出现 `3` 个，说明低深度参数仍不稳定。
- `c0e2` 在这一轮没有领先，并且 reply 变化最多。
- 本轮只能标记为 `L0 Observation`，不升级为 `L1 Hypothesis`。

下一轮建议：

```text
depth = 12,14,16
MultiPV = 1,2,4
Hash = 128 MB
```

也就是先加密 `depth x MultiPV`，再进入三参数 `+Hash`。
