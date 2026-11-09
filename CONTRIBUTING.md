# Contributing to Open MQTT Bridges

Contributions to the active bridges and their documentation are welcome. Archived repositories are historical references and do not accept changes.

## Before starting

Read the target repository's README, license, security policy, `docs/development.md` and Spec Kit constitution. Use its pinned toolchain and package manager; each repository owns its lockfile and release process. Search existing issues and pull requests before proposing a change. For larger changes, agree on the behavior in an issue first.

## Development and pull requests

1. Create a focused branch from the repository's default branch (`master` for Modbus, `main` for the other active projects).
2. Specify the user-visible outcome and compatibility constraints. Use the installed Codex Spec Kit skills where applicable; their configuration does not authorize automatic commits, releases or merges.
3. Keep changes and task commits scoped. Preserve public MQTT topics, payloads, command retention, configuration keys and compatible deployment examples. Document intentional breaking changes and migration steps explicitly.
4. Run the target's documented lint, type, test, build and documentation checks. Report commands and outcomes, including missing tests or external blockers.
5. Open a pull request referencing the issue. Include the resulting behavior and meaningful validation. Add a changeset when the repository's release conventions require it; do not publish or merge a release PR as part of feature work.

Use en-US for new public documentation, issues, commit messages and pull requests. Preserve existing source comments, formatting rules and third-party notices. Avoid unrelated dependency upgrades and formatting sweeps.

## Safe examples and reports

Never include passwords, tokens, sessions, private keys, personal device identifiers or live configuration. Redact logs and use example hosts and credentials. Report suspected vulnerabilities privately using [the security policy](SECURITY.md), not a public bug report.

## Standards

Document changed public contracts and important inputs, outputs, errors and side effects at their owning boundary. The repository's effective lint/format configuration is authoritative; passing syntax checks alone does not prove documentation completeness. Keep generated and vendored files outside routine cleanup. Be respectful and follow the [code of conduct](CODE_OF_CONDUCT.md).
