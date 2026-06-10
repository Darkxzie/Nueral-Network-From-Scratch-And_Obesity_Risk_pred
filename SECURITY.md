# Security Policy

## Reporting

If you discover a security issue in this repository, report it privately to the maintainer before opening a public issue.

## Current Controls

The repository includes:

- gitleaks secret scanning
- dependency auditing with `pip-audit`
- notebook-aware linting and formatting checks
- typed helper code under `submission_artifacts/`
- pytest coverage enforcement for the repository metadata helpers

## Scope

This project primarily distributes notebooks and documentation. The CI controls focus on repository hygiene, secrets exposure, and reproducibility rather than deployed-service hardening.

