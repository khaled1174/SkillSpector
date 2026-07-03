---
type: Loop
title: Main implementation loop
description: Default bounded implementation loop for SkillSpector.
status: active
risk_tier: medium
tags: [loop, implementation, verification]
timestamp: 2026-06-27T11:40:31Z
---

# Main Implementation Loop

OBSERVE → SPEC → ACT → VERIFY → RECORD

## Required spec

```text
GOAL:        <one sentence>
SCOPE:       <files/modules allowed and forbidden>
ORACLE:      <test/build/lint/browser/manual approval>
STOP_POLICY: max 2 repair cycles; stop on repeated failure or missing oracle
RISK:        low / medium / high
```

## Steps

1. Inspect source files listed in [source-of-truth map](../sources/source-of-truth.md).
2. Make the smallest scoped change.
3. Run [default verification](../oracles/default-verification.md) or a more specific oracle.
4. Repair only failures introduced by the change.
5. Stop and report if the task requires destructive, public, financial, credential, or production action.

## Evidence required

- files changed
- commands run
- pass/fail output
- remaining blockers
- verdict: `GO / NO-GO / PARTIAL`
