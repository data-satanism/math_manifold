from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
from pathlib import Path

import yaml


EXCLUDED = {".git", "node_modules", "public", "content", "_private", "90_admin", "00_inbox", ".obsidian"}
ALLOWED_CONTENT = {".md", ".png", ".svg", ".webp", ".jpg", ".jpeg", ".gif", ".html"}
HTML_RESOURCE_RE = re.compile(
    r"(?P<prefix>\b(?:src|href)=[\"'])"
    r"(?P<target>(?![a-z]+:|//|/|#)[^\"']+)"
    r"(?P<suffix>[\"'])",
    re.I,
)


def ignored(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(part in EXCLUDED for part in rel.parts)


def rebase_html_asset(text: str) -> str:
    """Account for Quartz emitting file.html as file/index.html."""

    def replace(match: re.Match[str]) -> str:
        return (
            f"{match.group('prefix')}../{match.group('target')}"
            f"{match.group('suffix')}"
        )

    return HTML_RESOURCE_RE.sub(replace, text)


def link_dependencies(repo: Path, preview: Path) -> Path:
    """Link preview directly to the physical dependency directory.

    On Windows the repository's ``node_modules`` can itself be a junction.
    Chaining another junction through it makes esbuild workers hang before
    Markdown parsing. Resolving the source first keeps the preview link flat.
    """

    source = repo / "node_modules"
    if not source.exists():
        raise FileNotFoundError(
            f"node_modules is missing in {repo}; install Quartz dependencies first"
        )
    resolved_source = source.resolve(strict=True)
    destination = preview / "node_modules"
    if os.name == "nt":
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(destination), str(resolved_source)],
            check=True,
            capture_output=True,
            text=True,
        )
    else:
        destination.symlink_to(resolved_source, target_is_directory=True)
    return resolved_source


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
    dependencies = link_dependencies(repo, preview)
    content = preview / "content"
    content.mkdir()
    for source in vault.rglob("*"):
        if not source.is_file() or ignored(source, vault) or source.suffix.lower() not in ALLOWED_CONTENT:
            continue
        destination = content / source.relative_to(vault)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix.lower() == ".html":
            destination.write_text(
                rebase_html_asset(source.read_text(encoding="utf-8")),
                encoding="utf-8",
                newline="\n",
            )
        else:
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
    print(f"node_modules={dependencies}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
