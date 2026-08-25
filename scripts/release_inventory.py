#!/usr/bin/env python3
"""Emit the deterministic source-tree-v1 inventory without executing plugin code."""

from __future__ import annotations

import fnmatch
import hashlib
import json
import stat
import sys
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


def main() -> int:
    recipe = json.loads(RECIPE_PATH.read_text(encoding="utf-8"))
    source = ROOT / recipe["source"]
    files: list[dict[str, object]] = []
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
        body = path.read_bytes()
        files.append(
            {
                "path": relative,
                "mode": "0755" if mode & 0o111 else "0644",
                "size": len(body),
                "sha256": hashlib.sha256(body).hexdigest(),
            }
        )
    canonical_files = json.dumps(files, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    output = {
        "schemaVersion": 1,
        "recipe": {"id": recipe["id"], "revision": recipe["revision"]},
        "source": recipe["source"],
        "inventoryDigest": "sha256:" + hashlib.sha256(canonical_files).hexdigest(),
        "files": files,
    }
    json.dump(output, sys.stdout, ensure_ascii=False, separators=(",", ":"))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
