# Patent Figures

Use this file after claims and specification have been reviewed.

## Figure Planning

Create `figures/发明专利附图详细解析.md` with `assets/templates/figure-analysis.md`. Also create or update `draft/application/说明书附图清单.md`.

For each figure, specify:

1. Figure number and name.
2. Purpose.
3. Corresponding specification paragraphs.
4. Corresponding claims.
5. Modules or steps.
6. Arrow direction.
7. Layout.
8. Exact figure text.
9. Content to exclude.
10. Check standard.

## Recommended Figure Types

- Abstract figure.
- Overall method flowchart.
- Data construction or preprocessing flowchart.
- Model/system structure diagram.
- Training and prediction flowchart.
- System/module architecture diagram.

## Do Not Draw

- Experiment result curves.
- Ablation charts.
- Benchmark comparison tables.
- Decorative architecture images.
- Dense formulas unless unavoidable.

## SVG Generation Rule

Generate one SVG at a time. After each SVG:

- parse it with `scripts/check_svg.py` resolved from the skill root;
- preview it if a browser/image tool is available;
- check text overlap, arrows, module names, figure number, and specification correspondence;
- revise before moving to the next figure.

Only create editable PPT versions when explicitly requested.
