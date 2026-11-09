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

## Implementation and local validation

All active repositories now include Spec Kit 1.3.2 and usable Codex skills; Roborock's earlier constitution/specifications were retained. Manifest hashes, Bash syntax and explicit feature prerequisites passed. Disposable smoke tests exercised feature creation, plan/task setup and prerequisites for legacy TypeScript, modern TypeScript, Rust and website tooling. The task helper resolves paths; the agent writes tasks from the installed template.

All missing own-content licenses were supplied as MIT under the owner's approved policy. Existing WLED/AdGuard MIT, Modbus GPL-3.0 and vendored notices were retained. Shared community defaults, both sorted bridge lists and matching brand assets passed validation. Generated contributor tooling is excluded from application lint and container contexts where applicable.

| Repository | Local checks | Review | Public deployment |
| --- | --- | --- | --- |
| `adguardhome` | Passed: `yarn build`; `yarn bundle` | [PR #2](https://github.com/open-mqtt-bridges/adguardhome/pull/2) | README only |
| `display` | Passed: `cargo fmt --all --check`; `cargo clippy --all-targets --all-features -- -D warnings`; `cargo test --all-targets --all-features`; `cargo build --release`; `pnpm docs:build` | [PR #21](https://github.com/open-mqtt-bridges/display/pull/21) | Pending approved merge |
| `homeconnect` | Passed: `pnpm lint`; `pnpm typecheck`; `pnpm test`; `pnpm build`; `pnpm docs:build` | [PR #42](https://github.com/open-mqtt-bridges/homeconnect/pull/42) | Pending approved merge |
| `landroid` | Passed: `pnpm lint`; `pnpm typecheck`; `pnpm test`; `pnpm build`; `pnpm docs:build` | [PR #41](https://github.com/open-mqtt-bridges/landroid/pull/41) | Pending approved merge |
| `modbus` | Passed: `cargo fmt --all --check`; `cargo clippy --all-targets --all-features -- -D warnings`; `cargo test --all-targets --all-features`; `cargo build --release`; `npm --prefix docs run build` | [PR #2](https://github.com/open-mqtt-bridges/modbus/pull/2) | Pending approved merge |
| `philips-hue` | Passed: `pnpm lint`; `pnpm typecheck`; `pnpm test`; `pnpm build`; `pnpm docs:build` | [PR #39](https://github.com/open-mqtt-bridges/philips-hue/pull/39) | Pending approved merge |
| `pocketbase` | Passed: `pnpm lint`; `pnpm typecheck`; `pnpm test`; `pnpm build`; `pnpm docs:build` | [PR #65](https://github.com/open-mqtt-bridges/pocketbase/pull/65) | Pending approved merge |
| `roborock` | Passed: `pnpm lint`; `pnpm typecheck`; `pnpm test`; `pnpm build`; `pnpm docs:build` | [PR #50](https://github.com/open-mqtt-bridges/roborock/pull/50) | Pending approved merge |
| `wled` | Passed: `pnpm lint`; `pnpm typecheck`; `pnpm test`; `pnpm build`; `pnpm docs:build` | [PR #34](https://github.com/open-mqtt-bridges/wled/pull/34) | Pending approved merge |
| `.github` | Shared community/profile/brand checks and Spec Kit passed | [PR #3](https://github.com/open-mqtt-bridges/.github/pull/3) | Community inheritance pending merge |
| `open-mqtt-bridges.github.io` | Nuxt UI lint/types/format, four Node tests, static routes/assets/version and browser acceptance passed | [PR #2](https://github.com/open-mqtt-bridges/open-mqtt-bridges.github.io/pull/2) | Actions source configured; feature deployment pending merge |
| `idm-energy` | Excluded; archived checkout unchanged | None | README only |

AdGuard Home has no automated application test suite; compilation/bundling and its repaired Docker build passed. The original floating Node LTS builder lacked Yarn; explicit Yarn Classic 1.22.22 installation repairs `yarn: not found`. Roborock passed 30 tests with one existing intentional skip. PocketBase's typecheck now uses the installed `tsc6` compatibility binary; global `tsc` can hide the old runner failure locally.

## Documentation and browser evidence

All eight docs builds passed local HTML/link/asset checks. Direct configuration routes and logos rendered in the local browser using repository-prefixed paths; obsolete edit-link owners were corrected as well. Pages builds run for relevant PR changes; deployments are guarded to the actual default branch and were skipped on PR checks. The main branch is `master` only for Modbus.

The organization website now uses Nuxt 4.6.3 and Nuxt UI 4.12.0, as explicitly requested during implementation. It retains static hosting, local search and all ten prerendered bridge links. Desktop, 390 px and 320 px layouts, keyboard navigation, search/empty/reset/focus, light/dark controls, client navigation and direct legal-page refresh passed browser acceptance. A script-blocked fixture retains all bridge cards and legal/footer links. The footer uses package version plus the actual deployment commit. Publisher/contact details for the legal pages were confirmed by the owner from Crateview. Review screenshots and technical/legal source notes live in the website repository.

## Dependency advisory findings

These are package-manager audit snapshots from 2026-11-09. Counts include development dependencies and are not normalized across different audit clients. They do not establish exploitability in a deployed bridge. Existing bridges were deliberately not subjected to broad dependency upgrades.

| Repository / audited dependency set | Critical | High | Moderate | Low |
| --- | --- | --- | --- | --- |
| `adguardhome` all Node dependencies | 0 | 28 | 32 | 2 |
| `display` docs | 0 | 0 | 0 | 0 |
| `homeconnect` all Node dependencies | 0 | 0 | 2 | 1 |
| `landroid` all Node dependencies | 0 | 0 | 2 | 1 |
| `modbus` docs | 0 | 13 | 5 | 1 |
| `philips-hue` all Node dependencies | 0 | 0 | 2 | 1 |
| `pocketbase` all Node dependencies | 0 | 0 | 2 | 1 |
| `roborock` all Node dependencies | 0 | 0 | 2 | 1 |
| `wled` all Node dependencies | 0 | 0 | 2 | 1 |
| Website (new Nuxt dependency set, after scoped overrides) | 0 | 0 | 0 | 1 |

- **AdGuard Home:** existing Axios, WebSocket and other runtime/build dependency advisories need a separate scoped remediation. High counts include repeated dependency-path findings; inspect the owning Yarn lockfile and affected API use before upgrading.
- **Modbus docs:** the existing VitePress/Mermaid tree contains high-severity advisories (including Vite, Vue, DOMPurify and parser/build dependencies). This is the documentation dependency set, not a Rust runtime advisory scan.
- **Six modern TypeScript bridges:** one low deepmerge and two moderate glob/minimatch advisories remain in the audited trees. Handle them in their own scoped dependency work; no runtime source was changed here.
- **Website:** new esbuild/glob/minimatch overrides select patched versions and passed its checks. One low deepmerge build-tooling advisory has no patched upstream version reported; no visitor input reaches that trusted configuration merge.
- **Display docs:** the JavaScript dependency audit reports no advisories. Rust advisory scanning was not run because cargo-audit is not installed; this result does not cover native runtime dependencies.

## Readiness limits and rollout

The public-source baseline is prepared, but repositories with unresolved dependency advisories are not represented as fully security-clean. This review does not replace a complete secret-history scan, transitive redistribution-license review, hardware/device acceptance or legal certification. Existing image coordinates and application protocols remain compatible. No image release, package publication, PR merge or device deployment was performed.

All feature PRs remain open for the user's merge approval, with auto-merge disabled. Inspect the current checks on each linked PR; older successful runs are not proof for a changed head. Merge shared community defaults before relying on inherited guides/templates, then the bridge docs fixes and website feature. After approved merges, verify actual public HTML, subpages, CSS, JavaScript, icons and the footer build version. Local browser/static evidence does not claim the new versions are already live.
