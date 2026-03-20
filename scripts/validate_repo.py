#!/usr/bin/env python3
"""Validate config, agents, and generated outputs."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_MODELS = {"gpt-5.4", "gpt-5.4-mini"}
ALLOWED_REASONING = {"low", "medium", "high"}
ALLOWED_SANDBOX = {"read-only", "workspace-write", "danger-full-access"}
REQUIRED_SECTIONS = [
    "Role",
    "Mission",
    "Inputs",
    "Workflow",
    "Output Contract",
    "Boundaries",
    "Escalation",
    "Failure Conditions",
]


def load_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def validate_config(errors: list[str], warnings: list[str]) -> None:
    build_config = ROOT / "build" / "config.toml"
    if not build_config.exists():
        errors.append("Missing build/config.toml. Run render_config.py first.")
        return
    data = load_toml(build_config)
    agents = data.get("agents")
    if not isinstance(agents, dict):
        errors.append("build/config.toml is missing [agents].")
        return
    if agents.get("max_depth") != 1:
        warnings.append("agents.max_depth is not 1; deeper nesting increases coordination risk.")
    if agents.get("max_threads", 0) > 6:
        warnings.append("agents.max_threads is above the documented default of 6.")


def validate_agent(path: Path, errors: list[str]) -> None:
    data = load_toml(path)
    for key in ("name", "description", "developer_instructions"):
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path.relative_to(ROOT)} missing or invalid {key}")

    model = data.get("model")
    if model not in ALLOWED_MODELS:
        errors.append(f"{path.relative_to(ROOT)} has unsupported model {model!r}")

    reasoning = data.get("model_reasoning_effort")
    if reasoning not in ALLOWED_REASONING:
        errors.append(f"{path.relative_to(ROOT)} has unsupported reasoning {reasoning!r}")

    sandbox = data.get("sandbox_mode")
    if sandbox not in ALLOWED_SANDBOX:
        errors.append(f"{path.relative_to(ROOT)} has unsupported sandbox {sandbox!r}")

    instructions = data.get("developer_instructions", "")
    for section in REQUIRED_SECTIONS:
        if section not in instructions:
            errors.append(f"{path.relative_to(ROOT)} is missing instruction section {section!r}")


def validate_registry(errors: list[str]) -> None:
    registry_path = ROOT / "registry" / "agents.json"
    if not registry_path.exists():
        errors.append("Missing registry/agents.json. Run update_registry.py first.")
        return
    payload = json.loads(registry_path.read_text(encoding="utf-8"))
    names = [agent["name"] for agent in payload.get("agents", [])]
    if len(names) != len(set(names)):
        errors.append("registry/agents.json contains duplicate agent names.")


def validate_with_skill_validator(errors: list[str]) -> None:
    validator = Path("/home/ryuga/.codex/skills/codex-subagent-builder/scripts/validate_subagent_setup.py")
    if not validator.exists():
        errors.append("Missing codex-subagent-builder validator script.")
        return

    result = subprocess.run(
        [
            sys.executable,
            str(validator),
            str(ROOT / "build" / "agents"),
            "--config",
            str(ROOT / "build" / "config.toml"),
        ],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        errors.append(result.stdout.strip() or result.stderr.strip() or "Skill validator failed.")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    validate_config(errors, warnings)
    for path in sorted((ROOT / "agents").rglob("*.toml")):
        validate_agent(path, errors)
    validate_registry(errors)
    validate_with_skill_validator(errors)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
