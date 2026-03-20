# Codex Config

Production-grade global Codex configuration and custom agent system.

This repository is the source of truth for a user-level Codex setup that can be cloned onto any machine, rendered into `~/.codex`, and extended with project-specific `.codex/` overrides when needed.

## What This Repo Manages

- Durable user-level defaults in `~/.codex/config.toml`
- Personal custom agents in `~/.codex/agents/`
- Versioned agent standards, routing guidance, and model allocation
- Scripts for render, validation, registry generation, and sync
- Templates and examples for project-level `.codex/config.toml` and `.codex/agents/`

## What This Repo Does Not Manage

- `~/.codex/auth.json`
- `~/.codex/history.jsonl`
- `~/.codex/log*`
- `~/.codex/state*.sqlite`
- `~/.codex/sessions/`
- `~/.codex/memories/`
- Other runtime state files created by Codex

## Operating Model

- Repo source of truth:
  - `config/base.toml`
  - `agents/**/*.toml`
  - `standards/*.md`
  - `templates/*`
  - `docs/*`
- Generated outputs:
  - `build/config.toml`
  - `build/agents/*.toml`
  - `registry/agents.json`
  - `registry/agent-catalog.md`
  - `registry/model-routing.md`
- Installed runtime targets:
  - `~/.codex/config.toml`
  - `~/.codex/agents/*.toml`

## Quick Start

```bash
cd ~/codex-config
python3 scripts/bootstrap.py
python3 scripts/render_config.py
python3 scripts/render_agents.py
python3 scripts/update_registry.py
python3 scripts/validate_repo.py
python3 scripts/sync_to_home.py --dry-run
python3 scripts/sync_to_home.py
```

Shell and PowerShell wrappers are available:

```bash
./scripts/bootstrap.sh
```

```powershell
./scripts/bootstrap.ps1
```

## Defaults

- `model = "gpt-5.4"`
- `model_reasoning_effort = "medium"`
- `plan_mode_reasoning_effort = "high"`
- `approval_policy = "on-request"`
- `sandbox_mode = "workspace-write"`
- `web_search = "cached"`
- `[agents].max_threads = 6`
- `[agents].max_depth = 1`
- `[agents].job_max_runtime_seconds = 1800`

The global baseline is intentionally conservative on depth and concurrency. Most routing and discovery is parallelized; nested delegation is not.

## Global Versus Project Scope

Use the global layer for defaults that should travel across repositories and machines:

- model defaults
- reasoning defaults
- shared personal agents
- common safety and runtime limits

Use a project `.codex/` layer for repository-specific behavior:

- repo MCP servers
- repo-specific agent prompts
- tighter sandbox roots
- stronger review defaults for a sensitive codebase

Project `.codex/` layers only load when the project is trusted by Codex. See [docs/project-overrides.md](/home/ryuga/codex-config/docs/project-overrides.md).

## Agent System

The cluster is organized by responsibility:

- Core orchestration
- Planning
- Research and discovery
- Coding and editing
- Quality and review
- Language specialists
- Delivery and repo operations

The orchestrator is not a blind fan-out layer. It solves simple tasks directly, uses read-heavy specialists before writers, and escalates to planners or deep reviewers only when the risk justifies the cost.

See:

- [docs/architecture.md](/home/ryuga/codex-config/docs/architecture.md)
- [docs/skill-usage.md](/home/ryuga/codex-config/docs/skill-usage.md)
- [registry/agent-catalog.md](/home/ryuga/codex-config/registry/agent-catalog.md)
- [registry/model-routing.md](/home/ryuga/codex-config/registry/model-routing.md)

## Installation Strategy

The default install mode is copy/sync render, not symlinks:

- safer across macOS, Linux, and Windows
- keeps runtime state in `~/.codex`
- avoids turning `~/.codex` into a git repo
- allows a clean managed-files manifest for safe pruning

See [docs/install-sync.md](/home/ryuga/codex-config/docs/install-sync.md).

## Project Override Templates

- [templates/project.config.toml](/home/ryuga/codex-config/templates/project.config.toml)
- [templates/project.agent.toml](/home/ryuga/codex-config/templates/project.agent.toml)
- [examples/project/.codex/config.toml](/home/ryuga/codex-config/examples/project/.codex/config.toml)

## Validation

```bash
python3 scripts/validate_repo.py
```

This checks:

- required custom-agent fields
- allowed model and reasoning values
- required instruction sections
- config renderability
- `[agents]` defaults and warnings
- generated registry consistency

## GitHub Workflow

Local initialization and commits are ready now. Remote creation requires `gh auth login` first.

```bash
cd ~/codex-config
gh auth login
gh repo create codex-config --private --source=. --remote=origin --push
```

See [docs/github-workflow.md](/home/ryuga/codex-config/docs/github-workflow.md) for the local commit structure and the current auth constraint.

## Sources

Primary sources are documented in [docs/sources.md](/home/ryuga/codex-config/docs/sources.md), including:

- OpenAI Codex subagents docs
- OpenAI Codex configuration docs
- the local `codex-subagent-builder` skill materials used during implementation
