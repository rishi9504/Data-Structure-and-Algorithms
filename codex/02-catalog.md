# Sources and Trees catalog

Copy the following prompt into Codex:

```text
Read codex/README.md, codex/PLAN.md, codex/DATA_MODEL.md, and codex/STATUS.md before changing code. Inspect existing repository instructions and preserve unrelated work. Implement only this phase. Use current official documentation to check APIs. Do not invent repository URLs, solved statuses, source contents, credentials, or acceptance evidence. Never expose secrets in browser bundles or logs. Add meaningful verification for the phase, run applicable checks, and fix failures. Update codex/STATUS.md with changes, commands/results, limitations, and next step. Keep existing learning content unchanged. Implement the app inside this Data-Structure-and-Algorithms repository. Never modify the external Leetcode repository. Do not push or deploy unless requested. Finish with a concise reviewable report.

Retrieve the Trees pattern post linked in README, inventory every unique outbound hyperlink visible in the retrieved content, and record source/title/fetch status in catalog/sources.json and docs/source-import-report.md. Follow approved linked DSA pattern collections one level, bounded by an explicit allowlist and crawl limit. Record blocked/inaccessible pages; never silently fabricate extracted material. Use exported HTML/Markdown if supplied. Curate 15–25 verified tree problems spanning traversal, BFS, paths, construction, tree-as-graph and BST, with stable LeetCode IDs, slugs and cross-pattern relationships. Draft original Python-first notes and attribution rather than copying solutions. Explicitly identify unverified entries. Validate IDs, references, hierarchy cycles and links. Gate: app loads catalog, report distinguishes fetched and pending material.
```
