# Product and implementation plan

## Version 1
A single-user, local-first React application. Trees first, with a model that accommodates Graphs, Dynamic Programming (DP), and other topics later. Start with a curated set of 15–25 tree problems rather than every linked collection.

## Architecture
- React + TypeScript + Vite for the app, React Router for bookmarkable routes.
- React Flow (@xyflow/react) for expandable box nodes; Dagre for initial layout. Implement expand/collapse in our code; do not assume access to paid examples.
- Accessible outline/list view alongside the canvas for tablet use, keyboard navigation, and large datasets.
- JSON catalog checked into the app repository for topics, patterns, questions, teaching notes, and sources.
- IndexedDB through a small storage adapter for confidence, review history, mapping overrides, and preferences; versioned JSON export/import for backup.
- Python command-line ingestion for both repositories, producing validated JSON snapshots. Run manually first; optional scheduled GitHub Actions later.
- No backend, login, paid service, or Large Language Model (LLM) API needed for version 1. Private GitHub credentials stay in CLI environment variables, never browser code.

React Flow handles nodes and edges; external layout is documented here: https://reactflow.dev/learn/layouting/layouting
GitHub tree API and truncation behavior: https://docs.github.com/en/rest/git/trees
Confirm current package versions and runtime requirements during scaffolding and lock dependencies.

## Main screens
1. Knowledge map: topic boxes, expandable branches, search, difficulty and confidence filters, fit/reset controls, breadcrumbs, count summaries.
2. Problem detail: recognition signal, recursion contract, intuition, worked dry run, Python solution, complexity, interview traps, connected problems, source and repo links.
3. Test Me: hide teaching notes and solution; ask what state moves, which traversal follows, what recursion returns, and what edge cases matter. User self-assesses after reveal.
4. Revision: due queue, weak patterns, recent independent solves, and coverage. Use explicit counts and explain metrics; avoid an invented interview-readiness percentage.
5. Sources/sync: both repositories, snapshot date and commit, sync warnings, unresolved matches, manual mappings, backup controls.

## Two-repository policy
Learning repo provides notes, dry runs, and organized Striver solutions. Dedicated LeetCode repo provides submission artifacts and additional implementations. Preserve both; do not choose one globally. Match by LeetCode ID, then canonical slug, then explicit override. Filename/title similarity is only a suggestion requiring review.

One canonical problem can have several patterns and several artifacts. Use a primary hierarchy placement and optional related edges; show a problem once in aggregate counts. Clicking any placement opens the same problem and progress record.

A repository artifact proves code exists, not that LeetCode accepted it. Display acceptance as unknown unless trustworthy submission metadata explicitly records an accepted verdict. Repository timestamps are sync/commit dates, not solve dates. A completed healthy scan can mark an old artifact missing; failed/incomplete scans preserve the last good snapshot and report stale data.

## Learning progress
Keep independent fields: artifact availability, acceptance evidence, self-reported learning status, and review attempts. Statuses: never_attempted, learned, solved_with_help, solved_independently, revised, interview_ready. Importing code never promotes confidence. Reviewed/ready is user assessed, not an automatic score.

Use a transparent initial review schedule: again → tomorrow; hard → 3 days; good → 7 days; easy → 14 days. Anchor to the user's configured timezone and local calendar date. This is a heuristic, not a validated mastery model. Store attempts append-only; recompute due date from latest attempt. Display counts per pattern with unique problem denominators.

## Source ingestion
Save source URL and extracted outbound link inventory. Traverse approved pattern-collection links one level by default, with host allowlist, deduplication, retry bounds, and a report of inaccessible pages. Do not crawl the entire web recursively. If LeetCode blocks access, accept a user-exported HTML/Markdown page and record the limitation. Preserve attribution and write original teaching explanations; do not bulk copy external solutions.

## Proposed repository layout
apps/dsa-knowledge-map/       React app and its catalog/config/scripts/snapshots
catalog/                     topic/pattern/problem/notes JSON
scripts/                     Python ingestion and validation
config/repositories.json     two read-only sources
snapshots/                   validated repository artifact index
codex/                       prompts and phase status
 docs/                       architecture and import reports

## Phases and exit gates
00 Discovery: sources and unknowns recorded; no invented repo URL.
01 Scaffold: app opens; routes, catalog schema, storage adapter compile.
02 Catalog: verified source inventory and 15–25 curated tree problems; inaccessible pages explicit.
03 Map: expand/collapse/search, stable placement, keyboard list alternative.
04 Teaching: detail pages and hidden-answer recall flow work with Python notes.
05 Repo sync: both configured sources, deterministic matching, duplicates and unresolved cases handled.
06 Progress: durable manual statuses, reviews, backups, due queue.
07 Integration: source snapshot and progress stay independent; stale/failure behavior verified.
08 Release: production build and critical behavior checks pass; deploy only when explicitly requested.

## Later
Scheduled sync; optional backend for cross-device progress and authentication; more topic packs; AI feedback on derivations after evaluation of correctness and cost. Do not require these for version 1.

## Repository placement
App code, catalog, configuration, scripts and snapshots live beneath apps/dsa-knowledge-map/. Planning and prompts stay in root codex/. Existing Striver notes and solutions are read-only ingestion inputs within the host repository. The external Leetcode repository is never written to. Exclude apps/ and codex/ from learning scans to prevent self-ingestion.
