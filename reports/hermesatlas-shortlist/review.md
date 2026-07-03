# HermesAtlas shortlist triage

Date: 2026-06-26
Scope: 5 repos discovered from hermesatlas.com/lists/top-skills, cloned read-only into `/tmp/hermesatlas-skill-triage`.

## Commands / evidence

- Metadata: `/tmp/hermesatlas-skill-triage/metadata.json`
- SkillSpector summary: `/Users/khaledmac/project/SkillSpector/reports/hermesatlas-shortlist/summary.json`
- Static reports directory: `/Users/khaledmac/project/SkillSpector/reports/hermesatlas-shortlist/` (files ending with `-static.json`)
- Smoke tests:
  - `conorbronsdon/avoid-ai-writing`: `npm test` passed.
  - `Agents365-ai/drawio-skill`: `python3 tests/test_scripts.py` passed, 31 tests.
  - `Sahil-SS9/hermaguard`: `python3 test_tools.py` passed, 46 tests, one ResourceWarning only.

## Verdicts

| Repo | Verdict | Why |
|---|---|---|
| `conorbronsdon/avoid-ai-writing` | GO as reference / adapter | Low risk, no external APIs, deterministic detector tests pass. English-centric; adapt before VRO/Arabic use. |
| `AkoliteZA/hermes-agent-idea-workflow` | GO as reference / light adapter | Safe markdown workflow. Overlaps existing planning skills; use ideas, not raw install. |
| `Sahil-SS9/hermaguard` | REVIEW / adapter only | Strong adversarial-review pattern; raw skill is user-specific and references external linters/global installs. Do not install raw. |
| `Agents365-ai/drawio-skill` | REVIEW / conditional install | Technically strong and tests pass, but requires draw.io desktop/Graphviz and has optional CDN logo fetch. Use when editable draw.io is needed. |
| `ReinaMacCredy/maestro` | HOLD / sandbox spike only | Valuable loop/proof-ledger concepts, but install modifies repo agent files/hooks and installer may remove shadowing binaries. Do not install in active projects without dedicated spike. |

## Adapter candidates

1. `humanize-official-arabic-writing` or patch `humanizer`: Arabic/VRO-safe version of avoid-ai-writing.
2. Patch `requesting-code-review`: add Hermaguard-style 3-lens reviewer: edge cases, adversarial/security, blast radius.
3. `drawio-diagram-workflow`: wrapper that checks local draw.io/Graphviz, forbids CDN icons unless user approves, exports verified images.
4. Patch `claude-code-loop-orchestration`: add Maestro-inspired card/proof-ledger pattern without installing Maestro.
5. Merge idea-workflow concepts into `claude-code-prompt-patterns` / `writing-plans`: idea capture -> design doc -> implementation handoff -> spec review.

## Do not do without explicit approval

- Do not run `curl ... | bash` from Maestro.
- Do not run `maestro init --yes` or `maestro install --agent claude` inside active repos.
- Do not run `npx skills add ... -g` for drawio or any repo.
- Do not globally install linters/packages just for Hermaguard.
- Do not copy third-party skills into default profile unchanged.
