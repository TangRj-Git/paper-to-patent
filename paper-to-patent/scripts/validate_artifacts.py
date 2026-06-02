from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


STAGE_REQUIREMENTS: dict[str, tuple[str, ...]] = {
    "latex-intake": ("draft/internal/latex-structure-summary.md",),
    "risk": ("draft/internal/公开时间与新颖性风险检查.md",),
    "feasibility": ("draft/internal/专利可行性判断报告.md",),
    "technical-disclosure": ("draft/internal/技术交底书.md",),
    "prior-art": ("draft/internal/现有技术检索报告.md",),
    "mapping-outline": (
        "draft/internal/论文-专利内容映射表.md",
        "draft/internal/当前小论文专属专利大纲.md",
    ),
    "protection-strategy": ("draft/internal/保护点策略分析.md",),
    "request-form": ("draft/application/请求书信息表.md",),
    "claims": ("draft/application/权利要求书.md",),
    "specification": ("draft/application/说明书.md",),
    "abstract": ("draft/application/说明书摘要.md",),
    "figures": (
        "figures/发明专利附图详细解析.md",
        "draft/application/说明书附图清单.md",
    ),
    "application-documents": (
        "draft/application/请求书信息表.md",
        "draft/application/权利要求书.md",
        "draft/application/说明书.md",
        "draft/application/说明书摘要.md",
        "draft/application/说明书附图清单.md",
    ),
    "review": ("draft/internal/发明专利正文检查报告.md",),
    "submission-check": ("final/提交前格式检查.md",),
    "final-pdf": ("final/发明专利PDF终稿检查报告.md",),
}

STAGE_OPTIONAL: dict[str, tuple[str, ...]] = {
    "application-documents": ("draft/application/摘要附图说明.md",),
    "review": ("draft/application/说明书_严格来源论文修订版.md",),
}


def requirements_for(stage: str) -> tuple[str, ...]:
    if stage == "complete":
        seen: list[str] = []
        for paths in STAGE_REQUIREMENTS.values():
            for path in paths:
                if path not in seen:
                    seen.append(path)
        return tuple(seen)
    try:
        return STAGE_REQUIREMENTS[stage]
    except KeyError as exc:
        valid = ", ".join(sorted([*STAGE_REQUIREMENTS, "complete"]))
        raise ValueError(f"Unknown stage '{stage}'. Valid stages: {valid}") from exc


def optional_for(stage: str) -> tuple[str, ...]:
    if stage == "complete":
        seen: list[str] = []
        for paths in STAGE_OPTIONAL.values():
            for path in paths:
                if path not in seen:
                    seen.append(path)
        return tuple(seen)
    return STAGE_OPTIONAL.get(stage, ())


def missing_artifacts(project_dir: Path, stage: str) -> list[str]:
    return [path for path in requirements_for(stage) if not (project_dir / path).exists()]


def missing_optional_artifacts(project_dir: Path, stage: str) -> list[str]:
    return [path for path in optional_for(stage) if not (project_dir / path).exists()]


def build_report(project_dir: Path, stage: str) -> dict[str, object]:
    missing = missing_artifacts(project_dir, stage)
    optional_missing = missing_optional_artifacts(project_dir, stage)
    return {
        "project_dir": str(project_dir),
        "stage": stage,
        "ok": not missing,
        "required": list(requirements_for(stage)),
        "optional": list(optional_for(stage)),
        "missing": missing,
        "optional_missing": optional_missing,
    }


def print_text_report(report: dict[str, object]) -> None:
    print(f"Project: {report['project_dir']}")
    print(f"Stage: {report['stage']}")
    if report["ok"]:
        print("OK: all required artifacts exist")
        return
    print("Missing artifacts:")
    for path in report["missing"]:
        print(f"- {path}")
    if report["optional_missing"]:
        print("Optional artifacts not found:")
        for path in report["optional_missing"]:
            print(f"- {path}")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate paper-to-patent stage artifacts.")
    parser.add_argument("--project", type=Path, default=Path("."), help="Patent project directory.")
    parser.add_argument("--stage", required=True, help="Stage name or 'complete'.")
    parser.add_argument("--json", action="store_true", help="Print JSON report.")
    args = parser.parse_args(argv)

    report = build_report(args.project, args.stage)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
