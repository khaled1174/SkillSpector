# codebase-memory-mcp high-signal review

Repo: https://github.com/DeusData/codebase-memory-mcp
Clone: `/tmp/codebase-memory-mcp-inspect/repo`
Commit inspected: `b075f05`
Date: 2026-06-27

## Verdict

**REVIEW / sandbox-only. Do not install into Khaled's default Claude/Hermes environment yet.**

The project is useful and unusually mature for a code-intelligence MCP: it builds locally, has a serious security-audit suite, uses local SQLite graph indexes, and has explicit path-containment checks for snippet reads. The main risk is operational blast radius: its installer modifies multiple agent configs, skills, hooks, PATH files, kills running MCP instances, and can delete/rebuild local indexes.

## Useful capability

- Indexes repositories into a persistent graph: functions, classes, routes, call paths, architecture, ADRs, semantic search.
- Local-first: static C binary, vendored SQLite/tree-sitter/mimalloc, bundled embedding data, no API key required for core operation.
- Supports many agents: Claude Code, Codex, Gemini, Cursor, VS Code, OpenClaw, Kiro, etc.
- Potentially useful for large codebases where repeated grep/read costs too many tokens.

## Evidence run

- `git clone --depth 1 https://github.com/DeusData/codebase-memory-mcp.git`
- `skillspector scan /tmp/codebase-memory-mcp-inspect/repo --no-llm --format json`
- `npm audit --package-lock-only --audit-level=moderate` in `graph-ui/` → `found 0 vulnerabilities`
- `make -f Makefile.cbm cbm` → production binary built successfully: `build/c/codebase-memory-mcp`
- `make -f Makefile.cbm security` → passed static audit, binary string audit, UI audit, temp-home install audit, MCP fuzz robustness 23/23, network audit skipped on Darwin due missing strace, vendored audit printed stale absolute MISSING paths but still ended `All security checks passed`.

## Important findings

### Positive

- Has `install --plan` code path intended to emit planned writes without mutation.
- Installer prompts by default; `-y/--yes` is explicit auto-yes.
- Download URLs are HTTPS-only except localhost/127.0.0.1 test override.
- GitHub release artifacts include checksums.
- `get_code_snippet` resolves root + file with realpath containment before reading.
- MCP file writes are mostly explicit: cache DBs, optional `.codebase-memory/graph.db.zst`, ADR file.
- Security docs and audit scripts are above-average.

### Risks

- Installer writes across many global agent locations: `~/.claude`, `~/.codex`, `~/.gemini`, `~/.cursor`, VS Code app support, etc.
- Installs Claude Code `PreToolUse` and `SessionStart` hooks that steer agent behavior toward this MCP.
- Writes skills into Claude Code config and removes old monolithic skill names.
- Updates shell rc PATH.
- Kills other running `codebase-memory-mcp` instances during install.
- Deletes existing graph indexes during install after confirmation; `delete_project` removes DB/WAL/SHM for named project.
- npm package has `postinstall` that downloads a GitHub release binary automatically. It verifies checksum when available, but checksum absence is non-fatal.
- Make `security-vendored` printed stale absolute paths under `/Users/martinvogel/...`; likely an audit-script path bug. It still passed, but the output is noisy and should be treated as a quality issue.
- Full test target was not completed; `test-foundation` failed to link on macOS arm64 because it referenced many suites/symbols not linked into that target. Production build and security target passed.

## SkillSpector

Report: `/Users/khaledmac/project/SkillSpector/reports/codebase-memory-mcp/repo-static.json`

Static findings: 765 total: 271 HIGH, 223 MEDIUM, 271 LOW. Many are expected/static false positives in tests, generated vendored code, docs, and known install/security scripts. They still justify sandbox review before any install.

## Recommendation for Khaled

1. Do **not** run raw install commands in the default environment:
   - `curl ... | bash`
   - `npm install -g codebase-memory-mcp`
   - `codebase-memory-mcp install -y`
2. If evaluating, use an isolated sandbox with temporary HOME and only index a non-sensitive toy repo first.
3. Prefer using only the built binary manually, without global hooks/config mutation, until proven useful.
4. If later adopted, create a Hermes-specific adapter/skill that:
   - never auto-installs hooks,
   - runs index/query only under explicit project paths,
   - excludes trading/VRO secrets and backup dirs,
   - stores indexes under a controlled cache path,
   - requires explicit approval before `delete_project`, persistence artifacts, or any global config changes.

## Final decision

`REVIEW / HOLD for install`.

Useful enough to test in sandbox; not safe enough to install globally into Khaled's live default agent environment today.
