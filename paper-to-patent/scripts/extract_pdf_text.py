from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


TEXT_SUFFIXES = {".txt", ".md"}


def extract_text(input_path: Path, output_path: Path) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if input_path.suffix.lower() in TEXT_SUFFIXES:
        output_path.write_text(input_path.read_text(encoding="utf-8"), encoding="utf-8")
        return

    if input_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF, TXT, and Markdown inputs are supported.")

    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext is not available. Install Poppler or provide a text/Markdown paper file.")

    result = subprocess.run(
        [pdftotext, "-enc", "UTF-8", str(input_path), str(output_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdftotext failed")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract paper text for patent drafting.")
    parser.add_argument("input", type=Path, help="PDF, TXT, or Markdown paper file.")
    parser.add_argument("output", type=Path, help="Output text/Markdown path.")
    args = parser.parse_args()

    extract_text(args.input, args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
