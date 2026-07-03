---
type: Template
title: Learning Template
description: Copy this template when creating one durable project learning.
status: active
tags: [learning-template, compounding-knowledge]
---

# Learning Template

Copy this shape into the correct `LEARNINGS/<category>/` folder.

```markdown
---
type: Learning
title: "<short searchable title>"
description: "<one sentence summary for retrieval>"
date: "YYYY-MM-DD"
category: "<bugs|architecture|conventions|workflows|decisions|tools|qa>"
project: "SkillSpector"
module: "<module-or-area>"
component: "<component-or-skill>"
problem_type: "<runtime_error|test_failure|logic_error|architecture_pattern|design_pattern|tooling_decision|convention|workflow_issue|best_practice>"
severity: "<low|medium|high|critical>"
applies_when:
  - "<future condition where this learning should be considered>"
tags: ["<searchable>", "<synonym>", "<module>"]
source_evidence:
  - "<file path, command output, source URL, or human approval note>"
status: "active"
supersedes: []
superseded_by: null
---

# <short searchable title>

## Problem

## Context

## Root cause / decision

## Solution / rule

## Applies when

## Verification / oracle

## Prevention checklist

## Related learnings
```
