# Swecha Submission Compliance Spec

## Summary

This spec captures the repository changes required to convert the original coursework repository into a Swecha-ready neural-network submission package without changing the underlying notebook work.

## Problem

The original repository had reviewer artifacts but lacked proper file naming, CI checks, pre-commit hooks, security scanning, dead-code detection, release metadata, and Spec-Kit scaffolding. It also bundled unrelated work that should not appear in this submission package.

## Scope

- In scope:
  - notebook file normalization
  - README and submission-oriented documentation refresh
  - GitLab CI, pre-commit, changelog, and security metadata
  - Python-based lint, type-check, test, coverage, audit, and dead-code commands
  - Spec-Kit scaffolding
- Out of scope:
  - notebook algorithm changes
  - model retraining
  - unrelated notebook content

## Requirements

1. Store the neural network notebook under a conventional path with the correct extension.
2. Reframe the repository as a Swecha-ready submission while keeping the artifact descriptions accurate.
3. Add explicit GitLab CI jobs for install, format, lint, type-check, test, coverage, dependency audit, secret scanning, and dead-code checks.
4. Add optional `pre-commit` hooks that cover formatting, linting, type-checking, tests, and secret scanning.
5. Add Spec-Kit scaffolding under `.specify/` and keep this compliance spec current.
6. Ensure root-level verification commands exist and can be run without relying on notebook execution.

## Risks

- Notebook formatting tools can rewrite metadata, so checks should be review-only by default.
- Heavy notebook dependencies such as TensorFlow should remain optional for local reruns.
- Compliance jobs must stay explicit and checker-detectable.

## Verification

- `python -m black --check submission_artifacts tests`
- `python -m nbqa black --check notebooks/neural_network_from_scratch.ipynb`
- `python -m ruff check submission_artifacts tests`
- `python -m nbqa ruff notebooks/neural_network_from_scratch.ipynb --ignore=E501`
- `python -m mypy submission_artifacts`
- `python -m pytest`
- `python -m pip_audit -r requirements-dev.txt`
- `python -m vulture submission_artifacts tests --min-confidence 80`
