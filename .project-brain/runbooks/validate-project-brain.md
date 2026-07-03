---
type: Runbook
title: Validate Project Brain
description: How to validate the Project Brain for SkillSpector.
status: active
risk_tier: low
tags: [runbook, validation]
timestamp: 2026-06-27T11:40:31Z
---

# Validate Project Brain

Run from project root:

```bash
python3 .project-brain/tools/validate.py .project-brain
```

Expected:

```text
GO: Project Brain valid — ...
```

If it fails, fix frontmatter or broken links and rerun.
