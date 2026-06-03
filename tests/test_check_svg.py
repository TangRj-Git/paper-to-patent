from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "paper-to-patent" / "scripts" / "check_svg.py"
SPEC = importlib.util.spec_from_file_location("check_svg", SCRIPT)
check_svg = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(check_svg)


class CheckSvgTests(unittest.TestCase):
    def test_valid_svg_parses(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            svg = Path(tmp) / "figure.svg"
            svg.write_text(
                "<svg width='100' height='80' xmlns='http://www.w3.org/2000/svg'>"
                "<text x='10' y='20'>图1</text></svg>",
                encoding="utf-8",
            )

            report = check_svg.inspect_svg(svg)
            self.assertTrue(report["ok"])
            self.assertEqual(report["errors"], [])

    def test_invalid_svg_reports_parse_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            svg = Path(tmp) / "broken.svg"
            svg.write_text("<svg><text>", encoding="utf-8")

            report = check_svg.inspect_svg(svg)
            self.assertFalse(report["ok"])
            self.assertIn("XML parse error", report["errors"][0])

    def test_missing_svg_reports_error(self) -> None:
        report = check_svg.inspect_svg(Path("missing.svg"))
        self.assertFalse(report["ok"])
        self.assertIn("SVG not found", report["errors"][0])

    def test_strict_mode_fails_when_svg_has_warnings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            svg = Path(tmp) / "color.svg"
            svg.write_text(
                "<svg width='100' height='80' xmlns='http://www.w3.org/2000/svg'>"
                "<rect x='1' y='1' width='10' height='10' fill='red'/>"
                "</svg>",
                encoding="utf-8",
            )

            report = check_svg.inspect_svg(svg)

            self.assertTrue(report["ok"])
            self.assertFalse(check_svg.is_acceptable(report, strict=True))


if __name__ == "__main__":
    unittest.main()
