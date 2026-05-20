# Pikafish 1024x48 Red WDL Playout Report

This is bounded engine self-play from generated legal samples, not a game-theoretic solution.

## Configuration

- Samples: `1024`.
- Sample source: `BFS legal positions from standard start, source_plies=2`.
- Max plies per sample: `48`.
- Repetition limit: `3` appearances per state.
- Pikafish engine: `tools/pikafish/MacOS/pikafish-apple-silicon`.
- Pikafish engine depth: `1`.
- Pikafish movetime: `20 ms`.
- Runtime seconds: `93.179`.

## Red WDL

- Red wins: `94`.
- Draws: `865`.
- Red losses: `65`.

## Termination Reasons

- `black_checkmated`: `94`.
- `max_plies`: `782`.
- `red_checkmated`: `65`.
- `repetition`: `83`.

## Plies

- Average plies: `45.4`.
- Median plies: `48.0`.
- Max plies observed: `48`.

## Red Initial Score

- Min: `-125`.
- Max: `433`.
- Average: `36.07`.

## Interpretation

A draw here means the playout did not reach checkmate inside the fixed 48-ply horizon, or repeated a state under this experiment's repetition rule. It is not a formal draw proof.
