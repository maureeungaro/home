---
layout: default
title: "GitHub Actions Marketplace"
permalink: /mynotes/github_marketplace.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Pubblicare un'action nel GitHub Marketplace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Questa nota usa [ThreadScale](https://github.com/gemc/ThreadScale) come esempio:
l'action nella radice del repository è pubblicata come
[ThreadScale sul Marketplace](https://github.com/marketplace/actions/threadscale)
e i workflow la richiamano con `uses: gemc/ThreadScale@v1`.

## Preparare il repository

Usa un repository pubblico dedicato all'action, con un unico `action.yml` o `action.yaml` nella sua radice.
Scegli un nome univoco per l'action che non entri in conflitto con i nomi del Marketplace o con i nomi
riservati di GitHub.

I metadati di ThreadScale includono i seguenti campi; il suo `action.yml` completo dichiara anche input e output:

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

Per la tua action, sostituisci il nome, la descrizione, il branding e il punto di ingresso. Includi il codice
a cui fa riferimento `runs.main`, un README che spieghi l'utilizzo e gli input, e una licenza. ThreadScale usa
la licenza MIT ed esegue direttamente il codice JavaScript senza dipendenze a runtime né una fase di build.
I suoi controlli locali sono:

```shell
npm run check
npm test
```

ThreadScale fornisce anche un workflow riutilizzabile in `.github/workflows/`; la sua scheda nel Marketplace
deriva dall'`action.yml` nella radice.

<br/>

## Pubblicare tramite GitHub

1. Apri l'`action.yml` nella radice del repository su GitHub e usa il banner di release per creare una bozza
   di release.
2. Abilita la casella di pubblicazione sul Marketplace nel modulo di release.
3. Se è disabilitata, il proprietario del repository o un proprietario dell'organizzazione deve accettare il
   Marketplace Developer Agreement tramite la pagina di release. La pubblicazione richiede anche
   l'autenticazione a due fattori.
4. Risolvi eventuali errori di validazione dei metadati, quindi seleziona una categoria principale e,
   facoltativamente, una seconda categoria.
5. Seleziona il tag di versione fisso per il codice che stai pubblicando, poi aggiungi un titolo e delle note
   alla release:
   - Se stai pubblicando sul Marketplace la versione esistente `v1.0.0`, seleziona quel tag. Se la relativa
     GitHub Release esiste già, modifica quella release e abilita lì la pubblicazione sul Marketplace.
   - Se stai rilasciando codice aggiornato, crea o seleziona `v1.0.1` sul commit testato. Quando crei il tag,
     verifica che il commit di destinazione della release sia quello che hai testato.
   - Usa il tag di versione fisso per la release; mantieni `v1` come tag mobile utilizzato dagli utenti.
6. Pubblica la release e controlla la scheda risultante nel Marketplace. Le action idonee compaiono
   immediatamente senza una revisione separata.

Consulta le [istruzioni di pubblicazione di GitHub][publishing] per i requisiti e l'interfaccia attuali.

<br/>

## Mantenere i tag di versione

Supponi che `v1` punti attualmente allo stesso commit di `v1.0.0`. Pubblicare quella versione esistente sul
Marketplace non richiede alcuna modifica ai tag. Non è necessario creare `v1.0.1` solo per aggiungere una
scheda nel Marketplace.

Quando il codice aggiornato è pronto, pubblica una nuova GitHub Release associata a `v1.0.1`, con la
pubblicazione sul Marketplace abilitata. Poi sposta `v1` sullo stesso commit di `v1.0.1`. Questo **non** avviene
automaticamente quando crei la nuova release; aggiorna tu stesso il tag oppure configura l'automazione delle
release affinché lo faccia.

Dopo aver pubblicato `v1.0.1`, esegui questi comandi dal repository della tua action:

```shell
git fetch origin tag v1.0.1
git tag -f v1 'v1.0.1^{}'
git push --force origin refs/tags/v1
```

Il suffisso `^{}` risolve il tag di versione nel commit a cui punta. Si sposta solo `v1`; `v1.0.0`, `v1.0.1` e
le relative GitHub Release mantengono le destinazioni originali. Gli utenti che usano `@v1` ricevono il codice
aggiornato nelle esecuzioni successive, mentre quelli che usano `@v1.0.0` mantengono quella versione. Consulta
la [nota su Git relativa ai tag di release][tags] per i dettagli.

Il workflow riutilizzabile di ThreadScale fa riferimento internamente anche a `gemc/ThreadScale@v1`, quindi
quel tag deve esistere prima che gli utenti eseguano il workflow. Gli utenti possono scegliere `@v1` per gli
aggiornamenti compatibili oppure vincolare la versione allo SHA completo di un commit.

Per le versioni successive, pubblica una nuova release versionata con la pubblicazione sul Marketplace
abilitata, poi aggiorna il tag della versione principale per le modifiche compatibili. Mantieni i tag delle
versioni precedenti.

<br/>

## Aiutare le persone a scoprire e provare l'action

- Apri il README con il problema risolto, un piccolo workflow funzionante e uno screenshot del risultato.
  Il grafico di scaling di ThreadScale è un esempio utile di cosa mostrare.
- Aggiungi una descrizione chiara del repository, topic pertinenti come `github-action`, `benchmark` e
  `performance`, e un link al Marketplace. Inserisci un link all'action nella tua homepage e nella
  documentazione dei progetti correlati.
- Pubblica un breve tutorial usando un'applicazione reale, includendone il workflow e il report risultante.
  Condividilo con le community di calcolo scientifico pertinenti, con i collaboratori e su LinkedIn.
- Proponi l'inclusione in elenchi aggiornati di GitHub Actions o di software scientifico, quando l'action
  rientra nel loro ambito. Segui le istruzioni per contribuire a ciascun elenco.
- Invita i primi utenti a segnalare i loro casi d'uso e aggiungi un breve elenco dei progetti che la adottano,
  con il loro permesso. Annuncia le release importanti con un esempio concreto del miglioramento.

## Aggiungere badge utili al README

ThreadScale ha già i badge del Marketplace, dello stato dei test e della licenza. Un badge delle stelle
aggiunge una misura pubblica dell'interesse. Copia questo Markdown nel README di un'action, sostituendo i nomi
del repository e del workflow secondo necessità:

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

Il [badge delle stelle][stars-docs] conta le stelle; il [badge del workflow][tests-docs] riporta lo stato dei
test del repository dell'action. Nessuno dei due misura la frequenza con cui altri progetti eseguono l'action.
Il badge del Marketplace è un link statico. Anche i download degli asset di release e le clonazioni del
repository non dovrebbero essere presentati come conteggi di esecuzioni dell'action.

## Mostrare prove di adozione

Per un badge di utilizzo utile, mantieni un conteggio dei **repository pubblici noti che usano l'action** e
collegalo alle relative prove. Parti da un elenco verificato manualmente; automatizza gli aggiornamenti solo
se mantenerlo diventa oneroso. Usa la [ricerca nel codice di GitHub][search-docs] per trovare potenziali
utilizzatori:

```text
"gemc/ThreadScale@" path:.github/workflows/ NOT repo:gemc/ThreadScale
"gemc/ThreadScale/.github/workflows/thread-scaling.yml@" path:.github/workflows/ NOT repo:gemc/ThreadScale
```

Esamina le corrispondenze per verificare la presenza di riferimenti `uses:` attivi, elimina i duplicati tra i
repository trovati nelle due ricerche ed escludi i fork e gli esempi copiati che non rappresentano un'adozione
indipendente. Registra la data e il metodo di conteggio. Questo è un conteggio parziale: mancheranno i
repository privati e gli utilizzatori non indicizzati o indiretti, e un riferimento in un workflow non
dimostra che il workflow sia stato eseguito.

Per mostrare il conteggio verificato, pubblica un piccolo file JSON sul tuo sito web e usa un
[badge endpoint di Shields][endpoint-docs]. Ad esempio, il seguente JSON usa **N come segnaposto**;
sostituiscilo con il tuo conteggio verificato prima di pubblicare:

```json
{
  "schemaVersion": 1,
  "label": "known public users",
  "message": "N repositories",
  "color": "blue"
}
```

Poi usa questo modello di README, sostituendo entrambi gli URL di esempio con il tuo endpoint JSON e la pagina
delle prove:

```markdown
[![Known public users][usage-badge]][usage-evidence]

[usage-badge]: https://img.shields.io/endpoint?url=https%3A%2F%2Fexample.org%2Fusage.json
[usage-evidence]: https://example.org/adopters
```

Per valutare i risultati della promozione, i manutentori del repository possono anche usare
**Insights → Traffic** per esaminare visitatori, clonazioni e siti di provenienza. La
[vista del traffico][traffic-docs] di GitHub copre gli ultimi 14 giorni per visitatori e clonazioni complete;
questi dati misurano il traffico del repository, non le esecuzioni dell'action.

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
