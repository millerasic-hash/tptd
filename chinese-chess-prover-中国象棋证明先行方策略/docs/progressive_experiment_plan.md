# 渐进式实验方案

目标不是一次性证明中国象棋标准开局红方必胜，而是逐层建立：

```text
可复现数据 -> 稳定候选 -> 小证书 -> 历史正确证书 -> DF-PN 闭合 -> 表库叶子 -> 更大证书
```

每一层必须有固定输入、固定资源预算、机器可读产物、人工可读报告和进入下一层的判据。任何阶段都不能把 Pikafish 分数直接当成证明。

## 全局实验约束

### 固定规则

当前主线规则：

```text
第三次重复，造成者负。
```

证明状态必须包含：

```text
棋盘 + 当前行棋方 + 历史局面计数签名
```

如果某个实验暂时没有接入完整历史签名，报告必须标注为：

```text
engine_probe_only
```

不能标注为 proof。

### 固定资源档位

为了适合普通本机，先固定三个资源档：

| 档位 | Threads | Hash | 单查询上限 | 用途 |
|:---|---:|---:|---:|:---|
| S | 1 | 64 MB | 15 秒 | 小参数高密度扫描 |
| M | 1 | 128 MB | 60 秒 | opening probe / top-k 稳定性 |
| L | 1-2 | 256 MB | 180 秒 | 少量候选深搜 |

默认先用 S 和 M。L 只用于已经筛出的少量候选，不做全量 44 首着扫。

### 固定产物

每个实验目录至少包含：

```text
report.md
report.json
command.txt
```

其中：

- `report.md` 给人读。
- `report.json` 给程序复核和二次统计。
- `command.txt` 保存原始命令。

已存在的历史报告命名可保留，后续新实验按这个结构走。

### 禁止结论

以下结论禁止出现：

```text
score >= T 所以必胜
depth N 最优所以证明
Pikafish 认为赢所以红方必胜
```

允许的结论格式是：

```text
在固定样本 S、固定资源 R、固定规则 G 下，
某类局面被证书闭合 / 未被证书闭合 / 分数稳定性如何。
```

## 阶段 0：规则和校验器基线

### 目标

保证本地规则生成器、证书校验器和 Pikafish 接口没有基本错误。

### 输入

- 标准开局 FEN。
- 人工构造的必胜/必败小局面。
- `proof.json`。

### 命令

```bash
python3 -m unittest -v
python3 light_prover.py verify proof.json
python3 light_prover.py moves
```

### 通过条件

- 标准开局合法首着数为 `44`。
- 单元测试全部通过。
- `proof.json` 可被独立校验。

### 产物

```text
pytest/unittest output
proof verification output
```

## 阶段 1：小参数高密度扫描

### 目标

看清低成本下的候选首着簇、分数波动和 MultiPV 扰动。

### 已完成基线

```text
reports/opening-grid-small/opening_grid_small_report.md
reports/opening-grid-small/opening_grid_small_report.json
```

### 当前命令

```bash
python3 opening_grid_probe.py \
  --depths 4,6,8,10,12 \
  --multipvs 1,2,3,4 \
  --hash-mb 64 \
  --per-query-max-seconds 15 \
  --out-dir reports/opening-grid-small
```

### 当前观察

depth 12 / MultiPV 4 前 5：

| Rank | 红方首着 | 黑方应着 | 红方分数 |
|---:|:---|:---|---:|
| 1 | `h2e2` | `h9g7` | `27` |
| 2 | `b2e2` | `b9c7` | `25` |
| 3 | `g0e2` | `g6g5` | `21` |
| 4 | `c0e2` | `c6c5` | `21` |
| 5 | `c3c4` | `b7c7` | `19` |

### 通过条件

不是要求发现胜势，而是要求形成稳定候选池：

```text
top_pool = 在多个 depth / MultiPV 下反复进入前 10 的首着
```

当前候选池：

```text
h2e2, b2e2, c3c4, g0e2, c0e2, g3g4, b0c2, h0g2, h2f2
```

### 下一层触发

如果候选池规模小于等于 `12`，进入阶段 2。

## 阶段 2：Top-k 候选稳定性深搜

### 目标

不再全量扫 44 首着，而是只对候选池做更深、更稳的参数扫描。

### 输入

阶段 1 生成的候选池。

### 建议参数

```text
depths = 14, 16, 18, 20, 22, 24
MultiPV = 4
Threads = 1
Hash = 128 MB
per-query-max-seconds = 60
```

### 需要新增脚本

```text
opening_candidate_probe.py
```

功能：

- 读取候选首着列表。
- 只跑候选首着。
- 输出每个候选在不同 depth 下的分数曲线。
- 输出 best reply 稳定性。
- 输出 PV 是否重复。

### 通过条件

进入阶段 3 的候选必须满足至少一条：

- 在 depth 18/20/22/24 中稳定进入前 5。
- best reply 不剧烈跳动。
- 分数没有随深度明显下降。
- PV 没有早期重复污染。

### 失败也有价值

如果所有候选分数都向 `0` 靠拢，说明开局强胜假设的经验支持变弱，应转向“证明和棋/不可败”方向。

## 阶段 3：小局面闭合证书

### 目标

先证明小局面，不碰标准开局。

这里检验的是：

```text
证书格式是否正确
校验器是否独立
WIN / LOSS 是否能闭合
```

### 输入类型

人工构造局面：

