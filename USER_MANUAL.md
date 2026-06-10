# User Manual

## Purpose

This repository packages a neural network from scratch notebook for review,
verification, and submission. It is not a deployed web app. The primary user
flows are:

- reviewing the notebook and report artifacts
- rerunning the notebook locally
- running repository compliance checks
- preparing the repository for GitHub or Swecha GitLab submission

## Repository Contents

The main files and folders are:

- `notebooks/neural_network_from_scratch.ipynb`: the MNIST neural network
  notebook
- `submission_artifacts/`: small Python helpers used for repository-level tests
- `tests/`: pytest checks for artifact presence and metadata validity
- `.gitlab-ci.yml`: GitLab CI quality gates
- `.pre-commit-config.yaml`: optional pre-commit hooks
- `.specify/` and `specs/`: Spec-Kit scaffolding and compliance spec

## 1. Reviewer Guide

### 1.1 What To Review

If you are reviewing the submission, check:

- the notebook structure and outputs
- the root documentation
- the declared compliance commands
- the branch used for submission

### 1.2 Open The Notebook

You can inspect the notebook in:

- GitHub's notebook viewer
- GitLab's notebook viewer
- Jupyter Notebook or JupyterLab locally
- Google Colab via the link in `README.md`

### 1.3 What The Notebook Contains

The notebook implements a handwritten neural network for MNIST digit
classification using NumPy-based model logic and TensorFlow's MNIST dataset
loader.

Key stages include:

- loading and preprocessing MNIST
- defining forward propagation
- defining backward propagation
- training with SGD
- tracking loss and accuracy
- visualizing predictions or learned weights

## 2. Local Usage Guide

### 2.1 Create A Virtual Environment

On PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

On Bash:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2.2 Install Development Dependencies

These are required for repository checks:

```bash
pip install -r requirements-dev.txt
```

### 2.3 Install Notebook Runtime Dependencies

These are only needed if you want to rerun the notebook:

```bash
pip install -r requirements-notebooks.txt
```

### 2.4 Start Jupyter

If you want to execute or inspect the notebook locally:

```bash
jupyter notebook
```

Then open:

`notebooks/neural_network_from_scratch.ipynb`

If Jupyter is not installed yet:

```bash
pip install notebook
```

## 3. Running Quality Checks

### 3.1 Formatting Checks

Run:

```bash
python -m black --check submission_artifacts tests
python -m nbqa black --check notebooks/neural_network_from_scratch.ipynb
```

### 3.2 Lint Checks

Run:

```bash
python -m ruff check submission_artifacts tests
python -m nbqa ruff notebooks/neural_network_from_scratch.ipynb --ignore=E501
```

`E501` is ignored for the notebook because long training-output strings and
notebook cell formatting are preserved intentionally.

### 3.3 Type Checks

Run:

```bash
python -m mypy submission_artifacts
```

### 3.4 Tests And Coverage

Run:

```bash
python -m pytest
```

This validates:

- expected artifact paths exist
- the notebook is valid nbformat JSON
- the helper metadata module resolves the repository root correctly

### 3.5 Dependency Audit

Run:

```bash
python -m pip_audit -r requirements-dev.txt
```

This checks the development dependency set for known published
vulnerabilities.

### 3.6 Secret Scanning

Run:

```bash
gitleaks git . --config .gitleaks.toml --redact --no-banner
```

### 3.7 Dead Code Detection

Run:

```bash
python -m vulture submission_artifacts tests --min-confidence 80
```

## 4. Git Workflow

### 4.1 Do Not Push Directly To Main

This repository is intended to be updated from feature or chore branches.

Recommended flow:

1. create a new branch
2. make changes
3. run the root checks
4. commit the changes
5. push the branch
6. open a PR or MR

### 4.2 Typical Commands

```bash
git checkout -b chore/update-submission
git add -A
git commit -m "chore: update submission package"
git push -u origin chore/update-submission
```

## 5. Docker Usage

The repository includes a basic Dockerfile for containerized verification.

### 5.1 Build The Image

```bash
docker build -t neural-network-submission .
```

### 5.2 Run The Default Command

```bash
docker run --rm neural-network-submission
```

The default container command runs:

```bash
python -m pytest
```

## 6. Troubleshooting

### 6.1 `pip_audit` Times Out

This can happen when external advisory services are slow.

Try:

- rerunning the command
- checking your network connection
- retrying after a short wait

### 6.2 Notebook Lint Complains About Line Length

The notebook lint command intentionally ignores `E501`:

```bash
python -m nbqa ruff notebooks/neural_network_from_scratch.ipynb --ignore=E501
```

Use that exact command instead of plain notebook Ruff invocation.

### 6.3 Jupyter Cannot Open The Notebook

Check:

- the file path is correct
- `nbformat` is installed
- Jupyter or notebook support is installed in the active environment

### 6.4 TensorFlow Install Fails

TensorFlow wheels can be platform-specific.

If notebook execution is not required, you can still run the repository
compliance checks with only `requirements-dev.txt`.

## 7. License

This project is licensed under the GNU Affero General Public License v3.0.
See the root `LICENSE` file for the full text.

