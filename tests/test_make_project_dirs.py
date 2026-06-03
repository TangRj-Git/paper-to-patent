from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "paper-to-patent" / "scripts" / "make_project_dirs.py"
SPEC = importlib.util.spec_from_file_location("make_project_dirs", SCRIPT)
make_project_dirs = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(make_project_dirs)


class MakeProjectDirsTests(unittest.TestCase):
    def test_creates_latex_first_project_layout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "patent-project"

            make_project_dirs.create_project_dirs(project)

            expected = [
                "paper/latex",
                "paper/pdf",
                "reference/prior-art",
                "draft/internal",
                "draft/application",
                "draft/figures",
                "final",
            ]
            for folder in expected:
                self.assertTrue((project / folder).is_dir(), folder)
            self.assertFalse((project / "ppt").exists())


if __name__ == "__main__":
    unittest.main()
