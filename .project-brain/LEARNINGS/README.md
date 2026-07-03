---
type: Guide
title: Compounding Learnings
description: Retrieval and capture protocol for durable SkillSpector project learnings.
status: active
tags: [learnings, retrieval, capture, compounding-knowledge]
---

# Compounding Learnings

This directory stores durable project learnings as one Markdown file per solved problem, convention, workflow pitfall, or decision.

## Categories

- `bugs/` — non-obvious defects, root causes, and prevention rules.
- `architecture/` — architecture and design patterns discovered in the project.
- `conventions/` — local conventions future agents must follow.
- `workflows/` — execution, review, and verification workflows.
- `decisions/` — durable decisions better expressed as a full learning than a table row.
- `tools/` — tool-specific lessons and command pitfalls.
- `qa/` — verifier, review, and oracle failure patterns.

## Retrieval rule

Before non-trivial planning, debugging, review, or Claude Code dispatch:

1. Search this directory plus `../PATTERNS.md`, `../CONCEPTS.md`, and `../DECISIONS.md`.
2. Keep only learnings where `applies_when` matches the current task.
3. Convert relevant learnings into constraints in the handoff/spec.
4. If a learning conflicts with current source files or command output, present evidence wins and the drift goes to `../DRIFT_QUEUE.md`.

## Capture rule

Add a learning only when the lesson will still matter after a week:

- repeated failure pattern;
- non-obvious fix;
- durable architecture/design/tooling decision;
- project convention future agents must follow;
- verifier failure that should become a stronger review check.

Do not store secrets, credentials, raw private logs, sensitive municipal/trading data, or temporary task progress.
