# Project Overrides

Project overrides belong in `.codex/` inside the repository.

## Files

- `.codex/config.toml`
- `.codex/agents/*.toml`

## When To Use Them

- repository-specific workflows
- stricter review or reasoning defaults
- project-local MCP servers
- repo-only specialist prompts

## Trust Behavior

Codex only loads project-scoped `.codex/` config and agents when the project is trusted.

Put trust declarations in the machine-local config layer, not the tracked global base:

```toml
[projects."/absolute/path/to/repo"]
trust_level = "trusted"
```

Templates and examples are included under `templates/` and `examples/project/`.

