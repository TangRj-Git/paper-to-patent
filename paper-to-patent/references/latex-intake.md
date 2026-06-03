# LaTeX Intake

Use this file when the user provides a `.tex` paper, a LaTeX project folder, or both LaTeX and PDF.

## Source Priority

Use LaTeX as the primary source. PDF text extraction often loses formulas, references, captions, table structure, and figure relationships. Use PDF only as a secondary check for rendered layout, figure order, or final visible content.

Preferred input package:

- `main.tex` or the actual entry `.tex` file;
- included `.tex` files referenced by `\input{}` or `\include{}`;
- `.bib` files;
- source figure files;
- optional compiled PDF for visual checking.

## Scripted Extraction

Run or adapt:

```powershell
python paper-to-patent/scripts/extract_latex_structure.py paper/latex/main.tex --output draft/internal/latex-structure-summary.md
```

The script extracts deterministic structure only: title, abstract, sections, equations, figures, tables, labels, refs, citations, bibliography declarations, and missing included files. It does not decide patentability.

If `missing_files` appears in the generated summary, stop patent drafting until the user supplies the missing `.tex` files or confirms that those files are irrelevant.

## Manual Intake Checks

After extraction, identify:

1. Core technical problem.
2. Method or system flow.
3. Inputs, outputs, and technical effect.
4. Equations that must be preserved.
5. Figures that can become patent drawing positions.
6. Experiment results that can support beneficial effects.
7. Future work or speculative claims that must be excluded.

## Output

Create `draft/internal/latex-structure-summary.md` using `assets/templates/latex-structure-summary.md`.

If no LaTeX is available, state that PDF/text extraction is being used as a fallback and list parsing limitations before any patent drafting.
