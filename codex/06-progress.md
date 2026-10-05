# Confidence and spaced revision

Copy the following prompt into Codex:

```text
Read codex/README.md, codex/PLAN.md, codex/DATA_MODEL.md, and codex/STATUS.md before changing code. Inspect existing repository instructions and preserve unrelated work. Implement only this phase. Use current official documentation to check APIs. Do not invent repository URLs, solved statuses, source contents, credentials, or acceptance evidence. Never expose secrets in browser bundles or logs. Add meaningful verification for the phase, run applicable checks, and fix failures. Update codex/STATUS.md with changes, commands/results, limitations, and next step. Keep existing learning content unchanged. Implement the app inside this Data-Structure-and-Algorithms repository. Never modify the external Leetcode repository. Do not push or deploy unless requested. Finish with a concise reviewable report.

Implement IndexedDB persistence independent from catalog and repo snapshots. Store manual learning statuses, personal notes and append-only review attempts. Calculate due dates using the transparent schedule in PLAN and configured local timezone; preserve UTC timestamps. Add revision queue, weak-pattern counts, and recent reviews with unique problem denominators. Show code-found, acceptance, confidence and last-reviewed separately. Add versioned JSON export/import with validation, preview and explicit merge/replace semantics; avoid silent destructive overwrite. Handle unknown imported problem IDs as recoverable orphan records. Gate: reload persists progress, sync cannot raise confidence, shared placements count once, timezone boundary and import failure preserve existing data.
```
