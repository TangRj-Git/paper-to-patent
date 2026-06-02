# paper-to-patent skill

`paper-to-patent` 是一个 Codex skill，用于把实验室小论文、技术报告、算法模型方案、软件系统方案或实验写作材料，按阶段转写为中国发明专利材料。

## 普通用户只看这里

你们实验室如果论文是 LaTeX，优先给 Codex：

1. `main.tex` 或真实入口 `.tex` 文件。
2. 被 `\input{}`、`\include{}` 引用的 `.tex` 文件。
3. `.bib` 文件。
4. 论文里的图片源文件。
5. 可选：编译后的 PDF，用来核对最终视觉效果。

推荐启动提示词：

```text
请使用 paper-to-patent skill，以我提供的 main.tex 为主，不要优先解析 PDF。先完成 LaTeX 结构摘要、公开风险检查、技术交底书、专利可行性判断、论文-专利映射、专属大纲和保护点策略。暂时不要生成 Word，不要批量生成图片。
```

PDF 可以作为辅助，但不建议作为主输入，因为 PDF 解析容易丢公式、图题、交叉引用、表格结构和 LaTeX 源码里的真实章节关系。

## 这个 skill 会生成什么

内部分析材料在 `draft/internal/`：

1. `latex-structure-summary.md`
2. `公开时间与新颖性风险检查.md`
3. `技术交底书.md`
4. `现有技术检索报告.md`
5. `专利可行性判断报告.md`
6. `论文-专利内容映射表.md`
7. `当前小论文专属专利大纲.md`
8. `保护点策略分析.md`
9. `发明专利正文检查报告.md`

五书对应草稿在 `draft/application/`：

| 五书模块 | 本项目输出 |
|---|---|
| 请求书 | `请求书信息表.md`，只是信息清单，不替代官方表格 |
| 权利要求书 | `权利要求书.md` |
| 说明书 | `说明书.md` |
| 说明书摘要 | `说明书摘要.md` |
| 说明书附图 | `说明书附图清单.md`，实际图片放在 `figures/` |

最终检查材料在 `final/`：

- `提交前格式检查.md`
- `发明专利PDF终稿检查报告.md`

## 推荐使用流程

1. 用 LaTeX 源码提取论文结构。
2. 确认论文公开状态和新颖性风险。
3. 生成技术交底书。
4. 做现有技术/相似专利检索规划。
5. 判断是否适合转成发明专利。
6. 建立论文到专利的内容映射。
7. 生成当前小论文专属专利大纲。
8. 分析保护点和权利要求布局。
9. 生成权利要求书。
10. 生成说明书。
11. 生成说明书摘要、附图清单和请求书信息表。
12. 检查来源、公式、术语、权利要求支撑关系。
13. 正文确认后再生成附图解析和逐张 SVG。
14. 需要时人工或工具整理 Word/PDF。
15. 做提交前格式检查和最终 PDF 检查。

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

## 脚本示例

创建项目目录：

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

检查 SVG 基本结构：

```powershell
python paper-to-patent/scripts/check_svg.py patent_project/figures/图1.svg
```

## 测试

```powershell
python -m unittest discover -s tests -v
```

## 注意

- 本 skill 不会自动创建专门的 agent；它是指导当前 Codex 按阶段执行。
- `references/` 是给 Codex 按需读取的流程说明，普通用户通常不用打开。
- `assets/templates/` 是生成 Markdown 产物时用的骨架，不是额外任务。
- `scripts/` 只做确定性辅助，例如建目录、解析 LaTeX、检查 SVG 和检查阶段产物。
- 最终权利要求和提交材料应由导师或专利代理人员复核。
