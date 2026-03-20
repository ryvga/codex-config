# Architecture

This repository is a global Codex configuration system, not a repo-local experiment.

## Layers

1. Source layer inside this repo
2. Rendered layer in `build/`
3. Installed layer in `~/.codex`
4. Optional project override layer in `.codex/`

## Design Choices

- Copy/sync install instead of symlinks
- Flat installed `~/.codex/agents/*.toml` for platform fidelity
- Categorized source directories for maintainability
- Conservative `[agents]` runtime defaults
- Explicit role-based prompts instead of a meta-framework

## Routing Philosophy

- Solve directly when the task is simple.
- Route to a planner for risky decomposition, not for every task.
- Use read-heavy specialists before spawning writers.
- Use multiple reviewers only when the result needs independent lenses.
- Keep nested delegation off by default.

