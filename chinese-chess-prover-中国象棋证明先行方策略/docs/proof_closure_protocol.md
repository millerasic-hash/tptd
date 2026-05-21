# Proof Closure Protocol

这份协议定义“多镜头实验结果如何升级为证明结论”。它的目标不是替代搜索器，而是防止实验报告、Pikafish 分数、DF-PN 结果和数学判断混在一起。

核心原则：

```text
发现可以多镜头。
证明只能闭合。
结论必须分层。
证书必须可独立校验。
```

## 1. 角色定义

### Pikafish

职责：

- 给候选着法排序。
- 给 `score / bestmove / pv / nodes / time / hashfull / wdl` 等观测量。
- 作为 proof cost 的启发式先验。
- 帮助找到更小的证明入口。

禁止：

- 不得把 `score >= T` 写成必胜证明。
- 不得把 `depth N bestmove` 写成数学定理。
- 不得用 PV 代替完整分支证明。

### Prover

职责：

- 按项目规则展开合法着法。
- 处理历史依赖和重复局面。
- 生成 `WIN / LOSS / UNKNOWN` 的证书或搜索摘要。
- 合并转置局面，尽量把树压成 DAG。

Prover 可以使用 Pikafish 排序，但最终结论必须来自规则递推。

### Verifier

职责：

- 独立读取证书。
- 不调用 Pikafish。
- 只根据规则、局面、历史签名和证书内容判断是否闭合。

Verifier 是结论升级的最终入口。

### Closure Orchestrator

也可称为：

```text
Proof Professor
数学联动教授
证明闭合调度器
```

它不是人设，不下棋，不相信分数。它只做调度：

```text
实验观察 -> 假设 -> 证明义务 -> 证明器/反例器任务 -> 校验结果 -> 结论升级或降级
```

每一轮必须输出：

```text
1. 当前最强假设
2. 未闭合证明债
3. 下一次最小实验
```

## 2. 结论等级

所有结论必须落在以下等级之一。

### L0 Observation

经验观察。

允许来源：

- Pikafish 分数。
- MultiPV 排名。
- depth 曲线。
- PV 重复检测。
- 候选熵。
- 节点、时间、hash 使用量。

示例：

```text
在 depth 24 / MultiPV 4 下，c3c4 与 b2e2 均为 +17 cp。
```

禁止升级为：

```text
c3c4 必胜。
```

### L1 Hypothesis

稳定性假设。

允许条件：

- 多个 depth 下排名稳定。
- 多个 MultiPV 设置下没有大幅反转。
- best reply 不剧烈跳动。
- 分数没有随深度系统性下降。
- 没有明显 PV 重复污染。

示例：

```text
c3c4 是下一轮优先证明候选。
```

### L2 Proof Obligation

证明义务。

这是从假设拆出的可执行任务。每条义务必须有：

```text
id
state_key
fen
side_to_move
history_signature
claim
budget
method
exit_condition
```

示例：

```text
PO-0001:
  claim = state after c3c4 is WIN for Red under repetition-loss rule
  method = dfpn
  budget = max_nodes 100000
  exit_condition = certificate_verified or counterexample_found or UNKNOWN
```

### L3 Verified Local Claim

局部已验证结论。

必须满足：

- 有证书。
- Verifier 不调用 Pikafish 也能通过。
- 证书包含完整分支闭合或完整 LOSS 分支覆盖。
- 历史签名没有被省略。

示例：

```text
PO-0001 在给定历史签名下被验证为 WIN。
```

### L4 Reusable Lemma

可复用引理。

必须满足：

- 覆盖一组状态，而不是单一状态。
- 等价类、模式、残局表库或吸引域边界可机器复核。
- 有反例搜索记录。

示例：

```text
某类双车控将局面在重复判负规则下为当前方 WIN。
```

### L5 Theorem

全局定理。

示例：

```text
标准开局红方必胜。
```

当前项目距离 L5 很远。任何 L5 表述必须由大量 L3/L4 结论拼接，并通过根局面证书闭合。

## 3. 证明状态

当前主线规则：

```text
第三次重复，造成者负。
```

证明状态不是单纯棋盘，而是：

```text
E = (board, side_to_move, history_signature)
```

其中：

```text
board = 棋盘子力位置
side_to_move = 当前行棋方
history_signature = 本局已出现基础局面的计数摘要
```

基础局面键：

```text
B = (board, side_to_move)
```

历史签名至少要区分：

```text
B 出现 0 次
B 出现 1 次
B 出现 2 次
```

如果走子后让目标基础局面第 3 次出现，则：

```text
这步棋对走子方立即失败。
```

任何没有 `history_signature` 的实验只能标为：

```text
engine_probe_only
```

不能标为 proof。

## 4. WIN / LOSS 闭合定义

对扩展状态 `E`：

```text
WIN(E)
  iff exists move m:
      m 不造成己方第三次重复失败
      and LOSS(apply(E, m))
```

```text
LOSS(E)
  iff for all legal moves m:
      m 造成己方第三次重复失败
      or WIN(apply(E, m))
```

如果一个节点无法满足上述任一闭合条件，则只能返回：

```text
UNKNOWN
```

`UNKNOWN` 不是和棋，不是失败，也不是反证。

## 5. 多镜头输入

Closure Orchestrator 接受多镜头输入，但每种输入的权重不同。

### 引擎镜头

字段：

```text
score_cp
score_mate
depth
seldepth
bestmove
pv
nodes
time_ms
hashfull
wdl
lowerbound
upperbound
```

用途：

