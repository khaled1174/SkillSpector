---
type: Guide
title: Project Brain
description: Self-maintaining knowledge base operating rules for SkillSpector.
status: active
tags: [project-brain, knowledge-base]
---

# Project Brain

This directory is the project's self-maintaining knowledge base.

## Operating rule

Every non-trivial project task must end by checking whether durable project knowledge changed.

Update the smallest correct file only when the fact will still matter later:

- `KNOWLEDGE_STATE.md` — current project state and boundaries.
- `DECISIONS.md` — durable decisions with rationale and source.
- `RUNBOOK.md` — verified commands and operational checks.
- `DRIFT_QUEUE.md` — proposed or pending documentation fixes.
- `SOURCES.md` — source-of-truth hierarchy and allowed inputs.

## Safety

Never store secrets, tokens, passwords, private keys, raw credentials, or sensitive data here.

Shared/high-risk knowledge changes require Khaled approval before applying:

- VRO / municipal documents;
- trading, strategy, execution, or risk settings;
- production or external-facing content;
- security, credentials, or permissions;
- policy or governance changes.

## Loop

```text
OBSERVE sources → COMPARE docs vs reality → DETECT drift → DRAFT patch → GATE approval → APPLY → VERIFY → RECORD
```

## Compounding learnings layer

Use `LEARNINGS/` for durable, searchable lessons that should influence future planning, debugging, review, and Claude Code dispatches.

```text
PLAN/DEBUG/REVIEW input
→ retrieve relevant LEARNINGS/PATTERNS/CONCEPTS
→ apply matching constraints
→ verify against current source/oracle
→ capture or queue drift at closeout
```

Present evidence beats memory: if an old learning conflicts with current files or command output, queue drift instead of following stale knowledge.

