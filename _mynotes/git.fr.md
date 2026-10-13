---
layout: default
title: "Using Git"
permalink: /mynotes/git.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Utiliser Git
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Cloner une seule branche ou un seul tag, sans historique, avec les sous-modules sans leur historique (clone superficiel)

```shell
git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
```

<br/>

## Git LFS (stockage de fichiers volumineux)

Installez Git LFS, puis initialisez-le une fois pour votre compte utilisateur :

```shell
# macOS
brew install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs

git lfs install
```

Activez Git LFS dans un dépôt et choisissez les types de fichiers à y stocker :

```shell
cd path/to/repository
git lfs track "*.zip"       # use a pattern or a specific file path
git add .gitattributes      # commit the tracking rules
git add path/to/archive.zip
git commit -m "Track ZIP files with Git LFS"
git push
```

Exécutez `git lfs ls-files` pour lister les fichiers suivis. Le suivi d'un motif ne concerne que les fichiers
nouvellement ajoutés ; migrer vers LFS des fichiers déjà enregistrés dans des commits Git classiques nécessite
`git lfs migrate`, qui réécrit l'historique du dépôt.

<br/>

## Publier une version immuable et déplacer son tag de version majeure

Utilisez deux tags pour une action GitHub versionnée ou tout autre projet :

* `v1.0.1` est le tag de version immuable. Ne le déplacez ni ne le réutilisez jamais.
* `v1` est un tag de compatibilité mobile. Les utilisateurs qui précisent `uses: owner/repository@v1` reçoivent la
  dernière version `v1.x.x` compatible.

La version publiée sur GitHub doit rester associée à `v1.0.1`. Seul le tag `v1` se déplace ; il n'existe pas de
version publiée distincte qui se déplacerait avec lui.

#### 1) Publier la version sur GitHub

Sur la page GitHub du dépôt :

1. Ouvrez **Releases** et sélectionnez **Draft a new release**.
2. Créez (ou choisissez) le tag `v1.0.1`. 
3. Ajoutez le titre de la version, les notes et les éventuels fichiers joints.


#### 2) Créer ou mettre à jour le tag de version majeure

Définissez la version immuable et la version majeure mobile :

```shell
version=v1.0.1
major=v1
```

Une fois seulement la version `v1.0.1` publiée sur GitHub, faites pointer `v1` vers elle. Lors de la première
publication, cela crée `v1` ; à chaque publication ultérieure (`v1.0.2`, `v1.1.2`, ...), la même commande met à
jour `v1` pour qu'il pointe vers le tag immuable le plus récent. Récupérez le tag que GitHub vient de créer,
faites pointer le tag local `v1` vers le commit référencé par `$version`, puis forcez la mise à jour de ce seul
tag sur GitHub :

```shell
git fetch origin tag "$version"
git tag -f "$major" "$version^{}"
git push --force origin "refs/tags/$major"
```

Le suffixe `^{}` déréférence le tag de version, de sorte que `v1` pointe directement vers le commit de la
version publiée. Le forçage est nécessaire car déplacer un tag est une mise à jour sans avance rapide
(non-fast-forward), et il est sans conséquence la première fois, lorsque `v1` n'existe pas encore. Protégez
les tags immuables tels que `v*.*.*` avec un ensemble de règles de tags GitHub, tout en autorisant le déplacement
des tags de version majeure prévus à cet effet.

<br/>

## Mettre à jour un tag / une version publiée (réécrire un tag existant)

**Utilisez ces variables**

* `tag` : le nom du tag GitHub (p. ex. `v1.2.3`)
* `btag` : nom de la branche temporaire créée à partir du tag
* `rtag` : chemin complet de la référence du tag (`refs/tags/<tag>`), utilisé pour la suppression distante

Exemple : `tag=v1.2.3`

```shell
btag="b$tag"
rtag="refs/tags/$tag"
```

#### 1) Créer une branche temporaire à partir du tag existant et s'y placer

