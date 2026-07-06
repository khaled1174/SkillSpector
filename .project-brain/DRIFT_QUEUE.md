---
type: DriftQueue
title: Drift Queue
description: Approval and recheck queue for project knowledge drift.
status: active
tags: [project-brain, knowledge-base]
---

# Drift Queue

Use this as the approval/recheck queue for KB maintenance.

| Date | Area | Drift / Missing Knowledge | Evidence | Proposed fix | Status |
|---|---|---|---|---|---|
| 2026-07-06 | Initial setup | Replace TBD entries after first real project review | `README.md`, `pyproject.toml`, `Makefile`, `.project-brain/tools/validate.py`, git state | Filled `KNOWLEDGE_STATE.md` and `RUNBOOK.md` with verified/current source-backed details | applied |
| 2026-07-06 | Full repo oracle | Tests/lint could not run because `pytest` and `ruff` executables were missing in current uv environment | `uv run pytest -m "not integration" tests/ -q` and `uv run ruff check src/ tests/` returned spawn errors | After explicit approval to install dependencies, run `make install-dev`, then `make test-unit` and `make lint` | pending |
| 2026-07-06 | External side effect | Branch is ahead of `origin/main`, but pushing to `https://github.com/NVIDIA/SkillSpector.git` is public/external | `git status --branch --short` showed `main...origin/main [ahead 2]` before the latest local commits | Push only after Khaled explicitly approves remote publication | blocked |

Status values:

- `pending` — needs review or source confirmation.
- `approved` — approved by Khaled or project owner.
- `applied` — patch applied and verified.
- `dismissed` — not useful or no longer true.
- `blocked` — missing source or approval.
