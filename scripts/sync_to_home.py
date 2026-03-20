#!/usr/bin/env python3
"""Sync rendered config and agents into ~/.codex while preserving runtime state."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
BUILD_AGENTS_DIR = BUILD_DIR / "agents"
HOME_CODEX = Path.home() / ".codex"
HOME_AGENTS = HOME_CODEX / "agents"
MANIFEST_PATH = HOME_CODEX / ".managed_manifest.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync managed Codex config into ~/.codex")
    parser.add_argument("--dry-run", action="store_true", help="Show intended changes without writing.")
    return parser.parse_args()


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {"agents": [], "config": None}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def write_file(source: Path, target: Path, dry_run: bool) -> None:
    print(f"{'Would write' if dry_run else 'Writing'} {target}")
    if dry_run:
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def remove_file(target: Path, dry_run: bool) -> None:
    if not target.exists():
        return
    print(f"{'Would remove' if dry_run else 'Removing'} {target}")
    if not dry_run:
        target.unlink()


def main() -> int:
    args = parse_args()
    HOME_CODEX.mkdir(parents=True, exist_ok=True)
    HOME_AGENTS.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    next_manifest = {"config": "config.toml", "agents": []}

    build_config = BUILD_DIR / "config.toml"
    if not build_config.exists():
        raise SystemExit("Missing build/config.toml. Run render_config.py first.")
    write_file(build_config, HOME_CODEX / "config.toml", args.dry_run)

    for source in sorted(BUILD_AGENTS_DIR.glob("*.toml")):
        target = HOME_AGENTS / source.name
        next_manifest["agents"].append(source.name)
        write_file(source, target, args.dry_run)

    for stale in manifest.get("agents", []):
        if stale not in next_manifest["agents"]:
            remove_file(HOME_AGENTS / stale, args.dry_run)

    if args.dry_run:
        print("Dry run complete.")
        return 0

    MANIFEST_PATH.write_text(json.dumps(next_manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

