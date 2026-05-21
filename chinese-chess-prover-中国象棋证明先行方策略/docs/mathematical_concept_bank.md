# 数学概念库：不要过早锁死证明对象

这个项目不能只把中国象棋看成一棵巨大搜索树。搜索树是最低层对象，但真正的突破往往来自换表述。

2026-05-20 OpenAI 公布的 Erdős 平面单位距离问题结果给了一个很好的提醒：问题表面是离散几何，突破却来自代数数论、代数数域、class field tower 和 Golod-Shafarevich 理论。这说明“对象能简单陈述”不等于“有效工具就在同一领域里”。

对中国象棋证明实验，也应建立一组数学镜头。每个镜头都必须产生可计算指标、可验证证书或剪枝理由；否则只作为启发，不进入 proof。

## 0. 基础对象不是唯一对象

最低层对象：

```text
E = 棋盘 + 当前行棋方 + 历史计数签名
```

但实验中还可以同时维护其他派生对象：

```text
状态图
吸引域
势函数
等价类
反驳集
证明成本
压缩证书
残局表库索引
QBF/SAT 编码
```

原则：

```text
证明对象可以多表述。
校验规则只能有一个。
```

也就是：搜索和发现可以使用很多数学结构，但最终 WIN/LOSS 仍由独立校验器确认。

## 1. 有限图与吸引域

### 数学对象

把扩展状态看成有向图：

```text
G = (V, E)
V = 所有扩展状态
E = 合法非立即失败走法
```

第三次重复造成者负，对应某些边直接进入当前方失败终点。

### 可实验指标

- `out_degree`: 当前方合法选择数量。
- `forced_loss_edges`: 会导致第三次重复失败的边数。
- `attractor_depth`: 从终局反推到该状态需要几层。
- `frontier_size`: 当前吸引域边界大小。

### 用途

证明某一方必胜可以转成吸引域计算：

```text
WIN = 能一步进入对手 LOSS 的吸引域
LOSS = 所有边都进入对手 WIN 或立即失败
```

这对应模型检查和博弈图算法，比“树”更自然。

## 2. μ-calculus / 不动点

### 数学对象

WIN/LOSS 是单调算子的最小或最大不动点：

```text
F(W, L) -> (W', L')
```

其中：

```text
W' = 存在后继在 L 中的状态
L' = 所有后继都在 W 中的状态
```

### 可实验指标

- 不动点迭代轮数。
- 每轮新增 WIN/LOSS 状态数。
- 剩余 UNKNOWN 边界。

### 用途

这适合残局库和局部闭包。它提供一种“反向归纳”的工程表达。

## 3. QBF / SAT / SMT 编码

### 数学对象

深度有限的必胜命题可以写成量词公式：

```text
exists red move
forall black reply
exists red move
forall black reply
...
terminal_win
```

这本质是 QBF。

### 可实验指标

- 给定深度 `d` 的 QBF 是否可满足。
- UNSAT core 对应哪些黑方反驳。
- SAT witness 对应哪条红方策略。

### 用途

对小深度、小局面，QBF/SAT 可以作为第二校验器或反例生成器。它不会解决全局问题，但能帮我们发现规则生成器错误和证明树遗漏分支。

## 4. 证明复杂度

### 数学对象

不是只问：

```text
这个局面是不是 WIN？
```

还要问：

```text
证明它是 WIN 至少需要多大证书？
```

### 可实验指标

- `certificate_nodes`
- `certificate_edges`
- `max_branching_factor`
- `and_node_coverage`
- `dag_compression_ratio`
- `merkle_bytes`

### 用途

如果某个候选首着分数高，但证明成本极大，它不是好的 MVP 入口。我们要找的是“高分且低证明成本”的交集。

## 5. 信息论与压缩

### 数学对象

证明证书是一段信息。可压缩性说明大量分支共享结构。

### 可实验指标

- 原始树节点数。
- DAG 节点数。
- Merkle 节点去重率。
- 同构子树数量。
- 每个证明节点平均字节数。

### 用途

如果证书无法压缩，说明它可能不是当前硬件可处理方向。若某类局面证书高度可压缩，就值得扩展。

## 6. 对称群与规范化

### 数学对象

中国象棋有左右镜像对称。某些局部结构还可能存在更弱的等价关系：

```text
mirror(board)
piece-renaming under color/side constraints
local formation equivalence
```