```shell
git fetch origin --tags
git switch -c "$btag" "$tag"
```

#### 2) Effectuer les modifications, les enregistrer dans un commit et pousser la branche temporaire

```shell
git commit -am "Fixes for $tag"
git push -u origin "$btag"
```

#### 3) Supprimer l'ancien tag local pointant vers l'ancien commit, recréer le tag localement sur le nouveau HEAD

(Vous êtes déjà sur `$btag`, donc le `git switch "$btag"` supplémentaire est redondant.)

```shell
git tag -d "$tag"
git tag "$tag"
```

#### 4) Remplacer le tag distant pour qu'il pointe vers le nouveau commit

Supprimez d'abord l'ancien tag distant, puis poussez le nouveau. 
Forcez explicitement la mise à jour du tag distant, car les tags sont immuables par convention et de nombreux
serveurs rejettent les mises à jour de tags sans avance rapide (non-fast-forward) si elles ne sont pas forcées.

```shell
git push origin ":$rtag"
git push --force origin "$rtag"
```

#### 5) Mettre à jour la version publiée sur GitHub (et les fichiers joints) si nécessaire
* Si vous avez téléversé des fichiers joints à la version publiée (binaires / .tar.gz personnalisés / etc.) :
   mettez à jour la version publiée existante en retirant les anciens fichiers et en téléversant les nouveaux
   (ou supprimez et recréez la version publiée). Déplacer le tag ne remplace pas les fichiers téléversés.
* Si seules les archives du code source générées par GitHub sont utilisées (« Source code (tar.gz/zip) ») :
  vous pouvez généralement laisser la version publiée telle quelle ; elle restera associée à $tag, et les archives
  générées suivront le tag mis à jour (cela peut prendre un court instant à cause de la mise en cache).
* Si les notes de version / le journal des modifications doivent changer :
  modifiez les notes de version existantes, ou supprimez et recréez la version publiée pour $tag.

#### 6) Nettoyage : supprimer la branche temporaire (distante + locale)

```shell
git push origin --delete "$btag"
git switch main
git branch -D "$btag"
```


<br/>

## Branches

Créer une nouvelle branche et s'y placer :

```shell
git checkout -b branchname
```

Se placer sur une branche existante :

```shell
git checkout branchname
```

Fusionner les modifications de branch1 dans branch2 (l'une d'elles peut être main). Utilisez `rebase` pour un
historique propre. Vous pouvez aussi utiliser `merge` pour conserver l'historique des deux branches.
```shell
git checkout branch2
git merge/rebase branch1 
```

Pousser une branche vers le dépôt distant :

```shell
git push -u origin branchname
```

Supprimer une branche distante :

```shell
git push origin --delete branchname
```

Lister toutes les branches distantes :

- `git branch -r` : liste toutes les branches distantes
- `git branch -a` : liste toutes les branches (locales et distantes)
- `git branch -vv` : liste toutes les branches avec leur dernier commit
- `git branch --merged` : liste les branches qui ont été fusionnées dans la branche courante
- `git branch --no-merged` : liste les branches qui n'ont pas été fusionnées dans la branche courante


<br/>

## Modifier une pull request ou une merge request existante

Une pull request (PR) GitHub ou une merge request (MR) GitLab issue d'un **fork** suit une **branche source dans
ce fork** et propose de la fusionner dans une **branche cible du dépôt d'origine** (souvent `main`). Un fork est
un dépôt distinct ; il contient lui aussi des branches. Ajoutez des commits à la même branche dans le même
fork, soit dans le navigateur, soit en poussant depuis un clone local, pour mettre à jour automatiquement une
demande ouverte. Il n'est pas nécessaire de créer une autre demande.

### Mettre à jour le code dans le navigateur

Vous n'avez pas besoin de cloner le fork. Vous devez toutefois avoir l'autorisation de modifier sa branche
source : l'auteur peut modifier son propre fork, et les mainteneurs peuvent contribuer lorsque l'auteur active
**Allow edits from maintainers** sur GitHub ou **Allow contributions from members** sur GitLab.

