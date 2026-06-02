from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


SECTION_COMMANDS = ("section", "subsection", "subsubsection", "paragraph")
EQUATION_ENVIRONMENTS = ("equation", "align", "gather", "multline", "eqnarray")


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        cut_at = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut_at = index
                break
        lines.append(line if cut_at is None else line[:cut_at])
    return "\n".join(lines)


def normalize_text(text: str) -> str:
    text = text.replace("~", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_balanced_braces(text: str, open_index: int) -> tuple[str, int]:
    if open_index >= len(text) or text[open_index] != "{":
        raise ValueError("Expected opening brace")
    depth = 0
    content_start = open_index + 1
    index = open_index
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[content_start:index], index + 1
        index += 1
    raise ValueError("Unclosed brace group")


def skip_optional_arguments(text: str, index: int) -> int:
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text) or text[index] != "[":
            return index
        depth = 1
        index += 1
        while index < len(text) and depth:
            if text[index] == "\\":
                index += 2
                continue
            if text[index] == "[":
                depth += 1
            elif text[index] == "]":
                depth -= 1
            index += 1
    return index


def iter_command_args(text: str, command: str) -> Iterable[tuple[str, int, int]]:
    pattern = re.compile(rf"\\{re.escape(command)}\*?(?![A-Za-z])")
    for match in pattern.finditer(text):
        index = skip_optional_arguments(text, match.end())
        if index >= len(text) or text[index] != "{":
            continue
        try:
            argument, end = extract_balanced_braces(text, index)
        except ValueError:
            continue
        yield normalize_text(argument), match.start(), end


def first_command_arg(text: str, command: str) -> str:
    return next((arg for arg, _, _ in iter_command_args(text, command)), "")


