# Contributing

## Principles

- Keep agents narrow and opinionated.
- Prefer inheritance over repeated config when agent-specific pinning adds no value.
- Default to `max_depth = 1`.
- Separate read-heavy discovery from write-heavy execution.
- Add a custom agent only when built-in `default`, `worker`, or `explorer` is not enough.

## Workflow

1. Edit source files under `config/`, `agents/`, `standards/`, `templates/`, or `docs/`.
2. Regenerate outputs:

```bash
python3 scripts/render_config.py
python3 scripts/render_agents.py
python3 scripts/update_registry.py
```

3. Validate:

```bash
python3 scripts/validate_repo.py
```

4. Review generated diffs in `build/` and `registry/`.
5. Commit source and generated outputs together.

## Adding An Agent

1. Start from [standards/agent-authoring.md](/home/ryuga/codex-config/standards/agent-authoring.md).
2. Scaffold a draft:

```bash
python3 scripts/scaffold_agent.py \
  --name example_agent \
  --description "Use for a narrow, explicit job." \
  --instructions-file /tmp/example-agent.txt \
  --model gpt-5.4-mini \
  --reasoning medium \
  --sandbox read-only \
  --output agents/research/example_agent.toml
```

3. Ensure the prompt contains all required sections:
  - `Role`
  - `Mission`
  - `Inputs`
  - `Workflow`
  - `Output Contract`
  - `Boundaries`
  - `Escalation`
  - `Failure Conditions`
4. Render and validate.
5. Update or regenerate the registry.

## Model Allocation Rules

- Use `gpt-5.4-mini` for fast, low-cost triage, discovery, narrow scans, and documentation cleanup.
- Use `gpt-5.4` for orchestration, planning, cross-cutting implementation, debugging, and serious review.
- Use `high` reasoning for review, security, edge-case analysis, architecture, and ambiguous debugging.
- Use `medium` as the default.
- Use `low` only when the task is clear and latency matters more than depth.

## Portability Rules

- Do not hardcode machine-specific paths in tracked agent TOMLs.
- Put per-machine trust settings and local MCP endpoints in `config/local.toml`.
- Keep repo scripts Python-stdlib only.

