---
layout: default
title: "GitHub Actions Marketplace"
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Publish an action to GitHub Marketplace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

This note uses [ThreadScale](https://github.com/gemc/ThreadScale) as the example:
its root action is published as [ThreadScale on Marketplace](https://github.com/marketplace/actions/threadscale)
and workflows call it with `uses: gemc/ThreadScale@v1`.

## Prepare the repository

Use a public repository dedicated to the action, with one `action.yml` or `action.yaml` at its root.
Choose a unique action name that does not conflict with Marketplace names or GitHub's reserved names.

ThreadScale's metadata includes the following fields; its full `action.yml` also declares inputs and outputs:

```yaml
name: ThreadScale
description: Measure strong scaling, speedup, throughput, and parallel efficiency across application threads.
author: GEMC Collaboration

branding:
  color: blue
  icon: activity

runs:
  using: node24
  main: src/main.js
```

For your own action, replace the name, description, branding, and entry point. Include the code referenced by
`runs.main`, a README explaining usage and inputs, and a license. ThreadScale uses the MIT license and runs
directly from JavaScript without runtime dependencies or a build step. Its local checks are:

```shell
npm run check
npm test
```

ThreadScale also provides a reusable workflow under `.github/workflows/`; its Marketplace listing comes from
the root `action.yml`.

<br/>

## Publish through GitHub

1. Open the repository's root `action.yml` on GitHub and use its release banner to draft a release.
2. Enable the Marketplace publication checkbox in the release form.
3. If it is disabled, the repository owner or an organization owner must accept the Marketplace Developer
   Agreement through the release page. Publishing also requires two-factor authentication.
4. Resolve any metadata validation errors, then select a primary category and optionally a second category.
5. Select the fixed version tag for the code you are publishing, then add a release title and notes:
   - If you are listing the existing `v1.0.0`, select that tag. If its GitHub Release already exists, edit
     that release and enable Marketplace publication there.
   - If you are releasing updated code, create or select `v1.0.1` at the tested commit. When creating the
     tag, check that the release target is the commit you tested.
   - Use the fixed version tag for the release; keep `v1` as the moving tag used by consumers.
6. Publish the release and check the resulting Marketplace listing. Eligible actions appear immediately
   without a separate review.

See [GitHub's publishing instructions][publishing] for the current requirements and interface.

<br/>

## Maintain the version tags

Suppose `v1` currently points to the same commit as `v1.0.0`. Publishing that existing version to Marketplace
requires no tag changes. You do not need to create `v1.0.1` just to add a Marketplace listing.

When updated code is ready, publish a new GitHub Release attached to `v1.0.1`, with Marketplace publication
enabled. Then move `v1` to the same commit as `v1.0.1`. This does **not** happen automatically when you create
the new release; update the tag yourself or configure release automation to do it.

After publishing `v1.0.1`, run these commands from your action repository:

```shell
git fetch origin tag v1.0.1
git tag -f v1 'v1.0.1^{}'
git push --force origin refs/tags/v1
```

The `^{}` suffix resolves the version tag to its commit. Only `v1` moves; `v1.0.0`, `v1.0.1`, and their
GitHub Releases retain their original targets. Consumers using `@v1` receive the updated code on subsequent
runs, while consumers using `@v1.0.0` keep that version. See the [Git note on release tags][tags] for details.

ThreadScale's reusable workflow also references `gemc/ThreadScale@v1` internally, so that tag must exist
before consumers run it. Users can choose `@v1` for compatible updates or pin a full commit SHA.

For subsequent versions, publish a new versioned release with Marketplace publication enabled, then update
the major tag for compatible changes. Leave earlier version tags in place.

<br/>

## Help people discover and try the action

- Lead the README with the problem solved, a small working workflow, and a screenshot of the result.
  ThreadScale's scaling chart is a useful example of what to show.
- Add a clear repository description, relevant topics such as `github-action`, `benchmark`, and
  `performance`, and a Marketplace link. Link the action from your homepage and related project documentation.
- Publish a short tutorial using a real application, including its workflow and resulting report.
  Share it with relevant scientific computing communities, collaborators, and on LinkedIn.
- Suggest inclusion in maintained GitHub Actions or scientific software directories when it fits their scope.
  Follow each directory's contribution instructions.
- Invite early users to report their use cases and add a small list of adopting projects, with permission.
  Announce substantial releases with a concrete example of the improvement.

## Add useful README badges

ThreadScale already has Marketplace, test-status, and license badges. A stars badge adds a public measure of
interest. Copy this Markdown into an action's README, replacing the repository and workflow names as needed:

```markdown
[![Marketplace][market-badge]][market]
[![Stars][stars-badge]][repo]
[![Tests][tests-badge]][tests]

[market-badge]: https://img.shields.io/badge/Marketplace-ThreadScale-2088FF
[stars-badge]: https://img.shields.io/github/stars/gemc/ThreadScale?style=flat
[tests-badge]: https://img.shields.io/github/actions/workflow/status/gemc/ThreadScale/test.yml
[market]: https://github.com/marketplace/actions/threadscale
[repo]: https://github.com/gemc/ThreadScale
[tests]: https://github.com/gemc/ThreadScale/actions/workflows/test.yml
```

The [stars badge][stars-docs] counts stars; the [workflow badge][tests-docs] reports the action repository's
test status. Neither measures how often other projects run the action. The Marketplace badge is a static link.
Release-asset downloads and repository clones should not be presented as action execution counts either.

## Show evidence of adoption

For a useful usage badge, maintain a count of **known public repositories using the action** and link it to
the evidence. Start with a manually reviewed list; automate updates only if maintaining it becomes tedious.
Use [GitHub code search][search-docs] to find candidate callers:

```text
"gemc/ThreadScale@" path:.github/workflows/ NOT repo:gemc/ThreadScale
"gemc/ThreadScale/.github/workflows/thread-scaling.yml@" path:.github/workflows/ NOT repo:gemc/ThreadScale
```

Review the matches for active `uses:` references, deduplicate repositories across both searches, and exclude
forks and copied examples that do not represent independent adoption. Record the date and counting method.
This is a partial count: private repositories and unindexed or indirect callers will be missing, and a
workflow reference does not prove that it has run.

To display the reviewed count, publish a small JSON file on your website and use a
[Shields endpoint badge][endpoint-docs]. For example, the following JSON uses **N as a placeholder**;
replace it with your verified count before publishing:

```json
{
  "schemaVersion": 1,
  "label": "known public users",
  "message": "N repositories",
  "color": "blue"
}
```

Then use this README template, replacing both example URLs with your JSON endpoint and evidence page:

```markdown
[![Known public users][usage-badge]][usage-evidence]

[usage-badge]: https://img.shields.io/endpoint?url=https%3A%2F%2Fexample.org%2Fusage.json
[usage-evidence]: https://example.org/adopters
```

For promotion feedback, repository maintainers can also use **Insights → Traffic** to inspect visitors,
clones, and referring sites. GitHub's [traffic view][traffic-docs] covers the past 14 days for visitors and
full clones; these measure repository traffic, not action runs.

[tags]: /home/mynotes/git#publish-an-immutable-release-and-move-its-major-version-tag
[publishing]:
  https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace
[stars-docs]: https://shields.io/badges/git-hub-repo-stars
[tests-docs]: https://shields.io/badges/git-hub-actions-workflow-status
[endpoint-docs]: https://shields.io/badges/endpoint-badge
[search-docs]:
  https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[traffic-docs]:
  https://docs.github.com/articles/viewing-traffic-to-a-repository
