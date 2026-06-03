# Claims Drafting

Use this file to draft `draft/application/权利要求书.md`. Use `assets/templates/claims.md` for the formal Markdown draft.

When the protection scope is not yet stable, first create `draft/internal/权利要求框架.md` from `assets/templates/claims-framework.md`. Treat it as a stage gate before the formal claims.

## Source Rule

Base every claim on the LaTeX paper, confirmed technical disclosure, mapping table, and protection strategy. PDF text is fallback material only. If a claim feature is not in the paper, mark it as a user-confirmation item before adding it to the formal claims.

## Claim Layout

For algorithm, software, data-processing, monitoring, prediction, scheduling, optimization, or system papers, consider:

1. Independent method claim.
2. Dependent method claims for inputs, preprocessing, feature construction, model structure, calculation, training, output, and application.
3. System or device claim mirroring method steps.
4. Electronic device claim when the method is software-executable.
5. Computer-readable storage medium claim when appropriate.

Only include a computer program product claim when the user or patent agent requests it.

## Independent Method Claim

The independent method claim should cover a complete technical loop:

- target object or application scenario;
- input data;
- construction of intermediate representation;
- core model, algorithm, module interaction, or processing step;
- output result;
- technical use of the output.

Do not include experiment rankings, exact performance numbers, random seeds, dataset-only details, paper contribution language, or future work.

## Dependent Claims

Group dependent claims by technical layer:

- input data and acquisition;
- data alignment, preprocessing, feature construction, or graph/sequence construction;
- model, algorithm, module structure, formula, loss, or constraint;
- output, decision, prediction, scheduling, diagnosis, or warning;
- training or optimization details when they are part of the technical solution.

## System Claim

Convert method steps into modules after method terms are stable. Module names must match the specification and figure positions.

Common module pattern:

- data acquisition module;
- intermediate construction module;
- core processing module;
- result output module;
- application or decision-support module.

## Formal Style Checks

- Number claims directly in Markdown.
- Do not use "如图所示" or "如说明书所述".
- Do not put drawings into the claims.
- Use consistent terms with the specification.
- Each claim should end with one full stop.
- Keep strategy notes in `draft/internal/保护点策略分析.md`, not in the formal `权利要求书.md`.
