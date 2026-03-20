# Agent Authoring Conventions

Every custom agent TOML must include:

- `name`
- `description`
- `developer_instructions`

Every `developer_instructions` block should include these labeled sections:

- `Role`
- `Mission`
- `Inputs`
- `Workflow`
- `Output Contract`
- `Boundaries`
- `Escalation`
- `Failure Conditions`

Authoring rules:

- One primary job per agent.
- Keep descriptions selection-oriented.
- Keep instructions operational.
- Pin `model`, `model_reasoning_effort`, or `sandbox_mode` only when the role clearly benefits.
- Prefer read-only agents for review, research, discovery, and planning.
- Keep write-heavy agents scoped and explicit.
- Do not hide multi-agent protocols inside vague prompts.

