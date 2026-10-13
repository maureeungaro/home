---
layout: default
title: "GitHub Actions Marketplace"
permalink: /mynotes/github_marketplace.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Publier une action sur GitHub Marketplace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Cette note utilise [ThreadScale](https://github.com/gemc/ThreadScale) comme exemple :
son action à la racine du dépôt est publiée sous le nom [ThreadScale sur Marketplace](https://github.com/marketplace/actions/threadscale)
et les workflows l'appellent avec `uses: gemc/ThreadScale@v1`.

## Préparer le dépôt

Utilisez un dépôt public dédié à l'action, avec un seul fichier `action.yml` ou `action.yaml` à sa racine.
Choisissez un nom d'action unique qui n'entre pas en conflit avec les noms sur Marketplace ni avec les noms
réservés de GitHub.

Les métadonnées de ThreadScale incluent les champs suivants ; son fichier `action.yml` complet déclare aussi des
entrées et des sorties :

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

Pour votre propre action, remplacez le nom, la description, l'identité visuelle et le point d'entrée. Incluez le
code référencé par `runs.main`, un README expliquant l'utilisation et les entrées, ainsi qu'une licence.
ThreadScale utilise la licence MIT et s'exécute directement en JavaScript, sans dépendances à l'exécution ni
étape de compilation. Ses vérifications locales sont :

```shell
npm run check
npm test
```

ThreadScale fournit également un workflow réutilisable sous `.github/workflows/` ; sa fiche sur Marketplace
provient du fichier `action.yml` à la racine du dépôt.

<br/>

## Publier via GitHub

1. Ouvrez le fichier `action.yml` à la racine du dépôt sur GitHub et utilisez sa bannière de création de release
   pour préparer une release.
2. Cochez la case de publication sur Marketplace dans le formulaire de release.
3. Si elle est désactivée, le propriétaire du dépôt ou un propriétaire de l'organisation doit accepter l'accord
   destiné aux développeurs de Marketplace via la page de release. La publication nécessite également
   l'authentification à deux facteurs.
4. Corrigez toute erreur de validation des métadonnées, puis sélectionnez une catégorie principale et,
   éventuellement, une seconde catégorie.
5. Sélectionnez le tag de version fixe correspondant au code que vous publiez, puis ajoutez un titre et des
   notes de release :
   - Si vous publiez sur Marketplace la version existante `v1.0.0`, sélectionnez ce tag. Si sa release GitHub
     existe déjà, modifiez cette release et activez-y la publication sur Marketplace.
   - Si vous publiez du code mis à jour, créez ou sélectionnez `v1.0.1` au commit testé. Lors de la création du
     tag, vérifiez que la cible de la release est bien le commit que vous avez testé.
   - Utilisez le tag de version fixe pour la release ; conservez `v1` comme tag flottant utilisé par les
     utilisateurs de l'action.
6. Publiez la release et vérifiez la fiche obtenue sur Marketplace. Les actions éligibles apparaissent
   immédiatement, sans examen distinct.

Consultez les [instructions de publication de GitHub][publishing] pour connaître les exigences et l'interface
actuelles.

<br/>

## Maintenir les tags de version

Supposons que `v1` pointe actuellement vers le même commit que `v1.0.0`. La publication de cette version
existante sur Marketplace ne nécessite aucune modification de tag. Vous n'avez pas besoin de créer `v1.0.1`
simplement pour ajouter une fiche sur Marketplace.

Lorsque le code mis à jour est prêt, publiez une nouvelle release GitHub rattachée à `v1.0.1`, avec la
publication sur Marketplace activée. Déplacez ensuite `v1` vers le même commit que `v1.0.1`. Cela ne se fait
**pas** automatiquement lorsque vous créez la nouvelle release ; mettez le tag à jour vous-même ou configurez
l'automatisation des releases pour le faire.

Après avoir publié `v1.0.1`, exécutez ces commandes depuis le dépôt de votre action :

```shell
git fetch origin tag v1.0.1
git tag -f v1 'v1.0.1^{}'
git push --force origin refs/tags/v1
```

Le suffixe `^{}` permet de résoudre le tag de version en son commit. Seul `v1` se déplace ; `v1.0.0`, `v1.0.1`
et leurs releases GitHub conservent leurs cibles d'origine. Les utilisateurs de `@v1` reçoivent le code mis à
jour lors des exécutions suivantes, tandis que ceux de `@v1.0.0` conservent cette version. Consultez la
[note Git sur les tags de release][tags] pour plus de détails.

Le workflow réutilisable de ThreadScale référence également `gemc/ThreadScale@v1` en interne ; ce tag doit donc
exister avant que les utilisateurs n'exécutent ce workflow. Les utilisateurs peuvent choisir `@v1` pour
bénéficier des mises à jour compatibles ou épingler un SHA de commit complet.

Pour les versions suivantes, publiez une nouvelle release versionnée avec la publication sur Marketplace
activée, puis mettez à jour le tag de version majeure pour les changements compatibles. Laissez en place les
tags des versions antérieures.

<br/>

## Aider les utilisateurs à découvrir et à essayer l'action

- Commencez le README par le problème résolu, un petit workflow fonctionnel et une capture d'écran du résultat.
  Le graphique de passage à l'échelle de ThreadScale est un bon exemple de ce qu'il faut montrer.
- Ajoutez une description claire du dépôt, des thèmes pertinents tels que `github-action`, `benchmark` et
  `performance`, ainsi qu'un lien vers Marketplace. Ajoutez un lien vers l'action depuis votre page d'accueil
  et la documentation des projets associés.
- Publiez un court tutoriel utilisant une application réelle, avec son workflow et le rapport obtenu.
  Partagez-le avec les communautés de calcul scientifique concernées, vos collaborateurs et sur LinkedIn.
- Proposez l'ajout de l'action à des annuaires régulièrement mis à jour consacrés aux actions GitHub ou aux
  logiciels scientifiques lorsqu'elle correspond à leur périmètre. Suivez les instructions de contribution
  de chaque annuaire.
- Invitez les premiers utilisateurs à décrire leurs cas d'usage et ajoutez une courte liste de projets qui
  utilisent l'action, avec leur autorisation. Annoncez les releases importantes avec un exemple concret de
  l'amélioration.

## Ajouter des badges utiles au README

ThreadScale possède déjà des badges Marketplace, d'état des tests et de licence. Un badge d'étoiles ajoute une
mesure publique de l'intérêt suscité. Copiez ce Markdown dans le README d'une action, en remplaçant les noms de
dépôt et de workflow selon vos besoins :

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

Le [badge d'étoiles][stars-docs] compte les étoiles ; le [badge de workflow][tests-docs] indique l'état des tests
du dépôt de l'action. Aucun des deux ne mesure la fréquence à laquelle d'autres projets exécutent l'action.
Le badge Marketplace est un lien statique. Les téléchargements de fichiers joints aux releases et les clonages
du dépôt ne doivent pas non plus être présentés comme des nombres d'exécutions de l'action.

## Montrer des preuves d'adoption

Pour un badge d'utilisation utile, tenez à jour un décompte des **dépôts publics connus utilisant l'action** et
associez-y un lien vers les preuves. Commencez par une liste vérifiée manuellement ; n'automatisez les mises à
jour que si sa maintenance devient fastidieuse. Utilisez la [recherche de code GitHub][search-docs] pour trouver
des workflows susceptibles d'appeler l'action :

```text
"gemc/ThreadScale@" path:.github/workflows/ NOT repo:gemc/ThreadScale
"gemc/ThreadScale/.github/workflows/thread-scaling.yml@" path:.github/workflows/ NOT repo:gemc/ThreadScale
```

Examinez les résultats pour y trouver des références `uses:` actives, éliminez les doublons de dépôts entre les
deux recherches et excluez les forks et les exemples copiés qui ne représentent pas une adoption indépendante.
Notez la date et la méthode de comptage. Il s'agit d'un décompte partiel : les dépôts privés et les workflows
non indexés ou appelant indirectement l'action seront absents, et une référence dans un workflow ne prouve pas
qu'il a été exécuté.

Pour afficher le décompte vérifié, publiez un petit fichier JSON sur votre site web et utilisez un
[badge Shields alimenté par un point de terminaison][endpoint-docs]. Par exemple, le JSON suivant utilise
**N comme valeur de substitution** ; remplacez-le par votre décompte vérifié avant publication :

```json
{
  "schemaVersion": 1,
  "label": "known public users",
  "message": "N repositories",
  "color": "blue"
}
```

Utilisez ensuite ce modèle de README, en remplaçant les deux URL d'exemple par celles de votre point de
terminaison JSON et de votre page de preuves :

```markdown
[![Known public users][usage-badge]][usage-evidence]

[usage-badge]: https://img.shields.io/endpoint?url=https%3A%2F%2Fexample.org%2Fusage.json
[usage-evidence]: https://example.org/adopters
```

Pour évaluer les retombées de la promotion, les mainteneurs de dépôts peuvent aussi utiliser
**Insights → Traffic** pour consulter les visiteurs, les clonages et les sites référents. La
[vue du trafic][traffic-docs] de GitHub couvre les 14 derniers jours pour les visiteurs et les clonages
complets ; ces données mesurent le trafic du dépôt, et non les exécutions de l'action.

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
