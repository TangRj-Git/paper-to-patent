# LaTeX Intake

Use this file when the user provides a `.tex` paper, a LaTeX project folder, or both LaTeX and PDF.

## Source Priority

Use LaTeX as the primary source because PDF text extraction often loses formulas, references, captions, table structure, and figure relationships. Use PDF as a secondary check for rendered layout, figure order, and final visible content.

Preferred input package:

- `main.tex` or the actual entry `.tex` file;
- included `.tex` files referenced by `\input{}` or `\include{}`;
- `.bib` files;
- source figure files;
- optional compiled PDF for visual checking.

## Scripted Extraction

Run:

```powershell
python paper-to-patent/scripts/extract_latex_structure.py paper/latex/main.tex --output draft/internal/latex-structure-summary.md
```

The script extracts deterministic structure only: title, abstract, sections, equations, figures, tables, labels, refs, citations, and bibliography declarations. It does not decide patentability.

## Manual Intake Checks

After extraction, identify:

1. Core technical problem.
2. Method or system flow.
3. Inputs, outputs, and technical effect.
4. Equations that must be preserved.
5. Figures that can become patent drawings.
6. Experiment results that can support beneficial effects.
7. Future work or speculative claims that must be excluded.

## Output

Create `draft/internal/latex-structure-summary.md`. If no LaTeX is available, state that PDF/text extraction is being used as a fallback and list parsing limitations.