### 可实验指标

- 镜像归一化命中率。
- 对称后节点减少比例。
- 对称等价类大小。

### 用途

减少重复证明。但必须把历史计数签名一起规范化，否则会犯 GHI 错误。

## 7. 偏序与支配关系

### 数学对象

如果局面 A 对红方“至少不差于”局面 B，可以写成偏序：

```text
A >=_red B
```

这不是天然存在的，需要谨慎定义。可从局部材料、将军权、活动空间、关键线控制等构造候选支配关系。

### 可实验指标

- 支配规则命中次数。
- 支配剪枝后仍能校验证书的比例。
- 被支配局面的反例数。

### 用途

如果能证明某类支配规则可靠，可以大幅减少分支。但未经证明的支配只能用于排序，不能用于剪枝。

## 8. 势函数 / Lyapunov 函数

### 数学对象

找一个函数：

```text
P(position)
```

希望在某类策略下单调变化，例如：

```text
红方可强制 P 增加
黑方无法长期阻止
P 达到阈值则进入已知 WIN 区
```

### 可实验指标

- PV 上的势函数变化。
- 自对弈中势函数是否震荡。
- 重复局面前势函数是否回到原值。

### 用途

它可能帮助解释“优势是否真的在积累”。当前 Pikafish 分数在开局只有几十 cp，未必是好势函数。

## 9. 随机过程与鞅

### 数学对象

把不确定走法排序、随机样本、自对弈扰动看成随机过程。

### 可实验指标

- 同一局面多次运行的分数方差。
- bestmove 稳定概率。
- top-k 留存率。
- 候选池熵。

### 用途

证明前先做稳定性科学。若一个候选只在少数参数下冒头，它不是证明入口。

## 10. 谱图与扩展性

### 数学对象

对局部状态图研究连通性、瓶颈和扩展性。

### 可实验指标

- frontier expansion ratio。
- 重复/转置密度。
- 局部 SCC 数量。
- 逃逸边数量。

### 用途

如果某个优势区域边界很小，容易闭合；如果边界极大，证明成本会爆炸。

## 11. 反例驱动与最小未闭合边界

### 数学对象

每次证明失败，不只输出 UNKNOWN，而是输出最小未闭合边界：

```text
frontier = 尚未证明的 AND/OR 边界
```

### 可实验指标

- frontier positions。
- 每个 frontier 的 `pn/dn`。
- 对应 Pikafish score。
- 未闭合原因。

### 用途

这把失败变成数据。下一轮实验优先攻击 frontier，而不是重新从开局开始。

## 12. 残局库与逆向分析

### 数学对象

低子力状态集合可以单独闭包：

```text
T_k = 子力数 <= k 的全部合法状态
```

对 `T_k` 做逆向分析，得到 WDL/DTM。

### 可实验指标

- 表库状态数。
- 每状态 bit 数。
- 表库命中率。
- 作为 proof leaf 后减少的搜索节点数。

### 用途

这是最实际的数学压缩。开局证明不一定走到将死，可以走到已验证表库叶子。

## 13. 范畴式接口：把工具当函子

这不是为了抽象而抽象，而是为了防止混用结论。

可以把每个工具看成从局面到某类对象的映射：

```text
EngineEval: Position -> Score
MoveGen: Position -> LegalMoves
Verifier: Certificate -> Bool
DFPN: Position -> CandidateCertificate
Tablebase: Position -> WDL
Canonicalizer: Position+History -> EquivalenceClass
```

只有 `Verifier` 输出能进入 proof。其他映射都只是辅助。

## 加入实验的方式

下一阶段报告应新增一组非证明指标：

```text
candidate_entropy
bestmove_stability
score_variance
dag_compression_estimate
frontier_size
transposition_density
symmetry_hit_rate
proof_cost_proxy
```

这些指标不直接证明胜负，但能告诉我们：

- 哪些候选值得深搜。
- 哪些局面可能证书短。
- 哪些失败边界该优先攻击。
- 哪些数学结构可能提供压缩。

## 当前优先级

近期不要把所有概念都实现。优先加入 5 个最有工程价值的：

1. `bestmove_stability`
2. `candidate_entropy`
3. `frontier_size`
4. `transposition_density`
5. `dag_compression_estimate`

这 5 个指标可以直接进入阶段 2 的 Top-k 候选稳定性深搜。

