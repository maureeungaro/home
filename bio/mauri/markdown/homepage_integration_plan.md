# Homepage Integration Plan

Goal: use the `bio/mauri` material to reach collaborators, hiring committees,
students, and technical users without making the homepage feel like a long CV.

## Recommended Homepage Changes

1. Add a compact `Professional Materials` row near the current outreach icons.

   Suggested links:

   - CV: `/home/assets/bio/mauri/mauri_cv.pdf`
   - Resume: `/home/assets/bio/mauri/mauri_resume.pdf`
   - Bio: `/home/assets/bio/mauri/mauri_bio.pdf`
   - Publications: `/home/assets/bio/mauri/markdown/publications.md`

2. Keep the top homepage concise.

   The homepage should still route users quickly to GEMC, Research & Talks,
   Notes, and profile links. CV/resume links should be visible but not
   dominate the page.

3. Add a dedicated future page called `Profile`.

   Source material:

   - `bio/mauri/markdown/profile.md`
   - `bio/mauri/markdown/cv_summary.md`
   - `bio/mauri/markdown/bios.md`

4. Add a publications page after reviewing generated INSPIRE output.

   Source material:

   - `bio/mauri/markdown/publications.md`
   - `bio/mauri/data/inspire_papers.yml`

## Suggested Homepage Section

```markdown
## Professional Materials

| Material | Use |
|:--|:--|
| [Scientific CV](/home/assets/bio/mauri/mauri_cv.pdf) | Full academic and technical record. |
| [Resume](/home/assets/bio/mauri/mauri_resume.pdf) | Shorter profile for applications and collaborations. |
| [Biography](/home/assets/bio/mauri/mauri_bio.pdf) | Short, medium, and long bio text. |
| [Publications](/home/assets/bio/mauri/markdown/publications.md) | Generated INSPIRE publication list. |
```
