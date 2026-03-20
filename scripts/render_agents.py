#!/usr/bin/env python3
"""Flatten categorized source agents into build/agents."""

from __future__ import annotations

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
AGENTS_DIR = ROOT / "agents"
BUILD_AGENTS_DIR = ROOT / "build" / "agents"


def iter_agent_files() -> list[Path]:
    return sorted(path for path in AGENTS_DIR.rglob("*.toml") if path.is_file())


def main() -> int:
    BUILD_AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for stale in BUILD_AGENTS_DIR.glob("*.toml"):
        stale.unlink()

    seen: dict[str, Path] = {}
    for path in iter_agent_files():
        name = path.name
        if name in seen:
            raise SystemExit(f"Agent filename collision: {path} and {seen[name]}")
        seen[name] = path
        shutil.copy2(path, BUILD_AGENTS_DIR / name)
        print(f"Rendered {path.relative_to(ROOT)} -> build/agents/{name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
