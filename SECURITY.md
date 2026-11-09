# Security policy

## Supported projects

The current default branch of each active repository is the target for security fixes. Archived repositories, including IDM Energy, are unsupported. This policy does not promise a response deadline or ongoing support for older releases.

## Report privately

Use the affected repository's **Security → Advisories → Report a vulnerability** option when available. If private vulnerability reporting is unavailable, email the maintainer at **tobias.waelde@gmail.com**. Do not post exploit details, credentials, logs containing secrets or live device configuration in public issues.

Include the repository and affected version/commit, impact, reproduction steps with redacted examples, and a proposed mitigation if available. Coordinate disclosure with the maintainer before publishing details. Repository-specific security policies take precedence.

## Deployment considerations

Keep MQTT brokers and device APIs on trusted networks, use authentication and transport encryption where supported, and grant containers only the required devices, files and network access. Use placeholders in shared configuration and keep credentials out of source control. Review the target bridge's deployment and protocol documentation before use.
