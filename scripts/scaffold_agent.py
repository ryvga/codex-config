#!/usr/bin/env python3
"""Scaffold a Codex custom agent TOML file."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Codex custom agent TOML file.")
    parser.add_argument("--name", required=True, help="Agent name")
    parser.add_argument("--description", required=True, help="When to use this agent")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--instructions", help="Inline developer instructions")
    group.add_argument("--instructions-file", help="Path to file containing developer instructions")
    parser.add_argument("--model", help="Optional model name")
    parser.add_argument("--reasoning", dest="reasoning_effort", help="Optional model_reasoning_effort")
    parser.add_argument("--sandbox", dest="sandbox_mode", help="Optional sandbox_mode")
    parser.add_argument("--nickname", action="append", default=[], help="Optional nickname candidate")
    parser.add_argument("--output", help="Write to this file instead of stdout")
    parser.add_argument("--force", action="store_true", help="Overwrite --output if it exists")
    return parser.parse_args()


def read_instructions(args: argparse.Namespace) -> str:
    if args.instructions is not None:
        return args.instructions.strip()
    return Path(args.instructions_file).read_text(encoding="utf-8").strip()


def toml_basic(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def toml_multiline(value: str) -> str:
    text = value.replace("\r\n", "\n").strip()
    if "'''" not in text:
        return "'''\n" + text + "\n'''"
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return '"""\n' + escaped + '\n"""'


def render_agent(args: argparse.Namespace, developer_instructions: str) -> str:
    lines = [
        f"name = {toml_basic(args.name)}",
        f"description = {toml_basic(args.description)}",
        f"developer_instructions = {toml_multiline(developer_instructions)}",
    ]

    if args.nickname:
        nickname_list = ", ".join(toml_basic(name) for name in args.nickname)
        lines.append(f"nickname_candidates = [{nickname_list}]")
    if args.model:
        lines.append(f"model = {toml_basic(args.model)}")
    if args.reasoning_effort:
        lines.append(f"model_reasoning_effort = {toml_basic(args.reasoning_effort)}")
    if args.sandbox_mode:
        lines.append(f"sandbox_mode = {toml_basic(args.sandbox_mode)}")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    try:
        developer_instructions = read_instructions(args)
        if not developer_instructions:
            print("Developer instructions cannot be empty.", file=sys.stderr)
            return 1
        content = render_agent(args, developer_instructions)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not args.output:
        sys.stdout.write(content)
        return 0

    output_path = Path(args.output)
    if output_path.exists() and not args.force:
        print(f"Refusing to overwrite existing file: {output_path}", file=sys.stderr)
        return 1
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

