#!/usr/bin/env python3
"""Bootstrap generated outputs for the repo."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def run(script: str) -> None:
    path = ROOT / "scripts" / script
    subprocess.run([sys.executable, str(path)], check=True)


def main() -> int:
    run("render_config.py")
    run("render_agents.py")
    run("update_registry.py")
    print("Bootstrap complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

