from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TemplateTests(unittest.TestCase):
    def test_drawing_templates_use_image_positions_not_embedded_images(self) -> None:
        for name in ("drawings.md", "abstract-drawing.md"):
            template = ROOT / "paper-to-patent" / "assets" / "templates" / name
            text = template.read_text(encoding="utf-8")

            self.assertIn("图片位置", text, name)
            self.assertNotIn("![", text, name)
            self.assertNotIn("<img", text.lower(), name)

    def test_figure_generation_template_tracks_abstract_drawing(self) -> None:
        template = ROOT / "paper-to-patent" / "assets" / "templates" / "figure-generation.md"
        text = template.read_text(encoding="utf-8")

        self.assertIn("说明书附图文件", text)
        self.assertIn("摘要附图文件", text)
        self.assertIn("图片文件", text)


if __name__ == "__main__":
    unittest.main()
