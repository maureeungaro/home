# Recipe collection

## Recipe files

Use one Markdown file per unique recipe and name it with a lowercase, hyphen-separated slug, such as
`spam-and-eggs.md`. Do not create duplicate files when a dish appears more than once. Create separate recipes
when the cooking method or sauce is materially different, such as ravioli with ragù, tomato, butter and sage,
or walnut sauce.

Write recipes for four servings unless requested otherwise. Place the content in this order:

- `# Recipe Name`
- A two-by-two HTML image table
- `## Background`, with a concise history, origin, or cultural note
- `## Ingredients`, with specific quantities
- `## How to cook`, with numbered, practical instructions

## Recipe images

Every recipe must have four photographs stored in `images/`. Normalize downloaded images to JPEG, limit the
longest dimension to 1,200 pixels, and name them `<recipe-slug>_img1.jpg` through
`<recipe-slug>_img4.jpg`. Reference the local paths from the image table, but keep each image wrapped in a link
to its original publisher page.

Search for clear photographs of the finished dish, reject loosely related results, use four distinct images,
and prefer four different source domains. Copyrighted images are permitted only because this is a private
repository for personal use; preserve the source links and do not present the images as original work.

## Validation

After adding or changing recipes:

- Verify that every recipe has four image references.
- Verify that every referenced image exists and decodes as JPEG data.
- Verify that no remote URL remains in an `<img src>` attribute.
- Keep prose within 112 columns; long publisher URLs are the only permitted exception.
- Add every new recipe and image to Git.
- Run `git diff --check`, then show and summarize the diff.
- Do not commit or push.
