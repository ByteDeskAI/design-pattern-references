#!/usr/bin/env python3
"""Stage the reviewed source tree for deterministic ByteDesk publication."""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECIPE_PATH = ROOT / "packaging" / "source-tree-v1.json"


def excluded(relative: str, patterns: list[str]) -> bool:
    parts = relative.split("/")
    return any(
        fnmatch.fnmatch(relative, pattern)
        or (pattern == ".in_use" and ".in_use" in parts)
        or (pattern == "**/__pycache__/**" and "__pycache__" in parts)
        for pattern in patterns
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="staging directory; defaults to the reviewed recipe output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    recipe = json.loads(RECIPE_PATH.read_text(encoding="utf-8"))
    source = (ROOT / recipe["source"]).resolve()
    output = Path(args.output).resolve() if args.output else (ROOT / recipe["output"]).resolve()
    if output == source or source in output.parents:
        raise SystemExit("release output may not replace or nest inside the authority source")
    if output.exists():
        if not args.output and output == (ROOT / "dist" / "design-patterns").resolve():
            shutil.rmtree(output)
        else:
            raise SystemExit(f"release output already exists: {output}")
    output.mkdir(parents=True)
    copied = 0
    for path in sorted(source.rglob("*"), key=lambda item: item.as_posix()):
        relative = path.relative_to(source).as_posix()
        if excluded(relative, recipe["exclude"]):
            continue
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise SystemExit(f"release source contains a symlink: {relative}")
        if path.is_dir():
            continue
        if not stat.S_ISREG(mode):
            raise SystemExit(f"release source contains a special file: {relative}")
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(path.read_bytes())
        os.chmod(destination, 0o755 if mode & 0o111 else 0o644)
        copied += 1
    if copied == 0:
        raise SystemExit("release source contains no files")
    print(f"staged {copied} files at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
