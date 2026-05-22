# 自我进化实验闭环

目标：把当前 Pikafish 参数实验从一次性报告，推进成可轮询、可复盘、可优化的闭环系统，逐步逼近可靠答案。

核心边界：

```text
搜索分数不是证明。
每轮输出必须能被复查。
每轮只能升级证据等级，不能直接跳到定理。
```

## 1. 循环结构

每轮按固定顺序执行：

| 环节 | 作用 | 输出 |
|:---|:---|:---|
| 事实读取 | 读取上一轮状态、参数报告、候选统计 | source facts |
| 复盘输出 | 判断上一轮哪些结论稳定，哪些只是噪声 | retrospective |
| 自我进化 | 找出当前体系最薄弱的假设 | weakness list |
| 优化策略 | 选择下一轮最小资源动作 | next action |
| 小资源执行 | 只跑一个可控实验镜头 | experiment report |
| 状态沉淀 | 写入 JSON/Markdown，供下一轮继续 | state + summary |

这个闭环不追求一次跑满。它追求每一轮都让问题更窄、更可检验。

## 2. 可靠性等级

| 等级 | 名称 | 含义 |
|:---|:---|:---|
| `L0 Observation` | 观察 | Pikafish 多参数下出现稳定信号，但没有证明义务 |
| `L1 Stable Hypothesis` | 稳定假设 | 多轮独立镜头下同一候选持续领先，且没有明显重复污染 |
| `L2 Proof Obligation` | 证明义务 | 已固定局面、行棋方、历史签名、循环规则和待证命题 |
| `L3 Local Certificate` | 局部证书 | 证明器能闭合某个局部命题，且独立校验通过 |
| `L4 Strategy Certificate` | 策略证书 | 证书能覆盖一组对手应着，而不是单线 PV |
| `L5 Solved Claim` | 完整结论 | 有可复查策略证书或等价数学证明 |

当前阶段仍为：

```text
L0 Observation
```

## 3. 当前事实基线

已完成的事实层：

- 44 个红方首着基线：depth `12 / 18 / 24 / 30`，`MultiPV=4`。
- 9 候选稳定性深搜：depth `14 / 16 / 18 / 20 / 22 / 24`。
- 参数组合阶梯：`22 -> 33 -> 44 -> 55 -> 66`。
- `66` 阶段最终候选：`h2e2 / c3c4`。
- `h2e2` 在 `66` 阶段 top share `0.737`，平均分 `22.476`。
- `c3c4` 在 `66` 阶段 top share `0.263`，平均分 `20.321`。

象棋记法：

| UCI | 象棋记法 |
|:---|:---|
| `h2e2` | 炮八平五 |
| `c3c4` | 兵三进一 |

## 4. 自我进化规则

每轮必须优先攻击当前最弱点，而不是只强化已有结论。

当前最弱点：

| 弱点 | 为什么重要 | 下一步动作 |
|:---|:---|:---|
| `66` 最高 depth 只有 22 | 不能说明更深搜索仍稳定 | 加 frontier depth 24/26 小镜头 |
| 两候选差距不大 | 分数差是 cp 级别，不是胜负级别 | 多镜头看 top share 和 rank |
| 仍无 proof obligation | 搜索结论不能进入证明器 | 固定候选后的黑方应着集合 |
| PV 只是主线 | 主线不是覆盖所有变化 | 后续转成对手应着集合和证明图 |

## 5. 优化策略

下一阶段不再扩大到 44 首着，也不盲目把 depth 拉满。优先做：

```text
h2e2 / c3c4 两候选 frontier extension
```

每轮只增加一个小镜头：

- `depth` 从 24 开始，稳定后再递增。
- `MultiPV` 取 4 和 8，观察是否依赖单主线。
- `Hash` 取 512 和 1024，稳定后再提高。
- `Threads=1`，减少并行非确定性。
- `ClearHash=true`，以冷搜索为主。
- `UCI_ShowWDL=true`，保留 WDL 镜头。

## 6. 停止和升级条件

升级到 `L1 Stable Hypothesis` 的建议条件：

- 连续至少 3 轮 frontier extension 中，同一候选 leader 不反转。
- leader 平均分领先至少 `2 cp`。
- leader 平均排名低于 `1.35`。
- PV 没有第三次重复污染。
- 黑方首选应着集合没有持续扩大。

进入 `L2 Proof Obligation` 的条件：

- 固定候选首着。
- 固定黑方应着集合。
- 固定循环判负规则。
- 为每个应着生成明确待证局面。
- 证明器输出可被独立校验。

## 7. 轮询命令

单轮复盘并执行小资源实验：

```bash
python3 evolution_loop_runner.py \
  --base-dir reports/evolution-loop \
  --target-seconds 300 \
  --execute
```

只复盘、不执行新搜索：

```bash
python3 evolution_loop_runner.py \
  --base-dir reports/evolution-loop \
  --target-seconds 300
```

每轮输出：

```text
reports/evolution-loop/state.json
reports/evolution-loop/latest_summary.md
reports/evolution-loop/round-XXXX/evolution_summary.md
reports/evolution-loop/round-XXXX/evolution_summary.json
```

如果执行搜索，还会写入：

```text
reports/evolution-loop/round-XXXX/experiment/parameter_combo_probe_report.md
reports/evolution-loop/round-XXXX/experiment/parameter_combo_probe_report.json
```
