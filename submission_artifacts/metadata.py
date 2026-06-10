from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SubmissionArtifact:
    label: str
    relative_path: str
    kind: str

    def absolute_path(self, repo_root: Path) -> Path:
        return repo_root / self.relative_path


ARTIFACTS: tuple[SubmissionArtifact, ...] = (
    SubmissionArtifact(
        label="Neural network notebook",
        relative_path="notebooks/neural_network_from_scratch.ipynb",
        kind="notebook",
    ),
)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def missing_artifacts(root: Path | None = None) -> list[str]:
    resolved_root = root or repo_root()
    return [
        artifact.relative_path
        for artifact in ARTIFACTS
        if not artifact.absolute_path(resolved_root).exists()
    ]
