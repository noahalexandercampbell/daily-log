"""Command-line interface for daily-log."""

from __future__ import annotations

import argparse
from pathlib import Path


def _load_entries(path: Path) -> list[str]:
    if not path.exists():
        raise SystemExit(f"path does not exist: {path}")
    if not path.is_file():
        raise SystemExit(f"path is not a file: {path}")
    return [line for line in path.read_text().splitlines() if line.strip()]


def review(path: str) -> int:
    entries = _load_entries(Path(path))
    print(f"entries: {len(entries)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="daily-log")
    parser.add_argument("command", choices=["review"])
    parser.add_argument("path")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "review":
        return review(args.path)
    raise SystemExit(f"unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
