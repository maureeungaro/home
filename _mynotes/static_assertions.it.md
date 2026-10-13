---
layout: default
title: "Assertions in C++"
permalink: /mynotes/static_assertions.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# Asserzioni statiche
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

| **Categoria**              | **Macro `static_assert( … )`**              | **Garanzia**                                                         | **Quando / Perché verificarla con un'asserzione**                                                                  | **Scenario tipico di fallimento**                                                |
|----------------------------|---------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Ciclo di vita / distruzione** | ``std::is_nothrow_destructible_v<T>``  | Il distruttore è dichiarato&nbsp;`noexcept` → non può lanciare eccezioni. | Gli oggetti possono essere distrutti durante lo srotolamento dello stack o su thread di lavoro; un distruttore che lancia eccezioni causerebbe una chiamata a `std::terminate`. | Qualcuno aggiunge `~T() { if(err) throw; }` o un membro il cui distruttore può lanciare eccezioni. |
|                            | ``std::is_trivially_destructible_v<T>``     | Il compilatore non fa *nulla* nel distruttore (distruzione bit a bit). | Necessario solo per codice POD / lock-free di bassissimo livello (ad es. per memorizzare oggetti in `std::atomic<T>`). | Aggiunta di un `std::vector`, di uno smart pointer o di un distruttore scritto dall'utente. |
| **Spostamento**             | ``std::is_nothrow_move_constructible_v<T>`` | Spostare un `T` non può lanciare eccezioni.                           | Garantisce che i contenitori (`std::vector`, `std::optional`) mantengano la garanzia forte di sicurezza rispetto alle eccezioni ed evitino copie. | Rimozione di `noexcept` dal costruttore di spostamento o aggiunta di un membro la cui operazione di spostamento può lanciare eccezioni. |
|                            | ``std::is_nothrow_move_assignable_v<T>``    | L'assegnazione per spostamento è `noexcept`.                          | Stesse ragioni di cui sopra; velocizza inoltre gli algoritmi che si affidano a uno `swap` veloce.                  | Come nella colonna precedente.                                                  |
| **Protezione dalla copia** | ``!std::is_copy_constructible_v<T>``        | La costruzione per copia è *eliminata*.                               | Oggetti grandi / unici non devono **mai** essere copiati accidentalmente (ad es. le tabelle di traduzione).        | Un contributore rimuove `= delete`, abilitando accidentalmente copie costose.      |
|                            | ``!std::is_copy_assignable_v<T>``           | L'assegnazione per copia è *eliminata*.                               | Come sopra.                                                                                                        | Idem.                                                                           |
| **Costo della copia / natura POD** | ``std::is_trivially_copyable_v<T>`` | L'oggetto può essere spostato direttamente con `memcpy` (senza operazioni di copia / spostamento o distruttori personalizzati). | Tipi valore molto piccoli passati per valore ad alta frequenza, dati in code lock-free.                         | Aggiunta di uno smart pointer o di operazioni di copia / spostamento o distruttori scritti dall'utente. |
| **Scambiabilità** (C++17)   | ``std::is_nothrow_swappable_v<T>``          | `swap(a,b)` è `noexcept` e ha un costo ridotto.                        | Consente agli algoritmi STL di usare percorsi di esecuzione con scambi veloci (ad es. all'interno di `std::sort`, `std::map::insert`). | Un `swap()` personalizzato perde `noexcept`, oppure le operazioni di spostamento iniziano a lanciare eccezioni. |

---

<br/>

## Come applicarne una

```cpp
#include <type_traits>
#include <utility>          // for std::is_nothrow_swappable_v

static_assert(std::is_nothrow_move_constructible_v<GTranslationTable>,
              "GTranslationTable move-ctor must be noexcept for vector reallocation!");

static_assert(!std::is_copy_constructible_v<GTranslationTable>,
              "Copying a translation table is disallowed — use move or shared_ptr.");

```

<br/>

## Scegliere l'asserzione corretta


| Intento                                  | Trait suggeriti                                      |
| ---------------------------------------- | ---------------------------------------------------- |
| **Tipo valore critico per le prestazioni** | `std::is_trivially_copyable_v<T>`                   |
| **Oggetto che gestisce risorse e viene solo *spostato*** | Eliminare le operazioni di copia + verificare con asserzioni i due trait di spostamento senza eccezioni |
| **Oggetto condiviso tra thread**         | Almeno `std::is_nothrow_destructible_v<T>`            |
| **`swap` personalizzato / uso in mappe ordinate** | Aggiungere `std::is_nothrow_swappable_v<T>`    |


<br/>
