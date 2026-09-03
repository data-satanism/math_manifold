from __future__ import annotations

import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import verify_production


class ProductionPrivacyTests(unittest.TestCase):
    def verify(self, body: str) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            content = root / "content"
            content.mkdir()
            note = content / "source.md"
            note.write_text(
                "---\nid: source\nstatus: canonical\npublish: true\n---\n" + body,
                encoding="utf-8",
            )
            manifest = root / "content-manifest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "version": 2,
                        "mode": "production",
                        "notes": [
                            {
                                "id": "source",
                                "path": "source.md",
                                "sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
                            }
                        ],
                        "assets": [],
                        "asset_count": 0,
                    }
                ),
                encoding="utf-8",
            )
            output = io.StringIO()
            with patch("sys.argv", ["verify_production", str(content), str(manifest)]):
                with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                    result = verify_production.main()
            return result, output.getvalue()

    def test_accepts_public_bibliographic_reference(self) -> None:
        code, _ = self.verify("Источник: https://example.org/book.\n")
        self.assertEqual(code, 0)

    def test_rejects_private_archive_path_for_both_separators(self) -> None:
        for path in ["_private/sources/book.pdf", "_private\\sources\\book.pdf"]:
            with self.subTest(path=path):
                code, output = self.verify(f"Приватная копия: `{path}`.\n")
                self.assertEqual(code, 1)
                self.assertIn("служебный путь", output)

    def test_rejects_absolute_windows_path(self) -> None:
        code, output = self.verify("Источник: `D:\\sources\\book.pdf`.\n")
        self.assertEqual(code, 1)
        self.assertIn("абсолютный Windows-путь", output)


if __name__ == "__main__":
    unittest.main()
