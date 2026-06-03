# Patent Figures

Use this file after claims and specification terms are stable enough to plan figures, mark figure positions, and generate late-stage patent drawing files.

If the figure set is unclear, first create `draft/internal/发明专利附图详细解析.md` from `assets/templates/figure-analysis.md`. This is an internal analysis file, not one of the five documents.

## Default Output

Create or update:

- `draft/application/说明书附图.md` from `assets/templates/drawings.md`
- `draft/application/摘要附图.md` from `assets/templates/abstract-drawing.md`

These Markdown files mark image positions only. Do not embed actual images, Markdown image syntax, HTML image tags, SVG content, or base64 data in them.

## Late-Stage Drawing Generation

After the claims, specification, drawing-position documents, and abstract-drawing choice are confirmed, generate real drawing files as a separate late-stage task. If the user has no preferred path, use:

- `draft/figures/专利附图生成清单.md`
- `draft/figures/图1-<图名>.svg`
- `draft/figures/图2-<图名>.svg`
- `draft/figures/摘要附图.svg`

Generate every specification drawing required by `说明书附图.md`, plus the selected abstract drawing. The abstract drawing may reuse one specification drawing if that is the chosen representative figure; still create or identify a dedicated `摘要附图` file or manifest entry.

Use simple black-and-white patent-style line drawings unless the user asks otherwise. Prefer SVG for flowcharts, system/module diagrams, model structures, and data-processing pipelines. Keep labels consistent with the claims and specification.

Create `专利附图生成清单.md` using `assets/templates/figure-generation.md`.

For generated SVG files, run or adapt `scripts/check_svg.py` to flag XML errors, missing size/viewBox, empty text labels, duplicate IDs, and obvious non-black fills. Treat warnings as drafting-review items, not legal filing guarantees.

## Figure Source Priority

Use LaTeX figure environments, captions, labels, and source image filenames as the primary source. Use PDF only to verify rendered figure order and visible numbering.

## Recommended Figure Types

- Overall method flowchart.
- System or module architecture diagram.
- Model structure diagram.
- Data construction or preprocessing flowchart.
- Training and prediction flowchart.
- Key decision, diagnosis, scheduling, or warning process.

Usually exclude:

- experiment result curves;
- ablation charts;
- benchmark comparison tables;
- decorative architecture images;
- dense formulas unless they explain the technical mechanism.

## Figure Planning Fields

For each figure, specify:

1. Figure number and name.
2. Source LaTeX figure or user-provided source.
3. Purpose.
4. Corresponding specification paragraphs.
5. Corresponding claims.
6. Modules or steps shown.
7. Whether the user must provide or redraw the image.

## Actual Drawing Boundary

Do not create actual drawing files early. Drawing generation happens only after the relevant text and figure positions are stable. Keep real drawing files separate from the five Markdown documents; do not embed them into `说明书附图.md` or `摘要附图.md`.
