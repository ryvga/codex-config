#!/usr/bin/env python3
"""Render build/config.toml from tracked base and optional local overlay."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
BUILD_DIR = ROOT / "build"


def main() -> int:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    base = (CONFIG_DIR / "base.toml").read_text(encoding="utf-8").strip()
    parts = [base]

    local_path = CONFIG_DIR / "local.toml"
    if local_path.exists():
        parts.append(local_path.read_text(encoding="utf-8").strip())

    rendered = "\n\n".join(part for part in parts if part) + "\n"
    target = BUILD_DIR / "config.toml"
    target.write_text(rendered, encoding="utf-8")
    print(f"Wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
