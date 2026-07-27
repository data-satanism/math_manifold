from __future__ import annotations

import argparse
import html.parser
import posixpath
import sys
import urllib.parse
from pathlib import Path, PurePosixPath


SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class LinkParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        for name, value in attrs:
            if value and name in {"href", "src"}:
                self.links.append(value)


def candidates(public: Path, source: Path, target: str, base_path: str) -> list[Path]:
    parsed = urllib.parse.urlsplit(target)
    path = urllib.parse.unquote(parsed.path)
    if not path:
        return []
    if path.startswith("/"):
        normalized = path
        prefix = f"/{base_path.strip('/')}" if base_path.strip("/") else ""
        if prefix and (normalized == prefix or normalized.startswith(prefix + "/")):
            normalized = normalized[len(prefix) :] or "/"
        relative = PurePosixPath(posixpath.normpath(normalized.lstrip("/")))
    else:
        source_dir = PurePosixPath(source.relative_to(public).as_posix()).parent
        combined = posixpath.normpath(
            posixpath.join(source_dir.as_posix(), path)
        )
        relative = PurePosixPath(combined)

    destination = public.joinpath(*relative.parts)
    result = [destination]
    if destination.suffix == "":
        result.extend(
            [
                destination.with_suffix(".html"),
                destination / "index.html",
            ]
        )
    if path.endswith("/"):
        result.append(destination / "index.html")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("public", type=Path)
    parser.add_argument("--base-path", default="")
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    public = args.public.resolve()
    missing: list[str] = []
    checked = 0

    for source in public.rglob("*.html"):
        document = LinkParser()
        document.feed(source.read_text(encoding="utf-8", errors="replace"))
        for target in document.links:
            parsed = urllib.parse.urlsplit(target)
            if parsed.scheme.lower() in SKIP_SCHEMES or target.startswith("//"):
                continue
            resolved = candidates(public, source, target, args.base_path)
            if not resolved:
                continue
            checked += 1
            if not any(path.is_file() for path in resolved):
                missing.append(
                    f"{source.relative_to(public).as_posix()} -> {target}"
                )

    if missing:
        for item in missing[: args.limit]:
            print(item, file=sys.stderr)
        if len(missing) > args.limit:
            print(
                f"... ещё {len(missing) - args.limit} отсутствующих ссылок",
                file=sys.stderr,
            )
        print(
            f"broken internal resources: {len(missing)} of {checked}",
            file=sys.stderr,
        )
        return 1
    print(f"built links verified: {checked} internal resources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