def split_latex_keys(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def iter_environment(text: str, name: str) -> Iterable[tuple[str, int, int]]:
    begin_pattern = re.compile(rf"\\begin\{{{re.escape(name)}\}}")
    for begin in begin_pattern.finditer(text):
        end_match = re.search(rf"\\end\{{{re.escape(name)}\}}", text[begin.end() :])
        if not end_match:
            continue
        content_start = begin.end()
        content_end = begin.end() + end_match.start()
        yield text[content_start:content_end].strip(), begin.start(), begin.end() + end_match.end()


def resolve_tex_path(current_file: Path, argument: str) -> Path:
    candidate = Path(argument.strip())
    if candidate.suffix == "":
        candidate = candidate.with_suffix(".tex")
    if not candidate.is_absolute():
        candidate = current_file.parent / candidate
    return candidate


def read_with_inputs(path: Path, seen: set[Path] | None = None, included: list[str] | None = None) -> str:
    seen = seen if seen is not None else set()
    included = included if included is not None else []
    resolved = path.resolve()
    if resolved in seen:
        return ""
    seen.add(resolved)
    included.append(str(resolved))

    text = strip_comments(resolved.read_text(encoding="utf-8"))
    output: list[str] = []
    cursor = 0
    include_pattern = re.compile(r"\\(input|include)\*?(?![A-Za-z])")
    for match in include_pattern.finditer(text):
        index = skip_optional_arguments(text, match.end())
        if index >= len(text) or text[index] != "{":
            continue
        try:
            argument, end = extract_balanced_braces(text, index)
        except ValueError:
            continue
        output.append(text[cursor : match.start()])
        include_path = resolve_tex_path(resolved, argument)
        if include_path.exists():
            output.append(read_with_inputs(include_path, seen, included))
        else:
            output.append(f"\n% Missing input file: {argument}\n")
        cursor = end
    output.append(text[cursor:])
    return "\n".join(output)


def extract_sections(text: str) -> list[dict[str, str]]:
    sections: list[tuple[int, dict[str, str]]] = []
    for command in SECTION_COMMANDS:
        for title, start, _ in iter_command_args(text, command):
            sections.append((start, {"level": command, "title": title}))
    return [section for _, section in sorted(sections, key=lambda item: item[0])]


def extract_equations(text: str) -> list[dict[str, str]]:
    equations: list[tuple[int, dict[str, str]]] = []
    for name in EQUATION_ENVIRONMENTS:
        for content, start, _ in iter_environment(text, name):
            equations.append(
                (
                    start,
                    {
                        "environment": name,
                        "label": first_command_arg(content, "label"),
                        "content": normalize_text(content),
                    },
                )
            )
    return [equation for _, equation in sorted(equations, key=lambda item: item[0])]


def extract_figures(text: str) -> list[dict[str, object]]:
    figures: list[dict[str, object]] = []
    for content, _, _ in iter_environment(text, "figure"):
        figures.append(
            {
                "caption": first_command_arg(content, "caption"),
                "label": first_command_arg(content, "label"),
                "graphics": [arg for arg, _, _ in iter_command_args(content, "includegraphics")],
            }
        )
    return figures


def extract_tables(text: str) -> list[dict[str, str]]:
    return [
        {
            "caption": first_command_arg(content, "caption"),
            "label": first_command_arg(content, "label"),
        }
        for content, _, _ in iter_environment(text, "table")
    ]


def extract_keys(text: str, commands: Iterable[str]) -> list[str]:
    keys: list[str] = []
    for command in commands:
        for argument, _, _ in iter_command_args(text, command):
            for key in split_latex_keys(argument):
                if key not in keys:
                    keys.append(key)
    return keys


def extract_project(main_tex: Path) -> dict[str, object]:
    included_files: list[str] = []
    text = read_with_inputs(main_tex, included=included_files)
    abstract = next((normalize_text(content) for content, _, _ in iter_environment(text, "abstract")), "")
    return {
        "source": str(main_tex),
        "included_files": included_files,
        "title": first_command_arg(text, "title"),
        "abstract": abstract,
        "sections": extract_sections(text),
        "equations": extract_equations(text),
        "figures": extract_figures(text),
        "tables": extract_tables(text),
        "labels": extract_keys(text, ("label",)),
        "refs": extract_keys(text, ("ref", "eqref", "autoref", "cref", "Cref")),
        "citations": extract_keys(text, ("cite", "citep", "citet", "parencite", "textcite")),
        "bibliography": extract_keys(text, ("bibliography", "addbibresource")),
    }


def to_markdown(result: dict[str, object]) -> str:
    sections = result.get("sections", [])
    equations = result.get("equations", [])
    figures = result.get("figures", [])
    tables = result.get("tables", [])

    lines = [
        "# LaTeX 论文结构摘要",
        "",
        "## 基本信息",
        f"- 入口文件：`{result.get('source', '')}`",
        f"- 标题：{result.get('title') or '未识别'}",
        f"- 摘要：{result.get('abstract') or '未识别'}",
        "",
        "## 已读取文件",
    ]
    lines.extend(f"- `{path}`" for path in result.get("included_files", []))

    lines.extend(["", "## 章节结构"])
    if sections:
        lines.extend(f"- {item['level']}: {item['title']}" for item in sections)  # type: ignore[index]
    else:
        lines.append("- 未识别")

    lines.extend(["", "## 公式"])
    if equations:
        for item in equations:  # type: ignore[assignment]
            lines.append(f"- {item.get('environment', '')} `{item.get('label') or '无标签'}`：{item.get('content', '')}")
    else:
        lines.append("- 未识别")

    lines.extend(["", "## 图表"])
    if figures:
        for index, item in enumerate(figures, 1):  # type: ignore[assignment]
            graphics = ", ".join(item.get("graphics", [])) or "未识别图片文件"
            lines.append(f"- 图{index} `{item.get('label') or '无标签'}`：{item.get('caption') or '无标题'}；图片：{graphics}")
    else:
        lines.append("- 未识别图")
    if tables:
        for index, item in enumerate(tables, 1):  # type: ignore[assignment]
            lines.append(f"- 表{index} `{item.get('label') or '无标签'}`：{item.get('caption') or '无标题'}")
    else:
        lines.append("- 未识别表")

    lines.extend(
        [
            "",
            "## 引用线索",
            "- 标签：" + (", ".join(result.get("labels", [])) or "未识别"),  # type: ignore[arg-type]
            "- 交叉引用：" + (", ".join(result.get("refs", [])) or "未识别"),  # type: ignore[arg-type]
            "- 文献引用：" + (", ".join(result.get("citations", [])) or "未识别"),  # type: ignore[arg-type]
            "- 参考文献文件：" + (", ".join(result.get("bibliography", [])) or "未识别"),  # type: ignore[arg-type]
            "",
            "## 可转专利重点线索",
            "- 优先检查摘要、方法章节、实验系统章节、公式、流程图、模块图和消融/对比表。",
            "- 将算法步骤、系统模块、参数约束、实验效果分别映射到技术问题、技术方案和有益效果。",
            "- 任何未在 LaTeX 正文、公式、图表或实验中出现的功能点，应标记为待确认假设。",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract a structured summary from a LaTeX paper.")
    parser.add_argument("main_tex", type=Path, help="Path to the paper's main .tex file.")
    parser.add_argument("--output", type=Path, help="Write Markdown summary to this path.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown.")
    args = parser.parse_args(list(argv) if argv is not None else None)

    result = extract_project(args.main_tex)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    markdown = to_markdown(result)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
