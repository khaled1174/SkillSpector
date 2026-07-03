---
type: KnowledgeState
title: Knowledge State
description: Current concise project state, scope, source hierarchy, and review triggers.
status: active
tags: [project-brain, knowledge-base]
---

# Knowledge State

Last reviewed: TBD

## Project purpose

TBD

## Current active scope

- TBD

## Explicitly out of scope

- TBD

## Current source-of-truth hierarchy

1. User's latest explicit instruction.
2. Project instruction files: `CLAUDE.md`, `AGENTS.md`, `PROJECT_CONTEXT*.md` when present.
3. Live files, tests, build output, and checked source data.
4. Hermes memory/skills only as routing context, not as proof of current source state.

## Verified commands

See `RUNBOOK.md`.

## Known risks / constraints

- Do not store secrets or credentials in project brain files.
- Shared/high-risk knowledge updates require Khaled approval.

## Next review trigger

- After the next non-trivial task that changes workflow, commands, architecture, data sources, or safety boundaries.
