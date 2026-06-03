# Final Word/PDF Review

Use this file only when the user provides a Word or PDF candidate after manually copying Markdown drafts into Word templates.

Create `final/发明专利PDF终稿检查报告.md` using `assets/templates/final-pdf-review.md`.

## Boundary

This skill does not create the Word final file by default. Review is limited to checking a user-provided Word/PDF candidate against the Markdown sources and visible patent-document requirements.

## Visible Content Checks

Check:

- title matches the current invention;
- five-document content is complete;
- abstract is concise and does not introduce unsupported content;
- claims are numbered continuously;
- claim references are valid;
- specification sections are complete;
- specification paragraph numbering is continuous;
- formulas display correctly;
- figures are readable and placed in the intended positions;
- figure numbers are continuous;
- each "参见图N" reference points to the correct figure.

## Old Template Residue

Search for:

- old title;
- old author;
- old technical field;
- old figure names;
- old module names;
- unrelated technical terms;
- leftover placeholders such as `[发明名称]` or `待确认`.

## PDF Metadata

When `pdfinfo` is available, inspect title, author, producer, creation date, and modification date with `scripts/inspect_pdf_metadata.py` resolved from the skill root.

## Report Rule

Report visible problems and the corresponding Markdown source when possible. Mark Word-only layout work as user-handled.
