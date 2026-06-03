from __future__ import annotations

import argparse
import json
import re
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
    "claims-framework": ("draft/internal/权利要求框架.md",),
    "request-form": ("draft/application/请求书信息表.md",),
    "claims": ("draft/application/权利要求书.md",),
    "specification": ("draft/application/说明书.md",),
    "abstract": ("draft/application/说明书摘要.md",),
    "abstract-drawing": ("draft/application/摘要附图.md",),
    "figure-positions": (
        "draft/application/说明书附图.md",
        "draft/application/摘要附图.md",
    ),
    "application-documents": (
        "draft/application/权利要求书.md",
        "draft/application/说明书.md",
        "draft/application/说明书附图.md",
        "draft/application/说明书摘要.md",
        "draft/application/摘要附图.md",
    ),
    "figure-analysis": ("draft/internal/发明专利附图详细解析.md",),
    "figure-files": ("draft/figures/专利附图生成清单.md",),
    "review": ("draft/internal/发明专利正文检查报告.md",),
    "submission-check": ("final/提交前格式检查.md",),
    "final-pdf": ("final/发明专利PDF终稿检查报告.md",),
}

STAGE_OPTIONAL: dict[str, tuple[str, ...]] = {
    "application-documents": ("draft/application/请求书信息表.md",),
    "review": ("draft/application/说明书_严格来源论文修订版.md",),
}

MARKDOWN_HANDOFF_REQUIREMENTS = (
    *STAGE_REQUIREMENTS["application-documents"],
    *STAGE_REQUIREMENTS["submission-check"],
)

FULL_HANDOFF_REQUIREMENTS = (
    *STAGE_REQUIREMENTS["application-documents"],
    *STAGE_REQUIREMENTS["figure-files"],
    *STAGE_REQUIREMENTS["submission-check"],
)

ALIASES = {
    "complete": "markdown-handoff",
}

PLACEHOLDER_RE = re.compile(
    r"\[(?=[^\]\n]{1,60}(?:[\u4e00-\u9fff]|TODO|TBD|待|填写|名称|对象|步骤|模块))[^\]\n]{1,60}\]",
    flags=re.IGNORECASE,
)
PENDING_MARKERS = ("待用户提供", "待用户确认", "待确认", "待填写", "TODO", "TBD")


def normalize_stage(stage: str) -> str:
    return ALIASES.get(stage, stage)


def requirements_for(stage: str) -> tuple[str, ...]:
    normalized = normalize_stage(stage)
    if normalized == "markdown-handoff":
        return MARKDOWN_HANDOFF_REQUIREMENTS
    if normalized == "full-handoff":
        return FULL_HANDOFF_REQUIREMENTS
    try:
        return STAGE_REQUIREMENTS[normalized]
    except KeyError as exc:
        valid = ", ".join(sorted([*STAGE_REQUIREMENTS, "markdown-handoff", "full-handoff", *ALIASES]))
        raise ValueError(f"Unknown stage '{stage}'. Valid stages: {valid}") from exc


def optional_for(stage: str) -> tuple[str, ...]:
    normalized = normalize_stage(stage)
    if normalized == "markdown-handoff":
        return STAGE_OPTIONAL["application-documents"]
    return STAGE_OPTIONAL.get(normalized, ())


def missing_artifacts(project_dir: Path, stage: str) -> list[str]:
    return [path for path in requirements_for(stage) if not (project_dir / path).exists()]


def missing_optional_artifacts(project_dir: Path, stage: str) -> list[str]:
    return [path for path in optional_for(stage) if not (project_dir / path).exists()]


def inspect_content(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    warnings: list[str] = []
    if not text.strip():
        warnings.append("empty file")
        return warnings
    if PLACEHOLDER_RE.search(text):
        warnings.append("contains bracket placeholder")
    if any(marker in text for marker in PENDING_MARKERS):
        warnings.append("contains pending marker")
    return warnings


def content_warnings(project_dir: Path, stage: str) -> list[dict[str, object]]:
    warnings: list[dict[str, object]] = []
    for rel_path in requirements_for(stage):
        path = project_dir / rel_path
        if not path.exists():
            continue
        item_warnings = inspect_content(path)
        if item_warnings:
            warnings.append({"path": rel_path, "warnings": item_warnings})
    return warnings


def build_report(project_dir: Path, stage: str, strict_content: bool = False) -> dict[str, object]:
    missing = missing_artifacts(project_dir, stage)
    optional_missing = missing_optional_artifacts(project_dir, stage)
    warnings = content_warnings(project_dir, stage)
    return {
        "project_dir": str(project_dir),
        "stage": stage,
        "ok": not missing and (not strict_content or not warnings),
        "strict_content": strict_content,
        "required": list(requirements_for(stage)),
        "optional": list(optional_for(stage)),
        "missing": missing,
        "optional_missing": optional_missing,
        "content_warnings": warnings,
    }


def print_text_report(report: dict[str, object]) -> None:
    print(f"Project: {report['project_dir']}")
    print(f"Stage: {report['stage']}")
    if report["ok"]:
        print("OK: all required artifacts exist")
    if report["missing"]:
        print("Missing artifacts:")
        for path in report["missing"]:
            print(f"- {path}")
    if report["optional_missing"]:
        print("Optional artifacts not found:")
        for path in report["optional_missing"]:
            print(f"- {path}")
    if report["content_warnings"]:
        print("Content warnings:")
        for item in report["content_warnings"]:
            print(f"- {item['path']}: {', '.join(item['warnings'])}")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate paper-to-patent stage artifacts.")
    parser.add_argument("--project", type=Path, default=Path("."), help="Patent project directory.")
    parser.add_argument("--stage", required=True, help="Stage name, 'markdown-handoff', or 'complete' alias.")
    parser.add_argument("--json", action="store_true", help="Print JSON report.")
    parser.add_argument("--strict-content", action="store_true", help="Fail when required artifacts contain placeholders or pending markers.")
    args = parser.parse_args(argv)

    report = build_report(args.project, args.stage, strict_content=args.strict_content)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
