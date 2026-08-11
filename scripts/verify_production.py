from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import yaml


WIKILINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
ASSET_SUFFIXES = {".png", ".svg", ".webp", ".jpg", ".jpeg", ".gif", ".html"}
FORBIDDEN = {
    ".pdf",
    ".ipynb",
    ".doc",
    ".docx",
    ".pptx",
    ".tif",
    ".tiff",
    ".txt",
    ".csv",
    ".py",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    content = Path(sys.argv[1]).resolve()
    manifest_path = Path(sys.argv[2]).resolve()
    errors: list[str] = []
    manifest: dict = {}
    if not manifest_path.exists():
        errors.append(
            "content-manifest.json отсутствует: production export не выполнен"
        )
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("mode") != "production":
            errors.append("manifest не production")
        if manifest.get("version") != 2:
            errors.append("неподдерживаемая версия manifest")

    note_files = list(content.rglob("*.md")) if content.exists() else []
    note_stems = {path.stem.lower() for path in note_files}
    manifest_paths: dict[str, str] = {}
    for item in manifest.get("notes", []) + manifest.get("assets", []):
        relative = item.get("path", "")
        expected = item.get("sha256", "")
        path = content / relative
        manifest_paths[relative] = expected
        if not path.is_file():
            errors.append(f"manifest ссылается на отсутствующий файл: {relative}")
        elif sha256(path) != expected:
            errors.append(f"не совпадает SHA-256: {relative}")

    for path in content.rglob("*") if content.exists() else []:
        if not path.is_file():
            continue
        relative = path.relative_to(content).as_posix()
        if path.suffix.lower() in FORBIDDEN:
            errors.append(f"запрещённый ресурс: {relative}")
        if path.suffix.lower() not in {".md", ".bib"} and relative not in manifest_paths:
            errors.append(f"ресурс отсутствует в manifest: {relative}")
        if path.suffix.lower() != ".md":
            continue

        text = path.read_text(encoding="utf-8")
        # Match drive-qualified paths only in a context where a path can
        # actually begin.  This avoids false positives for LaTeX fragments
        # such as ``x:\sup`` and ``p:\widetilde``.
        if re.search(r"(?:^|(?<=[\s`'\"(]))[A-Za-z]:\\", text, re.MULTILINE):
            errors.append(f"абсолютный Windows-путь: {relative}")
        try:
            _, frontmatter, body = text.split("---", 2)
            meta = yaml.safe_load(frontmatter) or {}
        except Exception:
            errors.append(f"повреждён frontmatter: {relative}")
            continue
        if meta.get("status") != "canonical" or meta.get("publish") is not True:
            errors.append(f"неутверждённая заметка: {relative}")
        if relative not in manifest_paths:
            errors.append(f"заметка отсутствует в manifest: {relative}")

        for raw_target in WIKILINK_RE.findall(body):
            target = raw_target.strip()
            if Path(target).suffix.lower() in ASSET_SUFFIXES:
                continue
            if Path(target).stem.lower() not in note_stems:
                errors.append(
                    f"Quartz не разрешит ссылку [[{target}]] в {relative}"
                )

    if manifest.get("asset_count") != len(manifest.get("assets", [])):
        errors.append("asset_count не совпадает с manifest.assets")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        "production content verified: "
        f"{len(note_files)} notes, {manifest.get('asset_count', 0)} assets"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
