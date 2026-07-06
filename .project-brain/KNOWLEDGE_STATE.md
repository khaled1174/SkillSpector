---
type: KnowledgeState
title: Knowledge State
description: Current concise project state, scope, source hierarchy, and review triggers.
status: active
tags: [project-brain, knowledge-base]
---

# Knowledge State

Last reviewed: 2026-07-06

## Project purpose

SkillSpector is a Python security scanner for AI agent skills. It scans Git repositories, URLs, zip files, directories, or single files for vulnerabilities, malicious patterns, and security risks before installation.

## Current active scope

- Local project-brain governance for agentic work in this repository.
- Static inspection reports under `reports/` as checked artifacts.
- Read-only/security-analysis workflows unless Khaled explicitly approves a broader side effect.
- Project verification through the Project Brain oracle and, when dependencies are installed, repository tests/lint from `Makefile`.

## Explicitly out of scope

- Auto-pushing to `origin` without explicit approval.
- Force-push, merge, deploy, publish, or release actions without approval.
- Capturing secrets, raw credentials, sensitive municipal data, trading credentials, or temporary task progress in `.project-brain`.
- Treating Hermes memory/model summaries as proof when project files or command output are available.

## Current source-of-truth hierarchy

1. User's latest explicit instruction.
2. Project source files: `README.md`, `pyproject.toml`, `Makefile`, `uv.lock`, `src/`, `tests/`, and checked reports.
3. Project instruction/brain files: `CLAUDE.md`, `.project-brain/`, relevant loops/oracles.
4. Live command output from this project.
5. Hermes memory/skills only as routing context, not as proof of current source state.

## Verified commands

See `RUNBOOK.md`.

## Known risks / constraints

- Remote is `https://github.com/NVIDIA/SkillSpector.git`; pushing is an external/public side effect and remains human-gated.
- Full repository tests/lint require an installed dev environment. In the current environment, `uv run pytest ...` and `uv run ruff ...` failed because the executables were not present; no dependency install was performed.
- Shared/high-risk knowledge updates require Khaled approval.

## Next review trigger

- Before any push/PR to `origin`.
- After installing dependencies and running full `make test-unit` / `make lint`.
- After the next non-trivial task that changes workflow, commands, architecture, data sources, reports, or safety boundaries.
