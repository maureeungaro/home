---
layout: default
title: "Using Git"
permalink: /mynotes/git.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Usare Git
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## Clonare un solo branch o tag, senza cronologia, con i sottomoduli senza la loro cronologia (shallow)

```shell
git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
```

<br/>

## Git LFS (Large File Storage)

Installa Git LFS, poi inizializzalo una volta per il tuo account utente:

```shell
# macOS
brew install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs

git lfs install
```

Abilita Git LFS in un repository e seleziona i tipi di file da memorizzare con esso:

```shell
cd path/to/repository
git lfs track "*.zip"       # use a pattern or a specific file path
git add .gitattributes      # commit the tracking rules
git add path/to/archive.zip
git commit -m "Track ZIP files with Git LFS"
git push
```

Esegui `git lfs ls-files` per elencare i file tracciati. Il tracciamento di un pattern riguarda solo i file
aggiunti successivamente; spostare in LFS file già salvati tramite commit in Git senza LFS richiede
`git lfs migrate`, che riscrive la cronologia del repository.

<br/>

## Pubblicare una release immutabile e spostare il suo tag di versione maggiore

Usa due tag per una GitHub Action versionata o un altro progetto:

* `v1.0.1` è il tag immutabile della release. Non spostarlo né riutilizzarlo mai.
* `v1` è un tag di compatibilità mobile. Gli utenti che specificano `uses: owner/repository@v1` ricevono
  l'ultima release `v1.x.x` compatibile.

La GitHub Release deve restare associata a `v1.0.1`. Solo il tag `v1` si sposta; non esiste una GitHub
Release mobile separata.

#### 1) Pubblicare la GitHub Release

Sulla pagina GitHub del repository:

1. Apri **Releases** e seleziona **Draft a new release**.
2. Crea (o scegli) il tag `v1.0.1`.
3. Aggiungi il titolo della release, le note ed eventuali asset.


#### 2) Creare o aggiornare il tag di versione maggiore

Imposta la versione immutabile e la versione maggiore mobile:

```shell
version=v1.0.1
major=v1
```

Solo dopo che la GitHub Release per `v1.0.1` è stata pubblicata, fai puntare `v1` ad essa. Alla prima release
questo crea `v1`; a ogni release successiva (`v1.0.2`, `v1.1.2`, ...) lo stesso comando aggiorna `v1` al tag
immutabile più recente. Recupera il tag appena creato da GitHub, fai puntare il tag locale `v1` al commit
a cui fa riferimento `$version`, poi forza l'aggiornamento solo di quel tag su GitHub:

```shell
git fetch origin tag "$version"
git tag -f "$major" "$version^{}"
git push --force origin "refs/tags/$major"
```

Il suffisso `^{}` dereferenzia il tag di versione, così `v1` punta direttamente al commit della release.
L'aggiornamento forzato è necessario perché spostare un tag è un aggiornamento non-fast-forward (ed è innocuo
la prima volta, quando `v1` non esiste ancora). Proteggi i tag immutabili come `v*.*.*` con un insieme di
regole per i tag su GitHub, consentendo lo spostamento dei tag di versione maggiore previsti a tale scopo.

<br/>

## Aggiornare un tag / una release (riscrivere un tag esistente)

**Usa queste variabili**

* `tag`: il nome del tag GitHub (es. `v1.2.3`)
* `btag`: nome del branch temporaneo creato dal tag
* `rtag`: percorso completo del riferimento del tag (`refs/tags/<tag>`), usato per la cancellazione remota

Esempio: `tag=v1.2.3`

```shell
btag="b$tag"
rtag="refs/tags/$tag"
```

#### 1) Creare e passare a un branch temporaneo a partire dal tag esistente

```shell
git fetch origin --tags
git switch -c "$btag" "$tag"
```

#### 2) Apportare le modifiche, fare commit e push del branch temporaneo

```shell
git commit -am "Fixes for $tag"
git push -u origin "$btag"
```

#### 3) Eliminare il vecchio tag locale che punta al vecchio commit e ricrearlo localmente sul nuovo HEAD

