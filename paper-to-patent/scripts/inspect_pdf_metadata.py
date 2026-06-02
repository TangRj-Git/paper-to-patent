from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def inspect_metadata(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Metadata inspection expects a PDF file.")

    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        raise RuntimeError("pdfinfo is not available. Install Poppler to inspect PDF metadata.")

    result = subprocess.run([pdfinfo, str(pdf_path)], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pdfinfo failed")
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect final patent PDF metadata.")
    parser.add_argument("pdf", type=Path, help="PDF file to inspect.")
    args = parser.parse_args()

    print(inspect_metadata(args.pdf))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
