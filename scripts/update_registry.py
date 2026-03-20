#!/usr/bin/env python3
"""Generate agent registry JSON and markdown from source agent files."""

from __future__ import annotations

import json
from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"
REGISTRY_DIR = ROOT / "registry"


def load_agent(path: Path) -> dict:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    data["category"] = path.parent.name
    data["source_path"] = str(path.relative_to(ROOT))
    return data


def iter_agents() -> list[dict]:
    agents = [load_agent(path) for path in sorted(AGENTS_DIR.rglob("*.toml"))]
    return sorted(agents, key=lambda agent: agent["name"])


def write_json(agents: list[dict]) -> None:
    payload = {"agents": agents}
    path = REGISTRY_DIR / "agents.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_catalog(agents: list[dict]) -> None:
    lines = [
        "# Agent Catalog",
        "",
        "| Name | Category | Model | Reasoning | Sandbox | Description |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for agent in agents:
        lines.append(
            "| {name} | {category} | {model} | {reasoning} | {sandbox} | {description} |".format(
                name=agent["name"],
                category=agent["category"],
                model=agent.get("model", "inherit"),
                reasoning=agent.get("model_reasoning_effort", "inherit"),
                sandbox=agent.get("sandbox_mode", "inherit"),
                description=agent["description"].replace("|", "\\|"),
            )
        )
    (REGISTRY_DIR / "agent-catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_model_routing(agents: list[dict]) -> None:
    lines = [
        "# Model Routing",
        "",
        "| Agent | Model | Reasoning | Intended use |",
        "| --- | --- | --- | --- |",
    ]
    for agent in agents:
        lines.append(
            "| {name} | {model} | {reasoning} | {description} |".format(
                name=agent["name"],
                model=agent.get("model", "inherit"),
                reasoning=agent.get("model_reasoning_effort", "inherit"),
                description=agent["description"].replace("|", "\\|"),
            )
        )
    (REGISTRY_DIR / "model-routing.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    agents = iter_agents()
    write_json(agents)
    write_catalog(agents)
    write_model_routing(agents)
    print(f"Updated registry for {len(agents)} agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

