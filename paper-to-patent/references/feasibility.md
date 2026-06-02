# Feasibility Review

Use this file to decide whether a paper can reasonably be converted into Chinese invention patent drafting materials.

## Positive Signals

- Clear technical field and application scenario.
- Clear technical problem in existing technology.
- Distinct technical solution rather than only experiment comparison.
- Executable processing flow with inputs, steps, intermediate results, and outputs.
- Key features suitable for claims.
- Technical effects connected to the solution.
- Figures can express method flow, module structure, system architecture, data construction, model structure, or training/prediction process.

## Negative Signals

- Pure theory, survey, business rule, management method, or teaching method.
- Only experiment results without a technical process.
- Only model name without input, structure, and output.
- Only performance improvement without implementation details.
- Future work written as if it were already implemented.
- Algorithm detached from a concrete technical field.

## Output Template

Create `draft/internal/专利可行性判断报告.md` using `assets/templates/feasibility-report.md`.

The report must include:

1. Recommended patent theme.
2. Technical field.
3. Technical problem.
4. Core technical solution.
5. Key protectable features.
6. Claimable feature candidates.
7. Content that should not enter the patent.
8. Missing information.
9. Feasibility conclusion: suitable, conditionally suitable, or not suitable.

## Decision Rule

If the paper is conditionally suitable, list the exact missing details needed before claims or specification drafting.