- 候选排序。
- proof cost 估计。
- 异常检测。

不允许：

- 直接生成证明结论。

### 稳定性镜头

字段：

```text
score_curve
rank_curve
best_reply_variants
candidate_entropy
score_variance
```

用途：

- 选择下一轮证明入口。
- 判断是否继续加深。
- 判断是否转向反例搜索。

### 图压缩镜头

字段：

```text
state_key
history_key
transposition_hits
transposition_density
dag_compression_estimate
frontier_size
```

用途：

- 判断证明树是否可以压成 DAG。
- 判断缓存是否有效。
- 估计证书存储成本。

### 证明镜头

字段：

```text
proof_number
disproof_number
expanded_nodes
closed_nodes
certificate_size
verified
```

用途：

- 结论升级。
- 比较不同启发式的真实证明收益。

## 6. 证明义务格式

建议机器可读 JSON 结构：

```json
{
  "id": "PO-0001",
  "created_from": "reports/opening-candidate-probe/opening_candidate_probe_report.json",
  "claim": "WIN",
  "fen": "string",
  "side_to_move": "b",
  "history_signature": "string",
  "rule": "third_repetition_causer_loses",
  "method": "dfpn",
  "budget": {
    "max_depth": 12,
    "max_nodes": 100000,
    "max_seconds": 60
  },
  "engine_hint": {
    "candidate_move": "c3c4",
    "score_cp": 17,
    "depth": 24,
    "multipv": 4
  },
  "status": "PENDING"
}
```

状态只能是：

```text
PENDING
RUNNING
VERIFIED_WIN
VERIFIED_LOSS
COUNTEREXAMPLE
UNKNOWN_BUDGET_EXHAUSTED
INVALID
```

## 7. 证书最低要求

### WIN 证书

必须包含：

```text
当前状态 E
至少一步 winning move
该 move 后的子状态 LOSS 证书
历史签名更新
```

### LOSS 证书

必须包含：

```text
当前状态 E
所有合法走法列表
每一步的结论：
  - 造成走子方第三次重复失败
  - 或进入对手 WIN 证书
```

### 禁止的证书

以下证书无效：

```text
只包含 bestmove
只包含 PV
只包含 score
只包含部分失败分支
省略 history_signature
调用 Pikafish 才能验证
```

## 8. 升级和降级规则

### Observation -> Hypothesis

需要至少满足两条：

- 跨 depth 排名稳定。
- 跨 MultiPV 稳定。
- 分数没有明显向 0 收敛。
- best reply 变化少。
- 没有重复污染。

### Hypothesis -> Proof Obligation

需要：

- 明确具体局面。
- 明确历史签名。
- 明确 `WIN / LOSS` 目标。
- 明确资源预算。

### Proof Obligation -> Verified Claim

需要：

- Prover 输出证书。
- Verifier 通过。
- 报告记录命令、预算、耗时、节点数。

### Verified Claim -> Reusable Lemma

需要：

- 证明覆盖一类状态。
- 有可复核的等价类或模式。
- 通过反例搜索。

### 降级规则

出现以下情况必须降级：

- 高分候选随深度向 0 收敛。
- best reply 大幅跳动。
- PV 出现早期重复污染。
- 证书省略历史签名。
- Verifier 失败。
- 同一假设找到反例。

## 9. 反例优先原则

任何强假设都必须先尝试找反例。

示例：

```text
假设：score >= 300 cp 的局面更容易证明为 WIN。
反例任务：寻找 score >= 300 但 DF-PN 在同预算下无法闭合或闭合为 LOSS 的局面。
```

如果找到反例：

```text
阈值假设降级为经验相关性。
```

如果找不到反例：

```text
只能提升置信度，不能直接升级为定理。
```

## 10. 每轮闭合循环

每一轮实验必须按这个循环执行：

```text
1. 读取上一轮 report.json
2. 选出最小候选集
3. 生成 proof obligations
4. 运行 prover
5. 运行 verifier
6. 运行反例搜索
7. 写入 closure_report.md/json
8. 决定升级、降级或继续 UNKNOWN
```

每轮最多只回答一个问题：

```text
这批候选里，哪一个最值得进入更贵的证明？
```

或：

```text
这个局部命题是否已经被证书闭合？
```

不要在同一轮同时追求全局定理。

## 11. 当前项目的下一步

基于当前 `opening-candidate-probe` 结果，下一步不直接证明标准开局。先生成四个 proof obligations：

```text
PO-c3c4-d24
PO-b2e2-d24
PO-c0e2-d24
PO-h2e2-control-d24
```

其中 `h2e2` 是对照组。

建议预算：

```text
max_depth = 10, 12, 14
max_nodes = 10000, 100000
threads = 1
hash = 128 MB
```

输出目录：

```text
reports/proof-closure-round-001/
```

最低产物：

```text
obligations.json
closure_report.json
closure_report.md
certificates/
counterexamples/
command.txt
```

如果四个义务全部 UNKNOWN，也不是失败。下一轮应比较：

```text
哪个候选的 proof_number / disproof_number / expanded_nodes 更好
哪个候选更适合继续投入资源
哪个候选应被降级
```

## 12. 结论

这个协议把项目从“Pikafish 跑分”推进到“证明闭合实验”：

```text
Pikafish 负责找到方向。
Prover 负责尝试闭合。
Verifier 负责确认闭合。
Closure Orchestrator 负责决定下一笔证明债。
```

在这个协议下，实验可以小资源迭代，也可以复用缓存和证书；但任何数学结论都必须通过证书闭合。
