---
name: paper-to-patent
description: Use when converting LaTeX or PDF academic papers, thesis drafts, technical reports, experiment write-ups, algorithm/model methods, software systems, or engineering schemes into Chinese invention patent workflow materials and application documents, including technical disclosure, prior-art search planning, feasibility review, paper-to-patent mapping, protection strategy, claims, specification, abstract, drawings, formula/terminology checks, and final submission review.
---

# Paper To Patent

## Core Rule

Work by stages. Prefer the paper's LaTeX source over PDF text extraction. Keep source traceability: every core patent feature must come from the supplied paper or be marked as an assumption needing user confirmation.

Do not promise legal safety, novelty, inventiveness, authorization, or grantability. Recommend supervisor or patent-agent review before filing.

Prefer Markdown artifacts. Do not generate Word, PPT, DOCX, or batch figures unless the user explicitly asks and the required tool is available.

## Input Priority

1. Use `main.tex` plus included `.tex`, `.bib`, and figure files as the primary source.
2. Use PDF only for visual verification, page/figure checks, or when LaTeX is unavailable.
3. Use plain text, screenshots, or notes only when neither LaTeX nor PDF is available.

For LaTeX projects, run or adapt `scripts/extract_latex_structure.py` to create `draft/internal/latex-structure-summary.md` before patent drafting.

## Stage Router

Load only the reference needed for the user's current stage:

| User task | Read | Required outputs |
|---|---|---|
| Full conversion request or unclear stage | `references/workflow-overview.md` | Stage plan and next action |
| LaTeX/PDF intake and source extraction | `references/latex-intake.md` | `draft/internal/latex-structure-summary.md` for LaTeX input |
| Publication status and novelty-risk intake | `references/intake-and-risk.md` | `draft/internal/公开时间与新颖性风险检查.md` when risk review is requested |
| Technical disclosure from the paper | `references/technical-disclosure.md` | `draft/internal/技术交底书.md` |
| Prior-art or similar-patent search planning | `references/prior-art-search.md` | `draft/internal/现有技术检索报告.md` |
| Decide whether the paper can become a patent | `references/feasibility.md` | `draft/internal/专利可行性判断报告.md` |
| Build paper-to-patent mapping and dedicated outline | `references/mapping-and-outline.md` | `draft/internal/论文-专利内容映射表.md`, `draft/internal/当前小论文专属专利大纲.md` |
| Analyze protection scope and claim strategy | `references/protection-strategy.md` | `draft/internal/保护点策略分析.md` |
| Draft claims | `references/claims.md`, then `references/patent-phrases.md` if wording help is needed | `draft/application/权利要求书.md` |
| Draft specification | `references/specification.md`, then `references/patent-phrases.md` | `draft/application/说明书.md` |
| Draft five application-document set | `references/application-documents.md` | `draft/application/请求书信息表.md`, `draft/application/权利要求书.md`, `draft/application/说明书.md`, `draft/application/说明书摘要.md`, `draft/application/说明书附图清单.md` |
| Check source, formulas, terminology, claims support | `references/review-source-formula-terms.md` | `draft/internal/发明专利正文检查报告.md` and optional `draft/application/说明书_严格来源论文修订版.md` |
| Plan or create patent figures | `references/figures.md` | `figures/发明专利附图详细解析.md`, `draft/application/说明书附图清单.md`, then one SVG per confirmed figure |
| Check submission format before agent/supervisor review | `references/submission-format-check.md` | `final/提交前格式检查.md` |
| Check final Word/PDF | `references/final-pdf-review.md` | `final/发明专利PDF终稿检查报告.md` |
| Current CNIPA/legal drafting constraints are relevant | `references/cnipa-current-rules.md` | Add current-rule notes to the relevant report; verify current facts from official sources when needed |

For a complete conversion, follow the stage order in `references/workflow-overview.md`. Stop at each stage gate unless the user explicitly asks to continue.

## Five-Document Mapping

The generated application materials should map to the Chinese invention patent "五书" structure:

| Module | Skill artifact |
|---|---|
| 请求书 | `draft/application/请求书信息表.md` as an information checklist, not an official form replacement |
| 权利要求书 | `draft/application/权利要求书.md` |
| 说明书 | `draft/application/说明书.md` |
| 说明书摘要 | `draft/application/说明书摘要.md` |
| 说明书附图 | `draft/application/说明书附图清单.md` plus confirmed figure files in `figures/` |

If drawings are used, also prepare `draft/application/摘要附图说明.md` or clearly mark which drawing is recommended as the abstract drawing.

## Stage Gates

- Do not draft full patent content before intake, technical disclosure, mapping table, and dedicated outline are clear.
- Do not draft claims before identifying the independent method/system protection point.
- Do not draft figures before the claims/specification relationship has been checked.
- Do not generate multiple SVG or PPT figures in one step unless the user explicitly requests batch generation.
- Do not treat publication-risk checks or prior-art search as legal advice.
- Do not add unsupported modules, effects, applications, or closed-loop control features beyond the paper.

## Tool And Script Use

This skill does not automatically create a separate agent. The current Codex instance follows these staged instructions. Use subagents only when the user explicitly asks for parallel review or the environment provides a suitable workflow.

Use bundled scripts for deterministic checks when applicable. Resolve script paths relative to this skill folder before running them from a patent project directory.

- `scripts/make_project_dirs.py`: create the recommended LaTeX-first project folders.
- `scripts/extract_latex_structure.py`: extract title, abstract, sections, equations, figures, tables, labels, refs, citations, and bibliography from `main.tex`.
- `scripts/extract_pdf_text.py`: extract or copy paper text into Markdown/text form when LaTeX is unavailable.
- `scripts/inspect_pdf_metadata.py`: inspect PDF metadata when `pdfinfo` is available.
- `scripts/validate_artifacts.py`: check whether required stage artifacts exist.
- `scripts/check_svg.py`: parse SVG and report basic drawing-quality issues.

Use external tools only when available and relevant:

- PDF tools such as `pdftotext`, `pdfinfo`, and `pdftoppm` for extraction, metadata, and rendered-page checks.
- Image/browser preview tools for SVG and rendered PDF inspection.
- Web search only for current laws, official requirements, prior art, source attribution, or changed external facts.
- DOCX/document tools only when the user explicitly asks to edit Word directly.
- Presentation tools only when editable PPT figures are requested.

## Output Rules

Write Chinese patent materials in Chinese unless the user asks otherwise. Keep source summaries and internal analysis in `draft/internal/`; keep application-facing drafts in `draft/application/`; keep figures, PPT, and final checks in separate folders. When information is missing, list the missing inputs and continue only with clearly labeled assumptions.
