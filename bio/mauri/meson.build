project('mauri-bio-cv', version: '0.1.0')

python = find_program('python3')
pdflatex = find_program('pdflatex', required: false)
env = find_program('env')

tex_sources = [
  'mauri_cv.tex',
  'mauri_resume.tex',
  'mauri_job_application.tex',
  'mauri_bio.tex',
]

run_target(
  'fetch-papers',
  command: [
    python,
    'scripts/fetch_inspire_papers.py',
    '--orcid', '0000-0001-6982-3310',
    '--output', 'data',
  ],
)

run_target(
  'check',
  command: [
    python,
    '-c',
    'import os; from pathlib import Path; root=Path(os.environ["MESON_SOURCE_ROOT"]); required=["data/profile.yml","tex/preamble.tex","markdown/profile.md"]; missing=[p for p in required if not (root / p).exists()]; raise SystemExit("missing: "+", ".join(missing) if missing else 0)',
  ],
)

if pdflatex.found()
  foreach tex_file : tex_sources
    custom_target(
      tex_file.underscorify() + '_pdf',
      input: ['tex/' + tex_file, 'tex/preamble.tex'],
      output: tex_file.replace('.tex', '.pdf'),
      command: [
        env,
        'TEXINPUTS=' + meson.current_source_dir() / 'tex' + ':',
        pdflatex,
        '-interaction=nonstopmode',
        '-halt-on-error',
        '-output-directory', meson.current_build_dir(),
        '@INPUT0@',
      ],
      build_by_default: true,
    )
  endforeach
else
  warning('pdflatex was not found; PDF targets are skipped. Install a TeX distribution to build PDFs.')
endif
