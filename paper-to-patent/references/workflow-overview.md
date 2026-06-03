# Workflow Overview

Use this file when the user asks for a complete paper-to-patent conversion or does not specify a stage.

## Core Position

This skill converts a paper into staged Chinese invention-patent materials. The source priority is `.tex` first, PDF second. The application text outputs are Markdown files. Real patent drawings are generated only in the late drawing stage after claims, specification, specification drawing positions, specification abstract, and abstract drawing position are stable. The user manually copies the Markdown content into Word templates and handles final Word layout.

The analyzed `template/` files are reference evidence for format and drafting rules, not direct output targets.

## Optional Project Folders

The folder layout below is a convenience for organized local outputs, not a requirement. If the user wants to work directly in chat, use the user's uploaded files and provide staged Markdown content without forcing a workspace structure. If the user provides their own folder or filenames, follow those names.

```text
patent_project/
  paper/
    latex/
    pdf/
  reference/
    prior-art/
  draft/
    internal/
    application/
  final/
```

Create these folders with `scripts/make_project_dirs.py` only when the user wants organized local outputs. Script paths are relative to the skill root.

## Plain User Flow

If the user is from a lab and says the paper is a `.tex` file, use this simple flow:

1. Ask for or locate the LaTeX entry file, usually `main.tex`.
2. Keep related `.tex`, `.bib`, and figure files with the LaTeX project.
3. Extract LaTeX structure into a structure-summary Markdown file.
4. Create technical disclosure, feasibility report, mapping table, and dedicated outline before writing claims.
5. Create protection strategy and claims framework before formal claims.
6. Generate the five application Markdown drafts step by step; use the five-document handoff stage only for organization or checking.

The user should not need to read `references/`, `scripts/`, or `assets/templates/`; those are for Codex to use.

## Stage Order

1. Ingest LaTeX source first; use PDF only as secondary visual verification.
2. Check publication status and public-disclosure risk when relevant.
3. Convert the paper into a technical disclosure.
4. Plan prior-art or similar-patent search terms and summarize known results if available.
5. Decide patent-conversion feasibility.
6. Create the paper-to-patent mapping table.
7. Create the dedicated patent outline.
8. Analyze protection points and claim strategy.
9. Draft a claims framework if the scope is not stable.
10. Draft `权利要求书.md`.
11. Draft `说明书.md`.
12. Draft `说明书附图.md` with image positions only.
13. Draft `说明书摘要.md`.
14. Draft `摘要附图.md` with the selected abstract-drawing position only.
15. Generate real specification drawing files and the selected abstract drawing.
16. Review source consistency, formulas, terminology, claims support, figure files, and patent style.
17. Check submission format for Markdown and drawing handoff.
18. Review final Word/PDF only if the user later provides a manually assembled file.

## Stage Gates

- Stop after feasibility if the paper lacks a complete technical solution.
- Stop before claims if mapping, outline, and protection strategy are unclear.
- Stop before specification if claim terms are unstable.
- Stop before abstract if claims and specification are not confirmed.
- Stop before final Word/PDF review if no Word/PDF candidate is provided.

## Suggested Artifact Sequence

Use these filenames only when the user has not supplied a naming convention:

1. `draft/internal/latex-structure-summary.md`
2. `draft/internal/公开时间与新颖性风险检查.md`
3. `draft/internal/技术交底书.md`
4. `draft/internal/现有技术检索报告.md`
5. `draft/internal/专利可行性判断报告.md`
6. `draft/internal/论文-专利内容映射表.md`
7. `draft/internal/当前小论文专属专利大纲.md`
8. `draft/internal/保护点策略分析.md`
9. `draft/internal/权利要求框架.md` when needed
10. `draft/application/权利要求书.md`
11. `draft/application/说明书.md`
12. `draft/application/说明书附图.md` with image positions only
13. `draft/application/说明书摘要.md`
14. `draft/application/摘要附图.md` with the abstract-drawing position only
15. `draft/figures/专利附图生成清单.md` and drawing files, including `摘要附图`
16. `draft/internal/发明专利正文检查报告.md`
17. `draft/application/说明书_严格来源论文修订版.md` when revision is needed
18. `draft/internal/发明专利附图详细解析.md` when figure analysis is requested
19. `final/提交前格式检查.md`
20. `final/发明专利PDF终稿检查报告.md` only after the user provides final Word/PDF

Use `scripts/validate_artifacts.py --stage markdown-handoff --strict-content` for the final Markdown-only handoff. Use `--stage full-handoff --strict-content` when the generated drawing manifest should also be present. The legacy `complete` stage name is only an alias for `markdown-handoff`, not a request to require every conditional artifact.

## Full-Conversion Start

If the user asks for everything at once, do not generate everything at once. Start with LaTeX intake, public-risk status, technical disclosure, feasibility, mapping, and outline. Continue stage by stage and state the next stage clearly.
