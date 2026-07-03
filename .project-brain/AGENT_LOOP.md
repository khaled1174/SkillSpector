---
type: Loop
title: Agent Execution Loop
description: Ultra/Fugo/Fable/worker execution loop and final reporting standard.
status: active
tags: [project-brain, knowledge-base]
---

# Agent Execution Loop — Ultra → Fugo → Fable → Worker

## Purpose

This project uses Khaled's agent loop. Do not treat a single worker response as completion. Work must pass through planning, structured handoff, worker execution, controller verification, and evidence-backed reporting.

```text
Khaled Request
→ Hermes Intake / Routing
→ Ultra = Strategic Planner
→ Fugo = Plan Structurer / Spec Builder
→ Fable = President / Controller / Final Verifier
→ Opus or Sonnet = Worker / Executor
→ Worker Verification
→ Fable Final Verification
→ Hermes Report to Khaled
```

## Role split

| Layer | Responsibility |
|---|---|
| Hermes | Intake, routing, memory/context, project safety, final Arabic report |
| Ultra | Strategic planning: goal, path, risks, success criteria |
| Fugo | Converts the plan into a concrete executable spec |
| Fable | Controller: approves/rewrites spec, dispatches worker, verifies evidence, decides repair/final |
| Opus/Sonnet | Worker: implements only the approved spec and returns evidence |
| Oracle | External truth: tests, build, lint, screenshots, source-of-truth, metrics, or Khaled approval |
| Khaled | Human gate for high-risk, public, financial, destructive, municipal, or trading-execution actions |

## Required handoff shape

```text
REQUEST:
  <Khaled's request>

HERMES_INTAKE:
  project:
  scope:
  risk:
  memory_context:
  approval_gate:

ULTRA_PLAN:
  goal:
  strategy:
  risks:
  success_criteria:
  preferred_worker_model:

FUGO_SPEC:
  execution_steps:
  files_routes_modules:
  forbidden_actions:
  verification_commands:
  stop_policy:

FABLE_CONTROLLER:
  approve_or_rewrite_spec:
  dispatch_to_worker:
  review_worker_evidence:
  decide_repair_or_final:

WORKER_EXECUTION:
  model: Opus | Sonnet
  task:
  commands:
  changed_files:
  evidence:
  blockers:

FABLE_FINAL_VERIFICATION:
  oracle_result:
  scope_check:
  quality_check:
  verdict: GO | PARTIAL | NO-GO

HERMES_REPORT:
  summary:
  evidence:
  risks:
  next_action:
```

## Operating rules

1. Fable is the controller before and after execution; the worker never self-certifies final success.
2. Worker execution must stay inside `FUGO_SPEC`; no scope expansion without returning to the controller.
3. Mechanical verification should be run by the worker first, then reviewed by Fable/Hermes where feasible.
4. No `GO` without an external oracle: tests, build, lint, browser/visual check, source reconciliation, metric, or Khaled approval.
5. Use a repair loop only with a bounded stop policy. Default: 2 repair cycles, then report `PARTIAL` or `NO-GO`.
6. Public, financial, destructive, credential-related, municipal source-of-truth, deployment, publishing, or trading-execution actions require Khaled approval.
7. Trading projects remain read-only/paper/proposal-only unless Khaled gives explicit written approval for a different mode.
8. Record durable lessons in project docs/skills only when they will remain useful; do not store secrets or temporary task progress.

## Final report standard

```text
الحكم: GO | PARTIAL | NO-GO

تم:
- ...

التحقق الفعلي:
- `<command/check>` → PASS/FAIL

الأدلة:
- files changed / screenshots / logs / source check

المخاطر أو المتبقي:
- ...
```
