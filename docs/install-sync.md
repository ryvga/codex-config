# Install And Sync

## Why Copy/Sync

The repo is designed to render and copy managed files into `~/.codex`:

- portable across operating systems
- safe for runtime state
- easy to version and roll back
- avoids making `~/.codex` the git repository

## Managed Targets

- `~/.codex/config.toml`
- `~/.codex/agents/*.toml`

## Config Merge Behavior

`sync_to_home.py` does not blindly replace the live `~/.codex/config.toml`.

It deep-merges the rendered repo config into the existing live config:

- repo-managed keys win when both sides define the same key
- live-only machine-specific keys are preserved
- nested tables are merged recursively

This preserves entries such as:

- `projects.<path>.trust_level`
- `mcp_servers.*`
- `notice.model_migrations`
- other local-only settings not managed by the repo

## Preserved Targets

- auth, history, sessions, memories, sqlite databases, logs, caches, temp files

## Commands

```bash
python3 scripts/render_config.py
python3 scripts/render_agents.py
python3 scripts/update_registry.py
python3 scripts/validate_repo.py
python3 scripts/sync_to_home.py --dry-run
python3 scripts/sync_to_home.py
```

The sync script writes a manifest so it can safely prune stale managed agent files on later runs.
