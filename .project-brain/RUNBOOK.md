---
type: Runbook
title: Runbook
description: Verified operational commands and safety notes for SkillSpector.
status: active
tags: [project-brain, knowledge-base]
---

# Runbook

Record only commands that were verified in this project or commands directly declared by project files.

## Install / setup

Declared by `README.md` and `Makefile`:

```bash
uv venv .venv && source .venv/bin/activate
make install-dev
```

Do not install dependencies automatically in agent runs unless Khaled approves that scope.

## Development server

Declared by `Makefile` for LangGraph development:

```bash
make langgraph-dev
```

## Build / test / lint

Declared by `Makefile`:

```bash
make test-unit
make lint
make format-check
make build
```

Direct equivalents from project config:

```bash
uv run pytest -m "not integration" tests/ -q
uv run ruff check src/ tests/
```

## Project Brain verification

Verified command:

```bash
python3 .project-brain/tools/validate.py .project-brain
```

Expected current result:

```text
GO: Project Brain valid — 19 concept file(s), 16 local link(s) checked
```

## Reports verification

For checked JSON reports:

```bash
python3 - <<'PY'
from pathlib import Path
import json
for p in Path('reports').rglob('*.json'):
    json.loads(p.read_text())
print('reports-json-ok')
PY
```

## Verification evidence

| Date | Command | Result | Notes |
|---|---|---|---|
| 2026-07-06 | `python3 .project-brain/tools/validate.py .project-brain` | GO | Project Brain valid: 19 concept files, 16 local links checked. |
| 2026-07-06 | JSON parse check for `reports/design-system-*.json` | GO | Both new design-system reports parsed successfully and quick secret-pattern scan found no hits. |
| 2026-07-06 | `uv run pytest -m "not integration" tests/ -q` | BLOCKED | `pytest` executable was missing in current uv environment; no dependency install performed. |
| 2026-07-06 | `uv run ruff check src/ tests/` | BLOCKED | `ruff` executable was missing in current uv environment; no dependency install performed. |

## Safety notes

- Do not add commands that require secrets unless documented as placeholders only.
- Do not record raw tokens, API keys, passwords, or credentials.
- Do not push to `origin` without Khaled's explicit approval for that side effect.
