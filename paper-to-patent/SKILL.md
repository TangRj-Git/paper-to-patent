---
name: paper-to-patent
description: Use when converting academic papers, thesis drafts, technical reports, or experiment write-ups into Chinese invention patent materials, including patent feasibility review, paper-to-patent mapping, patent outline, claims framework, specification draft, formula/terminology/source checks, patent figure analysis, SVG patent drawings, and final PDF review. 适用于小论文转发明专利、论文生成发明专利草案、权利要求书或权利要求框架、专利说明书、专利附图、附图解析、SVG 附图、正文检查、公式检查、术语检查和 PDF 终稿检查。
---

# Paper To Patent

## Core Rule

Transform a paper into a patent by stages. Prefer Markdown artifacts for content and checks. Do not generate Word directly unless the user explicitly asks and a document tool is available.

Always preserve source traceability: every core patent feature should come from the supplied paper or be clearly marked as an assumption needing user confirmation.

## References

Load only what is needed:

- For full execution order, stage gates, artifact names, figure workflow, and final PDF checks, read `references/小论文生成发明专利完整工作流程.md`.
- For wording, claims, specification structure, formulas, figure requirements, and patent-style phrase templates, read `references/小论文转发明专利通用参考模板.md`.

If context is tight, read headings first, then load only the relevant section.

## Default Workflow

When the user asks for a complete conversion, follow this order:

1. Ingest the paper and supporting files.
2. Check public-disclosure and novelty risk when the publication status is known or ask the user if it is necessary.
3. Decide whether the paper is suitable for invention patent drafting.
4. Create `论文-专利内容映射表.md`.
5. Create `当前小论文专属专利大纲.md`.
6. Create `权利要求框架.md`.
7. Create the patent content draft as Markdown, usually `发明专利正文_初稿.md` or `发明专利正文_严格来源论文版.md`.
8. Check source consistency, formulas, terminology, claims support, and patent-style wording.
9. After content is approved, create `发明专利附图详细解析.md`.
10. Generate SVG figures one at a time, checking each before moving to the next.
11. Generate PPT-editable versions one at a time only when requested.
12. Leave Word assembly to the user unless explicitly requested.
13. If a PDF final version is provided, check visible content, metadata, old-template residue, formulas, and figure-text correspondence.

## Stage Gates

Use these gates unless the user explicitly asks to skip them:

- Do not draft full patent content before the paper-to-patent mapping and patent outline are clear.
- Do not generate figures before the patent content is approved.
- Do not generate multiple figures in one step unless the user explicitly requests batch generation.
- Do not claim the patent is legally safe or grantable; recommend final review by a supervisor or patent agent.

## Drafting Constraints

Use patent-style expression:

- Focus on technical problem, technical solution, implementation flow, and beneficial effects.
- Write clear inputs, processing steps, outputs, and application modules.
- Avoid paper-style emphasis on experiments, comparison tables, and numerical performance unless the user asks.
- Avoid unsupported expansion beyond the paper.
- For algorithm/model patents, connect the algorithm to a concrete technical field and technical process.
- For formulas, write them in readable LaTeX-style Markdown, explain every symbol, and state what each formula computes and where the result is used.

## Figure Rules

Patent figures should be black-and-white line diagrams, flowcharts, module diagrams, data-construction diagrams, model-structure diagrams, training/prediction diagrams, or system-architecture diagrams.

For each figure:

1. Explain its purpose and corresponding patent paragraphs before generating it.
2. Keep text short and consistent with the claims/specification.
3. Avoid experiment charts, result curves, decorative images, and unnecessary formulas.
4. Check arrows, module names, figure number, text overlap, and correspondence with the specification.

## Tool Guidance

Use available tools according to the task and environment:

- Use file-system tools to read the paper, create Markdown artifacts, save SVG files, and organize outputs.
- Use PDF utilities such as `pdfinfo`, `pdftotext`, and `pdftoppm` when available to inspect PDF metadata, extract text, render pages, find old-template residue, and check figure-text correspondence.
- Use image viewing or browser-preview tools to inspect rendered PDF pages and generated SVG figures.
- Generate SVG directly when possible; use draw.io/svgmaker-style tools only when they are available and beneficial.
- Use presentation tools such as python-pptx or a Presentations plugin only when the user asks for editable PPT figures.
- Use DOCX/document tools only when the user explicitly asks to edit Word directly; otherwise prefer Markdown drafts and let the user assemble Word manually.
- Use web search only when current official requirements, laws, rules, or source attribution must be verified.
- Use skill-creation tools only when maintaining or packaging this skill, not during normal paper-to-patent conversion.

## Output Style

Write Chinese patent materials in Chinese unless the user asks otherwise.

When creating files, use clear filenames and report the paths changed. Keep intermediate artifacts separate from final Word/PDF files when possible.
