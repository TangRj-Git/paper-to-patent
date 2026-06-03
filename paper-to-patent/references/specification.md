# Specification Drafting

Use this file to draft `draft/application/说明书.md`.

## Source Rule

Draft from the LaTeX paper, mapping table, patent outline, and confirmed claims. PDF is secondary. Do not add unsupported modules, closed-loop controls, deployment effects, or application scenarios absent from the paper unless the user confirms them.

## Required Sections

Use `assets/templates/specification.md` for the application-facing Markdown draft.

The specification should include:

1. 发明名称
2. 技术领域
3. 背景技术
4. 发明内容
5. 附图说明
6. 具体实施方式

Add formula and symbol explanations inside 具体实施方式 where the formula is used. Do not create a separate formal "公式和符号说明" section unless the user or local convention asks for it.

## Drafting Rules

- Write the technical solution, not a compressed paper.
- Convert paper-style contribution language into patent-style technical effects.
- Convert "experiment proves better performance" into a cautious effect supported by the solution.
- Keep formulas readable in LaTeX-style Markdown.
- Explain every formula symbol and where the result is used.
- Avoid paper-style "本文提出", "实验表明", "消融实验", and detailed benchmark tables.
- Ensure every claim term is supported in the specification.

## Algorithm And Model Patents

Connect algorithms to a concrete technical field:

- specify input data and acquisition source;
- specify processing steps;
- specify output result;
- explain how the output supports monitoring, diagnosis, prediction, scheduling, control assistance, optimization, or another technical purpose.

## Figures In Specification

The specification should include an `附图说明` section matching `说明书附图.md`. The Markdown specification may refer to figure numbers, but actual images belong only as positions in `说明书附图.md`.

## Gate

After drafting, run the source/formula/terminology/support review before submission-format checking.
