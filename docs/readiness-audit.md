# Organization readiness audit

Audit baseline: 2026-11-09. Implementation branches are intentionally unmerged. This is a scoped repository-readiness review, not a comprehensive security certification.

## Baseline inventory

| Repository | Language | Package manager | Root license | Docs | Test files |
| --- | --- | --- | --- | --- | --- |
| `.github` | Organization metadata | none | missing | README / planned landing page | 0 |
| `adguardhome` | TypeScript | Yarn classic | LICENSE.txt | README / planned landing page | 0 |
| `display` | Rust | pnpm@11.28.9 | missing | VitePress | 0 |
| `homeconnect` | TypeScript | pnpm@11.28.9 | missing | VitePress | 7 |
| `landroid` | TypeScript | pnpm@11.28.9 | missing | VitePress | 6 |
| `modbus` | Rust | none | LICENSE | VitePress | 1 |
| `open-mqtt-bridges.github.io` | Static site | none | missing | README / planned landing page | 0 |
| `philips-hue` | TypeScript | pnpm@11.28.9 | missing | VitePress | 3 |
| `pocketbase` | TypeScript | pnpm@12.16.1 | missing | VitePress | 15 |
| `roborock` | TypeScript | pnpm@11.28.9 | missing | VitePress | 6 |
| `wled` | TypeScript | pnpm@11.28.9 | LICENSE.txt | VitePress | 11 |
| `idm-energy` | TypeScript | Yarn classic | LICENSE.txt (MIT) | README | excluded: archived |

## Confirmed baseline findings

- All eight Pages homepages respond, but sampled CSS/JavaScript assets return HTTP 404 because VitePress uses pre-transfer repository base paths.
- Six bridge repositories lack a root license file; display declares MIT in Cargo.toml. Preserve WLED/AdGuard MIT and Modbus GPL-3.0.
- Shared contributor documentation and issue/PR templates are missing. Existing repository-specific security policies reference old repository URLs.
- PocketBase CI run 42603001375 fails with `tsc: not found`; compiler repair is in scope.
- Existing container coordinates and historical changelogs are intentionally preserved. The transfer changes workflow registry coordinates dynamically; publishing/retagging images is separate from this readiness work.
- No archived IDM Energy changes are permitted.

## Sensitive-file review

A scoped scan checks tracked local configuration, private-key markers and common GitHub/AWS token signatures. Only file paths are recorded; no secret values are published. This does not prove the absence of credentials or remove them from history.
- No candidates found by the scoped tracked-file scan.

## Checks and delivery

Validation results, commit SHAs, PR links and external blockers will be added as tasks finish. Production deployments remain pending merge approval.
