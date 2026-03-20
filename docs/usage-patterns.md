# Usage Patterns

## Simple fix

- Use the main session directly or the `implementation_engineer`.

## Large feature

- `chief_engineer` -> `master_planner` -> discovery agents -> implementation -> review agents as needed

## Incident

- `chief_engineer` -> `incident_planner` -> `debugger` -> `reliability_reviewer`

## Refactor

- `chief_engineer` -> `refactor_planner` -> `refactor_engineer` -> `reviewer` or `api_reviewer`

## Security-sensitive change

- `chief_engineer` -> implementation path -> `security_reviewer`

## Repo evolution

- `agent_architect` for catalog changes, routing improvements, prompt tightening, and model-cost rebalancing

