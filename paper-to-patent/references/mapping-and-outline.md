# Mapping And Dedicated Outline

Use this file after feasibility review and before protection strategy, claims, or specification drafting.

## Mapping Table Purpose

The mapping table prevents unsupported expansion. Every patent feature should map back to the LaTeX paper or be marked as an assumption needing user confirmation.

Create `draft/internal/论文-专利内容映射表.md` using `assets/templates/mapping-table.md`.

Recommended rows:

- research background to 背景技术;
- method flow to 权利要求书 and 具体实施方式;
- model/system structure to 权利要求书, 说明书, and 说明书附图;
- formulas to 具体实施方式 and symbol explanation;
- data processing to claims and embodiments;
- experiment results to 有益效果 only when appropriate;
- ablation/comparison to usually excluded;
- future work to excluded unless already implemented.

## Dedicated Patent Outline

Create `draft/internal/当前小论文专属专利大纲.md` using `assets/templates/patent-outline.md`.

Include:

1. Candidate invention title.
2. Technical field.
3. Existing technical problem.
4. Core technical solution.
5. Key technical features.
6. Protection-point strategy.
7. Claim layout.
8. Specification section plan.
9. Formula usage plan.
10. Figure list and figure purpose.
11. Paper content that must be excluded.
12. Stage-by-stage generation order for the five Markdown documents.

## Gate

Do not draft claims until the mapping table and outline clearly identify the independent method claim candidate and the key dependent-claim groups.
