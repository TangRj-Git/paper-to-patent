from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SkillDocsTests(unittest.TestCase):
    def test_skill_entrypoint_states_text_markdown_and_late_drawing_workflow(self) -> None:
        text = (ROOT / "paper-to-patent" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("The application text outputs are Markdown files", text)
        self.assertIn("Generate real patent drawing files only in the late drawing stage", text)
        self.assertNotIn("one-by-one SVG generation", text)
        self.assertNotIn("editable PPT", text)

    def test_openai_default_prompt_matches_tex_first_and_late_drawing(self) -> None:
        text = (ROOT / "paper-to-patent" / "agents" / "openai.yaml").read_text(encoding="utf-8")

        self.assertIn("main.tex", text)
        self.assertIn("真实附图只在权利要求、说明书、说明书附图位置、说明书摘要和摘要附图位置确认后的后期阶段生成", text)
        self.assertIn("不要生成 Word", text)

    def test_readme_presents_late_stage_figure_generation(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("真实附图只在权利要求书、说明书、说明书附图位置、说明书摘要和摘要附图位置确认后的后期阶段生成", text)
        self.assertIn("真实专利附图在后期附图阶段单独生成", text)
        self.assertNotIn("逐张 SVG", text)
        self.assertNotIn("ppt/", text)

    def test_user_guide_emphasizes_staged_generation_and_search_gates(self) -> None:
        text = (ROOT / "USER_GUIDE.md").read_text(encoding="utf-8")

        self.assertIn("每次只复制一条命令给 Codex", text)
        self.assertIn("## 0. 启动命令", text)
        self.assertIn("## 4. 现有技术检索方案", text)
        self.assertIn("## 16. 生成真实专利附图和摘要附图", text)
        self.assertIn("公开风险、现有技术检索、专利可行性、保护点策略", text)


if __name__ == "__main__":
    unittest.main()
