#!/usr/bin/env python3
"""Validate a Project Brain OKF-style bundle using only Python stdlib.

Checks:
- every concept markdown file has YAML-like frontmatter
- required frontmatter keys: type, title, description
- reserved index.md/log.md are allowed without frontmatter
- local markdown links point to existing files or directories

This intentionally supports the simple frontmatter subset used by Project Brain
(key: value plus inline lists) so validation works without PyYAML.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

REQUIRED = ("type", "title", "description")
RESERVED = {"index.md", "log.md"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*\s*:")


def parse_simple_frontmatter(raw: str) -> dict[str, str]:
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if KEY_RE.match(line):
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip().strip('"\'')
        elif current_key and (line.startswith(" ") or line.startswith("-")):
            # Accept simple continuation/list lines without full YAML parsing.
            data[current_key] = (data[current_key] + " " + stripped).strip()
        else:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
    return data


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "missing frontmatter"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "unterminated frontmatter"
    raw = text[4:end]
    try:
        data = parse_simple_frontmatter(raw)
    except Exception as exc:
        return None, f"invalid frontmatter: {exc}"
    return data, None


def is_external(link: str) -> bool:
    parsed = urlparse(link)
    return bool(parsed.scheme and parsed.scheme not in ("", "file")) or link.startswith("mailto:")


def resolve_link(root: Path, source: Path, link: str) -> Path | None:
    clean = link.split("#", 1)[0].strip()
    if not clean or is_external(clean):
        return None
    if clean.startswith("/"):
        target = root / clean.lstrip("/")
    else:
        target = source.parent / clean
    if clean.endswith("/"):
        target = target / "index.md"
    return target.resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("brain", nargs="?", default=".project-brain")
    args = parser.parse_args()
    root = Path(args.brain).resolve()
    if not root.exists():
        print(f"NO-GO: brain directory not found: {root}")
        return 1

    errors: list[str] = []
    concept_count = 0
    links_checked = 0

    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if rel.parts and rel.parts[0] == "state":
            continue
        text = path.read_text(encoding="utf-8")
        if path.name in RESERVED:
            pass
        else:
            concept_count += 1
            fm, err = parse_frontmatter(path)
            if err:
                errors.append(f"{rel}: {err}")
            else:
                for key in REQUIRED:
                    if not (fm.get(key) or "").strip():
                        errors.append(f"{rel}: missing required key `{key}`")
        for match in LINK_RE.finditer(text):
            target = resolve_link(root, path, match.group(1))
            if target is None:
                continue
            links_checked += 1
            if not target.exists():
                errors.append(f"{rel}: broken link `{match.group(1)}` -> {target}")

    if errors:
        print(f"NO-GO: {len(errors)} issue(s) in {root}")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"GO: Project Brain valid — {concept_count} concept file(s), {links_checked} local link(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