1. Ouvrez la PR ou la MR existante et identifiez son **fork source et sa branche source**.
2. Ouvrez ce fork dans le navigateur et sélectionnez la branche source, par exemple `my-feature`.
3. Ouvrez le fichier et utilisez l'éditeur web. Pour des modifications sur plusieurs fichiers, utilisez l'éditeur
   web de GitHub ou le Web IDE de GitLab.
4. Relisez les modifications et enregistrez-les dans un commit directement sur la **branche source existante**.
   Si un choix vous est proposé, choisissez cette branche plutôt que de créer une nouvelle branche ou demande.

La PR ou la MR existante inclut automatiquement ces commits. Vérifiez le diff mis à jour et les résultats des
vérifications sur la page de la demande.

Vous pouvez aussi appliquer directement sur la PR ou la MR les suggestions issues des commentaires de revue
lorsque vous avez l'autorisation de modifier la branche source. Appliquer une suggestion crée un commit sur
cette branche.
Les relecteurs sans cette autorisation peuvent suggérer des modifications à appliquer par l'auteur ou un
mainteneur autorisé.

### Mettre à jour le code depuis un clone local

#### 1) Identifier le fork et sa branche source

Trouvez le fork source et la branche sur la page de la demande, par exemple `your-user/repository` et `my-feature`.
Vous avez besoin d'un accès en écriture à la branche source de ce fork. Créer un autre fork ou pousser sur une
branche différente ne mettra pas à jour la demande existante.

Dans votre clone local, vérifiez vers quel dépôt pointe chaque dépôt distant configuré :

```shell
git remote -v
```

Les commandes ci-dessous utilisent un dépôt distant nommé `fork` pointant vers le fork source de la demande.
Si ce fork est déjà votre `origin`, remplacez `fork` par `origin` partout. Si aucun dépôt distant ne pointe vers
lui, ajoutez-en un à l'aide de l'URL de clonage SSH ou HTTPS du fork fournie par GitHub ou GitLab :

```shell
git remote add fork <fork-clone-url>
```

#### 2) Se placer sur la branche source dans le fork

Commencez avec un arbre de travail propre : enregistrez dans un commit ou remisez toute modification sans rapport
avant de changer de branche.

```shell
git status
git fetch fork
git switch my-feature
# If the branch does not exist locally, use this instead:
# git switch --track fork/my-feature
git pull --ff-only fork my-feature
```

Si la récupération signale des branches divergentes, réconciliez les commits locaux et distants avant de continuer.

#### 3) Modifier les fichiers, relire les modifications, créer un commit et pousser vers le fork

Effectuez les modifications demandées et exécutez les vérifications pertinentes, puis :

```shell
git diff
git add path/to/file path/to/another-file
git diff --cached
git commit -m "Address review feedback"
git push fork HEAD:my-feature
```

`HEAD:my-feature` pousse votre commit courant vers la branche source existante du fork. La PR ou la MR du dépôt
d'origine inclut désormais les nouveaux commits. Relisez le diff mis à jour et les résultats des vérifications
sur sa page.

#### 4) Mettre à jour le titre ou la description si nécessaire

Ouvrez la demande existante sur GitHub ou GitLab et modifiez son titre ou sa description. Ces modifications ne
nécessitent pas de commit Git. Si la portée a changé, décrivez la modification finale pour que les relecteurs
puissent la comprendre.

#### Si vous avez amendé des commits ou rebasé la branche source

Amender ou rebaser des commits déjà poussés réécrit leur historique. Coordonnez-vous avec toute personne
partageant la branche, puis utilisez `git push --force-with-lease fork HEAD:my-feature` pour mettre à jour la
même demande. Si la vérification du bail rejette la poussée, récupérez et examinez les modifications distantes
avant de réessayer. La protection de branche peut interdire les poussées forcées ; ajouter un nouveau commit
évite de réécrire l'historique.

