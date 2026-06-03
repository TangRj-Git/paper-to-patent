# Source, Formula, Terminology, And Support Review

Use this file to check drafted Markdown patent materials and generated drawing files before submission checks.

Create `draft/internal/发明专利正文检查报告.md` using `assets/templates/review-report.md`.

## Source Consistency

Check every core feature:

- Does it come from the LaTeX paper?
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
- claims, specification, and figure positions use the same module names;
- abbreviations have full names at first use;
- paper/code/patent terms are not mixed without explanation;
- old template terms are removed.

## Claims Support

Every claim term should appear in the specification with enough support. System modules should correspond to method steps. Device and medium claims should refer to the correct claim range.

## Drawing File Review

When real drawing files have been generated, check:

- every required `说明书附图.md` position has a corresponding drawing file or clear user-provided source;
- the selected abstract drawing has a generated file or an explicit reuse entry;
- figure numbers, figure names, modules, arrows, and step labels match the specification;
- drawing labels do not introduce unsupported features;
- generated drawings remain separate files and are not embedded into the Markdown five-document files.

## Revision Rule

If problems are found, update the relevant Markdown drafts or create `draft/application/说明书_严格来源论文修订版.md`. Do not proceed to final review while unresolved placeholders or unsupported features remain.