(Sei già su `$btag`, quindi l'ulteriore `git switch "$btag"` è ridondante.)

```shell
git tag -d "$tag"
git tag "$tag"
```

#### 4) Sostituire il tag remoto facendolo puntare al nuovo commit

Prima elimina il vecchio tag remoto, poi fai push del nuovo.
Forza esplicitamente l'aggiornamento del tag remoto perché i tag sono immutabili per convenzione e molti server
rifiutano gli aggiornamenti di tag non-fast-forward a meno che non vengano forzati.

```shell
git push origin ":$rtag"
git push --force origin "$rtag"
```

#### 5) Aggiornare la GitHub Release (e gli asset) se necessario
* Se hai caricato asset di release (binari / .tar.gz personalizzati / ecc.):
   aggiorna la release esistente rimuovendo i vecchi asset e caricando quelli nuovi (oppure elimina e ricrea
   la release).
   Spostare il tag non sostituisce gli asset caricati.
* Se vengono usati solo gli archivi sorgente generati da GitHub (“Source code (tar.gz/zip)”):
  di solito puoi lasciare la release così com'è; continuerà a essere “per $tag”, e gli archivi generati
  seguiranno il tag aggiornato (potrebbe richiedere un po' di tempo a causa della cache).
* Se le note di release o il changelog devono cambiare:
  modifica le note di release esistenti, oppure elimina e ricrea la release per $tag.

#### 6) Pulizia: eliminare il branch temporaneo (remoto + locale)

```shell
git push origin --delete "$btag"
git switch main
git branch -D "$btag"
```


<br/>

## Branch

Creare un nuovo branch e passare ad esso:

```shell
git checkout -b branchname
```

Passare a un branch esistente:

```shell
git checkout branchname
```

Unire le modifiche da branch1 in branch2 (uno dei due può essere main). Usa `rebase` per una cronologia
pulita. In alternativa, puoi usare `merge` per conservare la cronologia di entrambi i branch.
```shell
git checkout branch2
git merge/rebase branch1 
```

Fare push di un branch sul remoto:

```shell
git push -u origin branchname
```

Eliminare un branch remoto:

```shell
git push origin --delete branchname
```

Elencare tutti i branch remoti:

- `git branch -r`: elenca tutti i branch remoti
- `git branch -a`: elenca tutti i branch (locali e remoti)
- `git branch -vv`: elenca tutti i branch con il loro ultimo commit
- `git branch --merged`: elenca i branch che sono stati uniti nel branch corrente
- `git branch --no-merged`: elenca i branch che non sono stati uniti nel branch corrente


<br/>

## Modificare una pull request o merge request esistente

Una pull request (PR) di GitHub o una merge request (MR) di GitLab da un **fork** segue un **branch sorgente
in quel fork** e propone di unirlo in un **branch di destinazione nel repository originale** (spesso `main`).
Un fork è un repository separato; contiene comunque dei branch. Aggiungi commit allo stesso branch nello
stesso fork, dal browser o facendo push da un clone locale, per aggiornare automaticamente una richiesta
aperta. Non è necessario creare un'altra richiesta.

### Aggiornare il codice dal browser

Non è necessario clonare il fork. Ti serve comunque il permesso di aggiornare il suo branch sorgente:
l'autore può modificare il proprio fork, e i maintainer possono contribuire quando l'autore abilita **Allow
edits from maintainers** su GitHub o **Allow contributions from members** su GitLab.

1. Apri la PR o MR esistente e individua il suo **fork sorgente e branch sorgente**.
2. Apri quel fork nel browser e seleziona il branch sorgente, ad esempio `my-feature`.
3. Apri il file e usa l'editor web. Per modifiche su più file, usa l'editor web di GitHub o il Web IDE di
   GitLab.
4. Rivedi le modifiche e fai commit direttamente sul **branch sorgente esistente**. Se ti viene offerta una
   scelta, scegli quel branch invece di creare un nuovo branch o una nuova richiesta.

La PR o MR esistente include automaticamente quei commit. Controlla il diff aggiornato e i risultati dei
controlli sulla pagina della richiesta.

Puoi anche applicare le modifiche suggerite nei commenti di revisione direttamente sulla PR o MR quando hai
il permesso di aggiornare il branch sorgente. Applicare un suggerimento crea un commit su quel branch.
I revisori senza quel permesso possono suggerire modifiche che l'autore o un maintainer autorizzato potrà
applicare.

### Aggiornare il codice da un clone locale

#### 1) Individuare il fork e il suo branch sorgente

Trova il fork e il branch sorgente sulla pagina della richiesta, ad esempio `your-user/repository` e
`my-feature`. Ti serve accesso in scrittura al branch sorgente di quel fork. Creare un altro fork o fare push
su un branch diverso non aggiornerà la richiesta esistente.

Nel tuo clone locale, controlla a quale repository punta ciascun remote:

```shell
git remote -v
```

I comandi seguenti usano un remote chiamato `fork` che punta al fork sorgente della richiesta. Se quel fork è
già il tuo `origin`, sostituisci `fork` con `origin` ovunque. Se nessun remote punta ad esso, aggiungine uno
usando l'URL di clone SSH o HTTPS del fork da GitHub o GitLab:

```shell
git remote add fork <fork-clone-url>
```

#### 2) Passare al branch sorgente nel fork

Parti con un albero di lavoro pulito: fai commit o stash di eventuali modifiche non correlate prima di
cambiare branch.

```shell
git status
git fetch fork
git switch my-feature
# If the branch does not exist locally, use this instead:
# git switch --track fork/my-feature
git pull --ff-only fork my-feature
```

Se il pull segnala branch divergenti, riconcilia i commit locali e remoti prima di continuare.

#### 3) Modificare i file, rivedere le modifiche, fare commit e push sul fork

Apporta le modifiche richieste ed esegui i controlli pertinenti, poi:

```shell
git diff
git add path/to/file path/to/another-file
git diff --cached
git commit -m "Address review feedback"
git push fork HEAD:my-feature
```

`HEAD:my-feature` fa push del tuo commit corrente sul branch sorgente esistente del fork. La PR o MR del
repository originale ora include i nuovi commit. Rivedi il diff aggiornato e i risultati dei controlli sulla
sua pagina.

#### 4) Aggiornare il titolo o la descrizione se necessario

Apri la richiesta esistente su GitHub o GitLab e modifica il titolo o la descrizione. Queste modifiche non
richiedono un commit Git. Se l'ambito è cambiato, descrivi la modifica finale così che i revisori possano
comprenderla.

#### Se hai modificato i commit con amend o fatto rebase del branch sorgente

Fare amend o rebase di commit già inviati al remoto riscrive la loro cronologia. Coordinati con chiunque
condivida il branch, poi usa `git push --force-with-lease fork HEAD:my-feature` per aggiornare la stessa
richiesta. Se il controllo del lease rifiuta il push, fai fetch e rivedi le modifiche remote prima di
riprovare. La protezione del branch potrebbe vietare i push forzati; aggiungere un nuovo commit evita di
riscrivere la cronologia.

Una volta che una richiesta è stata unita, invia ulteriori modifiche tramite un nuovo branch e una nuova PR o
MR.

<br/>

## Prendere file specifici da un altro branch (non un merge completo)

Quando vuoi solo uno o pochi file da un altro branch (o commit/tag), non unire l'intero branch — porta nel
tuo albero di lavoro corrente solo quei percorsi.

> ⚠️ Questi comandi **sovrascrivono** la copia locale dei percorsi elencati. Eventuali modifiche non salvate
> tramite commit su quei percorsi vanno perse. Esegui prima `git status` se non sei sicuro.

#### Visualizzare prima la differenza

```shell
git diff main..otherbranch -- path/to/file        # what would change in that file
git show otherbranch:path/to/file                 # print the file as it is on otherbranch
```

#### Copiare i file (sostituire la versione locale)

```shell
# Modern (recommended). --source can be a branch, tag, or commit SHA.
git restore --source=otherbranch --staged --worktree -- path/to/file [more/files...]

# Classic equivalent (also stages the result):
git checkout otherbranch -- path/to/file [more/files...]
```

`git checkout <branch> -- <path>` aggiorna sia l'albero di lavoro sia l'indice (il file è già in staging).
`git restore --source=<ref> -- <path>` aggiorna solo l'albero di lavoro per impostazione predefinita — aggiungi
`--staged` (come sopra) per aggiornare anche l'indice. Poi fai commit normalmente:

```shell
git add path/to/file        # only needed if the file is not already staged
git commit -m "Bring path/to/file from otherbranch"
```

#### Prendere solo alcune modifiche all'interno di un file (in modo interattivo, hunk per hunk)

Questa è l'operazione più vicina al "merge" di un singolo file: scegli quali blocchi di modifiche importare.

```shell
git restore -p --source=otherbranch -- path/to/file   # or: git checkout -p otherbranch -- path/to/file
```

#### Vero merge a tre vie di un singolo file

`checkout`/`restore` *sostituiscono* il file; non ne uniscono il contenuto con il tuo. Per un vero merge riga
per riga di un file tra due versioni, usa `git merge-file`:

```shell
git show otherbranch:path/to/file > /tmp/theirs       # their version
git show $(git merge-base HEAD otherbranch):path/to/file > /tmp/base   # common ancestor
git merge-file path/to/file /tmp/base /tmp/theirs     # merges into path/to/file, marks conflicts
```


<br/>

## Conflitti

### 1. Risolvere i conflitti

- Controlla cosa è in conflitto:

```shell
git status
```

* **Conflitti di testo (`UU`, ecc.)**: apri il file e risolvi i conflitti indicati da `<<<<<<< ======= >>>>>>>`, poi:

```shell
git add path
```

* **Mantieni una delle due versioni** (scegli ours o theirs):

```shell
git checkout --ours  path   # keep our version (rebase source)
git checkout --theirs path  # keep their version (rebase target)
git add path
```

* **Vuoi che il file venga rimosso (es. conflitto `DU` / eliminazione contro modifica)**:

```shell
git rm -- path
# if the file is already gone locally:
git rm --cached -- path
git add -u
```

### 2. Finalizzare un rebase o un merge

```shell
git rebase --continue   # repeat until it finishes
git push origin branch2
```

oppure
```shell
git commit -m "merge branch1 into branch2"
git push origin branch2
```

<br/>


### Codici di stato dei file non uniti

* `DD` eliminato da entrambe le parti
* `AU` aggiunto da noi
* `UD` eliminato da loro
* `UA` aggiunto da loro
* `DU` eliminato da noi *(spesso: decidi se mantenere o eliminare; usa `git rm` per eliminare)*
* `AA` aggiunto da entrambe le parti
* `UU` modificato da entrambe le parti

<br/>


## Cronologia

### Mostrare commit + diff per un file specifico

```shell
git log -p -- path/to/file
```

### Cronologia compatta con una riga per commit
```shell
git log --follow --date=short --pretty=format:"%h %ad %an %s" -- path/to/file
```

### Per rimuovere tutta la cronologia da un repository:

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

## Fare revert o annullare l'ultimo commit

Ci sono due modi molto diversi di "annullare" l'ultimo commit. Scegli in base al fatto che il commit sia già
stato inviato al remoto o meno.

#### Già inviato al remoto → `git revert` (sicuro, mantiene la cronologia)

`git revert` non elimina il commit; crea un commit **nuovo** che annulla le sue modifiche. La cronologia è
preservata e non serve alcun push forzato, quindi questa è la scelta giusta per un branch condiviso o già
inviato al remoto.

```shell
git revert HEAD          # opens an editor for the revert message
git revert --no-edit HEAD   # reuse the default message, no editor
git push
```

Per annullare il revert stesso, basta fare revert del revert (`git revert HEAD`) — oppure eliminarlo finché è
ancora locale con i comandi reset qui sotto.

#### Solo locale → `git reset` (riscrive la cronologia)

Se il commit **non** è stato inviato al remoto, sposta il puntatore del branch indietro di un commit. Ciò che
succede alle modifiche dipende dal flag:

```shell
git reset --soft  HEAD~1   # undo the commit, keep changes staged
git reset --mixed HEAD~1   # undo the commit, keep changes in the working tree (default)
git reset --hard  HEAD~1   # undo the commit AND discard the changes
```

> ⚠️ `--hard` scarta permanentemente le modifiche nell'albero di lavoro di quel commit. Esegui `git status`
> (e, se non sei sicuro, `git stash`) prima.

Caso comune: mantenere il lavoro ma rifare il commit — `git reset --soft HEAD~1`, poi aggiorna l'area di
staging e crea un nuovo commit secondo necessità.

Correggere solo il messaggio o aggiungere file dimenticati all'ultimo commit senza fare reset:

```shell
git commit --amend            # edit message and/or fold in staged changes
git commit --amend --no-edit  # keep the message, just add the staged changes
```

#### Se era già stato inviato al remoto

Fare reset di un commit inviato al remoto riscrive la cronologia, quindi il push è non-fast-forward e deve
essere forzato. Preferisci `--force-with-lease`, che rifiuta il push se qualcun altro ha fatto push nel frattempo:

```shell
git reset --hard HEAD~1
git push --force-with-lease
```

> ⚠️ Fallo solo su un branch che controlli tu. Riscrivere una cronologia condivisa crea problemi negli altri
> cloni — su un branch condiviso usa invece `git revert`.

#### Recuperare un commit eliminato per errore

`reset` non elimina immediatamente i commit; il precedente commit di punta resta nel reflog per un po':

```shell
git reflog                 # find the SHA of the lost commit
git reset --hard <sha>     # or: git cherry-pick <sha>
```

<br/>

## Token (Personal Access Token)

Un **Personal Access Token (PAT)** è una credenziale legata al **tuo account personale**, non a un
repository. Lo crei sempre in:

```
Personal Settings > Developer Settings > Personal access tokens
```

Due fatti chiave che è facile fraintendere:

* Il token **eredita i permessi dell'account che lo crea**. Per agire su un repository (avviare i suoi
  workflow, fare push, scaricare immagini private), quell'account deve avere i permessi necessari su
  **quel** repository.
* GitHub mostra la stringa del token **solo una volta**, al momento della creazione. Non può essere riletta
  in seguito (né dalle tue impostazioni, né da un secret in cui è stata incollata). Se la perdi, rigenerala.

Puoi usare `regenerate` per rigenerare un token esistente (nuovo valore) o modificare gli scope di un token
classico senza sostituirlo (valore invariato) — entrambe le operazioni dalla stessa pagina. Imposta sempre
una data di scadenza personalizzata.

### Quale scope / permesso mi serve?

Scegli la riga in base a ciò che il token deve **fare**, non al repository in cui risiede:

| Obiettivo                                 | Scope classico         | Permesso granulare             |
|-------------------------------------------|------------------------|--------------------------------|
| **Avviare** il workflow di un altro repository (API) | `repo` / `public_repo` | **Actions → Read and write**   |
| Aggiungere / modificare file `.github/workflows/*` | `workflow`       | **Workflows → Read and write** |
| Scaricare immagini private di container    | `read:packages`        | **Packages → Read**            |

> ⚠️ Errore comune: lo scope `workflow` serve **solo** per fare commit di file di workflow. **Non** ti
> consente di *avviare* un'esecuzione. Per avviare un `workflow_dispatch` / `repository_dispatch` ti serve
> `repo` (`public_repo` per i repository pubblici) su un token classico, oppure **Actions: Read and write**
> su un token con permessi granulari.

### Link diretti

* Permessi granulari: <https://github.com/settings/personal-access-tokens/new>
  → Proprietario `gemc`, repository es. `gemc/clas12-systems`, permesso **Actions: Read and write**
* Classico: <https://github.com/settings/tokens/new>
  → Scope: ✅ `repo` (include `public_repo`); aggiungi `read:packages` per le immagini private

Un token usato da uno strumento locale (non da un workflow) dovrebbe essere messo in un file letto da quello
strumento, tipicamente nella directory home, ad esempio `.bob`.


<br/>

## Secret

Un **secret di GitHub Actions** è una variabile cifrata memorizzata nelle impostazioni di un repository. I
workflow in quel repository lo leggono durante l'esecuzione tramite
{% raw %}`${{ secrets.SECRET_NAME }}`{% endraw %}; il valore non viene mai stampato nei log né mostrato a chi
naviga nel repository.

Tieni le due parti separate — risiedono in posti diversi:

* **Il token** (la stringa `ghp_…` / `github_pat_…`) viene creato nel **tuo account personale** (sopra).
* **Il secret** è una *copia* di quella stringa, memorizzata nel repository **il cui workflow lo userà** —
  cioè il repository che avvia il workflow, **non** quello in cui il workflow viene avviato.

### Come crearlo e memorizzarlo

1. **Genera il token** nel tuo **account personale** (Developer settings), scegliendo lo scope/permesso per
   il repository **di destinazione** su cui vuoi che il workflow agisca (vedi la tabella sopra). L'account
   deve avere accesso in scrittura a quel repository di destinazione.

2. **Copia il valore del token** mostrato a schermo (visibile solo una volta).

3. **Aggiungi il secret al repository il cui workflow lo usa**
   - Vai a quel repository → **Settings → Secrets and variables → Actions**
     (es. <https://github.com/gemc/pygemc/settings/secrets/actions>)
   - Clicca **New repository secret**
   - Nome: es. `GEMC_SRC_PAT` (deve corrispondere al nome a cui fa riferimento il YAML del workflow)
   - Valore: incolla il token
   - Clicca **Add secret**


<br/>

## Avviare un workflow in un altro repository

Il `GITHUB_TOKEN` integrato **non può** avviare workflow in un repository diverso, quindi i trigger tra
repository usano un PAT memorizzato come secret. Lo schema: il workflow del **repository A** chiama l'API di
GitHub per avviare il workflow del **repository B**.

Ti servono tre cose:

1. **Un PAT** appartenente a un account con **accesso in scrittura al repository B**, con i permessi per
   avviare le Actions (`repo` per un token classico, oppure **Actions: Read and write** su B per un token
   con permessi granulari). Vedi la tabella dei Token sopra.
2. **Il secret** che contiene quel PAT, memorizzato nel **repository A** (la sorgente del trigger).
3. **Un trigger attivabile tramite dispatch sul workflow del repository B** — aggiungi `workflow_dispatch:`
   (con `inputs:` opzionali) al blocco `on:` del workflow di destinazione, altrimenti la chiamata API
   restituisce `404`/`422`.

### La chiamata di dispatch (nel workflow del repository A)

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

Le chiavi di `inputs` devono corrispondere agli `inputs:` dichiarati sotto `workflow_dispatch:` nel workflow
del repository B.

### Sicurezza: proteggere i trigger concatenati con `workflow_run`

Un workflow con `on: workflow_run` viene eseguito con **privilegi elevati** (può accedere ai secret/PAT) e si
attiva anche per gli eventi di PR da fork, quindi limita l'esecuzione del job con una condizione — altrimenti
una PR da fork potrebbe raggiungere lo step privilegiato e qualsiasi codice di cui esso esegua il checkout
tramite `workflow_run.head_sha`. Questo è anche il motivo per cui CodeQL segnala il "checkout di codice non
attendibile in un contesto privilegiato".

**Quale campo controllare dipende dalla posizione nella catena** — questo punto può creare confusione:

* **1° passaggio** — in ascolto su un workflow attivato *direttamente* da `push`/`pull_request` (es. un `Deploy`
  eseguito con `on: workflow_run` di `Test`): `github.event.workflow_run.event` è l'evento originale, quindi
  usa come condizione di protezione `event == 'push'`.

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.event == 'push'
        }}
  ```
  {% endraw %}

* **2° passaggio** — in ascolto su un workflow che è *esso stesso* attivato da `workflow_run` (es. un job
  eseguito dopo `Deploy`, che a sua volta usa `on: workflow_run`): qui `workflow_run.event` è **sempre
  `workflow_run`**, mai `push`. Usare `event == 'push'` fa sì che il job non venga mai eseguito; usare
  `event == 'workflow_run'` dà sempre esito positivo (nessuna protezione). Controlla invece il repository
  sorgente — i campi `head_*` conservano la sorgente originale lungo la catena:

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.head_repository.full_name == github.repository
        }}
  ```
  {% endraw %}

  `head_repository.full_name == github.repository` è vero per i push nello stesso repository e falso per le
  catene originate da PR da fork: è esattamente la protezione desiderata contro il checkout di codice non
  attendibile.

### Esempi in questo progetto

| Sorgente del trigger (repository A) | Nome del secret (in A) | Destinazione (repository B) | Permessi necessari al token (su B) |
|-------------------------|-----------------------|----------------------|-------------------------|
| `gemc/pygemc`           | `GEMC_SRC_PAT`        | `gemc/src`           | avviare le Actions su src  |
| `gemc/src`              | `CLAS12_SYSTEMS_PAT`  | `gemc/clas12-systems`| avviare le Actions su clas12-systems |
