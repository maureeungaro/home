---
layout: default
title: "Assertions in C++"
permalink: /mynotes/static_assertions.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Assertions statiques
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

| **Catégorie** | **Macro `static_assert( … )`** | **Garantie** | **Quand / Pourquoi vérifier cette propriété** | **Scénario d’échec typique** |
|----------------------------|---------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Durée de vie / destruction** | ``std::is_nothrow_destructible_v<T>`` | Le destructeur est déclaré&nbsp;`noexcept` → il ne peut pas lever d’exception. | Les objets peuvent être détruits pendant le dépilement ou sur des threads de travail ; un destructeur qui lève une exception provoquerait un appel à `std::terminate`. | Quelqu’un ajoute `~T() { if(err) throw; }` ou un membre dont le destructeur peut lever une exception. |
|                            | ``std::is_trivially_destructible_v<T>`` | Le compilateur ne fait *rien* dans le destructeur (destruction bit à bit). | Nécessaire uniquement pour du code POD / sans verrou de très bas niveau (par ex. stockage dans `std::atomic<T>`). | Ajout d’un `std::vector`, d’un pointeur intelligent ou d’un destructeur écrit par l’utilisateur. |
| **Déplacement** | ``std::is_nothrow_move_constructible_v<T>`` | Déplacer un `T` ne peut pas lever d’exception. | Garantit que les conteneurs (`std::vector`, `std::optional`) conservent la garantie forte de sûreté vis-à-vis des exceptions et évitent les copies. | Retrait de `noexcept` du constructeur par déplacement ou ajout d’un membre dont le déplacement peut lever une exception. |
|                            | ``std::is_nothrow_move_assignable_v<T>`` | L’affectation par déplacement est `noexcept`. | Mêmes raisons que ci-dessus ; accélère aussi les algorithmes qui reposent sur un `swap` rapide. | Idem colonne précédente. |
| **Protection contre la copie** | ``!std::is_copy_constructible_v<T>`` | La construction par copie est *supprimée*. | Les objets volumineux / uniques ne doivent **jamais** être copiés par accident (par ex. les tables de traduction). | Un contributeur retire `= delete`, réactivant par accident des copies coûteuses. |
|                            | ``!std::is_copy_assignable_v<T>`` | L’affectation par copie est *supprimée*. | Comme ci-dessus. | Idem. |
| **Coût de copie / caractère POD** | ``std::is_trivially_copyable_v<T>`` | L’objet peut être déplacé avec un simple `memcpy` (sans copie / déplacement / destructeur personnalisé). | Petits types à sémantique de valeur passés par valeur à haute fréquence, données dans des files sans verrou. | Ajout d’un pointeur intelligent ou d’opérations de copie / déplacement ou d’un destructeur écrits par l’utilisateur. |
| **Permutabilité** (C++17) | ``std::is_nothrow_swappable_v<T>`` | `swap(a,b)` est `noexcept` et peu coûteux. | Permet aux algorithmes de la STL d’utiliser des chemins de permutation rapides (par ex. dans `std::sort`, `std::map::insert`). | Un `swap()` personnalisé perd son `noexcept`, ou les opérations de déplacement se mettent à lever des exceptions. |

---

<br/>

## Comment en appliquer une

```cpp
#include <type_traits>
#include <utility>          // for std::is_nothrow_swappable_v

static_assert(std::is_nothrow_move_constructible_v<GTranslationTable>,
              "GTranslationTable move-ctor must be noexcept for vector reallocation!");

static_assert(!std::is_copy_constructible_v<GTranslationTable>,
              "Copying a translation table is disallowed — use move or shared_ptr.");

```

<br/>

## Choisir la bonne assertion


| Intention | Trait(s) suggéré(s) |
| ---------------------------------------- | ---------------------------------------------------- |
| **Type à sémantique de valeur dont les performances sont critiques** | `std::is_trivially_copyable_v<T>` |
| **Objet détenant une ressource que l’on *déplace* uniquement** | Supprimer les opérations de copie + vérifier par assertion les deux traits de déplacement sans exception |
| **Objet partagé entre threads** | Au moins `std::is_nothrow_destructible_v<T>` |
| **`swap` personnalisé / utilisé dans des tables associatives ordonnées** | Ajouter `std::is_nothrow_swappable_v<T>` |


<br/>
