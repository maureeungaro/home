# Homepage Integration

The homepage now contains the biography, project overview, and professional document links.
The separate Profile and Projects pages have been retired.

## Source Material

- `markdown/bios.md`: short, medium, and long biographies, plus ORCID and LinkedIn text.
- `markdown/profile.md`: reusable professional profile text; it is not a separate navigation page.
- `markdown/cv_summary.md`: concise research and technical highlights.
- `data/profile.yml`: structured profile, project, and skills data.
- `tex/`: source documents for the CV, resume, biography sheet, and application material.

## Homepage Sections

- Keep About Me concise so visitors can quickly identify the research and software focus.
- Use What I Work On for research, detector, simulation, computing, and support projects.
- Keep the full biography and all professional document links in Biography and Documents.
- Retain the professional profile icons, experience, education, research talks, and technical notes.
- Keep recent development summaries consistent with the biography sources without duplicating a full CV.

## Updating Documents

Edit the sources under `bio/mauri`, preserve the explicit LaTeX page breaks, then run:

```sh
python3 scripts/update_material.py --skip-fetch
```

This builds the PDFs and refreshes the linkable assets under `assets/bio/mauri/` using existing
publication data. The separate Publications page continues to use the generated INSPIRE list.