Une fois une demande fusionnée, soumettez les modifications ultérieures via une nouvelle branche et une nouvelle
PR ou MR.

<br/>

## Récupérer des fichiers précis depuis une autre branche (sans fusion complète)

Lorsque vous ne voulez qu'un ou quelques fichiers d'une autre branche (ou d'un commit/tag), ne fusionnez pas
toute la branche — récupérez uniquement ces chemins dans votre arbre de travail courant.

> ⚠️ Ces commandes **écrasent** la copie locale des chemins listés. Toute modification non enregistrée dans un
> commit sur ces chemins est perdue. Exécutez `git status` d'abord en cas de doute.

#### Prévisualiser d'abord la différence

```shell
git diff main..otherbranch -- path/to/file        # what would change in that file
git show otherbranch:path/to/file                 # print the file as it is on otherbranch
```

#### Copier les fichiers (remplacer la version locale)

```shell
# Modern (recommended). --source can be a branch, tag, or commit SHA.
git restore --source=otherbranch --staged --worktree -- path/to/file [more/files...]

# Classic equivalent (also stages the result):
git checkout otherbranch -- path/to/file [more/files...]
```

`git checkout <branch> -- <path>` met à jour à la fois l'arbre de travail et l'index (le résultat est déjà indexé).
`git restore --source=<ref> -- <path>` ne met à jour par défaut que l'arbre de travail — ajoutez `--staged`
(comme ci-dessus) pour indexer aussi le résultat. Créez ensuite un commit normalement :

```shell
git add path/to/file        # only needed if the file is not already staged
git commit -m "Bring path/to/file from otherbranch"
```

#### Récupérer seulement certaines modifications d'un fichier (interactif, bloc par bloc)

C'est ce qui ressemble le plus à une « fusion » d'un seul fichier : choisissez les blocs de modifications à importer.

```shell
git restore -p --source=otherbranch -- path/to/file   # or: git checkout -p otherbranch -- path/to/file
```

#### Véritable fusion à trois voies d'un seul fichier

`checkout`/`restore` *remplacent* le fichier ; ils ne fusionnent pas son contenu avec le vôtre. Pour une
véritable fusion ligne par ligne d'un fichier entre deux versions, utilisez `git merge-file` :

```shell
git show otherbranch:path/to/file > /tmp/theirs       # their version
git show $(git merge-base HEAD otherbranch):path/to/file > /tmp/base   # common ancestor
git merge-file path/to/file /tmp/base /tmp/theirs     # merges into path/to/file, marks conflicts
```


<br/>

## Conflits

### 1. Résoudre les conflits

- Vérifiez ce qui est en conflit :

```shell
git status
```

* **Conflits textuels (`UU`, etc.)** : ouvrez le fichier et résolvez les conflits marqués par `<<<<<<< ======= >>>>>>>`, puis :

```shell
git add path
```

* **Conserver un seul côté** (choisir notre version ou la leur) :

```shell
git checkout --ours  path   # keep our version (rebase source)
git checkout --theirs path  # keep their version (rebase target)
git add path
```

* **Vous voulez supprimer le fichier (p. ex. conflit `DU` / suppression contre modification)** :

```shell
git rm -- path
# if the file is already gone locally:
git rm --cached -- path
git add -u
```

### 2. Finaliser un rebasage ou une fusion

```shell
git rebase --continue   # repeat until it finishes
git push origin branch2
```

ou
```shell
git commit -m "merge branch1 into branch2"
git push origin branch2
```

<br/>


### Codes de statut des fichiers non fusionnés

* `DD` supprimé des deux côtés
* `AU` ajouté par nous
* `UD` supprimé par eux
* `UA` ajouté par eux
* `DU` supprimé par nous *(souvent : décidez de le conserver ou de le supprimer ; utilisez `git rm` pour le supprimer)*
* `AA` ajouté des deux côtés
* `UU` modifié des deux côtés

<br/>


## Historique

### Afficher les commits et les diffs pour un fichier précis

```shell
git log -p -- path/to/file
```

### Historique compact avec une ligne par commit
```shell
git log --follow --date=short --pretty=format:"%h %ad %an %s" -- path/to/file
```

### Pour supprimer tout l'historique d'un dépôt :

```shell
	git checkout --orphan new-main
	git add -A
	git commit -m 'new files'
	git branch -D main
	git branch -m main
	git push -f origin main
	git branch --set-upstream-to=origin/main main
```

<br/>

## Annuler ou défaire le dernier commit

Il existe deux façons très différentes d'« annuler » le dernier commit. Choisissez selon que le commit a déjà
été poussé ou non.

#### Déjà poussé → `git revert` (sûr, conserve l'historique)

`git revert` ne supprime pas le commit ; il crée un **nouveau** commit qui inverse ses modifications.
L'historique est préservé et aucune poussée forcée n'est nécessaire : c'est donc le bon choix pour une branche
partagée ou déjà poussée.

```shell
git revert HEAD          # opens an editor for the revert message
git revert --no-edit HEAD   # reuse the default message, no editor
git push
```

Pour annuler le commit d'annulation lui-même, annulez-le à son tour (`git revert HEAD`) — ou supprimez-le tant
qu'il est encore local avec les commandes de réinitialisation ci-dessous.

#### Local uniquement → `git reset` (réécrit l'historique)

Si le commit **n'a pas** été poussé, reculez le pointeur de la branche d'un commit. Ce qu'il advient des
modifications dépend de l'option :

```shell
git reset --soft  HEAD~1   # undo the commit, keep changes staged
git reset --mixed HEAD~1   # undo the commit, keep changes in the working tree (default)
git reset --hard  HEAD~1   # undo the commit AND discard the changes
```

> ⚠️ `--hard` supprime définitivement de l'arbre de travail les modifications issues de ce commit. Exécutez
> `git status` (et, en cas de doute, `git stash`) d'abord.

Cas courant : conserver le travail mais refaire le commit — `git reset --soft HEAD~1`, puis indexez à nouveau
les modifications et créez un commit selon les besoins.

Corriger uniquement le message ou ajouter des fichiers oubliés au dernier commit sans réinitialisation :

```shell
git commit --amend            # edit message and/or fold in staged changes
git commit --amend --no-edit  # keep the message, just add the staged changes
```

#### S'il a déjà été poussé

Réinitialiser un commit poussé réécrit l'historique : la poussée se fait donc sans avance rapide et doit être
forcée. Préférez `--force-with-lease`, qui refuse si quelqu'un d'autre a poussé entre-temps :

```shell
git reset --hard HEAD~1
git push --force-with-lease
```

> ⚠️ Ne faites cela que sur une branche que vous contrôlez. Réécrire un historique partagé perturbe les autres
> clones — sur une branche partagée, utilisez plutôt `git revert`.

#### Récupérer un commit supprimé par erreur

`reset` ne supprime pas immédiatement les commits ; l'ancienne pointe de la branche reste dans le reflog
pendant un certain temps :

```shell
git reflog                 # find the SHA of the lost commit
git reset --hard <sha>     # or: git cherry-pick <sha>
```

<br/>

## Jetons (jetons d'accès personnels)

Un **jeton d'accès personnel (PAT)** est un identifiant d'authentification lié à **votre compte personnel**,
et non à un dépôt. Vous le créez toujours sous :

```
Personal Settings > Developer Settings > Personal access tokens
```

Deux faits essentiels faciles à mal comprendre :

* Le jeton **hérite des autorisations du compte qui le crée**. Pour agir sur un dépôt (déclencher ses workflows,
  pousser, récupérer des images privées), ce compte doit disposer des accès correspondants à **ce** dépôt.
* GitHub n'affiche la chaîne du jeton **qu'une seule fois**, à la création. Elle ne peut pas être relue par la
  suite (ni depuis vos paramètres, ni depuis un secret où elle a été collée). Si vous la perdez, régénérez le jeton.

Vous pouvez `regenerate` un jeton existant, c'est-à-dire le régénérer (nouvelle valeur), ou modifier les portées
d'un jeton classique sur place (valeur inchangée) — les deux sur la même page. Définissez toujours une date
d'expiration personnalisée.

### De quelle portée / quelle autorisation ai-je besoin ?

Choisissez la ligne correspondant à ce que le jeton doit **faire**, et non au dépôt où il réside :

| Objectif                                      | Portée classique       | Autorisation fine              |
|-------------------------------------------|------------------------|--------------------------------|
| **Déclencher** le workflow d'un autre dépôt (API) | `repo` / `public_repo` | **Actions → Lecture et écriture** |
| Ajouter / modifier des fichiers `.github/workflows/*` | `workflow`       | **Workflows → Lecture et écriture** |
| Récupérer des images de conteneurs privées | `read:packages`        | **Packages → Lecture**         |

> ⚠️ Erreur fréquente : la portée `workflow` ne sert **qu'à** enregistrer des fichiers de workflow dans des commits.
> Elle ne permet **pas** de *déclencher* une exécution. Pour lancer un `workflow_dispatch` / `repository_dispatch`,
> vous avez besoin de `repo` (`public_repo` pour les dépôts publics) sur un jeton classique, ou de
> **Actions : Lecture et écriture** sur un jeton à autorisations fines.

### Liens directs

* À autorisations fines : <https://github.com/settings/personal-access-tokens/new>
  → Propriétaire `gemc`, dépôt p. ex. `gemc/clas12-systems`, autorisation **Actions : Lecture et écriture**
* Classique : <https://github.com/settings/tokens/new>
  → Portée : ✅ `repo` (couvre `public_repo`) ; ajoutez `read:packages` pour les images privées

Un jeton utilisé par un outil local (et non par un workflow) doit être placé dans un fichier lu par cet outil,
généralement dans le répertoire personnel, par exemple `.bob`.


<br/>

## Secrets

Un **secret GitHub Actions** est une variable chiffrée stockée dans les paramètres d'un dépôt. Les workflows de
ce dépôt le lisent à l'exécution via {% raw %}`${{ secrets.SECRET_NAME }}`{% endraw %} ; la valeur n'est jamais affichée
dans les journaux ni montrée à quiconque parcourt le dépôt.

Gardez les deux éléments séparés — ils résident à des endroits différents :

* **Le jeton** (la chaîne `ghp_…` / `github_pat_…`) est créé dans **votre compte personnel** (ci-dessus).
* **Le secret** est une *copie* de cette chaîne, stockée dans le dépôt **dont le workflow l'utilisera** — c.-à-d.
  le dépôt qui effectue le déclenchement, et **non** le dépôt déclenché.

### Comment le créer et le stocker

1. **Générez le jeton** dans votre **compte personnel** (paramètres de développement), en choisissant la portée
   ou l'autorisation pour le dépôt **cible** sur lequel le workflow doit agir (voir le tableau ci-dessus).
   Le compte doit avoir un accès en écriture à ce dépôt cible.

2. **Copiez la valeur du jeton** affichée à l'écran (visible une seule fois).

3. **Ajoutez le secret au dépôt dont le workflow l'utilise**
   - Allez dans ce dépôt → **Settings → Secrets and variables → Actions**
     (p. ex. <https://github.com/gemc/pygemc/settings/secrets/actions>)
   - Cliquez sur **New repository secret**
   - Nom : p. ex. `GEMC_SRC_PAT` (doit correspondre au nom référencé dans le YAML du workflow)
   - Valeur : collez le jeton
   - Cliquez sur **Add secret**


<br/>

## Déclencher un workflow dans un autre dépôt

Le `GITHUB_TOKEN` intégré **ne peut pas** démarrer de workflows dans un dépôt différent ; les déclenchements
entre dépôts utilisent donc un PAT stocké en tant que secret. Le principe : le workflow du **dépôt A** appelle
l'API GitHub pour déclencher le workflow du **dépôt B**.

Vous avez besoin de trois choses :

1. **Un PAT** appartenant à un compte ayant un **accès en écriture au dépôt B**, autorisé à déclencher Actions
   (jeton classique avec `repo`, ou à autorisations fines avec **Actions : Lecture et écriture** sur B).
   Voir le tableau des jetons ci-dessus.
2. **Le secret** contenant ce PAT, stocké dans le **dépôt A** (la source du déclenchement).
3. **Un déclencheur activable par l'API sur le workflow du dépôt B** — ajoutez `workflow_dispatch:` (avec des
   `inputs:` facultatifs) au bloc `on:` du workflow cible, sinon l'appel API renvoie `404`/`422`.

### L'appel de déclenchement (dans le workflow du dépôt A)

{% raw %}
```yaml
      - name: Trigger workflow_dispatch on repo B
        run: |
          curl --fail-with-body -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${{ secrets.B_PAT }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/<owner>/<repoB>/actions/workflows/test.yml/dispatches \
            -d '{"ref":"main","inputs":{"triggered_by":"repo A"}}'
```
{% endraw %}

Les clés `inputs` doivent correspondre aux `inputs:` déclarés sous `workflow_dispatch:` dans le workflow du dépôt B.

### Sécurité : protéger les déclenchements en chaîne via `workflow_run`

Un workflow avec `on: workflow_run` s'exécute avec des **privilèges élevés** (il peut accéder aux secrets/PAT)
et se déclenche aussi pour les événements de PR issues de forks ; conditionnez donc l'exécution du job.
Sinon, une PR issue d'un fork pourrait atteindre l'étape privilégiée, y compris avec le code que celle-ci
récupère via `workflow_run.head_sha`. C'est aussi pourquoi CodeQL signale la « récupération de code non fiable
dans un contexte privilégié ».

**Le champ à vérifier dépend de la position dans la chaîne** — c'est une source fréquente d'erreurs :

* **1er maillon** — à l'écoute d'un workflow déclenché *directement* par `push`/`pull_request` (p. ex. un
  `Deploy` déclenché par `on: workflow_run` pour `Test`) : `github.event.workflow_run.event` est l'événement
  d'origine ; conditionnez donc l'exécution avec `event == 'push'`.

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.event == 'push'
        }}
  ```
  {% endraw %}

* **2e maillon** — à l'écoute d'un workflow lui-même *déclenché par* `workflow_run` (p. ex. un job qui s'exécute
  après `Deploy`, lui-même déjà déclenché par `on: workflow_run`) : ici `workflow_run.event` vaut **toujours
  `workflow_run`**, jamais `push`. Utiliser `event == 'push'` empêche toute exécution du job ; utiliser
  `event == 'workflow_run'` est toujours vrai (aucune protection). Vérifiez plutôt le dépôt source — les
  champs `head_*` conservent la source d'origine à travers la chaîne :

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.head_repository.full_name == github.repository
        }}
  ```
  {% endraw %}

  `head_repository.full_name == github.repository` est vrai pour les poussées dans le même dépôt et faux pour
  les chaînes issues de PR de forks : c'est précisément la protection recherchée contre la récupération de code
  non fiable.

### Exemples dans ce projet

| Source du déclenchement (dépôt A) | Nom du secret (dans A) | Cible (dépôt B) | Autorisations du jeton (sur B) |
|-------------------------|-----------------------|----------------------|-------------------------|
| `gemc/pygemc`           | `GEMC_SRC_PAT`        | `gemc/src`           | déclencher Actions sur src |
| `gemc/src`              | `CLAS12_SYSTEMS_PAT`  | `gemc/clas12-systems`| déclencher Actions sur clas12-systems |
