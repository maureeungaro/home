---
layout: default
title: "HTCondor"
permalink: /mynotes/htcondor.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# HTCondor
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## Verifica delle configurazioni dei siti

Interroga il collector per vedere quali siti sono disponibili in un pool e se espongono i repository CVMFS
di cui i job hanno bisogno. I due comandi seguenti riportano, per ciascun sito, `GLIDEIN_Site` insieme ai
flag `HAS_CVMFS_oasis_opensciencegrid_org` e `HAS_CVMFS_jlab_opensciencegrid_org`, quindi raggruppano le
righe distinte indicando il conteggio di ciascuna.

Per il pool JLab CHTC, limitato al gruppo GlideinWMS `clas12`:

```shell
condor_status -startd -pool jlab-cm.osg.chtc.io -const 'GLIDEClient_Group == "clas12"' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

Per l'OSPool:

```shell
condor_status -startd -pool cm-1.ospool.osg-htc.org -const 'OSPool' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

<br/>

## Modifica dei requisiti per i job inviati

La modifica di un file di invio influisce solo sugli invii futuri. Usa `condor_qedit` sull'host di invio,
come proprietario del job, per modificare i job già in coda. I comandi seguenti funzionano in Bash e zsh.
Consulta la [documentazione di condor_qedit](https://htcondor.readthedocs.io/en/25.x/man-pages/condor_qedit.html).

Un ID di cluster come `9291` seleziona tutti i suoi subjob in coda; `9291.10` seleziona solo il subjob `10`.
Senza un vincolo sullo stato, `condor_qedit` modifica i job in attesa, in stato held e in esecuzione.
Non mette in hold né rilascia i job. Le modifiche influiscono sui successivi abbinamenti alle risorse,
non sull'esecuzione o sull'allocazione corrente di un job in esecuzione.

### Esaminare i requisiti e lo stato del job

`Requirements` è il nome dell'attributo; non sostituirlo con un altro valore in questi comandi di ispezione.
Usa `-long` per vedere l'espressione memorizzata per un singolo job:

```shell
condor_q 9291.10 -long -attributes Requirements
```

Per l'intero cluster, includi gli ID dei job (questo può produrre una grande quantità di output):

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

L'opzione `-af Requirements` da sola valuta l'espressione invece di stamparne il testo. Senza gli attributi
di un worker, il risultato può essere `false` anche quando l'espressione memorizzata contiene condizioni
di abbinamento valide. Quell'output non significa che i requisiti memorizzati siano letteralmente `false`,
né che i job non possano essere abbinati a un worker. Non sovrascrivere i requisiti basandoti su quell'output.
Se `-long` mostra che l'espressione stessa è letteralmente `false`, allora non corrisponde ad alcun worker.

Per contare i job per stato senza stampare migliaia di righe:

```shell
condor_q 9291 -af JobStatus | sort | uniq -c
```

La prima colonna è il conteggio; la seconda è lo stato: `1` significa in attesa, `2` in esecuzione e `5` held.
Per esempio, `2560 1`, `301 2` e `1 5` significano 2.560 job in attesa, 301 in esecuzione e uno in stato held.
Questi conteggi non permettono di diagnosticare un problema nei requisiti.

Quando acquisisci un'espressione in una variabile di shell, usa `-af:r Requirements`: la `r` richiede
l'output grezzo, non valutato. Consulta la
[documentazione di condor_q](https://htcondor.readthedocs.io/en/24.x/man-pages/condor_q.html).

### Impostare i requisiti per tutti i job di un cluster

Esamina le espressioni memorizzate come descritto sopra prima di decidere se modificarle.

Il comando seguente imposta i requisiti per ogni job in coda nel cluster `9291`. Richiede il repository CVMFS
di JLab e rimuove i precedenti requisiti relativi alla disponibilità e alla revisione di Oasis:

```shell
condor_qedit 9291 Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

Le virgolette doppie e i backslash finali passano l'espressione come un unico argomento senza caratteri
di nuova riga letterali. Mantieni ciascun backslash all'estremità della sua riga, senza spazi finali.
Non sostituire le virgolette doppie con virgolette singole: la continuazione di riga tramite backslash
non funziona all'interno delle virgolette singole.

Questo sostituisce l'intera espressione. Se l'invio originale prevedeva ulteriori requisiti relativi a
risorse, architettura o trasferimento dei file, includi quelle clausole dal file di invio o da un job
equivalente con requisiti integri. Le quattro clausole qui sopra non ripristinano automaticamente i
requisiti generati da HTCondor. Verifica inoltre che gli script del job usino i percorsi `/cvmfs/` previsti;
modificare i requisiti non modifica quei percorsi.

Verifica il risultato:

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

I job in attesa usano i nuovi requisiti al prossimo abbinamento. I job in stato held restano in quello stato.
I job in esecuzione proseguono il tentativo corrente e usano i nuovi requisiti se occorre un nuovo abbinamento.

Solo se intendi interrompere e riavviare i job in esecuzione, esegui `condor_hold 9291` **prima** della modifica,
conferma che i job siano in stato held (`JobStatus == 5`), quindi esegui `condor_release 9291` dopo aver
verificato le modifiche. Mettere in hold i job in esecuzione può far perdere i progressi o l'output salvato
localmente sul worker; senza checkpointing, aspettati un riavvio. Mettere in hold i job in attesa impedisce
anche che vengano avviati durante una serie di modifiche.

### Impostare i requisiti solo per i job in stato held di un cluster

Per lasciare invariati i job in attesa e in esecuzione, seleziona sia il cluster sia lo stato held
(`JobStatus == 5`). Visualizza in anteprima i job selezionati:

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

Applica la sostituzione solo ai job in stato held nel momento in cui viene eseguita la modifica:

```shell
condor_qedit -constraint 'ClusterId == 9291 && JobStatus == 5' Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

Valgono le stesse considerazioni sull'espressione completa viste sopra. Non è necessario mettere prima
in hold il cluster: questo comando seleziona i job già in stato held e li lascia in quello stato.
Verifica le modifiche:

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

Quando sei pronto a ritentare l'esecuzione dei job in stato held in questo cluster:

```shell
condor_release -constraint 'ClusterId == 9291 && JobStatus == 5'
```

Ogni comando valuta il proprio vincolo in modo indipendente. Se un altro job passa allo stato held tra la
modifica e il rilascio, il rilascio seleziona anche quel job. Usa ID di job espliciti se devi rilasciare
esattamente l'insieme modificato.

Gli esempi relativi alla memoria e ai siti qui sotto riguardano un singolo job, `8897.10`; sostituiscilo
con l'ID del job che ti interessa.

### Modificare la memoria richiesta

Per un fabbisogno misurato di 4 GiB, imposta `RequestMemory` a `4096` MB:

```shell
condor_qedit 8897.10 RequestMemory 4096
condor_q 8897.10 -long -attributes RequestMemory,Requirements
```

Il consueto requisito generato, `TARGET.Memory >= RequestMemory`, usa automaticamente la richiesta aggiornata.
Se invece l'espressione contiene una soglia di memoria fissa, esamina anche quella clausola. Una richiesta
maggiore può aumentare il tempo di attesa e non risolve un memory leak. Ha effetto alla prossima allocazione,
non sul tentativo attualmente in esecuzione. Per gli invii futuri, aggiorna `request_memory = 4096` nel
file di invio.

### Escludere un sito problematico

Usa il valore esatto di `GLIDEIN_Site` dichiarato dal pool, come mostrato nelle query sui siti qui sopra.
Sostituisci `SITE_TO_AVOID` qui sotto con quel valore. Leggi l'espressione più recente in modo da preservare
le modifiche precedenti:

```bash
requirements=$(condor_q 8897.10 -af:r Requirements)
printf '%s\n' "$requirements"
```

Fermati se la query è fallita o non ha restituito alcuna espressione. Poi aggiungi l'esclusione:

```bash
condor_qedit 8897.10 Requirements \
  "($requirements) && (TARGET.GLIDEIN_Site =!= \"SITE_TO_AVOID\")"
```

L'operatore ClassAd `=!=` ammette anche i worker in cui `GLIDEIN_Site` non è definito. Per richiedere un sito
noto, includi `!isUndefined(TARGET.GLIDEIN_Site)` come ulteriore clausola. Escludere un sito non interrompe
un tentativo già in corso su quel sito; usa la procedura hold/edit/release per riavviarlo altrove.

### Verificare e rilasciare

Per gli esempi relativi a un singolo job, verifica che ogni modifica sia riuscita ed esamina i valori finali.
Rilascia il job solo se è in stato held e sei pronto a ritentarne l'esecuzione:

```shell
condor_q 8897.10 -long -attributes JobStatus,Requirements,RequestMemory
condor_release 8897.10
condor_q 8897.10
condor_q 8897.10 -better-analyze
```

Il job torna al processo di abbinamento e può restare in attesa di un worker adatto. Usa `-better-analyze`
per indagare sui requisiti non soddisfatti. Applica le stesse modifiche previste al file di invio per i job
futuri.

<br/>

## Debug dei job in stato held

Esegui i comandi seguenti sull'host di invio, come `scosg2202`. Sostituisci `8897.10` con l'ID del cluster e
l'ID del processo del job. Questi esempi riguardano un singolo job, non l'intero cluster.

### Leggere il motivo dell'hold e l'uso delle risorse

```shell
condor_q 8897.10
condor_q 8897.10 -long \
  -attributes JobStatus,HoldReason,HoldReasonCode,HoldReasonSubCode,RequestMemory,MemoryUsage
```

Controlla `JobStatus` insieme a `HoldReason`: il motivo di un hold precedente può rimanere dopo un rilascio.
I valori di stato comuni sono `1` (in attesa), `2` (in esecuzione) e `5` (held).

Il log degli eventi registra l'attività dello scheduler separatamente da stdout e stderr dell'applicazione.
Cerca `012` (messo in hold), `013` (rilasciato), `004` (rimosso dal worker) e `001` (in esecuzione).
Una rimozione dal worker seguita da un'altra esecuzione non è necessariamente un hold.

Per esempio, il job `8897.10` ha registrato questo hold il 15 settembre 2026:

```text
memory usage exceeded request_memory
Code 21 Subcode 102
Memory (MB): Usage 2440   Request 2311   Allocated 2432
```

Il job ha superato la memoria allocata. Dopo il rilascio, un tentativo successivo ha raggiunto 17.712 MB,
con una crescita persistente di circa 60 MB ogni cinque minuti per gran parte dell'esecuzione. Questo
suggerisce un memory leak o un accumulo di dati, ma il log degli eventi da solo non può identificare il
programma responsabile. Il log fornito terminava con un aggiornamento sull'uso della memoria, non con un
secondo hold.

Aumentare leggermente la richiesta o rilasciare ripetutamente il job non risolve una crescita persistente
dell'uso della memoria. Identifica prima il processo e la fase della pipeline, poi misura il suo fabbisogno
di memoria.

### Esaminare l'output mentre il job è in esecuzione

```shell
condor_tail -maxbytes 20000 8897.10
condor_tail -stderr -maxbytes 20000 8897.10
```

Cerca l'ultimo messaggio `Running ...` per identificare la fase attiva della pipeline. Il buffering
dell'applicazione può ritardare l'output. Questi comandi richiedono un job in esecuzione e raggiungibile;
non recuperano i file di un worker precedente dopo che quel tentativo è terminato.

Controlla le impostazioni effettive di logging del job in coda:

```shell
condor_q 8897.10 -long \
  -attributes Iwd,Out,Err,WhenToTransferOutput,StreamOut,StreamErr
```

Il portale attualmente genera `when_to_transfer_output = ON_EXIT` e non abilita esplicitamente lo streaming
di stdout/stderr. Con queste impostazioni, l'output dell'applicazione può rimanere sul worker fino alla
terminazione. Il `.log` dello scheduler può quindi continuare ad aggiornarsi mentre `.out` e `.err` sono
assenti o vuoti in locale. Un tentativo interrotto potrebbe non restituire il proprio output.

### Quando condor_tail non riesce a connettersi allo starter

```text
Failed to peek at file from starter: Failed to connect to starter
```

Questo significa che `condor_tail` non riesce a raggiungere lo starter HTCondor del worker. Non permette
di stabilire se i file di stdout o stderr esistano. Sull'host di invio, come proprietario del job, controlla
lo stato attuale:

```shell
condor_q 8897.10 -long \
  -attributes JobStatus,RemoteHost,LastRemoteHost,HoldReason,RequestMemory,MemoryUsage
tail -80 log/job.8897.10.log
```

Esegui il comando `tail` dalla directory di invio, oppure usa il percorso completo del log degli eventi del job.

| JobStatus | Significato | Passaggio successivo |
| --- | --- | --- |
| `5` | In stato held | Di solito non c'è uno starter in esecuzione; prepara il logging per un nuovo tentativo diagnostico. |
| `1` | In attesa | Attendi un worker; non c'è output attivo da esaminare. |
| `2` | In esecuzione | Prova ad accedere al worker e controlla gli ultimi eventi per disconnessioni o rimozioni dal worker. |

Per un job in esecuzione, prova:

```shell
condor_ssh_to_job 8897.10
```

Questo comando può fallire per lo stesso problema di connettività. Le possibili cause includono un worker
non raggiungibile, un problema di rete o del broker delle connessioni (CCB), oppure un worker scomparso prima
che lo scheduler aggiornasse lo stato del job. L'errore di connessione da solo non distingue tra queste cause.

Acquisisci lo stato e le ultime voci del log degli eventi prima di mettere in hold o riavviare un job in
esecuzione: interrompere il tentativo può far perdere l'accesso ai suoi file correnti nella directory di scratch.

Se il job è già in stato held, segui le istruzioni qui sotto per un nuovo tentativo con streaming.
Lo streaming può preservare l'output sull'host di invio prima di un altro errore, ma dipende comunque dalla
connettività e dal buffering dell'applicazione. Non può recuperare l'output del tentativo precedente né
risolvere la crescita dell'uso della memoria.

### Identificare il processo che consuma memoria

Se il sito supporta l'accesso ai job in esecuzione:

```shell
condor_ssh_to_job 8897.10
```

All'interno della sessione sul worker, esamina i processi e ripeti dopo un minuto:

```shell
ps -eo pid,ppid,rss,vsz,etime,pcpu,args --sort=-rss | head -25
```

`RSS` è la memoria residente in KB; `VSZ` è la memoria virtuale in KB. Usa il PID, il comando e le variazioni
di RSS per distinguere il generatore, GEMC, la ricostruzione o un altro processo. La dimensione dell'immagine
registrata nel log degli eventi non è la stessa misura della memoria residente.

Nella directory di scratch del job, i file che raccolgono stdout/stderr sono solitamente disponibili come:

```shell
tail -100 _condor_stdout
tail -100 _condor_stderr
```

Lo script del portale esegue la pipeline in una sottodirectory `output/`, mentre i file che raccolgono
l'output normalmente rimangono nella directory di scratch superiore.

### Abilitare lo streaming per un nuovo tentativo diagnostico

Per un job in stato held, abilita lo streaming di stdout/stderr per il tentativo successivo:

```shell
condor_qedit 8897.10 StreamOut True
condor_qedit 8897.10 StreamErr True
```

Quando sei pronto a riavviare il job:

```shell
condor_release 8897.10
```

Questo modifica il logging, non la richiesta di memoria né il comportamento dell'applicazione.
Il nuovo tentativo diagnostico può raggiungere lo stesso limite di memoria; il suo scopo è acquisire
la fase attiva e l'output prima dell'errore. Senza checkpointing dell'applicazione, aspettati che la
pipeline ricominci da capo.

Modificare il file di invio originale non aggiorna un job già in coda. Usa `condor_qedit` per gli
attributi dei job in coda e conferma il risultato con `condor_q -long`.

### Modificare nodescript.sh

Modificare lo script sull'host di invio non può cambiare la copia già in esecuzione su un worker. Per un
tentativo successivo, i normali file di input possono essere trasferiti di nuovo, ma HTCondor potrebbe aver
conservato una copia dell'eseguibile acquisita al momento dell'invio. Non fare affidamento sulla modifica
di `nodescript.sh` sul posto seguita da un rilascio per sostituirlo. Modificare gli input condivisi può
inoltre influenzare altri job avviati successivamente.

Per un test dal comportamento prevedibile, prepara un nuovo invio diagnostico in una directory separata:

1. Copia il file di invio generato, `nodescript.sh`, `functions.sh` e tutti gli altri input necessari.
2. Mantieni gli argomenti del job fallito, incluso l'indice del subjob `10` e il suo URI Lund, se applicabile.
   Un nuovo invio con un solo job ha `$(Process) = 0`; imposta esplicitamente l'indice originale per riprodurlo.
3. Sostituisci l'istruzione queue originale con `queue 1` e rimuovi le dipendenze dalle vecchie variabili di queue.
4. Controlla i percorsi di eseguibile, input, directory di lavoro e log affinché si riferiscano ai file diagnostici.
5. Reindirizza l'upload finale a una destinazione separata o disabilitalo, per evitare di sostituire l'output esistente.
6. Aggiungi le seguenti impostazioni al file di invio diagnostico:

```javascript
stream_output = True
stream_error = True
```

Per il tracciamento dei comandi Bash, aggiungi questo vicino all'inizio dello script diagnostico,
dopo lo shebang:

```bash
PS4='+ ${BASH_SOURCE}:${LINENO}: '
set -x
```

Il tracciamento scrive i comandi e gli argomenti espansi su stderr. Identifica il comando invocato ma non
mostra cosa accade all'interno di un programma compilato. Evita di tracciare comandi che espongono credenziali.

Dopo aver esaminato il file diagnostico e la sua istruzione queue per un solo job, esegui l'invio da quella
directory:

```shell
condor_submit debug.condor
```

Usa il nuovo ID del job con `condor_tail` e `condor_ssh_to_job`. Se l'uso della memoria continua a crescere,
riproduci il comando della pipeline identificato con un input più piccolo e indaga sull'uso della memoria
di quel programma.
