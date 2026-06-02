# Source, Formula, Terminology, And Support Review

Use this file to check a drafted patent body before figures or final assembly.

Create `draft/internal/发明专利正文检查报告.md` using `assets/templates/review-report.md`.

## Source Consistency

Check every core feature:

- Does it come from the paper?
- If not, is it clearly marked as an assumption?
- Does the draft turn future work into an implemented feature?
- Does it extend offline experiments into online control without support?
- Does each technical effect have basis in the solution?

## Formula Review

For each formula, check:

- same formula or technically consistent formula as the paper;
- all symbols explained;
- subscript/superscript and variable meanings consistent;
- formula purpose explained;
- formula output connected to a method step;
- no unnecessary long derivation copied from the paper.

## Terminology Review

Check:

- one term per concept;
- claims, specification, and figures use the same module names;
- abbreviations have full names at first use;
- paper/code/patent terms are not mixed without explanation.

## Claims Support

Every claim term should appear in the specification with enough support. System modules should correspond to method steps. Device and medium claims should refer to the correct claim range.

## Revision Rule

If problems are found, create or update `draft/application/说明书_严格来源论文修订版.md`. If no revision is needed, this file is optional.
