# Divergence Log

## Agent Config Indirection

- Skill materials emphasize standalone custom-agent TOMLs.
- Official config reference also supports role config indirection via `agents.<name>.config_file`.
- Final choice: standalone TOMLs only, to keep the installed system transparent and portable.

## Runtime Dependency On Skills

- The local skill provides scaffolding and validation helpers.
- Official Codex behavior does not require a skill dependency at runtime.
- Final choice: use the skill during authoring and validation, but ship repo-local scripts for long-term portability.

## Model Pinning

- Skill guidance encourages pinning where role-specific behavior matters.
- Official docs allow inheritance and Codex-selected balancing when fields are omitted.
- Final choice: pin model and reasoning for each production agent in this cluster because explicit routing is part of the system design.

