---
layout: default
title: "cpp sanitizers"
permalink: /mynotes/cpp_sanitizers.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Sanitizer per C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Di seguito è riportato l'elenco consigliato di sanitizer utili, portabili, facili da integrare e utilizzabili su più distribuzioni.

Altri sanitizer come `integer`, `memory`, `HWASan` non sono stati inclusi perché meno utili
o perché la loro implementazione potrebbe non essere supportata o fornire risultati diversi a seconda della distribuzione, del compilatore, ecc.

## `address`: ASan — AddressSanitizer (`-fsanitize=address`)

**Scopo:** rileva errori di **sicurezza della memoria** a runtime.

* letture/scritture fuori dai limiti (heap/stack/variabili globali)
* use-after-free
* doppia deallocazione / deallocazione non valida
* alcune modalità di rilevamento di use-after-return/use-after-scope (dipendenti dalla toolchain)

Uso tipico: «individuare rapidamente crash e corruzione della memoria».

**Problemi tipici rilevati**

* Buffer overflow / underflow nell'heap
* Buffer overflow / underflow nello stack
* Use-after-free
* Use-after-return / use-after-scope (a seconda delle opzioni del compilatore)
* Doppia deallocazione, deallocazione non valida, alcuni usi scorretti dell'allocatore

**Come funziona (concettualmente)**

* Strumenta le operazioni di lettura/scrittura e usa la **memoria ombra** insieme a zone di guardia contrassegnate come non accessibili attorno alle allocazioni per rilevare rapidamente gli accessi fuori dai limiti e gli use-after-free (UAF).

**Avvertenze**

* Overhead: di solito moderato (spesso 1,5–3× più lento, con un maggiore consumo di memoria).
* Incompatibilità: nella pratica **ASan e TSan non possono essere combinati** nello stesso binario; vanno trattati come modalità di build separate.
* Falsi positivi: rari, ma possono verificarsi con allocatori personalizzati / tecniche di basso livello se non adeguatamente annotati.

<br/>

## `thread`: TSan — ThreadSanitizer (`-fsanitize=thread`)

Rileva **data race** e altri problemi di concorrenza:

* accessi concorrenti non sincronizzati (di cui almeno uno in scrittura)
* segnala gli stack di chiamate coinvolti nelle race e il contesto di sincronizzazione

Uso tipico: «verificare la sicurezza rispetto agli accessi concorrenti dei thread».
Nota: di solito viene eseguito in una build separata da quella con ASan.

**Scopo:** rileva **data race** e alcuni altri errori di concorrenza.

**Problemi tipici rilevati**

* Data race (accessi concorrenti non sincronizzati, di cui almeno uno in scrittura)
* Schemi di uso scorretto di mutex e operazioni atomiche (a seconda del runtime)
* Possono comparire alcuni messaggi diagnostici relativi ai deadlock, ma il beneficio principale è il rilevamento delle race.

**Come funziona**

* Strumenta gli accessi alla memoria e le operazioni di sincronizzazione, costruisce un modello della relazione happens-before e segnala gli accessi in conflitto.

**Avvertenze**

* Overhead: significativo (spesso 5–15× più lento, con un notevole consumo aggiuntivo di memoria).
* Incompatibilità: in genere non viene combinato con ASan/LSan/UBSan in un'unica build; usare una configurazione «tsan» dedicata.
* Per essere efficace, richiede che la maggior parte del codice (e idealmente le principali librerie di terze parti) sia compilata con la strumentazione TSan.

<br/>

## `undefined` UBSan — UndefinedBehaviorSanitizer (`-fsanitize=undefined` più controlli specifici)

Rileva **comportamenti indefiniti** in C/C++:

* overflow di interi con segno (quando il controllo è abilitato)
* scorrimenti di bit non validi (di un numero di posizioni negativo o troppo grande)
* accessi non allineati
* vptr non validi (in alcune modalità), valori enum fuori intervallo, ecc.

Uso tipico: «rilevare comportamenti indefiniti (UB) che potrebbero non causare crash ma sono comunque errati».

**Scopo:** rileva **comportamenti indefiniti** a runtime (violazioni delle regole del linguaggio/ABI).

**Problemi tipici rilevati** (esempi)

* Overflow di interi con segno (se il controllo è abilitato)
* Scorrimenti di bit non validi (di un numero di posizioni negativo o ≥ alla larghezza in bit)
* Dereferenziazione di puntatori non allineati
* Problemi con puntatori nulli in alcuni contesti (a seconda delle opzioni)
* Valori enum non validi, controlli sui vptr, ecc. (a seconda dei flag)

**Come funziona**

* Inserisce controlli per specifiche categorie di UB e genera un trap o segnala l'errore a runtime.

**Avvertenze**

* «UBSan» è in realtà una **suite di controlli**; i controlli effettivi dipendono dai flag specificati.
* Alcuni controlli possono produrre numerose segnalazioni in basi di codice che si affidano intenzionalmente a schemi di «UB benigno».

<br/>

## `leak` LSan — LeakSanitizer (`-fsanitize=leak` o rilevamento delle perdite di memoria di ASan)

Rileva **perdite di memoria** (allocazioni non liberate che diventano irraggiungibili al termine del programma).

Uso tipico: «evitare che servizi/test di lunga durata accumulino perdite di memoria senza segnalarle».
Spesso viene usato come parte di ASan su Linux.

**Scopo:** rileva **perdite di memoria** (oggetti allocati ma non raggiungibili al termine del programma).

**Problemi tipici rilevati**

* Allocazioni nell'heap non liberate e non più raggiungibili
* Perdite di memoria da determinate API di allocazione, se intercettate

**Come funziona**

* All'uscita del processo (o su richiesta), analizza la memoria raggiungibile a partire dalle radici e segnala le allocazioni che non sono mai state liberate e non sono raggiungibili.

**Avvertenze**

* Il rilevamento delle perdite di memoria è più affidabile quando il programma termina in modo «pulito» e le allocazioni provengono da allocatori intercettabili.
* Spesso viene usato **come parte di ASan** nei flussi di lavoro su Linux; molti team eseguono semplicemente ASan con il rilevamento delle perdite di memoria abilitato anziché usare build separate dedicate al solo rilevamento delle perdite.

<br/>
