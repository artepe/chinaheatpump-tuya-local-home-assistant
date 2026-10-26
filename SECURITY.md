# Security policy

## Reporting a vulnerability

Please do not report security problems in public issues. Use GitHub's private vulnerability reporting (**Security → Report a vulnerability** on this repository) or contact the maintainer privately through the GitHub profile [@artepe](https://github.com/artepe). Please allow time for a fix before publishing details.

## Supported versions

Security fixes are made to the latest release and the `main` branch only.

## Security design

- The Tuya local key is stored in the Home Assistant config entry, entered through a password field and redacted (with device ID and host) from diagnostics. The optional Pi credential export is deleted after a successful import.
- The dashboard websocket returns only entities the logged-in user may read, marks write access per entity, and all writes go through Home Assistant services and permissions. Card output is HTML-escaped.
