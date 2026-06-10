# Contributing

This repository is packaged as a reviewable Swecha submission for notebook-based AI/ML work.

## Local Setup

1. Create a virtual environment.
2. Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

3. Install notebook runtime dependencies if you plan to rerun the notebooks:

```bash
pip install -r requirements-notebooks.txt
```

## Verification

Run the same compliance checks used by CI:

```bash
python -m black --check submission_artifacts tests
python -m nbqa black --check notebooks/neural_network_from_scratch.ipynb
python -m ruff check submission_artifacts tests
python -m nbqa ruff notebooks/neural_network_from_scratch.ipynb --ignore=E501
python -m mypy submission_artifacts
python -m pytest
python -m pip_audit -r requirements-dev.txt
python -m vulture submission_artifacts tests --min-confidence 80
gitleaks git . --config .gitleaks.toml --redact --no-banner
```

## Pre-commit

Optional `pre-commit` integration is included:

```bash
pre-commit install
pre-commit run --all-files
```

## Commits And Releases

- Prefer conventional commits such as `feat:`, `fix:`, `docs:`, `test:`, and `ci:`.
- Generate the changelog with `git-cliff --config cliff.toml --output CHANGELOG.md`.
- Use tags in the form `v<semver>`.
