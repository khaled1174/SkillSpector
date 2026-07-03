---
type: SourceMap
title: SkillSpector source-of-truth map
description: Sources that outrank memory/model summaries for SkillSpector.
status: active
risk_tier: medium
tags: [sources, grounding]
timestamp: 2026-06-27T11:40:31Z
---

# Source-of-truth Map

| Source | Purpose | Notes |
|---|---|---|
| [`../../README.md`](../../README.md) | project overview | public project framing |
| [`../../pyproject.toml`](../../pyproject.toml) | Python tooling config | pytest/ruff/mypy settings |

## Grounding rule

Read direct project sources before relying on memory. If source files conflict, surface the conflict and ask for a decision if needed.
