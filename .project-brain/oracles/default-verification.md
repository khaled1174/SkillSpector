---
type: Oracle
title: Default verification oracle
description: Default verification gate for SkillSpector.
status: active
risk_tier: medium
tags: [oracle, verification]
timestamp: 2026-06-27T11:40:31Z
---

# Default Verification Oracle

## Command selection

Use the first applicable command from project files:

```bash
# Python project
uv run python -m pytest -q

# Node project
npm test
npm run build

# Brain-only verification
python3 .project-brain/tools/validate.py .project-brain
```

## Passing condition

- command exits 0
- no new safety violation
- if a full suite is not available or too expensive, run the targeted oracle and state the limitation
