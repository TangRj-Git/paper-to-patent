from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable


def _strip_namespace(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _text_content(element: ET.Element) -> str:
    parts: list[str] = []
    if element.text:
        parts.append(element.text)
    for child in element:
        parts.append(_text_content(child))
    if element.tail:
        parts.append(element.tail)
    return "".join(parts).strip()


def inspect_svg(svg_path: Path) -> dict[str, object]:
    if not svg_path.exists():
        return {"ok": False, "errors": [f"SVG not found: {svg_path}"], "warnings": []}

    try:
        root = ET.parse(svg_path).getroot()
    except ET.ParseError as exc:
        return {"ok": False, "errors": [f"XML parse error: {exc}"], "warnings": []}

    errors: list[str] = []
    warnings: list[str] = []

    if _strip_namespace(root.tag) != "svg":
        errors.append("Root element is not <svg>.")

    has_size = any(root.get(attr) for attr in ("width", "height", "viewBox"))
    if not has_size:
        warnings.append("SVG has no width, height, or viewBox.")

    text_nodes = [node for node in root.iter() if _strip_namespace(node.tag) == "text"]
    if not text_nodes:
        warnings.append("SVG contains no <text> nodes; confirm figure labels are present.")

    for index, node in enumerate(text_nodes, start=1):
        text = _text_content(node)
        if not text:
            warnings.append(f"Text node {index} is empty.")
        if len(text) > 24:
            warnings.append(f"Text node {index} is long ({len(text)} chars): {text[:24]}...")

    ids: list[str] = []
    for node in root.iter():
        node_id = node.get("id")
        if node_id:
            ids.append(node_id)
    duplicates = sorted({node_id for node_id in ids if ids.count(node_id) > 1})
    for node_id in duplicates:
        warnings.append(f"Duplicate id: {node_id}")

    raw = svg_path.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"fill=['\"](?!none|#000|#000000|black)", raw, flags=re.I):
        warnings.append("SVG may contain non-black fill colors; patent figures should usually be black-and-white.")

    return {"ok": not errors, "errors": errors, "warnings": warnings}


def print_text_report(report: dict[str, object]) -> None:
    if report["ok"]:
        print("OK: SVG parsed successfully")
    else:
        print("Errors:")
        for error in report["errors"]:
            print(f"- {error}")
    if report["warnings"]:
        print("Warnings:")
        for warning in report["warnings"]:
            print(f"- {warning}")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check basic SVG patent figure quality.")
    parser.add_argument("svg", type=Path, help="SVG file to inspect.")
    parser.add_argument("--json", action="store_true", help="Print JSON report.")
    args = parser.parse_args(argv)

    report = inspect_svg(args.svg)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text_report(report)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
