# Sync visibility and resilient UX

Copy the following prompt into Codex:

```text
Read codex/README.md, codex/PLAN.md, codex/DATA_MODEL.md, and codex/STATUS.md before changing code. Inspect existing repository instructions and preserve unrelated work. Implement only this phase. Use current official documentation to check APIs. Do not invent repository URLs, solved statuses, source contents, credentials, or acceptance evidence. Never expose secrets in browser bundles or logs. Add meaningful verification for the phase, run applicable checks, and fix failures. Update codex/STATUS.md with changes, commands/results, limitations, and next step. Keep existing learning content unchanged. Implement the app inside this Data-Structure-and-Algorithms repository. Never modify the external Leetcode repository. Do not push or deploy unless requested. Finish with a concise reviewable report.

Wire real snapshots into artifact links and Sources screen, showing per-source commit, scan date, stale status, unmatched artifacts and errors. Default browser app consumes precomputed snapshots; do not imply its refresh button can run the Python CLI on a static host. Provide exact local sync commands and a reload-snapshot action. Keep last good evidence on transient errors; distinguish artifact missing from source scan failed. Add mapping management export for the CLI. Validate catalog and snapshot at load with actionable error screens. Render external content safely, allowlist outbound schemes, and never render tokens. Gate: healthy learning source plus failed LeetCode source is understandable; progress stays intact when snapshots change.
```
