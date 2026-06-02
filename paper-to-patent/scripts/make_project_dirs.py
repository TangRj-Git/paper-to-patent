from __future__ import annotations

import argparse
from pathlib import Path


FOLDERS = (
    "paper/latex",
    "paper/pdf",
    "reference/prior-art",
    "draft/internal",
    "draft/application",
    "figures",
    "ppt",
    "final",
)


def create_project_dirs(project_dir: Path) -> list[Path]:
    created: list[Path] = []
    project_dir.mkdir(parents=True, exist_ok=True)
    for name in FOLDERS:
        path = project_dir / name
        path.mkdir(parents=True, exist_ok=True)
        created.append(path)
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description="Create paper-to-patent project folders.")
    parser.add_argument("project_dir", type=Path, help="Target patent project directory.")
    args = parser.parse_args()

    created = create_project_dirs(args.project_dir)
    for path in created:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
