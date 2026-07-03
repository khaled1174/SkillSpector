---
type: Index
title: Learnings Index
description: Search index and retrieval entry point for SkillSpector learnings.
status: active
tags: [learnings-index, retrieval, project-brain]
---

# Learnings Index

Use this as the entry point before non-trivial SkillSpector work.

## Current learnings

No project-specific learnings have been captured yet.

## Search protocol

```bash
rg -n "tags:.*(<term1>|<term2>)|module:.*<module>|problem_type:.*<type>|applies_when:" .project-brain
rg -n "<exact error>|<command>|<component>|<concept>" .project-brain/LEARNINGS .project-brain/PATTERNS.md .project-brain/CONCEPTS.md
```

## Retrieval decision

| Result | Action |
|---|---|
| Relevant learning found | Add it as a constraint in the plan/spec/review. |
| Learning conflicts with present source | Present evidence wins; add drift to `DRIFT_QUEUE.md`. |
| No relevant learning found | State that none were found; continue with current oracle. |
| Repeated new failure pattern found | Draft one learning at closeout. |
