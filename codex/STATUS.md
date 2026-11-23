# Build status

Updated 23 November 2026. First working React revision studio is implemented in `apps/dsa-knowledge-map/`. This is a focused initial release; the original roadmap is not fully complete.

| Phase | Status | Evidence / remaining work |
| --- | --- | --- |
| 00-discovery | Completed for Trees MVP | 29 tracker entries inspected; both repo URLs configured; birthday Caddy architecture inspected read-only |
| 01-scaffold | Completed with adaptations | React/Vite app and hash-based bookmark routes; JavaScript instead of TypeScript; localStorage rather than IndexedDB |
| 02-catalog | Partial | All 29 Trees tracker entries/notes/code imported; external all-patterns hyperlink traversal remains pending |
| 03-map | Completed with adaptation | Responsive expandable pattern boxes and search/filter; pan/zoom React Flow graph deferred |
| 04-teaching | Partial | Original notes/Python for 29; 10 deterministic traces, recall/reveal and related recursive patterns; 19 animations remain |
| 05-repo-ingestion | Partial | Local tracker importer and canonical-slug external solution snapshot; refresh CLI preserves prior snapshot on failure; unresolved-match UI and truncated-tree subtree traversal deferred |
| 06-progress | Partial | Confidence, personal notes, dated reviews, due queue, backup import/export; local browser only, no automatic account sync |
| 07-integration | Partial | Source SHAs, acceptance distinction and links shown; no background live sync |
| 08-verification-release | Local checks passed; deployment pending | 8 tests, production build, browser trace/recall/persistence checks; see app VERIFICATION.md |

## Lightsail

User selected the existing birthday Lightsail instance. Prepared isolated container and Caddy hostname recipe at `apps/dsa-knowledge-map/deploy/LIGHTSAIL.md`. No live server changes were made. Current workspace lacks authorized AWS/SSH access; need actual deployment connection and the chosen Recall hostname before inspecting and applying host changes.

## Next priorities

1. Complete phone/tablet QA and deploy to the chosen hostname once authorized instance access is available.
2. Add animations for distance K/burning tree, width, construction, serialization and Morris.
3. Add authenticated cross-device progress sync if desired; preserve existing local export/import migration.
4. Expand beyond the Trees tracker with explicit source provenance and no inferred LeetCode acceptance.
