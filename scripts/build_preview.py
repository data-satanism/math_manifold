from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


def node_major(executable: Path) -> int:
    result = subprocess.run(
        [str(executable), "-p", "process.versions.node.split('.')[0]"],
        check=True,
        capture_output=True,
        text=True,
    )
    return int(result.stdout.strip())


def find_node(explicit: str | None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    candidates.append(
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "node"
        / "bin"
        / ("node.exe" if os.name == "nt" else "node")
    )
    discovered = shutil.which("node")
    if discovered:
        candidates.append(Path(discovered))

    for candidate in candidates:
        if not candidate.is_file():
            continue
        try:
            if node_major(candidate) >= 22:
                return candidate.resolve()
        except (OSError, subprocess.SubprocessError, ValueError):
            continue
    raise RuntimeError("Quartz 5 requires Node.js 22 or newer")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    parser.add_argument("preview", type=Path)
    parser.add_argument("--node")
    parser.add_argument("--concurrency", type=int, default=1)
    args = parser.parse_args()

    repo = args.repo.resolve()
    preview = args.preview.resolve()
    content = preview / "content"
    output = preview / "public"
    config = preview / "quartz.config.yaml"
    bootstrap = repo / "quartz" / "bootstrap-cli.mjs"
    for required in (content, config, bootstrap):
        if not required.exists():
            raise FileNotFoundError(required)

    node = find_node(args.node)
    environment = os.environ.copy()
    environment["QUARTZ_CONFIG_PATH"] = str(config)
    environment["npm_node_execpath"] = str(node)
    environment["PATH"] = os.pathsep.join(
        [str(node.parent), environment.get("PATH", "")]
    )

    command = [
        str(node),
        str(bootstrap),
        "build",
        f"--directory={content}",
        f"--output={output}",
        f"--concurrency={args.concurrency}",
    ]
    print(f"Quartz runtime: {node}")
    print(f"Quartz config: {config}")
    print(f"Content: {content}")
    return subprocess.run(command, cwd=repo, env=environment).returncode


if __name__ == "__main__":
    raise SystemExit(main())
