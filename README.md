# Swecha Neural Network Submission Pack

This repository is a submission-ready packaging of a neural-network-from-scratch notebook prepared for Swecha-style review workflows. The original modeling work is preserved, while the repository structure, documentation, and compliance tooling have been refreshed so it can be pushed through branch-based GitHub and GitLab review.

## Included Artifact

### `notebooks/neural_network_from_scratch.ipynb`

A handwritten MNIST digit classifier built around manual forward propagation, backpropagation, ReLU, softmax, cross-entropy loss, and SGD updates. The notebook uses NumPy for the network implementation and pulls MNIST from `tensorflow.keras.datasets`.

## Repository Layout

```text
.
|-- notebooks/
|   `-- neural_network_from_scratch.ipynb
|-- submission_artifacts/
|   `-- metadata.py
|-- tests/
|   `-- test_submission_artifacts.py
|-- .specify/
|-- specs/
|   `-- swecha-submission-compliance/
|-- LICENSE
|-- USER_MANUAL.md
|-- README.md
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- pyproject.toml
`-- requirements-dev.txt
```

## Quick Start

Install repository maintenance dependencies:

```bash
pip install -r requirements-dev.txt
```

Install notebook runtime dependencies only if you want to rerun the notebooks:

```bash
pip install -r requirements-notebooks.txt
```

## Compliance Checks

The repository now includes explicit root-level checks modeled on the `waterwatch` compliance setup:

- formatting: `python -m black --check submission_artifacts tests` and `python -m nbqa black --check notebooks/neural_network_from_scratch.ipynb`
- linting: `python -m ruff check submission_artifacts tests` and `python -m nbqa ruff notebooks/neural_network_from_scratch.ipynb --ignore=E501`
- type-checking: `python -m mypy submission_artifacts`
- tests and coverage: `python -m pytest`
- dependency audit: `python -m pip_audit -r requirements-dev.txt`
- secret scanning: `gitleaks git . --config .gitleaks.toml --redact --no-banner`
- dead-code detection: `python -m vulture submission_artifacts tests --min-confidence 80`

These same checks are wired into `.gitlab-ci.yml` and `.pre-commit-config.yaml`.

## License

This repository is licensed under the GNU Affero General Public License v3.0.
The full license text is included in the root `LICENSE` file.

## Documentation And Operations Files

The root of the repository now includes:

- `USER_MANUAL.md` for reviewer and contributor usage
- `.editorconfig` for editor-level formatting consistency
- `CODE_OF_CONDUCT.md` for community standards
- `.env.example` to document non-secret environment expectations
- `Dockerfile` and `.dockerignore` for containerized verification

## Spec-Kit

Lightweight Spec-Kit scaffolding is present under `.specify/` and `specs/`.

- `.specify/memory/constitution.md` records repository rules.
- `.specify/templates/` contains reusable spec, plan, and task templates.
- `specs/swecha-submission-compliance/` captures the compliance refresh applied to this repo.

## Colab Links

| Artifact | Link |
| --- | --- |
| Neural Network From Scratch | [Open in Colab](https://colab.research.google.com/drive/1ToCk_H3EcrSDSRa1icoB382aAZraj66D) |

## Author

Kamal Kumar Manchenella
