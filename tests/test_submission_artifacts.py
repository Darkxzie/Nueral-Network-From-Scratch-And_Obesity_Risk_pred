from __future__ import annotations

import json
from pathlib import Path

from submission_artifacts.metadata import ARTIFACTS, missing_artifacts, repo_root


def test_expected_artifacts_exist() -> None:
    assert missing_artifacts() == []


def test_notebooks_are_valid_nbformat_json() -> None:
    root = repo_root()
    notebook_paths = [
        artifact.absolute_path(root)
        for artifact in ARTIFACTS
        if artifact.kind == "notebook"
    ]

    for notebook_path in notebook_paths:
        content = json.loads(notebook_path.read_text(encoding="utf-8"))
        assert content["nbformat"] >= 4
        assert content["cells"]


def test_repo_root_points_to_repository() -> None:
    root = repo_root()
    assert isinstance(root, Path)
    assert (root / "README.md").exists()
