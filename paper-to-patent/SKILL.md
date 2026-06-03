---
name: paper-to-patent
description: Use when converting LaTeX or PDF academic papers, thesis drafts, technical reports, algorithms, software systems, or engineering schemes into staged Chinese invention patent materials, including five-document Markdown drafts, source-grounded review, late-stage patent drawing files, and abstract drawing files.
---

# Paper To Patent

## Core Rule

Work by stages. Prefer the paper's LaTeX source over PDF text extraction. Keep source traceability: every core patent feature must come from the supplied paper or be marked as an assumption needing user confirmation.

The application text outputs are Markdown files. Do not generate Word, DOC, DOCX, or PPT. Generate real patent drawing files only in the late drawing stage, after claims, specification, drawing positions, and the abstract-drawing choice are stable. The user manually copies Markdown content into the lab Word templates and inserts the generated or user-provided drawings there.

Do not promise legal safety, novelty, inventiveness, authorization, or grantability. Recommend supervisor or patent-agent review before filing.

## Agent Availability

This is a Codex skill, not an automatically spawned standalone agent. `agents/openai.yaml` provides display text and a default prompt for the skill UI. Once the `paper-to-patent` folder is installed in a Codex skill root, the current Codex instance can use this skill when the user asks for paper-to-patent conversion.

## Input Priority

1. Use `main.tex` plus included `.tex`, `.bib`, and figure files as the primary source.
2. Use PDF only for visual verification, page/figure checks, or when LaTeX is unavailable.
3. Use plain text, screenshots, or notes only when neither LaTeX nor PDF is available.

For LaTeX projects, run or adapt `scripts/extract_latex_structure.py` to create a LaTeX structure summary before patent drafting. Use the user's requested output path; if none is given, use `draft/internal/latex-structure-summary.md`.

## Workflow At A Glance

Follow this order for a full conversion. Do not generate all five documents at once.

1. LaTeX intake and structure extraction.
2. Public-disclosure risk check when relevant.
3. Technical disclosure.
4. Prior-art search plan or result comparison.
5. Feasibility review.
6. Paper-to-patent mapping and dedicated outline.
7. Protection strategy and optional claims framework.
8. Claims.
9. Specification.
10. Specification drawing positions.
11. Specification abstract.
12. Abstract drawing position.
13. Patent drawing file generation, including the selected abstract drawing.
14. Source/formula/terminology/support review.
15. Submission-format check for Markdown handoff and drawing handoff.
16. Final Word/PDF review only if the user later provides a manually assembled file.

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
| Draft a claims framework before formal claims | `references/claims.md` | `draft/internal/权利要求框架.md` |
| Draft claims | `references/claims.md`, then `references/patent-phrases.md` if wording help is needed | `draft/application/权利要求书.md` |
| Draft specification | `references/specification.md`, then `references/patent-phrases.md` | `draft/application/说明书.md` |
| Organize or check the five-document Markdown handoff | `references/application-documents.md` | `draft/application/权利要求书.md`, `draft/application/说明书.md`, `draft/application/说明书附图.md`, `draft/application/说明书摘要.md`, `draft/application/摘要附图.md` |
| Mark drawing positions | `references/figures.md` | `draft/application/说明书附图.md`, `draft/application/摘要附图.md` |
| Analyze candidate patent drawings before position marking | `references/figures.md` | `draft/internal/发明专利附图详细解析.md` |
| Generate real patent drawing files after positions are stable | `references/figures.md` | `draft/figures/专利附图生成清单.md` and generated drawing files for specification drawings and abstract drawing |
| Check source, formulas, terminology, claims support | `references/review-source-formula-terms.md` | `draft/internal/发明专利正文检查报告.md` and optional `draft/application/说明书_严格来源论文修订版.md` |
| Check submission format before supervisor or agent review | `references/submission-format-check.md` | `final/提交前格式检查.md` |
| Check final Word/PDF | `references/final-pdf-review.md` | `final/发明专利PDF终稿检查报告.md` |
| Current CNIPA/legal drafting constraints are relevant | `references/cnipa-current-rules.md` | Add current-rule notes to the relevant report; verify current facts from official sources when needed |

For a complete conversion, follow the stage order in `references/workflow-overview.md`. Stop at each stage gate before continuing.

## Five-Document Mapping

The generated application materials map to the lab's five-document patent package:

| Module | Skill artifact |
|---|---|
| 权利要求书 | `draft/application/权利要求书.md` |
| 说明书 | `draft/application/说明书.md` |
| 说明书附图 | `draft/application/说明书附图.md` with image positions only |
| 说明书摘要 | `draft/application/说明书摘要.md` |
| 摘要附图 | `draft/application/摘要附图.md` with the abstract-drawing position only |

If request-form information is needed, prepare `draft/application/请求书信息表.md` as an auxiliary checklist, not as one of the five documents.

Real patent drawings, when generated, are separate files outside the five Markdown documents. Prefer `draft/figures/` when no user path is specified. Include every needed specification drawing and the selected abstract drawing.

## Stage Gates

- Do not draft full patent content before intake, technical disclosure, mapping table, and dedicated outline are clear.
- Do not draft claims before identifying the independent method/system protection point.
- Do not draft the specification before claim terms are stable.
- Do not draft the abstract before claims and specification are stable.
- In `说明书附图.md` and `摘要附图.md`, mark only image positions; do not embed actual images.
- Do not generate real drawing files before claims, specification, drawing positions, and abstract-drawing selection are stable.
- When generating drawings, include both specification drawings and the selected abstract drawing, and then check figure numbers, names, modules, and step labels against the specification.
- Do not treat publication-risk checks or prior-art search as legal advice.
- Do not add unsupported modules, effects, applications, or closed-loop control features beyond the paper.

## Tool And Script Use

This skill does not automatically create a separate agent. The current Codex instance follows these staged instructions. Use subagents only when the user explicitly asks for parallel review or the environment provides a suitable workflow.

Use bundled scripts for deterministic checks when applicable. Resolve script paths relative to this skill folder. The organized folder layout is optional; use it only when the user wants local file outputs or asks for a repeatable project workspace.

- `scripts/make_project_dirs.py`: create optional recommended LaTeX-first Markdown project folders.
- `scripts/extract_latex_structure.py`: extract title, abstract, sections, equations, figures, tables, labels, refs, citations, and bibliography from `main.tex`.
- `scripts/extract_pdf_text.py`: extract or copy paper text into Markdown/text form when LaTeX is unavailable.
- `scripts/inspect_pdf_metadata.py`: inspect PDF metadata when `pdfinfo` is available.
- `scripts/validate_artifacts.py`: check whether required stage artifacts exist; use `--stage markdown-handoff --strict-content` before the final Markdown handoff to flag placeholders and pending markers. `complete` is only a backward-compatible alias for `markdown-handoff`.
- `scripts/check_svg.py`: optional checker for generated or user-provided SVG patent drawings.

Use external tools only when available and relevant:

- PDF tools such as `pdftotext`, `pdfinfo`, and `pdftoppm` for extraction, metadata, and rendered-page checks.
- Web search only for current laws, official requirements, prior art, source attribution, or changed external facts.
- DOCX/document tools only when the user explicitly asks to review a Word/PDF candidate or edit Word directly.

## Output Rules

Write Chinese patent materials in Chinese unless the user asks otherwise. Prefer the user's requested output paths and filenames. If the user does not specify paths, use `draft/internal/` for source summaries and internal analysis, `draft/application/` for application-facing drafts, and `final/` for final checks. When information is missing, list the missing inputs and continue only with clearly labeled assumptions.
