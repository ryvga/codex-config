# Agent Catalog

| Name | Category | Model | Reasoning | Sandbox | Description |
| --- | --- | --- | --- | --- | --- |
| agent_architect | core | gpt-5.4 | high | workspace-write | Use to evaluate, improve, extend, or refactor the global Codex agent system itself, including prompts, routing, standards, and model allocation. |
| api_reviewer | quality | gpt-5.4 | high | read-only | Use for API and contract review covering request and response shapes, schema changes, compatibility, and consumer breakage risk. |
| architecture_planner | planning | gpt-5.4 | high | read-only | Use for architecture-level planning involving interfaces, boundaries, migrations, compatibility, and cross-system design decisions. |
| chief_engineer | core | gpt-5.4 | high | workspace-write | Use as the master orchestrator for ambiguous, high-value, or multi-step engineering work that needs decomposition, routing, and a coherent final result. |
| codebase_discoverer | research | gpt-5.4-mini | medium | read-only | Use for fast read-heavy discovery of repository structure, entrypoints, ownership boundaries, and likely change locations. |
| debugger | coding | gpt-5.4 | high | workspace-write | Use for root-cause analysis and fixes when behavior is failing, symptoms are noisy, or logs and code must be traced together. |
| deep_scanner | research | gpt-5.4 | medium | read-only | Use for cross-file, dependency, and control-flow analysis when the work depends on understanding interactions across a larger slice of the system. |
| delivery_planner | planning | gpt-5.4 | medium | read-only | Use for execution sequencing, release planning, rollout strategy, and dependency ordering for engineering work. |
| docs_synthesizer | research | gpt-5.4-mini | medium | read-only | Use for turning code, plans, and research findings into concise internal documentation, migration notes, or knowledge summaries. |
| implementation_engineer | coding | gpt-5.4 | medium | workspace-write | Use for general coding work: features, bug fixes, and moderate-scope edits that need pragmatic implementation and verification. |
| incident_planner | planning | gpt-5.4 | high | read-only | Use for debugging and incident response planning when failure analysis, containment, and verification need a structured path. |
| master_planner | planning | gpt-5.4 | high | read-only | Use for top-level decomposition of substantial engineering work into executable phases, specialists, risks, and validation. |
| performance_reviewer | quality | gpt-5.4 | high | read-only | Use for performance review of latency, throughput, query patterns, memory pressure, and algorithmic cost. |
| rails_specialist | specialists | gpt-5.4 | medium | workspace-write | Use for Rails-focused implementation and review work involving models, controllers, transactions, callbacks, routing, and framework conventions. |
| refactor_engineer | coding | gpt-5.4 | high | workspace-write | Use for behavior-preserving refactors that improve structure, reduce coupling, or simplify implementation without changing intended behavior. |
| refactor_planner | planning | gpt-5.4 | high | read-only | Use for behavior-safe refactor planning, including slicing, dependency mapping, and regression control. |
| release_docs_writer | delivery | gpt-5.4-mini | medium | workspace-write | Use for changelogs, migration notes, release notes, and upgrade guidance derived from real code and interface changes. |
| reliability_reviewer | quality | gpt-5.4 | high | read-only | Use for resilience and edge-case review covering failure handling, retries, fallbacks, state transitions, and rollout risk. |
| repo_operator | delivery | gpt-5.4-mini | medium | workspace-write | Use for git and GitHub workflow work such as branch hygiene, commit planning, release prep, and repository operations. |
| reviewer | quality | gpt-5.4 | high | read-only | Use for general code review focused on correctness, regressions, missing tests, and maintainability risks. |
| ruby_specialist | specialists | gpt-5.4 | medium | workspace-write | Use for Ruby-focused implementation and review work that benefits from language-specific idioms, tradeoffs, and failure patterns. |
| security_reviewer | quality | gpt-5.4 | high | read-only | Use for security-focused review of authentication, authorization, injection risk, data handling, secret exposure, and trust boundaries. |
| surgical_editor | coding | gpt-5.4-mini | low | workspace-write | Use for tiny, explicit, low-risk file edits where speed and precision matter more than broad reasoning. |
| task_router | core | gpt-5.4-mini | low | read-only | Use for cheap task triage when the main question is which specialist or workflow should handle the work. |
| test_author | coding | gpt-5.4 | medium | workspace-write | Use for authoring or strengthening tests around changed behavior, regressions, edge cases, and safety boundaries. |
| web_researcher | research | gpt-5.4 | medium | read-only | Use for authoritative web research, source comparison, and citation-backed synthesis when information may be current or unstable. |
