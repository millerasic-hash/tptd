# Experimental proof-number helper for Pikafish analysis

This is a draft proposal, not a claim that engine centipawn scores prove wins.

## Purpose

Add an out-of-core, optional proof helper around Pikafish:

1. Use Pikafish only for move ordering and proof-cost priors.
2. Use a small independent legal-move generator and certificate verifier for bounded proofs.
3. Calibrate, under fixed resources, which score bands tend to close into proofs on a selected benchmark set.

## Why outside the core engine first

The module is intentionally external because:

- proof search has different correctness requirements than playing strength;
- repetition and graph-history interaction need stricter treatment than a normal TT cutoff;
- the current implementation is a bounded experimental certificate generator, not a full solver.

## Current method

- Proof-number style recurrence:
  - `pn`: effort to prove side-to-move is winning.
  - `dn`: effort to disprove side-to-move is winning.
- GHI-safe transposition key:
  - board state
  - remaining depth
  - capped repetition history signature
- Pikafish score integration:
  - `mate N` and `cp` values map to proof-cost priors only.
  - scores never bypass certificate verification.
- Calibration command:
  - runs fixed sample positions under fixed depth/node/time budgets;
  - reports a sample/resource-bounded threshold;
  - explicitly avoids universal claims.

## Local 1024x12 baseline

Command shape:

```bash
python3 run_1024x12_report.py \
  --sample-count 1024 \
  --source-plies 2 \
  --depth 12 \
  --max-nodes 1024 \
  --engine-depth 1 \
  --out-dir reports/1024x12
```

Observed result:

- `UNKNOWN: 1024`
- `WIN: 0`
- `LOSS: 0`
- score range: `-119` to `428`
- runtime: `975.034` seconds
- `threshold_all_above_proven_win: null`

Interpretation: this budget is enough to exercise the pipeline, but not enough
to prove opening-near positions. No centipawn threshold is justified by this
baseline.

## Acceptance bar before upstreaming

- Replace the Python move generator with direct engine legal move export or a generated differential test suite.
- Add large perft coverage.
- Add repetition-rule compatibility tests.
- Add benchmark suites for proof closure rate versus node budget.
- Keep proof code optional and disabled by default.

## Non-goals

- This does not solve Xiangqi.
- This does not turn a centipawn threshold into a theorem.
- This does not replace endgame tablebases or formal proof certificates.
