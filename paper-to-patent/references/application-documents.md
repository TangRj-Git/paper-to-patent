# Application Documents

Use this file when organizing or checking the five application-facing Markdown documents for the lab patent package.

Do not use this file as permission to generate all five documents in one pass. Formal drafting should still happen stage by stage: claims, specification, drawing positions, abstract, and abstract drawing.

## Boundary

The five application text documents are Markdown only. Do not generate Word, DOC, DOCX, or embedded drawings in this stage. Real drawing files are generated separately in the late drawing stage after the specification drawing positions and abstract drawing position are stable. The user copies the Markdown contents into the lab Word templates and handles final Word layout.

Use the analyzed `template/` materials only as drafting guidance:

- claims use continuous numbering and avoid figure references;
- specification follows 技术领域、背景技术、发明内容、附图说明、具体实施方式;
- specification abstract is under 300 Chinese characters and has no title in the final Word form;
- specification drawings and abstract drawing Markdown files mark image positions only; real drawing files are separate.

## Outputs

Create these files under `draft/application/`:

1. `权利要求书.md` from `assets/templates/claims.md`
2. `说明书.md` from `assets/templates/specification.md`
3. `说明书附图.md` from `assets/templates/drawings.md`
4. `说明书摘要.md` from `assets/templates/abstract.md`
5. `摘要附图.md` from `assets/templates/abstract-drawing.md`

If request-form information is needed, create `请求书信息表.md` from `assets/templates/request-form-info.md` as an auxiliary checklist. It is not one of the five documents.

## Mapping To 五书

| 五书模块 | Local artifact | Notes |
|---|---|---|
| 权利要求书 | `权利要求书.md` | Defines protection scope |
| 说明书 | `说明书.md` | Supports every claim and explains embodiments |
| 说明书附图 | `说明书附图.md` | Image positions only |
| 说明书摘要 | `说明书摘要.md` | Concise technical summary, under 300 Chinese characters |
| 摘要附图 | `摘要附图.md` | Abstract-drawing position only |

## Drafting Order

Do not generate the five documents all at once. Preferred order:

1. Claims framework and claims.
2. Specification supporting every claim term.
3. Specification drawing positions based on confirmed figure list.
4. Abstract from the confirmed claims and specification.
5. Abstract drawing position after selecting the representative figure.

## Cross-Document Consistency

- Claim terms must appear in the specification.
- System or device modules must mirror method steps.
- Abstract must not introduce content absent from claims and specification.
- Figure names and numbers must match the specification and drawings documents.
- `说明书附图.md` and `摘要附图.md` must not contain Markdown image syntax or HTML image tags.
- Real drawing files, when generated, must include every required specification drawing and the selected abstract drawing.
- Request-form information must not invent inventor, applicant, address, or priority data.
