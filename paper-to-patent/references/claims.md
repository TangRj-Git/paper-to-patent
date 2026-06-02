# Claims Drafting

Use this file to draft `draft/application/权利要求书.md`. Use `assets/templates/claims.md` for the formal draft or `assets/templates/claims-framework.md` only when the user asks for a strategy/framework instead of a full claims draft.

## Claim Layout

For algorithm, software, data-processing, system, monitoring, prediction, scheduling, or control papers, consider:

1. Independent method claim.
2. Dependent method claims for inputs, preprocessing, feature construction, model structure, calculation, training, output, or application.
3. System/device claim mirroring method steps.
4. Electronic device claim.
5. Computer-readable storage medium claim.

For the final application-facing artifact, write numbered claims directly. Keep strategy notes in `draft/internal/保护点策略分析.md`, not inside the claims document.

## Independent Method Claim

The independent method claim should cover:

- target object or application scenario;
- input data;
- key processing steps;
- core model/algorithm/system operation;
- output result;
- technical purpose of the output.

Do not include experiment rankings, exact performance numbers, random seeds, dataset-only details, or future work.

## System Claim

Convert method steps into modules:

- data acquisition module;
- data processing or preprocessing module;
- feature/model construction module;
- core processing module;
- result output module;
- application/decision-support module.

Module names must match the specification and figures.

## Device And Medium Claims

Use these only when the method can be implemented by software or program execution:

```text
一种电子设备，包括处理器和存储器，所述存储器存储有计算机程序，其特征在于，所述处理器执行所述计算机程序时实现权利要求1至N中任一项所述的方法。
```

```text
一种计算机可读存储介质，其上存储有计算机程序，其特征在于，所述计算机程序被处理器执行时实现权利要求1至N中任一项所述的方法。
```

## Checks

- Independent claim covers the full technical loop.
- Dependent claims add real limitations without repeating the full independent claim.
- Claims are supported by the mapping table and outline.
- Terms are consistent with the paper and future specification.
- Every claim term can be located in `draft/application/说明书.md`.
