# Workflow Overview

Use this file when the user asks for a complete paper-to-patent conversion or does not specify a stage.

## Recommended Project Folders

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
  figures/
  ppt/
  final/
```

Create these folders with `scripts/make_project_dirs.py` when the user wants organized local outputs. Script paths are relative to the skill root.

## Plain User Flow

If the user is from a lab and says the paper is a `.tex` file, use this simple flow:

1. Ask for the LaTeX entry file, usually `main.tex`.
2. Put related `.tex`, `.bib`, and figure files under `paper/latex/` if the user wants a project folder.
3. Extract LaTeX structure into `draft/internal/latex-structure-summary.md`.
4. Create technical disclosure, feasibility, mapping, and outline before writing claims.
5. Generate the five application-document drafts only after the protection strategy is clear.

The user should not need to read `references/`, `scripts/`, or `assets/templates/`; those are for Codex to use.

## Stage Order

1. Ingest LaTeX source first; use PDF only as secondary visual verification.
2. Check publication status and public-disclosure risk when relevant.
3. Convert the paper into a technical disclosure.
4. Plan prior-art/similar-patent search terms and summarize known results if the user provides search output.
5. Decide patent-conversion feasibility.
6. Create the paper-to-patent mapping table.
7. Create the dedicated patent outline.
8. Analyze protection points and claim strategy.
9. Draft claims.
10. Draft the specification.
11. Draft the abstract, request-form information checklist, and drawings list.
12. Review source consistency, formulas, terminology, claims support, and patent style.
13. Plan figures only after the body is checked.
14. Generate and check SVG figures one at a time.
15. Generate editable PPT figures only when requested.
16. Assemble Word manually unless the user explicitly asks for DOCX automation.
17. Check submission format and final Word/PDF visible content.

## Stage Gates

- Stop after feasibility if the paper lacks a complete technical solution.
- Stop before claims if the mapping, outline, and protection strategy are unclear.
- Stop before figures if the claims/specification relation has not been checked.
- Stop before final review if no Word/PDF is provided.

## Artifact Sequence

Use these filenames unless the user has a project convention:

1. `draft/internal/latex-structure-summary.md`
2. `draft/internal/公开时间与新颖性风险检查.md`
3. `draft/internal/技术交底书.md`
4. `draft/internal/现有技术检索报告.md`
5. `draft/internal/专利可行性判断报告.md`
6. `draft/internal/论文-专利内容映射表.md`
7. `draft/internal/当前小论文专属专利大纲.md`
8. `draft/internal/保护点策略分析.md`
9. `draft/application/请求书信息表.md`
10. `draft/application/权利要求书.md`
11. `draft/application/说明书.md`
12. `draft/application/说明书摘要.md`
13. `draft/application/说明书附图清单.md`
14. `draft/internal/发明专利正文检查报告.md`
15. `draft/application/说明书_严格来源论文修订版.md` when revision is needed
16. `figures/发明专利附图详细解析.md`
17. `figures/摘要附图.svg`, `figures/图1.svg`, `figures/图2.svg`
18. `final/提交前格式检查.md`
19. `final/发明专利PDF终稿检查报告.md`

## Full-Conversion Start

If the user asks for everything at once, do not generate everything at once. Start with LaTeX intake, public-risk status, technical disclosure, feasibility, mapping, and outline. Report the next stage and ask for confirmation only when a gate requires human approval.
