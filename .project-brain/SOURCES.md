---
type: Sources
title: Sources
description: Source-of-truth hierarchy and allowed inputs for SkillSpector.
status: active
tags: [project-brain, knowledge-base]
---

# Sources

Define what counts as source of truth for this project.

## Allowed sources

- User's latest explicit instruction.
- Project files in this repository.
- Verified command output from this project.
- Project-specific issue trackers, documents, or dashboards explicitly provided by Khaled.
- Hermes skills/memory only for routing and historical context.

## Source hierarchy

1. Current source files and live verified outputs.
2. Project instruction/context files.
3. Recent approved decisions in `DECISIONS.md`.
4. Historical session context only when original sources are unavailable.

## Never store here

- API keys, tokens, passwords, private keys, raw credentials.
- Sensitive VRO/municipal data unless the file is explicitly part of an approved VRO project workspace.
- Trading credentials, account IDs, private logs, or live execution data.
- Temporary task progress that will be stale within a week.

## External advisor boundary

If Fugu Ultra or another external model is used, send only sanitized summaries unless Khaled explicitly authorizes a narrower source scope.
