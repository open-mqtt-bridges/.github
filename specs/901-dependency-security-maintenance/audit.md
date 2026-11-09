# Maintenance evidence

Issue: https://github.com/open-mqtt-bridges/.github/issues/4
Base: `3694e204de9204a2a85fc026e4ba794cf2a32183` on `main`. Runtime used for local Node checks: Node 26.13.0; Cargo checks: Rust/Cargo 1.99.

## Baseline and selected targets

Original declared versions, aliases, engines and overrides are preserved in `baseline.json`. Registry metadata and release notes supplied target versions and peer/engine constraints.

| Dependency               | Before         | After                       |
| ------------------------ | -------------- | --------------------------- |
| Application dependencies | None to update | Existing ecosystem retained |

## Compatibility decisions

## Release-age policy and deferred updates

The user explicitly selected versions published at least 24 hours before update selection, following a fresh-container pnpm policy rejection. NestJS 12.4.2, dotenv 18.0.10, eventsource 5.1.5, eslint-plugin-import-x 4.18.1 and ws 8.22.2 are deferred where applicable. Further fresh Rollup/Vite/follow-redirects and Cargo fixedbitset/itoa/syn/uuid versions were checked and reverted to aged stable resolutions. No new minimumReleaseAgeExclude entries, peer/engine bypass, registry changes or build-script trust expansions are retained. Existing TypeScript aliases are preserved where tooling excludes TypeScript 7.

## Security coverage

GitHub API readback confirms Dependabot alerts, secret scanning and secret-scanning push protection enabled. Public repository dependency graphs support the enabled alerts. Available Dependabot security updates were enabled for dependency-bearing repositories. Secret-scanning open-alert lists were empty after activation. CodeQL configuration is added or retained for the repository's supported source language; successful PR/default-branch analysis must be verified separately. Dependabot entries match actual manifests, with coupled NestJS updates grouped and pnpm workspaces tracked at their lockfile root. Action major references were checked against official releases; release/deployment trigger behavior is preserved.

## Lockfile audits

No application lockfiles exist in this community repository.

### Residual findings

None found by the applicable lockfile audits.

## Validation

- `python3 scripts/check-community.py`: passed.
- `python3 scripts/check-community.py`: passed.

## Delivery

One consolidated PR will close the linked issue. Existing matching Dependabot PRs remain open and are linked as superseded. Required CI must pass on the PR current head before any separately authorized merge. No release, deployment or release-PR merge was performed.
