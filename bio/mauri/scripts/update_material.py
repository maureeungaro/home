#!/usr/bin/env python3
"""Refresh Maurizio Ungaro bio/CV materials and install web assets.

This script is intended to be run from anywhere inside the repository.
It can:

1. refresh publication data from INSPIRE;
2. configure/build the Meson project;
3. install PDFs, Markdown, and machine-readable publication data under
   assets/bio/mauri so they can be linked from the homepage.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve()
SOURCE_DIR = SCRIPT.parents[1]
REPO_ROOT = SCRIPT.parents[3]
DEFAULT_BUILD_DIR = SOURCE_DIR / "build"
DEFAULT_INSTALL_DIR = REPO_ROOT / "assets" / "bio" / "mauri"


PDFS = [
    "mauri_cv.pdf",
    "mauri_resume.pdf",
    "mauri_job_application.pdf",
    "mauri_bio.pdf",
]

MARKDOWN_FILES = [
    "bios.md",
    "profile.md",
    "cv_summary.md",
    "job_application_notes.md",
    "publications.md",
]

DATA_FILES = [
    "profile.yml",
    "publications_seed.yml",
    "inspire_papers.yml",
    "inspire_query.url",
]


def run(command: list[str], cwd: Path) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def ensure_meson_build(build_dir: Path) -> None:
    if not (build_dir / "build.ninja").exists():
        run(["meson", "setup", str(build_dir), str(SOURCE_DIR)], cwd=REPO_ROOT)


def fetch_papers(size: int) -> None:
    run(
        [
            sys.executable,
            str(SOURCE_DIR / "scripts" / "fetch_inspire_papers.py"),
            "--orcid",
            "0000-0001-6982-3310",
            "--output",
            str(SOURCE_DIR / "data"),
            "--size",
            str(size),
        ],
        cwd=REPO_ROOT,
    )


def build_documents(build_dir: Path) -> None:
    ensure_meson_build(build_dir)
    run(["meson", "compile", "-C", str(build_dir)], cwd=REPO_ROOT)


def copy_if_exists(source: Path, destination: Path) -> None:
    if not source.exists():
        print(f"skip missing {source}")
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    print(f"installed {destination}")


def install_outputs(build_dir: Path, install_dir: Path) -> None:
    install_dir.mkdir(parents=True, exist_ok=True)

    for pdf in PDFS:
        copy_if_exists(build_dir / pdf, install_dir / pdf)

    for name in MARKDOWN_FILES:
        copy_if_exists(SOURCE_DIR / "markdown" / name, install_dir / "markdown" / name)

    for name in DATA_FILES:
        copy_if_exists(SOURCE_DIR / "data" / name, install_dir / "data" / name)

    for name in ["all_papers.tex", "first_author_papers.tex"]:
        copy_if_exists(SOURCE_DIR / "data" / name, install_dir / "tex" / name)

    publications_source = SOURCE_DIR / "markdown" / "publications.md"
    publications_page = REPO_ROOT / "p_publications.markdown"
    if publications_source.exists():
        publications_page.write_text(
            "\n".join(
                [
                    "---",
                    "layout: default",
                    "title: Publications",
                    "description: INSPIRE publication list for Maurizio Ungaro with first-author papers and source links.",
                    "permalink: /publications/",
                    "nav_exclude: true",
                    "---",
                    "",
                    "{% raw %}",
                    publications_source.read_text().strip(),
                    "{% endraw %}",
                    "",
                ]
            )
        )
        print(f"installed {publications_page}")

    index = install_dir / "README.md"
    index.write_text(
        "\n".join(
            [
                "# Maurizio Ungaro Bio/CV Assets",
                "",
                "Generated from `bio/mauri`.",
                "",
                "## PDFs",
                "",
                "- [Scientific CV](mauri_cv.pdf)",
                "- [Resume](mauri_resume.pdf)",
                "- [Application Profile](mauri_job_application.pdf)",
                "- [Biography Sheet](mauri_bio.pdf)",
                "",
                "## Markdown",
                "",
                "- [Bios](markdown/bios.md)",
                "- [Profile](markdown/profile.md)",
                "- [CV Summary](markdown/cv_summary.md)",
                "- [Job Application Notes](markdown/job_application_notes.md)",
                "- [Publications](markdown/publications.md)",
                "",
            ]
        )
    )
    print(f"installed {index}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, default=DEFAULT_BUILD_DIR)
    parser.add_argument("--install-dir", type=Path, default=DEFAULT_INSTALL_DIR)
    parser.add_argument("--size", type=int, default=300)
    parser.add_argument("--skip-fetch", action="store_true")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument("--skip-install", action="store_true")
    args = parser.parse_args()

    if not args.skip_fetch:
        fetch_papers(args.size)
    if not args.skip_build:
        build_documents(args.build_dir)
    if not args.skip_install:
        install_outputs(args.build_dir, args.install_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
