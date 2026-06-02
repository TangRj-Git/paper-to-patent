# Specification Drafting

Use this file to draft `draft/application/说明书.md`. If review finds unsupported content, create `draft/application/说明书_严格来源论文修订版.md`.

## Recommended Sections

1. 发明名称
2. 技术领域
3. 背景技术
4. 发明内容
5. 附图说明
6. 具体实施方式
7. 公式和符号说明

Use `assets/templates/specification.md` for the application-facing draft. Use `assets/templates/specification-draft.md` only as a legacy all-in-one skeleton.

## Drafting Rules

- Write the technical solution, not a compressed paper.
- Convert "experiment proves better performance" into a technical effect supported by the solution.
- Keep formulas readable in LaTeX-style Markdown.
- Explain every formula symbol and where the result is used.
- Avoid adding unsupported new modules, closed-loop control, deployment claims, or application effects.
- Avoid paper-style "本文提出", "实验表明", "消融实验", and detailed benchmark tables.

## Algorithm And Model Patents

Connect algorithms to a concrete technical field:

- specify input data and acquisition source;
- specify processing steps;
- specify output result;
- explain how the output supports monitoring, diagnosis, prediction, scheduling, control assistance, or other technical purpose.

## Gate

After drafting, run the review stage before creating figures or final formatting.
