# Self Evolution Loop Round 0001

## 结论等级

```text
L0 Observation
```

本轮仍然不把 Pikafish 分数、bestmove 或 PV 写成证明。

## 事实复盘

- `66` 阶段最终候选：`h2e2, c3c4`。
- `66` 阶段状态：`complete`。
- `66` 阶段 cursor：`1728 / 1728`。
- 当前闭环目标：在小资源下持续攻击最弱假设，筛出可进入 proof obligation 的候选。

## 自我进化

本轮识别的薄弱点：

- `66` 阶段最高 depth 只有 22，需要 frontier depth 复查。
- 两个候选仍是 cp 级差距，不是胜负证明。
- 还没有固定局面、历史签名和循环判负条件。
- 还没有覆盖黑方应着集合的证明图。

## 优化策略

本轮选择动作：`frontier_extension`。

理由：首轮攻击 66 阶段最高 depth 只有 22 的弱点，用 depth 24 做 frontier extension。

参数：

- candidates: `h2e2, c3c4`
- depth: `24`
- MultiPV: `4, 8`
- Hash MB: `512, 1024`
- Threads: `1`
- ClearHash: `true`
- UCI_ShowWDL: `true`
- per-query max seconds: `41.2`

## 本轮执行

- execute: `True`
- experiment report: `reports/evolution-loop/round-0001/experiment/parameter_combo_probe_report.json`

## 本轮结果

- rows: `8`
- completed rows: `8`
- max_seconds rows: `0`
- PV repeat rows: `0`
- leader: `h2e2`
- score gap: `3.5`

| Rank | Move | 象棋记法 | Top count | Top share | Avg score | Score range | Avg rank | Replies | Max seconds |
|---:|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `h2e2` | 炮八平五 | `3` | `0.75` | `18.75` | `2` | `1.25` | `2` | `0` |
| 2 | `c3c4` | 兵三进一 | `1` | `0.25` | `15.25` | `7` | `1.75` | `1` | `0` |

## 复盘输出

本轮继续支持 `h2e2` 稳定领先，但仍只能保持 L0，尚未形成证明义务。

## 下一轮方向

- 如果 `h2e2` 连续稳定领先，下一轮提高 depth。
- 如果出现反转、超时或重复，下一轮不加深，改为更宽 MultiPV / Hash 复查。
- 连续至少 3 轮稳定后，才考虑把 `h2e2 / c3c4` 转成 L2 proof obligation。
