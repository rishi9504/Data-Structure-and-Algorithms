# Canonical data model

Use stable IDs independent of hierarchy placement and filenames. Validate JSON at ingestion and app load; reject dangling references, duplicate IDs, cycles in the primary hierarchy, and malformed URLs.

| Entity | Essential fields |
| --- | --- |
| Topic | id, label, parentTopicId nullable |
| Pattern | id, topicId, label, recognitionSignals, relatedPatternIds |
| Problem | id (lc-124), leetcodeId, slug, title, difficulty, primaryPatternId, patternIds, leetcodeUrl, noteId |
| TeachingNote | id, problemId, intuition, informationFlow, recursionContract, dryRun, pythonSolution, timeComplexity, spaceComplexity, traps, recallQuestions, attribution |
| Source | id, url, title, fetchedAt, fetchStatus, sourceKind |
| SourceLink | sourceId, targetUrl, relation, fetchStatus, problemId nullable |
| RepoSource | id, url, branch nullable (resolve default), includePaths, excludePaths, role |
| Artifact | id, repoSourceId, path, blobSha, commitSha, language, artifactKind, problemId nullable, matchMethod, evidence |
| SyncSnapshot | schemaVersion, scannedAt, sources with commit/status/errors/completeness, artifacts, unresolved |
| Progress | problemId, learningStatus, updatedAt, personalNotes |
| ReviewAttempt | id, problemId, completedAt UTC, localDate, timezone, rating, independentlySolved, notes |
| MappingOverride | repoSourceId, path, problemId, reason |
| AcceptanceEvidence | problemId, verdict, sourceArtifactId, submissionId nullable, submittedAt nullable |

Artifact kinds: solution, note, test, other. Count solution artifacts only for the code-found badge. Never execute ingested code. Render imported Markdown safely; disable raw HTML unless sanitized.

Problem example: lc-124, binary-tree-maximum-path-sum, primary pattern postorder-global, additional pattern tree-dp.
Teaching contract: child returns best single downward branch; node evaluates left + node + right for the global best. Clamp negative child gains to zero; initialize global answer to negative infinity for an all-negative tree. O(n) time, O(h) recursion stack.

Both source URLs are configured. Verify canonical LeetCode IDs using problem links in file content: numbered folder prefixes may use internal IDs and must not be assumed to equal public problem numbers.
