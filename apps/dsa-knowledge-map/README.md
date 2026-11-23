# Recall — personal DSA revision studio

A working first release of the DSA Knowledge Map, housed in the existing learning repo. Responsive React app with a pattern hierarchy, your original notes and Python code, deterministic animations, active recall, and local review scheduling.

## Run

Requires Node 20.19+ or 22.12+ (verified here with Node 24) and Python 3.10+ for catalog refresh.

```sh
cd apps/dsa-knowledge-map
npm ci
npm run dev
npm test
npm run build
npm run preview
```

Do not use the development server for production. `npm run build` creates `dist/` and a versioned service worker. The app is designed for its own hostname at `/`, not a birthday subdirectory.

## Included

- All 29 entries from `Striver/BinaryTrees/tracker.md`, original note sections and Python implementations.
- Ten hand-authored algorithm traces: preorder, inorder, postorder, level order, zigzag, right view, depth, balance, diameter and maximum path sum.
- Pause/play, previous/next, speed, seek, custom level-order input with nulls, recursion stack/queue and returned values. Duplicate node values are tracked by unique node IDs.
- Search, pattern families, bookmarkable question URLs, related recursive skeletons, hidden-answer recall and personal notes.
- Local browser persistence, explicit confidence, dated review attempts, due queue, JSON backup and merge import.
- Matching external solution links for 15 tree questions using canonical slugs from `rishi9504/Leetcode`. Folder numeric prefixes are deliberately ignored. This is a snapshot, not live account access or verified LeetCode acceptance.
- Home-screen manifest and cached offline production assets after first visit on HTTPS. New worker activates after older open tabs close; reopen when updating. External repo links need internet.

## Honest boundaries

19 questions have notes and code but no authored animation yet. The full LeetCode repository and the external all-patterns article are not yet imported as learning packs. No claim that the old prompts' every phase is complete. A responsive outline of expandable pattern boxes replaces the previously proposed pan/zoom React Flow canvas for version 1, to simplify phone use.

Your tracker confidence is displayed as imported context. Manual Recall confidence starts unassessed; code presence never sets it. Reviews use a simple 1/3/7/14 calendar-day schedule, not a mastery score. Personal notes are plain text and stay on this browser. Move progress using Sources & backup; cross-device account sync is not implemented. Incognito storage can be temporary. Scratchpad text is intentionally temporary and clearly labeled.

All source catalog content is already public in the user's repositories. No credentials or personal progress are included in the build.

## Refresh learning data

From this directory:

```sh
npm run catalog
npm test
npm run build
```

The catalog builder parses the host repository's tracker and notes. It fails rather than silently skipping missing note anchors or files. `scripts/leetcode-tree.json` is a solution-file snapshot from a complete GitHub tree response, including its commit SHA. To refresh it using the public GitHub API:

```sh
python3 scripts/refresh_leetcode.py
npm run catalog
```

Optional `GITHUB_TOKEN` is read only from the command environment, never committed or bundled. Refresh writes atomically and preserves the prior snapshot on a failed/truncated API response. Source scan dates are not solve dates. Rerun the catalog and build to publish refreshed source data.

See [Lightsail deployment](deploy/LIGHTSAIL.md), [verification evidence](VERIFICATION.md), and repository-root `codex/STATUS.md`.
