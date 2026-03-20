# Planning Standards

All planning agents return:

1. Objectives
2. Assumptions
3. Constraints
4. Risks
5. Execution Steps
6. Validation
7. Rollback or Fallback

Planning should scale with risk:

- No planner for trivial local changes.
- Lightweight plan for medium-scope implementation.
- Deep plan for architecture, incidents, cross-cutting refactors, risky releases, or conflicting evidence.

