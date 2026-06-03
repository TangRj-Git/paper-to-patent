from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "paper-to-patent" / "scripts" / "validate_artifacts.py"
SPEC = importlib.util.spec_from_file_location("validate_artifacts", SCRIPT)
validate_artifacts = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validate_artifacts)


class ValidateArtifactsTests(unittest.TestCase):
    def test_missing_latex_intake_summary_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = validate_artifacts.missing_artifacts(Path(tmp), "latex-intake")
            self.assertEqual(missing, ["draft/internal/latex-structure-summary.md"])

    def test_missing_feasibility_report_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = validate_artifacts.missing_artifacts(Path(tmp), "feasibility")
            self.assertEqual(missing, ["draft/internal/专利可行性判断报告.md"])

    def test_existing_feasibility_report_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            target = project / "draft" / "internal" / "专利可行性判断报告.md"
            target.parent.mkdir(parents=True)
            target.write_text("# report\n", encoding="utf-8")

            report = validate_artifacts.build_report(project, "feasibility")
            self.assertTrue(report["ok"])
            self.assertEqual(report["missing"], [])

    def test_review_report_passes_without_optional_revised_draft(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            target = project / "draft" / "internal" / "发明专利正文检查报告.md"
            target.parent.mkdir(parents=True)
            target.write_text("# review\n", encoding="utf-8")

            report = validate_artifacts.build_report(project, "review")
            self.assertTrue(report["ok"])
            self.assertEqual(report["missing"], [])
            self.assertEqual(report["optional_missing"], ["draft/application/说明书_严格来源论文修订版.md"])

    def test_application_documents_requires_five_document_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = validate_artifacts.missing_artifacts(Path(tmp), "application-documents")
            self.assertEqual(
                missing,
                [
                    "draft/application/权利要求书.md",
                    "draft/application/说明书.md",
                    "draft/application/说明书附图.md",
                    "draft/application/说明书摘要.md",
                    "draft/application/摘要附图.md",
                ],
            )

    def test_figure_positions_stage_requires_only_markdown_position_docs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = validate_artifacts.missing_artifacts(Path(tmp), "figure-positions")
            self.assertEqual(
                missing,
                [
                    "draft/application/说明书附图.md",
                    "draft/application/摘要附图.md",
                ],
            )
            with self.assertRaises(ValueError):
                validate_artifacts.requirements_for("figures")

    def test_claims_framework_and_figure_analysis_stages_are_checkable(self) -> None:
        self.assertEqual(
            validate_artifacts.requirements_for("claims-framework"),
            ("draft/internal/权利要求框架.md",),
        )
        self.assertEqual(
            validate_artifacts.requirements_for("figure-analysis"),
            ("draft/internal/发明专利附图详细解析.md",),
        )
        self.assertEqual(
            validate_artifacts.requirements_for("figure-files"),
            ("draft/figures/专利附图生成清单.md",),
        )

    def test_complete_is_markdown_handoff_alias_not_every_stage(self) -> None:
        required = validate_artifacts.requirements_for("complete")

        self.assertEqual(required, validate_artifacts.requirements_for("markdown-handoff"))
        self.assertIn("draft/application/权利要求书.md", required)
        self.assertIn("final/提交前格式检查.md", required)
        self.assertNotIn("draft/internal/公开时间与新颖性风险检查.md", required)
        self.assertNotIn("draft/application/请求书信息表.md", required)
        self.assertNotIn("final/发明专利PDF终稿检查报告.md", required)

    def test_full_handoff_includes_figure_generation_manifest(self) -> None:
        required = validate_artifacts.requirements_for("full-handoff")

        self.assertIn("draft/application/权利要求书.md", required)
        self.assertIn("draft/figures/专利附图生成清单.md", required)
        self.assertIn("final/提交前格式检查.md", required)
        self.assertNotIn("final/发明专利PDF终稿检查报告.md", required)

    def test_content_warnings_report_empty_and_placeholder_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            target = project / "draft" / "application" / "权利要求书.md"
            target.parent.mkdir(parents=True)
            target.write_text("# 权利要求书\n\n一种[发明名称]，待用户提供。\n", encoding="utf-8")

            report = validate_artifacts.build_report(project, "claims")

            self.assertTrue(report["ok"])
            self.assertIn("contains bracket placeholder", report["content_warnings"][0]["warnings"])
            self.assertIn("contains pending marker", report["content_warnings"][0]["warnings"])

    def test_strict_content_makes_placeholder_stage_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            target = project / "draft" / "application" / "权利要求书.md"
            target.parent.mkdir(parents=True)
            target.write_text("# 权利要求书\n\n一种[发明名称]。\n", encoding="utf-8")

            report = validate_artifacts.build_report(project, "claims", strict_content=True)

            self.assertFalse(report["ok"])
            self.assertEqual(report["missing"], [])

    def test_numeric_paragraph_markers_are_not_placeholder_warnings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            target = project / "draft" / "application" / "说明书.md"
            target.parent.mkdir(parents=True)
            target.write_text("# 说明书\n\n[0001] 本发明涉及一种数据处理方法。\n", encoding="utf-8")

            report = validate_artifacts.build_report(project, "specification", strict_content=True)

            self.assertTrue(report["ok"])
            self.assertEqual(report["content_warnings"], [])

    def test_unknown_stage_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            validate_artifacts.requirements_for("unknown")


if __name__ == "__main__":
    unittest.main()