```text
单方杀王
一步杀
两步杀
重复造成者负
无合法着法
```

### 需要新增能力

证书中显式写：

```text
state_key
history_signature
claim = WIN / LOSS
children
```

### 通过条件

- 至少 20 个小证书全部可校验。
- 至少包含 5 个重复判负证书。
- 修改 Pikafish 或关闭 Pikafish 不影响校验结果。

### 产物

```text
certificates/small/*.json
reports/certificate-smoke/report.md
```

## 阶段 4：历史正确的 DAG 证书

### 目标

把树证书压成 DAG，同时不犯 GHI 错误。

### 核心规则

DAG 节点 key 不能只是棋盘：

```text
bad_key = board + side
good_key = board + side + history_count_signature
```

### 实验

构造两个到达同一棋盘、但历史不同的局面：

```text
E1 = same board, history A
E2 = same board, history B
```

验证：

- 如果只按棋盘缓存，会得出错误复用。
- 如果按历史签名缓存，校验通过。

### 通过条件

- 有一个专门的 GHI 回归测试。
- DAG 证书校验器拒绝缺少历史签名的重复相关证书。

## 阶段 5：DF-PN 原型

### 目标

把当前 bounded search 升级成真正的 proof/disproof number 搜索。

### 输入

先用阶段 3 的小局面，再扩到阶段 2 的候选首着后若干层局面。

### 资源预算

```text
max_nodes = 10^4, 10^5, 10^6
max_seconds = 10, 60, 300
```

### 输出指标

```text
status = WIN / LOSS / UNKNOWN
proof_nodes
disproof_nodes
expanded_nodes
transposition_hits
certificate_size_bytes
```

### 通过条件

同一资源下，DF-PN 比 bounded search 闭合更多小局面，且每个 WIN/LOSS 都能输出可校验证书。

## 阶段 6：Pikafish 作为 proof-cost 先验

### 目标

检验引擎分数是否真的减少证明节点。

### 对照组

每个样本都跑三种排序：

```text
random_order
legal_order
pikafish_order
```

### 成功指标

不是看分数高低，而是看：

```text
同一 max_nodes 下，pikafish_order 闭合率是否更高
同一闭合目标下，pikafish_order 节点数是否更少
```

### 阈值报告格式

```text
score_bucket
sample_count
closed_win
closed_loss
unknown
avg_nodes
max_nodes
```

### 通过条件

Pikafish 排序在多个样本集上稳定降低证明成本，才进入下一阶段。

## 阶段 7：低子力残局库叶子

### 目标

让证明树可以落到可验证残局表，而不是一直展开到将死。

### 起步范围

先不要做全残局库，先做小表：

```text
K + R vs K
K + R + A/B vs K + A/B
K + C vs K
K + P vs K
```

### 产物

```text
tablebases/<name>/index.bin
tablebases/<name>/meta.json
tablebases/<name>/sha256.txt
```

### 通过条件

- 表库生成可复现。
- 表库查询可校验。
- 证书叶子可以引用表库 hash。

## 阶段 8：候选首着局部证明

### 目标

对阶段 2 的候选首着做局部证明尝试。

### 命题不是“红方必胜”

先证明更小命题：

```text
首着 r 后，黑方某个应着 b 是否必败？
首着 r 后，黑方 top-k 应着是否都能被压入同一类优势结构？
某个 PV 分支是否能闭合为 WIN？
```

### 通过条件

能对至少一个候选首着的至少一个黑方应着生成可验证 WIN 证书。

如果不能闭合，输出最小未闭合边界：

```text
frontier positions
pn/dn
engine_score
reason = node_limit / time_limit / tablebase_missing / repetition_history
```

## 阶段 9：公开可复核证书包

### 目标

让别人不用信任我们的搜索，只需要信任规则校验器。

### 包结构

```text
certificate-pack/
  README.md
  verifier.py
  rules.md
  root.json
  nodes/
  tablebases/
  manifest.json
  sha256.txt
```

### 通过条件

新机器上运行：

```bash
python3 verifier.py root.json
```

能得到：

```text
VERIFIED WIN
```

或：

```text
VERIFIED LOSS
```

## 决策表

| 现象 | 下一步 |
|:---|:---|
| 小参数 leader 剧烈跳动 | 不加深，先扩大重复跑和稳定性统计 |
| top-k 到 depth 24 仍集中在 +30 cp 内 | 不宣称胜势，转向证明小局面和残局库 |
| 某候选首着随深度稳定上升 | 进入候选首着局部证明 |
| DF-PN 小局面闭合率低 | 先修 move ordering / transposition / GHI |
| 证书体积爆炸 | 上 DAG / Merkle / tablebase leaf |
| Pikafish 排序不降低节点数 | 不再把分数当 proof-cost，改训练或手写 proof-cost |

## 当前应立即做的下一步

下一步不是继续全量 depth 30 以上扫 44 首着，而是：

```text
阶段 2：Top-k 候选稳定性深搜
```

建议候选池：

```text
h2e2
b2e2
c3c4
g0e2
c0e2
g3g4
b0c2
h0g2
h2f2
```

建议先跑：

```text
depth = 14,16,18,20,22,24
MultiPV = 4
Threads = 1
Hash = 128 MB
per-query-max-seconds = 60
```

如果这些候选仍然都在几十 cp 内震荡，证明方向应优先转为：

```text
历史正确证书校验器 + 小局面闭合 + 残局库叶子
```

而不是继续堆开局深度。

