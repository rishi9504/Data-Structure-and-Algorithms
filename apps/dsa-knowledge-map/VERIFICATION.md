# Verification — 23 November 2026

## Passed

- `npm test`: 8 meaningful Node tests: traversal contracts, maximum path sum forks/negative-only/empty input, diameter in edges and below root, balance sentinel and skewed depth, BFS levels and zigzag/right view, invalid/orphan/duplicate inputs, immutable trace frames, calendar scheduling and backup validation/merge.
- `npm run build`: Vite production bundle and deterministic versioned service worker generated successfully.
- `python3 scripts/build_catalog.py`: all 29 tracker entries have valid note anchors and Python files; 15 questions match external solution artifacts by canonical slug.
- Browser: map loads with all six topic groups; maximum path sum default trace ends at 42; negative-only custom input `[-3,-8,-1]` ends at −1; Test Me initially hides explanation and recognition hints; reveal displays original notes; recording a Good review survives reload and schedules 30 November from 23 November.
- Desktop layout visually inspected in managed preview. Source responsive rules include mobile navigation, one-column lessons, scrollable tree/code panels and 44px primary touch targets.

## Not verified

- Phone/tablet visual QA on actual devices; the available browser did not expose viewport emulation through its control API.
- Production service worker offline behavior on a real HTTPS hostname; cache assets are generated, but development preview does not register the worker.
- Docker image execution, runtime memory usage or live Caddy route: Docker and Lightsail authentication are not available here.
- Live Lightsail deployment, DNS or TLS. Deployment docs are prepared for a separate hostname alongside the birthday app; its current live configuration still requires inspection.

## Source provenance

Learning repository commit is recorded in catalog.json. External Leetcode snapshot SHA is recorded separately. Neither source timestamp is a solve date. Acceptance is explicitly unverified. Old tracker confidence is shown without turning it into a current independent-solve claim.
