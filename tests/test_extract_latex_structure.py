from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import textwrap
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "paper-to-patent" / "scripts" / "extract_latex_structure.py"
SPEC = importlib.util.spec_from_file_location("extract_latex_structure", SCRIPT)
extract_latex_structure = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(extract_latex_structure)


class ExtractLatexStructureTests(unittest.TestCase):
    def test_extracts_core_structure_from_main_tex_and_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "sections").mkdir()
            (project / "figs").mkdir()
            (project / "main.tex").write_text(
                textwrap.dedent(
                    r"""
                    \documentclass{article}
                    \title{A Robust Signal Fusion Method}
                    \author{Lab Team}
                    \begin{document}
                    \maketitle
                    \begin{abstract}
                    We propose a fusion method that improves detection accuracy.
                    \end{abstract}
                    \section{Introduction}
                    Prior work is discussed in \cite{smith2025fusion}.
                    \input{sections/method}
                    See Fig.~\ref{fig:pipeline}.
                    \bibliography{refs}
                    \end{document}
                    """
                ).strip(),
                encoding="utf-8",
            )
            (project / "sections" / "method.tex").write_text(
                textwrap.dedent(
                    r"""
                    \section{Method}
                    \subsection{Weighted Fusion}
                    \begin{equation}
                    \label{eq:fusion}
                    y = \alpha x_1 + (1-\alpha)x_2
                    \end{equation}
                    \begin{figure}
                    \centering
                    \includegraphics[width=0.8\linewidth]{figs/pipeline.pdf}
                    \caption{Overall fusion pipeline}
                    \label{fig:pipeline}
                    \end{figure}
                    \begin{table}
                    \caption{Ablation results}
                    \label{tab:ablation}
                    \end{table}
                    """
                ).strip(),
                encoding="utf-8",
            )

            result = extract_latex_structure.extract_project(project / "main.tex")

            self.assertEqual(result["title"], "A Robust Signal Fusion Method")
            self.assertIn("improves detection accuracy", result["abstract"])
            self.assertEqual(
                [(section["level"], section["title"]) for section in result["sections"]],
                [("section", "Introduction"), ("section", "Method"), ("subsection", "Weighted Fusion")],
            )
            self.assertEqual(result["figures"][0]["caption"], "Overall fusion pipeline")
            self.assertEqual(result["figures"][0]["graphics"], ["figs/pipeline.pdf"])
            self.assertEqual(result["tables"][0]["label"], "tab:ablation")
            self.assertEqual(result["equations"][0]["label"], "eq:fusion")
            self.assertEqual(result["citations"], ["smith2025fusion"])
            self.assertEqual(result["bibliography"], ["refs"])
            self.assertEqual(
                [Path(path).name for path in result["included_files"]],
                ["main.tex", "method.tex"],
            )

    def test_markdown_summary_contains_patent_intake_sections(self) -> None:
        sample = {
            "source": "main.tex",
            "included_files": ["main.tex"],
            "missing_files": ["sections/missing.tex"],
            "title": "Paper Title",
            "abstract": "Abstract text",
            "sections": [{"level": "section", "title": "Method"}],
            "equations": [{"environment": "equation", "label": "eq:one", "content": "a=b"}],
            "figures": [{"caption": "System flow", "label": "fig:flow", "graphics": ["flow.pdf"]}],
            "tables": [],
            "labels": ["eq:one", "fig:flow"],
            "refs": ["fig:flow"],
            "citations": ["ref1"],
            "bibliography": ["refs"],
        }

        markdown = extract_latex_structure.to_markdown(sample)

        self.assertIn("# LaTeX 论文结构摘要", markdown)
        self.assertIn("## 可转专利重点线索", markdown)
        self.assertIn("Paper Title", markdown)
        self.assertIn("System flow", markdown)
        self.assertIn("## 缺失文件", markdown)
        self.assertIn("sections/missing.tex", markdown)

    def test_reports_missing_inputs_and_extracts_starred_environments(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "main.tex").write_text(
                textwrap.dedent(
                    r"""
                    \title{Starred Environments}
                    \section*{Unnumbered Background}
                    \input{sections/missing}
                    \begin{align*}
                    z &= x + y
                    \end{align*}
                    \begin{figure*}
                    \includegraphics{wide-system}
                    \caption{Wide system architecture}
                    \label{fig:wide}
                    \end{figure*}
                    \begin{table*}
                    \caption{Wide result table}
                    \label{tab:wide}
                    \end{table*}
                    """
                ).strip(),
                encoding="utf-8",
            )

            result = extract_latex_structure.extract_project(project / "main.tex")

            self.assertEqual(result["missing_files"], ["sections/missing.tex"])
            self.assertEqual(result["sections"][0]["title"], "Unnumbered Background")
            self.assertEqual(result["equations"][0]["environment"], "align*")
            self.assertEqual(result["figures"][0]["caption"], "Wide system architecture")
            self.assertEqual(result["tables"][0]["caption"], "Wide result table")


if __name__ == "__main__":
    unittest.main()
