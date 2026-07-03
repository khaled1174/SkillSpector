# CLAUDE.md

## Project Brain

Before any non-trivial work, read:

- `.project-brain/index.md`
- `.project-brain/project.md`
- `.project-brain/LEARNINGS_INDEX.md` and matching files under `.project-brain/LEARNINGS/`
- the relevant loop under `.project-brain/loops/`
- the relevant oracle under `.project-brain/oracles/`

Do not mark work done unless the relevant oracle passes. If the oracle is missing, return `NO-GO` and ask for a real verification gate.

This project uses `.project-brain/` as its operational brain.

## Self-maintaining knowledge base

This project uses Khaled's self-maintaining KB protocol. After non-trivial work, check whether durable project knowledge changed and update `.project-brain/` or its `DRIFT_QUEUE.md`.

Rules:
- observe real project sources before changing docs;
- draft evidence-backed updates, not vague reminders;
- require Khaled approval for shared/high-risk knowledge;
- never store secrets, credentials, sensitive municipal data, or trading credentials in the KB.

<!-- KHALED_AGENT_LOOP_START -->
## Khaled Agent Loop

For non-trivial work in this project, use `.project-brain/AGENT_LOOP.md`:

```text
Hermes Intake → Ultra Plan → Fugo Spec → Fable Controller → Opus/Sonnet Worker → Worker Verification → Fable Final Verification → Hermes Report
```

Do not treat worker completion as final success. Return evidence to the Fable/controller layer and require an external oracle before `GO`.
<!-- KHALED_AGENT_LOOP_END -->

## Compounding knowledge lifecycle

Before non-trivial planning, debugging, review, or Claude Code dispatch, search `.project-brain/LEARNINGS/`, `.project-brain/PATTERNS.md`, `.project-brain/CONCEPTS.md`, and `.project-brain/DECISIONS.md` for relevant constraints. Current source files and oracle output override stale learnings; queue conflicts in `.project-brain/DRIFT_QUEUE.md`.

