# paper-to-patent skill

`paper-to-patent` 是一个 Codex skill，用于把实验室小论文、技术报告、算法模型方案、软件系统方案或实验写作材料，按阶段转写为中国发明专利 Markdown 草稿。

命令式使用流程见 [USER_GUIDE.md](USER_GUIDE.md)。普通使用者可以直接复制里面的阶段命令，让 Codex 按步骤分析自己的 `.tex` 小论文；不强制使用固定目录结构。

## 普通用户只看这里

如果论文是 LaTeX，优先给 Codex：

1. `main.tex` 或真实入口 `.tex` 文件。
2. 被 `\input{}`、`\include{}` 引用的 `.tex` 文件。
3. `.bib` 文件。
4. 论文里的图片源文件。
5. 可选：编译后的 PDF，用来核对图号、页码和最终视觉效果。

推荐启动提示词：

```text
请使用 paper-to-patent skill，以我提供的 main.tex 为主，PDF 只作为辅助核对。请按阶段一步一步分析和生成内容，不要一次性生成完整五书。先完成 LaTeX 结构摘要、公开风险检查、技术交底书、专利可行性判断、论文-专利映射、专属大纲和保护点策略。不要生成 Word、PPT、DOCX；真实附图只在权利要求书、说明书、说明书附图位置、说明书摘要和摘要附图位置确认后的后期阶段生成。
```

PDF 可以作为辅助，但不建议作为主输入，因为 PDF 解析容易丢公式、图题、交叉引用、表格结构和 LaTeX 源码里的真实章节关系。

## 现在这个 agent 能用吗

能用，但要理解它的形式：这里的 `agents/openai.yaml` 是 Codex skill 的展示信息和默认提示词，不是会自动启动的独立 agent。把 `paper-to-patent/` 安装到 Codex 的 skills 目录后，当前 Codex 在识别到“小论文转发明专利”任务时就可以加载这个 skill，并按 `SKILL.md` 的阶段流程工作。

也就是说，使用方式不是“运行一个 agent 程序”，而是对 Codex 说：

```text
请使用 paper-to-patent skill，以 paper/latex/main.tex 为主，把这篇小论文按阶段转成发明专利 Markdown 材料。
```

## 这个 skill 会生成什么

五书文字内容输出 Markdown。使用者后续自行把 Markdown 内容复制到实验室 Word 模板，并在 Word 里处理字体、页边距和页码。真实专利附图在后期附图阶段单独生成或由使用者提供，再插入 Word。

内部分析材料在 `draft/internal/`：

1. `latex-structure-summary.md`
2. `公开时间与新颖性风险检查.md`
3. `技术交底书.md`
4. `现有技术检索报告.md`
5. `专利可行性判断报告.md`
6. `论文-专利内容映射表.md`
7. `当前小论文专属专利大纲.md`
8. `保护点策略分析.md`
9. `权利要求框架.md`
10. `发明专利正文检查报告.md`

五书对应草稿在 `draft/application/`：

| 五书模块 | 本项目输出 |
|---|---|
| 权利要求书 | `权利要求书.md` |
| 说明书 | `说明书.md` |
| 说明书附图 | `说明书附图.md`，只标注图片位置；真实图文件后期单独生成 |
| 说明书摘要 | `说明书摘要.md` |
| 摘要附图 | `摘要附图.md`，只标注摘要附图位置；摘要附图文件后期单独生成 |

`请求书信息表.md` 可以作为辅助信息清单生成，但不算入这套“五书”。

`说明书附图.md` 和 `摘要附图.md` 里面不放真实图片，也不嵌入图片链接；只写“此处放置图1”“此处放置摘要附图”这类位置说明。真实图片文件建议放在 `draft/figures/`，包括说明书附图和摘要附图。

后期附图材料通常在 `draft/figures/`：

- `专利附图生成清单.md`
- `图1-<图名>.svg`
- `图2-<图名>.svg`
- `摘要附图.svg`，或在清单中明确复用哪一张说明书附图。

最终检查材料在 `final/`：

- `提交前格式检查.md`
- `发明专利PDF终稿检查报告.md`，仅在使用者已经手动整理出 Word/PDF 后检查。

仓库根目录下的 `template/` 只是前期分析用的本地 Word/PDF 参考来源，不属于默认安装的 skill 内容；已经提炼出的格式规则放在 `paper-to-patent/references/` 和 `paper-to-patent/assets/templates/` 中。

## 推荐使用流程

1. 用 LaTeX 源码提取论文结构。
2. 确认论文公开状态和新颖性风险。
3. 生成技术交底书。
4. 做现有技术/相似专利检索规划。
5. 判断是否适合转成发明专利。
6. 建立论文到专利的内容映射。
7. 生成当前小论文专属专利大纲。
8. 分析保护点和权利要求布局。
9. 必要时生成权利要求框架。
10. 生成权利要求书。
11. 生成说明书。
12. 生成说明书附图图片位置。
13. 生成说明书摘要。
14. 生成摘要附图图片位置。
15. 后期生成真实说明书附图和摘要附图。
16. 检查来源、公式、术语、权利要求支撑关系。
17. 做提交前 Markdown 和附图文件检查。
18. 使用者自行复制到 Word 模板。

## 目录结构

```text
paper-to-patent/
  SKILL.md
  agents/
    openai.yaml
  references/
    workflow-overview.md
    latex-intake.md
    intake-and-risk.md
    technical-disclosure.md
    prior-art-search.md
    feasibility.md
    mapping-and-outline.md
    protection-strategy.md
    claims.md
    specification.md
    application-documents.md
    review-source-formula-terms.md
    figures.md
    submission-format-check.md
    final-pdf-review.md
    cnipa-current-rules.md
    patent-phrases.md
  assets/
    templates/
    examples/
  scripts/
    make_project_dirs.py
    extract_latex_structure.py
    extract_pdf_text.py
    inspect_pdf_metadata.py
    validate_artifacts.py
    check_svg.py
tests/
```

## 可选脚本示例

如果想把输出保存得更整齐，可以创建项目目录；这不是强制要求：

```powershell
python paper-to-patent/scripts/make_project_dirs.py patent_project
```

提取 LaTeX 论文结构：

```powershell
python paper-to-patent/scripts/extract_latex_structure.py patent_project/paper/latex/main.tex --output patent_project/draft/internal/latex-structure-summary.md
```

检查某阶段产物是否齐全：

```powershell
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage application-documents
```

最终交付前建议使用严格内容检查：

```powershell
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage markdown-handoff --strict-content
```

检查说明书附图和摘要附图位置文件是否齐全：

```powershell
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage figure-positions
```

可单独检查中间阶段：

```powershell
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage claims-framework
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage figure-analysis
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage figure-files
```

如果已经完成五书 Markdown 和真实附图生成清单，可以检查带图交付：

```powershell
python paper-to-patent/scripts/validate_artifacts.py --project patent_project --stage full-handoff --strict-content
```

## 测试

```powershell
python -m unittest discover -s tests -v
```

## 注意

- 本 skill 不会自动创建专门的 agent；它是指导当前 Codex 按阶段执行。
- `references/` 是给 Codex 按需读取的流程说明，普通用户通常不用打开。
- `assets/templates/` 是生成 Markdown 产物时用的骨架，不是额外任务。
- `scripts/` 只做确定性辅助，例如建目录、解析 LaTeX、提取 PDF 文本和检查阶段产物。
- `complete` 只是 `markdown-handoff` 的兼容别名；如果需要同时检查真实附图生成清单，用 `full-handoff`。
- 最终权利要求和提交材料应由导师或专利代理人员复核。
