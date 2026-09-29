#### Plots and slides are updated on jlabl2 by the cronjob `update_mauriplots_jlabl2` 




## Local recipe publishing

Edit recipes in `../casetta/food/recipes`, then run `zsh ../cronjobs/diff_homes.zsh` to refresh the
homepage's `recipes/` directory, including photos. The script copies recipes before comparing the two
homepages; exit status 1 can mean those comparisons found differences after the copy succeeded.

Recipe front matter uses `title`, `type` (a list containing `breakfast`, `lunch`, and/or `dinner`), and
`cuisine`. Set `planner: false` for sides or desserts that should appear in the directory without being
selected as a standalone meal. Review and add newly copied files to Git before publishing the homepage.
The copy updates and adds files; it does not remove previously published recipes when originals are deleted.

The shared `../casetta/food/recipes/basic_ingredients.yml` list applies to every recipe. Edit it to choose
which pantry staples the planner omits; the publishing script also copies it into Jekyll's `_data/` directory.
Use ingredient names without quantities, such as `salt`, `olive oil`, `water`, `milk`, or `butter`.
The planner recognizes quantities
and common modifiers such as extra-virgin or fine, while retaining dishes like tuna packed in olive oil.
An individual recipe's `basic_ingredients` header can add exact ingredient lines or components to omit,
such as an optional cheese topping. Keep quantities in the recipe itself; this only filters the shopping list.

The WFD page runs its meal planner in the browser. The suggestion/fix form opens an email draft to the
configured site email address; visitors review and send it through their email app.

## Icons and html symbols

https://feathericons.com (need download to use)<br/>

https://icons8.com

https://www.w3schools.com/charsets/ref_utf_arrows.asp


# Twitter links:

Use https://publish.twitter.com/#
