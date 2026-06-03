# Prior-Art Search

Use this file when the user asks for similar patents, novelty risk, prior art, or search planning.

## Boundary

This skill can plan searches, summarize user-provided results, and compare technical features. It cannot guarantee novelty, inventiveness, authorization, grantability, or freedom to operate.

Use web search only when the user requests current or external search, and prefer official patent databases or reliable source links. For CNIPA/current legal requirements, verify from official sources.

## Search Plan

Create `draft/internal/现有技术检索报告.md` using `assets/templates/prior-art-search-report.md`.

Include:

1. Invention theme and technical field.
2. Chinese and English keyword groups.
3. Applicant, inventor, lab, or company names if relevant.
4. IPC/CPC clues if known.
5. Core technical features used as search filters.
6. Similar-paper and similar-patent comparison table.
7. Novelty-risk points needing human review.

## Comparison Rule

Compare by technical features, not by title similarity. Focus on:

- input data and acquisition;
- processing pipeline;
- model/module structure;
- key formulas or parameter constraints;
- output and technical purpose;
- differences that may support protection scope.

## Effect On Drafting

Use the search report to adjust background technology, independent-claim breadth, dependent-claim fallback features, and specification distinction points. Do not copy prior-art text into the five Markdown documents without source attribution and user confirmation.
