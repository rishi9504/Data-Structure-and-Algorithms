# Deploy Recall alongside the birthday application

Prepared for the existing Lightsail instance. NOT deployed or verified on that host. Read-only inspection of `frontendPractice/deploy/Caddyfile` and `docs/deployment.md` on 23 November 2026 shows the birthday stack uses Caddy and private app networks. Live host state must be inspected before applying this recipe.

## Inputs needed

- Authorized SSH access to the existing instance, the SSH username, and current live deployment paths.
- A distinct hostname for Recall with DNS pointing to the instance; do not reuse the birthday hostname or change its routing.
- Whether Caddy runs on the host or inside Docker, its container/service name, config path and proxy network name.

This workspace has no AWS deployment connector, CLI credentials or SSH key. The AWS capability record in the birthday repo documents another session, not current access. No instance, security group, DNS record, TLS setting or birthday deployment was changed.

## Build separately

Use an isolated checkout/release directory on the server, or build `dist/` on a laptop and copy only those assets to the server. Prefer building off the shared server during the birthday event to avoid build-time memory contention. No new database or AWS service is needed.

```sh
cd /YOUR/SEPARATE/CHECKOUT/apps/dsa-knowledge-map
# Optional build on this server only after verifying memory/disk headroom:
docker compose -p recall -f compose.yaml build recall
docker compose -p recall -f compose.yaml up -d recall
curl --fail http://127.0.0.1:8092/health
```

Compose publishes to host loopback only. It does not claim ports 80/443 or alter the birthday containers/volumes/networks. Check port 8092 is free before starting; choose another loopback port if needed. Resource caps apply at runtime, not during image builds. Static content is served by nginx; Python/Node are not runtime services.

### Existing host-level Caddy

Append a NEW site block based on `Caddyfile.fragment` with the actual hostname. Validate the full existing configuration, then gracefully reload the running Caddy. Save a timestamped backup of its current config first; never replace the birthday site block. The fragment proxies to host loopback port 8092.

### Existing Docker Caddy (birthday setup)

Container localhost points to Caddy itself. Identify its existing **proxy** network using `docker inspect`; do not attach Recall to a database/data network. Add ONLY Recall to that proxy network using a separate override file and an explicit alias `recall`:

```yaml
# compose.proxy.yaml — replace ACTUAL_PROXY_NETWORK after inspection.
services:
  recall:
    networks:
      default: {}
      shared-proxy:
        aliases: [recall]
networks:
  shared-proxy:
    external: true
    name: ACTUAL_PROXY_NETWORK
```

Start with both files: `docker compose -p recall -f compose.yaml -f compose.proxy.yaml up -d recall`. The additional Caddy block then uses `reverse_proxy recall:8080`. Leave all birthday forwarding trust settings and networks unchanged. Reload only Caddy after validation using its documented live deployment command; do not recreate the birthday stack just to add a hostname.

## Verification and rollback

1. Request Recall `/health`, `/`, one bundled asset, `/manifest.webmanifest` and `/sw.js` via the new HTTPS hostname.
2. Open `/#problem/lc-124`; check result 42 on the default tree, custom negative-only input, notes, Python, Test Me reveal and saved review after reload.
3. On the phone, add to home screen and revisit once offline after the initial asset cache is populated. Verify backup export/import on a second device.
4. Confirm existing birthday `/` and `/contribute` responses and expected authorization behavior remain unchanged.
5. Roll back by restoring only the prior Caddy config and gracefully reloading it. Stop/remove only the `recall` Compose project if desired. Do not use global Docker cleanup or touch birthday volumes. Keep the prior Recall image/release for a future rollback; deleting browser progress requires a user decision.

Automated cross-device progress sync will require an authenticated backend and durable per-user storage. It is deliberately not exposed as an unauthenticated write endpoint in this release.
