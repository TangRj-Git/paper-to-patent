# Protection Strategy

Use this file after mapping and outline, before drafting claims.

Create `draft/internal/保护点策略分析.md` using `assets/templates/protection-strategy.md`.

## Decisions To Make

1. What is the independent protection point?
2. Is the best independent claim a method, system/device, or both?
3. Which steps are essential and must appear in claim 1?
4. Which details should become dependent claims?
5. Which paper details should stay in embodiments only?
6. Which claims might be too narrow because they copy experiments or implementation settings?
7. Which unsupported points must be removed or confirmed by the user?

## Recommended Strategy For Algorithm Papers

- Put the technical data flow and result generation in the independent method claim.
- Put model internals, preprocessing, feature construction, loss/formula details, and parameter constraints in dependent claims.
- Mirror the method into system modules only after method terms are stable.
- Add electronic device and computer-readable storage medium claims when the method is software-executable.

## Gate

Do not draft `draft/application/权利要求书.md` until the independent claim candidate and dependent-claim groups are clear.
