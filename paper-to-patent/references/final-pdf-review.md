# Final Word/PDF Review

Use this file when the user provides a final Word or PDF candidate.

Create `final/发明专利PDF终稿检查报告.md` using `assets/templates/final-pdf-review.md`.

## Visible Content

Check:

- title matches the current invention;
- abstract is complete and concise;
- claims are numbered continuously;
- claim references are valid;
- specification paragraphs are complete;
- formulas display correctly;
- figures are readable;
- figure numbers are continuous;
- each "参见图N" reference points to the correct figure.

## Old Template Residue

Search for:

- old title;
- old author;
- old technical field;
- old figure names;
- old module names;
- unrelated technical terms.

## PDF Metadata

When `pdfinfo` is available, inspect title, author, producer, creation date, and modification date with `scripts/inspect_pdf_metadata.py` resolved from the skill root.

## Figure-Text Correspondence

Check abstract figure, figure 1 through figure N, and all specification references. Report missing figures, unreferenced figures, and mismatched terminology.
