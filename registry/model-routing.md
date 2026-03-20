# Model Routing

| Agent | Model | Reasoning | Intended use |
| --- | --- | --- | --- |
| agent_architect | gpt-5.4 | high | Use to evaluate, improve, extend, or refactor the global Codex agent system itself, including prompts, routing, standards, and model allocation. |
| api_reviewer | gpt-5.4 | high | Use for API and contract review covering request and response shapes, schema changes, compatibility, and consumer breakage risk. |
| architecture_planner | gpt-5.4 | high | Use for architecture-level planning involving interfaces, boundaries, migrations, compatibility, and cross-system design decisions. |
| chief_engineer | gpt-5.4 | high | Use as the master orchestrator for ambiguous, high-value, or multi-step engineering work that needs decomposition, routing, and a coherent final result. |
| codebase_discoverer | gpt-5.4-mini | medium | Use for fast read-heavy discovery of repository structure, entrypoints, ownership boundaries, and likely change locations. |
| debugger | gpt-5.4 | high | Use for root-cause analysis and fixes when behavior is failing, symptoms are noisy, or logs and code must be traced together. |
| deep_scanner | gpt-5.4 | medium | Use for cross-file, dependency, and control-flow analysis when the work depends on understanding interactions across a larger slice of the system. |
| delivery_planner | gpt-5.4 | medium | Use for execution sequencing, release planning, rollout strategy, and dependency ordering for engineering work. |
| docs_synthesizer | gpt-5.4-mini | medium | Use for turning code, plans, and research findings into concise internal documentation, migration notes, or knowledge summaries. |
| implementation_engineer | gpt-5.4 | medium | Use for general coding work: features, bug fixes, and moderate-scope edits that need pragmatic implementation and verification. |
| incident_planner | gpt-5.4 | high | Use for debugging and incident response planning when failure analysis, containment, and verification need a structured path. |
| master_planner | gpt-5.4 | high | Use for top-level decomposition of substantial engineering work into executable phases, specialists, risks, and validation. |
| performance_reviewer | gpt-5.4 | high | Use for performance review of latency, throughput, query patterns, memory pressure, and algorithmic cost. |
| rails_specialist | gpt-5.4 | medium | Use for Rails-focused implementation and review work involving models, controllers, transactions, callbacks, routing, and framework conventions. |
| refactor_engineer | gpt-5.4 | high | Use for behavior-preserving refactors that improve structure, reduce coupling, or simplify implementation without changing intended behavior. |
| refactor_planner | gpt-5.4 | high | Use for behavior-safe refactor planning, including slicing, dependency mapping, and regression control. |
| release_docs_writer | gpt-5.4-mini | medium | Use for changelogs, migration notes, release notes, and upgrade guidance derived from real code and interface changes. |
| reliability_reviewer | gpt-5.4 | high | Use for resilience and edge-case review covering failure handling, retries, fallbacks, state transitions, and rollout risk. |
| repo_operator | gpt-5.4-mini | medium | Use for git and GitHub workflow work such as branch hygiene, commit planning, release prep, and repository operations. |
| reviewer | gpt-5.4 | high | Use for general code review focused on correctness, regressions, missing tests, and maintainability risks. |
| ruby_specialist | gpt-5.4 | medium | Use for Ruby-focused implementation and review work that benefits from language-specific idioms, tradeoffs, and failure patterns. |
| security_reviewer | gpt-5.4 | high | Use for security-focused review of authentication, authorization, injection risk, data handling, secret exposure, and trust boundaries. |
| surgical_editor | gpt-5.4-mini | low | Use for tiny, explicit, low-risk file edits where speed and precision matter more than broad reasoning. |
| task_router | gpt-5.4-mini | low | Use for cheap task triage when the main question is which specialist or workflow should handle the work. |
| test_author | gpt-5.4 | medium | Use for authoring or strengthening tests around changed behavior, regressions, edge cases, and safety boundaries. |
| web_researcher | gpt-5.4 | medium | Use for authoritative web research, source comparison, and citation-backed synthesis when information may be current or unstable. |
