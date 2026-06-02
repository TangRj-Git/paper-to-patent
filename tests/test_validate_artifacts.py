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
                    "draft/application/请求书信息表.md",
                    "draft/application/权利要求书.md",
                    "draft/application/说明书.md",
                    "draft/application/说明书摘要.md",
                    "draft/application/说明书附图清单.md",
                ],
            )

    def test_unknown_stage_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            validate_artifacts.requirements_for("unknown")


if __name__ == "__main__":
    unittest.main()
