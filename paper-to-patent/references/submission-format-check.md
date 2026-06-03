# Submission Format Check

Use this file before the user sends Markdown materials to a supervisor, patent agent, or manual Word formatting workflow.

Create `final/提交前格式检查.md` using `assets/templates/submission-format-check.md`.

## Checkpoints

1. The five Markdown application-document artifacts exist.
2. Claim numbers are continuous and dependencies are valid.
3. Every claim term is supported by the specification.
4. Formula symbols are explained.
5. Figure numbers, captions, and text references match.
6. Abstract is under 300 Chinese characters and does not introduce unsupported content.
7. `说明书附图.md` and `摘要附图.md` mark image positions only and do not embed actual images.
8. Abstract drawing position is selected and matches the abstract.
9. Real drawing files exist for each required specification drawing and the selected abstract drawing, or missing drawings are marked for user action.
10. Request-form information checklist, if present, separates known values from missing values.
11. Any current-rule or legal-format question is marked for patent-agent review.
12. `scripts/validate_artifacts.py --strict-content` reports no placeholder or pending-marker warnings for the handoff stage.

## Manual Word Workflow

The final handoff remains Markdown. The user manually copies:

- `权利要求书.md` into the Word claims template;
- `说明书.md` into the Word specification template;
- `说明书附图.md` image positions into the Word drawing template, then inserts generated or user-provided real images manually;
- `说明书摘要.md` into the Word abstract template;
- `摘要附图.md` image position into the Word abstract-drawing template, then inserts the generated or user-provided selected image manually.

Do not mark this skill as having produced a Word filing package.

## Boundary

This is a drafting-quality check, not a legal filing guarantee. If official formatting or current CNIPA rules matter, verify with official sources or a patent agent.
