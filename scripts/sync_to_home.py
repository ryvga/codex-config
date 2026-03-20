#!/usr/bin/env python3
"""Sync rendered config and agents into ~/.codex while preserving runtime state."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import tomllib
import re


ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
BUILD_AGENTS_DIR = BUILD_DIR / "agents"
HOME_CODEX = Path.home() / ".codex"
HOME_AGENTS = HOME_CODEX / "agents"
MANIFEST_PATH = HOME_CODEX / ".managed_manifest.json"
BARE_KEY_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")


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


def load_toml(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def deep_merge(managed: object, existing: object) -> object:
    if isinstance(managed, dict) and isinstance(existing, dict):
        merged = dict(existing)
        for key, value in managed.items():
            merged[key] = deep_merge(value, existing.get(key))
        return merged
    return managed


def diff_preserved(managed: object, existing: object, prefix: str = "") -> list[str]:
    preserved: list[str] = []
    if not isinstance(existing, dict):
        return preserved

    managed_dict = managed if isinstance(managed, dict) else {}
    for key, value in existing.items():
        dotted = f"{prefix}.{key}" if prefix else key
        if key not in managed_dict:
            preserved.append(dotted)
            continue
        if isinstance(value, dict) and isinstance(managed_dict[key], dict):
            preserved.extend(diff_preserved(managed_dict[key], value, dotted))
    return preserved


def format_key(key: str) -> str:
    if BARE_KEY_PATTERN.match(key):
        return key
    escaped = key.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def format_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def format_scalar(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return format_string(value)
    raise TypeError(f"Unsupported scalar value: {value!r}")


def format_array(values: list[object]) -> str:
    rendered = []
    for value in values:
        if isinstance(value, list):
            rendered.append(format_array(value))
        elif isinstance(value, dict):
            raise TypeError("Array-of-tables must be handled separately")
        else:
            rendered.append(format_scalar(value))
    return "[" + ", ".join(rendered) + "]"


def serialize_table(data: dict, path: tuple[str, ...] = ()) -> list[str]:
    lines: list[str] = []
    scalar_items: list[tuple[str, object]] = []
    dict_items: list[tuple[str, dict]] = []
    array_of_tables: list[tuple[str, list[dict]]] = []

    for key, value in data.items():
        if isinstance(value, dict):
            dict_items.append((key, value))
        elif isinstance(value, list) and value and all(isinstance(item, dict) for item in value):
            array_of_tables.append((key, value))
        else:
            scalar_items.append((key, value))

    if path:
        lines.append("[" + ".".join(format_key(part) for part in path) + "]")
    for key, value in scalar_items:
        if isinstance(value, list):
            lines.append(f"{format_key(key)} = {format_array(value)}")
        else:
            lines.append(f"{format_key(key)} = {format_scalar(value)}")

    for key, children in array_of_tables:
        for entry in children:
            if lines:
                lines.append("")
            lines.append("[[" + ".".join(format_key(part) for part in (*path, key)) + "]]")
            lines.extend(serialize_table(entry, () ))

    for key, value in dict_items:
        if lines:
            lines.append("")
        lines.extend(serialize_table(value, (*path, key)))
    return lines


def render_toml(data: dict) -> str:
    return "\n".join(serialize_table(data)) + "\n"


def merge_config(build_config: Path, live_config: Path) -> tuple[str, list[str]]:
    managed = load_toml(build_config)
    existing = load_toml(live_config) if live_config.exists() else {}
    merged = deep_merge(managed, existing)
    preserved = sorted(diff_preserved(managed, existing))
    return render_toml(merged), preserved


def main() -> int:
    args = parse_args()
    HOME_CODEX.mkdir(parents=True, exist_ok=True)
    HOME_AGENTS.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    next_manifest = {"config": "config.toml", "agents": []}

    build_config = BUILD_DIR / "config.toml"
    if not build_config.exists():
        raise SystemExit("Missing build/config.toml. Run render_config.py first.")
    live_config = HOME_CODEX / "config.toml"
    merged_config, preserved_keys = merge_config(build_config, live_config)
    print(f"{'Would write' if args.dry_run else 'Writing'} {live_config}")
    if preserved_keys:
        print("Preserving live config keys not managed by the repo:")
        for key in preserved_keys:
            print(f"  - {key}")
    if not args.dry_run:
        live_config.write_text(merged_config, encoding="utf-8")

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
