---
type: Project
title: SkillSpector
description: Operational project brain for SkillSpector.
status: active
risk_tier: medium
tags: [project, project-brain]
timestamp: 2026-06-27T11:40:31Z
---

# SkillSpector

## Mission / note

Skill/project inspection tooling; favor read-only analysis and explicit approval before modifying external profiles.

## Default workflow

For any non-trivial change:

1. Read this file and [source-of-truth map](sources/source-of-truth.md).
2. Define `GOAL`, `SCOPE`, `ORACLE`, `STOP_POLICY`, and `RISK`.
3. Apply the [main implementation loop](loops/main-implementation-loop.md).
4. Run the relevant oracle.
5. Report `GO / NO-GO / PARTIAL` with real evidence.

## Durable rule

If an external source or project file conflicts with memory/model output, trust the source file and surface the conflict.
