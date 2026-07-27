from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import yaml


EXCLUDED = {".git", "node_modules", "public", "content", "_private", "90_admin", "00_inbox", ".obsidian"}
ALLOWED_CONTENT = {".md", ".png", ".svg", ".webp", ".jpg", ".jpeg", ".gif", ".html"}


def ignored(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(part in EXCLUDED for part in rel.parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    parser.add_argument("vault", type=Path)
    parser.add_argument("preview", type=Path)
    args = parser.parse_args()
    repo, vault, preview = map(Path.resolve, (args.repo, args.vault, args.preview))
    if preview.exists():
        shutil.rmtree(preview)
    shutil.copytree(repo, preview, ignore=shutil.ignore_patterns(".git", "node_modules", "public", "content"))
    content = preview / "content"
    content.mkdir()
    for source in vault.rglob("*"):
        if not source.is_file() or ignored(source, vault) or source.suffix.lower() not in ALLOWED_CONTENT:
            continue
        destination = content / source.relative_to(vault)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    bib = vault / "60_sources" / "bibliography.bib"
    if bib.exists():
        shutil.copy2(bib, preview / "bibliography.bib")
    config_path = preview / "quartz.config.yaml"
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    config["configuration"]["baseUrl"] = "localhost:8080"
    for plugin in config["plugins"]:
        source = plugin.get("source")
        if source == "github:quartz-community/explicit-publish":
            plugin["enabled"] = False
        if source == "github:quartz-community/remove-draft":
            plugin["enabled"] = False
    config_path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8")
    print(f"preview={preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

