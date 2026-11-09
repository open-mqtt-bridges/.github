# Organization dependency and security maintenance

## Outcome

All 12 organization repositories were inventoried. The 11 active repositories have issue-linked maintenance PRs; archived idm-energy remains unchanged. Dependency and security settings are implemented, with current-head GitHub CI tracked on each PR. No release or deployment was performed.

## Pull requests and remaining lockfile findings

| Repository                  | Issue                                                                           | PR                                                                            | Remaining vulnerability findings                                                                |
| --------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| open-mqtt-bridges.github.io | [#7](https://github.com/open-mqtt-bridges/open-mqtt-bridges.github.io/issues/7) | [#8](https://github.com/open-mqtt-bridges/open-mqtt-bridges.github.io/pull/8) | One low-severity deepmerge advisory; no upstream fix                                            |
| pocketbase                  | [#66](https://github.com/open-mqtt-bridges/pocketbase/issues/66)                | [#67](https://github.com/open-mqtt-bridges/pocketbase/pull/67)                | One low-severity deepmerge advisory; no upstream fix                                            |
| homeconnect                 | [#43](https://github.com/open-mqtt-bridges/homeconnect/issues/43)               | [#44](https://github.com/open-mqtt-bridges/homeconnect/pull/44)               | One low-severity deepmerge advisory; no upstream fix                                            |
| landroid                    | [#42](https://github.com/open-mqtt-bridges/landroid/issues/42)                  | [#43](https://github.com/open-mqtt-bridges/landroid/pull/43)                  | One low-severity deepmerge advisory; no upstream fix                                            |
| philips-hue                 | [#40](https://github.com/open-mqtt-bridges/philips-hue/issues/40)               | [#41](https://github.com/open-mqtt-bridges/philips-hue/pull/41)               | One low-severity deepmerge advisory; no upstream fix                                            |
| wled                        | [#35](https://github.com/open-mqtt-bridges/wled/issues/35)                      | [#36](https://github.com/open-mqtt-bridges/wled/pull/36)                      | One low-severity deepmerge advisory; no upstream fix                                            |
| roborock                    | [#51](https://github.com/open-mqtt-bridges/roborock/issues/51)                  | [#52](https://github.com/open-mqtt-bridges/roborock/pull/52)                  | One low-severity deepmerge advisory; no upstream fix                                            |
| adguardhome                 | [#3](https://github.com/open-mqtt-bridges/adguardhome/issues/3)                 | [#7](https://github.com/open-mqtt-bridges/adguardhome/pull/7)                 | None in npm/Cargo audits                                                                        |
| display                     | [#22](https://github.com/open-mqtt-bridges/display/issues/22)                   | [#23](https://github.com/open-mqtt-bridges/display/pull/23)                   | One upstream serde_yaml advisory through the bundled MCCS database; see reachability assessment |
| modbus                      | [#3](https://github.com/open-mqtt-bridges/modbus/issues/3)                      | [#6](https://github.com/open-mqtt-bridges/modbus/pull/6)                      | None in npm/Cargo audits                                                                        |
| .github                     | [#4](https://github.com/open-mqtt-bridges/.github/issues/4)                     | [#5](https://github.com/open-mqtt-bridges/.github/pull/5)                     | No application lockfile                                                                         |

## Security coverage and compatibility

- GitHub API readback confirms Dependabot alerts, secret scanning and push protection enabled in all 11 active repositories. Open secret-scanning alert lists were empty after activation. Dependency-bearing repositories also have Dependabot security updates enabled.
- CodeQL configuration now covers Python community tooling, JavaScript/TypeScript applications/site, and Rust bridges; existing workflows remain intact. PR and default-branch analysis results must be checked independently from settings.
- NestJS runtime/testing packages update together to 12.4.0. Website uses Nuxt 4.6.4 and @nuxt/eslint 1.17.0 with a compatible import plugin. AdGuardHome adopts envalid 9 and TypeScript 7 with an explicit rootDir. Modbus adopts tokio-modbus 0.17 and drops unused TLS dependencies from its plain-TCP MQTT client.
- The user selected stable versions at least 24 hours old after clean-container checks rejected fresh versions. Fresh NestJS 12.4.2 and other affected npm/Cargo targets are deferred. No release-age exemptions or forced peer/engine acceptance remain.
- Protected compiler aliases, package managers and runtime constraints are retained. TypeScript 7 remains deferred where ESLint/Jest peers exclude it. Roborock 3.40.3 remains deferred for missing Node 26 engine support; the existing 3.40.2 resolution is retained and its engine mismatch is documented.
- Display retains the old serde_yaml parser only behind the latest stable ddc-hi/mccs-db bundled-data path; no remotely supplied YAML path was found. Unmaintained YAML dependency warnings remain documented in the native bridges.

## Validation

- All pnpm projects passed immutable installation in isolated directories with empty pnpm stores. Yarn and npm projects passed isolated frozen/clean installs. Owning lockfiles remained unchanged.
- Applicable lint/type/test/application/docs builds passed. Both Rust bridges passed formatting, Clippy with warnings denied, tests and release builds. The community checker passed.
- All nine application container builds and synthetic HTTP-health or MQTT-status smoke tests passed. Device instances were disabled and no host devices were mapped. No real cloud accounts, devices or production services were exercised.
- Website browser checks covered desktop/mobile layout, bridge filtering, empty results, keyboard interactions, FAQ expansion and client navigation, with no console warning/error or broken image observed.
- Per-repository version tables, migration details, residual findings and validation evidence are in each PR's `specs/901-dependency-security-maintenance/audit.md`.

## Delivery boundaries

Existing Dependabot PRs remain open and are linked as superseded. Changesets-generated release PRs remain untouched. Merges require separate approval and successful current-head CI. Default-branch release/deployment workflows must be considered before any merge because this maintenance request excludes releases and deployments.
