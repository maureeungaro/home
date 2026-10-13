---
layout: default
title: "cpp sanitizers"
permalink: /mynotes/cpp_sanitizers.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Sanitizers C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Vous trouverez ci-dessous la liste recommandée des sanitizers utiles, portables, faciles à utiliser et compatibles
avec plusieurs distributions.

D'autres sanitizers comme `integer`, `memory` ou `HWASan` n'ont pas été retenus, car ils sont moins utiles ou
leur implémentation peut ne pas être prise en charge, ou donner des résultats différents selon les
distributions, les compilateurs, etc.

## `address` : ASan — AddressSanitizer (`-fsanitize=address`)

**Objectif :** détecter les bugs de **sûreté mémoire** à l'exécution.

* lectures/écritures hors limites (tas/pile/variables globales)
* utilisation après libération (use-after-free)
* double libération / libération invalide
* certains modes de détection des utilisations après retour de fonction ou sortie de portée (selon la chaîne d'outils)

Usage typique : « trouver rapidement les plantages et les corruptions de mémoire. »

**Erreurs typiquement détectées**

* Accès au-delà de la fin ou avant le début d'un tampon sur le tas
* Accès au-delà de la fin ou avant le début d'un tampon sur la pile
* Utilisation après libération
* Utilisation après retour de fonction / sortie de portée (selon les options du compilateur)
* Double libération, libération invalide, certains usages incorrects de l'allocateur

**Principe de fonctionnement (conceptuel)**

* Instrumente les lectures/écritures et utilise une **mémoire fantôme (shadow memory)** ainsi que des zones de garde
  « empoisonnées » autour des allocations pour détecter rapidement les accès hors limites et les utilisations
  après libération (UAF).

**Points d'attention**

* Surcoût : généralement modéré (souvent 1,5 à 3× plus lent, consommation mémoire plus élevée).
* Incompatibilités : **ASan et TSan ne peuvent pas être combinés** dans un même binaire en pratique ; traitez-les
  comme des modes de compilation distincts.
* Faux positifs : rares, mais possibles avec des allocateurs personnalisés ou des astuces de bas niveau sans
  annotations appropriées.

<br/>

## `thread` : TSan — ThreadSanitizer (`-fsanitize=thread`)

Détecte les **courses aux données (data races)** et d'autres problèmes de concurrence :

* accès concurrents non synchronisés (avec au moins une écriture)
* signale les piles d'appels associées aux courses aux données et le contexte de synchronisation

Usage typique : « valider la sûreté des accès depuis plusieurs threads. »
Remarque : s'exécute généralement dans une version compilée séparément de celle utilisant ASan.

**Objectif :** détecter les **courses aux données (data races)** et certains autres bugs de concurrence.

**Erreurs typiquement détectées**

* Courses aux données (accès concurrents non synchronisés, avec au moins une écriture)
* Usages incorrects des mutex ou des opérations atomiques (selon l'environnement d'exécution)
* Certains diagnostics liés aux interblocages peuvent apparaître, mais l'intérêt principal reste les courses
  aux données.

**Principe de fonctionnement**

* Instrumente les accès mémoire et les opérations de synchronisation, construit un modèle de la relation
  happens-before (« se produit avant ») et signale les accès conflictuels.

**Points d'attention**

* Surcoût : important (souvent 5 à 15× plus lent, consommation mémoire nettement accrue).
* Incompatibilités : ne se combine généralement pas avec ASan/LSan/UBSan dans une même compilation ; utilisez une
  configuration « tsan » dédiée.
* Pour être efficace, nécessite que la majeure partie de votre code (et idéalement les principales bibliothèques
  tierces) soit compilée avec l'instrumentation TSan.

<br/>

## `undefined` UBSan — UndefinedBehaviorSanitizer (`-fsanitize=undefined` et vérifications supplémentaires)

Détecte les **comportements indéfinis** en C/C++ :

* dépassement de capacité des entiers signés (lorsque la vérification est activée)
* décalages invalides (négatifs ou trop grands)
* accès mal alignés
* pointeur de table virtuelle (vptr) invalide (certains modes), valeur d'énumération hors plage, etc.

Usage typique : « repérer les comportements indéfinis qui ne provoquent pas forcément de plantage mais sont
erronés. »

**Objectif :** détecter les **comportements indéfinis** à l'exécution (violations des règles du langage ou de
l'ABI).

**Erreurs typiquement détectées** (exemples)

* Dépassement de capacité des entiers signés (si la vérification est activée)
* Décalages invalides (nombre de bits de décalage négatif ou ≥ au nombre de bits du type)
* Déréférencement d'un pointeur mal aligné
* Problèmes liés aux pointeurs nuls dans certains contextes (selon les options)
* Valeurs d'énumération invalides, vérifications de vptr, etc. (selon les options)

**Principe de fonctionnement**

* Insère des vérifications pour des catégories spécifiques de comportements indéfinis, puis interrompt
  l'exécution ou signale les erreurs à l'exécution.

**Points d'attention**

* « UBSan » est en réalité une **suite de vérifications** ; les vérifications effectuées dépendent des options
  exactes.
* Certaines vérifications peuvent produire de nombreux signalements dans les bases de code qui s'appuient
  intentionnellement sur des pratiques relevant d'un « comportement indéfini bénin ».

<br/>

## `leak` LSan — LeakSanitizer (`-fsanitize=leak` ou détection de fuites d'ASan)

Détecte les **fuites de mémoire** (allocations non libérées qui deviennent inaccessibles à la fin du programme).

Usage typique : « éviter les fuites de mémoire silencieuses dans les services ou tests de longue durée. »
Souvent utilisé dans le cadre d'ASan sous Linux.

**Objectif :** détecter les **fuites de mémoire** (objets alloués mais inaccessibles à la fin du programme).

**Erreurs typiquement détectées**

* Allocations sur le tas à l'origine de fuites de mémoire
* Fuites provenant de certaines API d'allocation lorsque leurs appels sont interceptés

**Principe de fonctionnement**

* À la sortie du processus (ou sur demande), parcourt les racines permettant d'identifier la mémoire accessible
  et signale les allocations qui n'ont jamais été libérées et ne sont plus accessibles.

**Points d'attention**

* La détection de fuites est la plus fiable lorsque le programme se termine « proprement » et lorsque les
  allocations proviennent d'allocateurs dont les appels peuvent être interceptés.
* Souvent utilisé **dans le cadre d'ASan** sous Linux ; de nombreuses équipes exécutent simplement ASan avec la
  détection de fuites activée plutôt que de compiler des versions dédiées à la seule détection des fuites.

<br/>
