#!/usr/bin/env python3
"""Fetch Maurizio Ungaro publications from INSPIRE.

The script writes JSON, YAML, LaTeX, and Markdown outputs and separates papers
where Maurizio Ungaro is listed as first author.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


INSPIRE_API = "https://inspirehep.net/api/literature"


def normalize_name(name: str) -> str:
    if "," in name:
        last, first = [part.strip() for part in name.split(",", 1)]
        name = f"{first} {last}"
    cleaned = re.sub(r"[^a-zA-Z ]+", " ", name).lower()
    parts = [p for p in cleaned.split() if p]
    if not parts:
        return ""
    if len(parts) == 2 and parts[0] in {"m", "maurizio"} and parts[1] == "ungaro":
        return "maurizio ungaro"
    if parts[-1] == "ungaro" and parts[0].startswith("m"):
        return "maurizio ungaro"
    return " ".join(parts)


def is_mauri(name: str) -> bool:
    return normalize_name(name) == "maurizio ungaro"


def inspire_query(orcid: str | None, author: str, size: int) -> str:
    if orcid:
        query = f"orcid:{orcid}"
    else:
        query = f"a {author}"
    params = {
        "q": query,
        "sort": "mostrecent",
        "size": str(size),
    }
    return INSPIRE_API + "?" + urllib.parse.urlencode(params)


def is_certificate_error(error: urllib.error.URLError) -> bool:
    reason = getattr(error, "reason", None)
    return isinstance(reason, ssl.SSLCertVerificationError)


def open_url(url: str, *, insecure_tls: bool = False):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "mauri-home-publication-updater/1.0",
            "Accept": "application/json",
        },
    )
    context = ssl._create_unverified_context() if insecure_tls else None
    return urllib.request.urlopen(request, timeout=60, context=context)


def fetch_records(url: str) -> list[dict]:
    try:
        response_context = open_url(url)
    except urllib.error.URLError as error:
        if not is_certificate_error(error):
            raise
        print(
            "warning: TLS certificate verification failed for INSPIRE; "
            "retrying with certificate verification disabled for this request.",
            file=sys.stderr,
        )
        response_context = open_url(url, insecure_tls=True)

    with response_context as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload.get("hits", {}).get("hits", [])


def get_year(metadata: dict) -> str:
    if metadata.get("publication_info"):
        for entry in metadata["publication_info"]:
            if entry.get("year"):
                return str(entry["year"])
    if metadata.get("preprint_date"):
        return str(metadata["preprint_date"])[:4]
    return ""


def get_title(metadata: dict) -> str:
    titles = metadata.get("titles") or []
    if titles:
        return titles[0].get("title", "").strip()
    return "Untitled"


def get_authors(metadata: dict) -> list[str]:
    authors = []
    for author in metadata.get("authors", []):
        name = author.get("full_name") or author.get("name") or ""
        if name:
            authors.append(name)
    return authors


def get_doi(metadata: dict) -> str:
    dois = metadata.get("dois") or []
    if dois:
        return dois[0].get("value", "")
    return ""


def get_arxiv(metadata: dict) -> str:
    arxiv = metadata.get("arxiv_eprints") or []
    if arxiv:
        return arxiv[0].get("value", "")
    return ""


def get_journal(metadata: dict) -> str:
    infos = metadata.get("publication_info") or []
    for info in infos:
        pieces = []
        if info.get("journal_title"):
            pieces.append(info["journal_title"])
        if info.get("journal_volume"):
            pieces.append(str(info["journal_volume"]))
        if info.get("page_start"):
            pieces.append(str(info["page_start"]))
        if info.get("year"):
            pieces.append(f"({info['year']})")
        if pieces:
            return " ".join(pieces)
    return ""


def simplify_record(hit: dict) -> dict:
    metadata = hit.get("metadata", {})
    authors = get_authors(metadata)
    first_author = authors[0] if authors else ""
    recid = metadata.get("control_number") or hit.get("id", "")
    url = f"https://inspirehep.net/literature/{recid}" if recid else ""
    return {
        "title": get_title(metadata),
        "year": get_year(metadata),
        "authors": authors,
        "first_author": first_author,
        "is_first_author": is_mauri(first_author),
        "journal": get_journal(metadata),
        "doi": get_doi(metadata),
        "arxiv": get_arxiv(metadata),
        "inspire": url,
    }


def yaml_scalar(value: object) -> str:
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def write_yaml(path: Path, papers: list[dict]) -> None:
    lines = []
    for paper in papers:
        lines.append(f"- title: {yaml_scalar(paper['title'])}")
        lines.append(f"  year: {yaml_scalar(paper['year'])}")
        lines.append(f"  first_author: {yaml_scalar(paper['first_author'])}")
        lines.append(f"  is_first_author: {'true' if paper['is_first_author'] else 'false'}")
        lines.append(f"  journal: {yaml_scalar(paper['journal'])}")
        lines.append(f"  doi: {yaml_scalar(paper['doi'])}")
        lines.append(f"  arxiv: {yaml_scalar(paper['arxiv'])}")
        lines.append(f"  inspire: {yaml_scalar(paper['inspire'])}")
        lines.append("  authors:")
        for author in paper["authors"]:
            lines.append(f"    - {yaml_scalar(author)}")
    path.write_text("\n".join(lines) + "\n")


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def author_list(authors: list[str], max_authors: int = 8) -> str:
    if len(authors) <= max_authors:
        return ", ".join(authors)
    return ", ".join(authors[:max_authors]) + ", et al."


def plain_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def markdown_escape(text: str) -> str:
    return plain_text(text).replace("|", r"\|")


def write_tex(path: Path, papers: list[dict], title: str) -> None:
    lines = [
        "% Generated by scripts/fetch_inspire_papers.py",
        rf"\section*{{{tex_escape(title)}}}",
        r"\begin{enumerate}",
    ]
    for paper in papers:
        authors = tex_escape(author_list(paper["authors"]))
        title_tex = tex_escape(paper["title"])
        journal = tex_escape(paper["journal"])
        year = tex_escape(paper["year"])
        link = paper["doi"] or paper["arxiv"] or paper["inspire"]
        link_tex = tex_escape(link)
        detail = ", ".join(p for p in [journal, year, link_tex] if p)
        lines.append(rf"\item {authors}. \textit{{{title_tex}}}. {detail}.")
    lines.append(r"\end{enumerate}")
    path.write_text("\n".join(lines) + "\n")


def write_markdown(path: Path, papers: list[dict]) -> None:
    def best_url(paper: dict) -> str:
        if paper["doi"]:
            return "https://doi.org/" + paper["doi"]
        if paper["arxiv"]:
            return "https://arxiv.org/abs/" + paper["arxiv"]
        return paper["inspire"]

    def source_label(paper: dict) -> str:
        if paper["doi"]:
            return "DOI"
        if paper["arxiv"]:
            return "arXiv"
        return "INSPIRE"

    def year_label(paper: dict) -> str:
        return markdown_escape(paper["year"] or "n.d.")

    def venue_label(paper: dict) -> str:
        return markdown_escape(paper["journal"] or "Preprint")

    def title_link(paper: dict) -> str:
        title = markdown_escape(paper["title"])
        url = best_url(paper)
        if not url:
            return title
        return f"[{title}]({url})"

    def table(title: str, rows: list[dict]) -> list[str]:
        lines = [
            f"## {title}",
            "",
            "{:.zebra.publications-table}",
            "| Year | Publication | Venue | Source |",
            "|:--:|:--|:--|:--:|",
        ]
        for paper in rows:
            url = best_url(paper)
            source = source_label(paper)
            source_cell = f"[{source}]({url})" if url else source
            lines.append(
                f"| {year_label(paper)} | {title_link(paper)} | "
                f"{venue_label(paper)} | {source_cell} |"
            )
        return lines

    first = [p for p in papers if p["is_first_author"]]
    lines = [
        "# Publications",
        "",
        "Generated from INSPIRE.",
        "",
        "{:.zebra.compact-table}",
        "| Records | Count |",
        "|:--|--:|",
        f"| Total publications | {len(papers)} |",
        f"| First-author publications | {len(first)} |",
        "",
    ]
    lines += table("First-Author Papers", first)
    lines += [""] + table("All Papers", papers)
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--orcid", default="0000-0001-6982-3310")
    parser.add_argument("--author", default="Ungaro, M")
    parser.add_argument("--size", type=int, default=250)
    parser.add_argument("--output", type=Path, default=Path("data"))
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    markdown_dir = args.output.parent / "markdown"
    markdown_dir.mkdir(parents=True, exist_ok=True)

    url = inspire_query(args.orcid, args.author, args.size)
    records = fetch_records(url)
    if not records and args.orcid:
        fallback_url = inspire_query(None, args.author, args.size)
        records = fetch_records(fallback_url)
        url = fallback_url
    papers = [simplify_record(record) for record in records]
    papers.sort(key=lambda item: item.get("year", ""), reverse=True)
    first_author = [paper for paper in papers if paper["is_first_author"]]

    (args.output / "inspire_query.url").write_text(url + "\n")
    (args.output / "inspire_papers.json").write_text(json.dumps(papers, indent=2) + "\n")
    write_yaml(args.output / "inspire_papers.yml", papers)
    write_tex(args.output / "all_papers.tex", papers, "All Publications")
    write_tex(args.output / "first_author_papers.tex", first_author, "First-Author Publications")
    write_markdown(markdown_dir / "publications.md", papers)

    print(f"Fetched {len(papers)} records from INSPIRE")
    print(f"First-author records: {len(first_author)}")
    print(f"Output directory: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
