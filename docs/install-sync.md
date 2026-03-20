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

