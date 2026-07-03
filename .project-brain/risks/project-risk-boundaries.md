---
type: RiskRegister
title: Project risk boundaries
description: Risk and approval boundaries for SkillSpector.
status: active
risk_tier: medium
tags: [risk, governance]
timestamp: 2026-06-27T11:40:31Z
---

# Project Risk Boundaries

## Human-gated actions

- destructive deletes
- force-push/merge/deploy/publish
- credentials/secrets
- spending/external side effects
- production/live operations

## Default allowed work

- read-only inspection
- local docs and planning
- tests/build/lint/smoke checks
- proposal-only recommendations
- non-destructive local edits within explicit scope

## Escalation rule

If a task crosses a human-gated action, stop and ask Khaled before executing.
