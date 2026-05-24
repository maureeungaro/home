# Maurizio Ungaro Bio/CV Package

This directory is a structured replacement for the older resume, CV, biography,
and application files in `tmp/`.

It is organized for three audiences:

- **Scientific CV**: complete academic and technical record.
- **Targeted resume**: shorter document for job applications, collaborations, and leadership roles.
- **Web/profile material**: short biographies and Markdown summaries for the homepage, ORCID, LinkedIn, conference bios, and project pages.

## Contents

- `data/profile.yml`: canonical profile data used by the documents.
- `data/publications_seed.yml`: curated seed list of representative papers from the homepage.
- `scripts/fetch_inspire_papers.py`: retrieves publications from INSPIRE and separates first-author papers.
- `tex/mauri_cv.tex`: scientific CV.
- `tex/mauri_resume.tex`: compact technical/research resume.
- `tex/mauri_job_application.tex`: application-oriented profile document.
- `tex/mauri_bio.tex`: biography sheet with short, medium, and long bios.
- `tex/preamble.tex`: shared LaTeX style.
- `markdown/profile.md`: web-ready profile page draft.
- `markdown/bios.md`: short/medium/long bio text for websites, ORCID, LinkedIn, and conference programs.
- `markdown/cv_summary.md`: concise web summary of CV highlights.
- `meson.build`: Meson build file for validation and optional PDF builds.

## Build

From this directory:

```sh
meson setup build
meson compile -C build
```

If `pdflatex` is installed, Meson builds PDFs for the LaTeX documents. If LaTeX
is not installed, Meson still configures and reports that PDF targets are skipped.

## Refresh and Install Web Assets

To refresh papers, build PDFs, and install linkable files under
`assets/bio/mauri/`:

```sh
python3 scripts/update_material.py
```

Installed files can be linked from the homepage using paths such as:

- `/home/assets/bio/mauri/mauri_cv.pdf`
- `/home/assets/bio/mauri/mauri_resume.pdf`
- `/home/assets/bio/mauri/mauri_bio.pdf`
- `/home/assets/bio/mauri/markdown/publications.md`

## Retrieve Publications

Network access is required to query INSPIRE:

```sh
python3 scripts/fetch_inspire_papers.py --orcid 0000-0001-6982-3310 --output data
```

The script writes:

- `data/inspire_papers.json`
- `data/inspire_papers.yml`
- `data/all_papers.tex`
- `data/first_author_papers.tex`
- `markdown/publications.md`

It classifies first-author papers by checking whether the first listed author is
`Maurizio Ungaro`, `M. Ungaro`, or an equivalent normalized form.

## Web Use

The `markdown/` files are intentionally Jekyll-friendly. They can be copied into
the homepage as pages or included in future sections such as:

- `Biography`
- `For collaborators`
- `For hiring committees`
- `Selected publications`
- `Technical leadership`
