# How `codex-subagent-builder` Was Used

This repository used the local `codex-subagent-builder` skill as an implementation accelerator, not as a runtime dependency.

## Files Used

- [SKILL.md](/home/ryuga/.codex/skills/codex-subagent-builder/SKILL.md)
- [official-subagent-guidance.md](/home/ryuga/.codex/skills/codex-subagent-builder/references/official-subagent-guidance.md)
- [scaffold_custom_agent.py](/home/ryuga/.codex/skills/codex-subagent-builder/scripts/scaffold_custom_agent.py)
- [validate_subagent_setup.py](/home/ryuga/.codex/skills/codex-subagent-builder/scripts/validate_subagent_setup.py)

## How It Helped

- Confirmed the documented global and project agent locations.
- Confirmed the required custom-agent TOML fields and common optional fields.
- Reinforced the default-safe guidance for `[agents].max_depth = 1`.
- Reinforced the design rule to keep agents narrow and avoid parallel write-heavy fan-out.
- Provided a reliable scaffold for agent TOML generation.
- Provided a validator that was integrated into the repo validation flow.

## Concrete Usage In This Repo

- The skill's `scaffold_custom_agent.py` script was used directly during implementation to regenerate selected agent files from prompt text, proving the catalog can be scaffolded with the helper rather than only hand-written.
- The skill's `validate_subagent_setup.py` script is invoked by [scripts/validate_repo.py](/home/ryuga/codex-config/scripts/validate_repo.py) against the rendered `build/agents/` catalog and `build/config.toml`.
- A repo-local [scripts/scaffold_agent.py](/home/ryuga/codex-config/scripts/scaffold_agent.py) was added so this repository remains portable even on machines where the local skill is absent.

## Source-Of-Truth Rule

The official OpenAI Codex docs win if they conflict with the skill's distilled guidance. This repository follows that rule.

