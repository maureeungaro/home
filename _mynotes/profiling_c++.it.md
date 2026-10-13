---
layout: default
title: "Profiling C++"
permalink: /mynotes/profiling_c++.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Profiling su macOS con Instruments e xctrace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

### Variabili d'ambiente

L'ambiente viene passato al comando `xctrace`[^1] tramite le opzioni `--env`.
Dato un file `env.dat` con le impostazioni delle variabili d'ambiente (ad esempio da `export`),
si può usare il seguente comando su una sola riga per ottenere le opzioni da passare a `xctrace`:

[^1]:  assicurati che `xctrace` punti a quello di Xcode:
```shell
xcrun --find xctrace
```

```shell
 awk '{print "--env "$0" \\"}' env.dat
```

<br/>

### Template

Il template più usato per il profiling è `Time Profiler`, che consente di analizzare l'utilizzo della CPU.

Per elencare tutti i template disponibili, usa:

```
xcrun xctrace list templates
```

L'opzione `--template` può essere usata per selezionare un template. Ad esempio:

```shell
 --template 'Time Profiler'  
```

<br/>

### Altre opzioni

- `--output` per specificare il file di output per i dati della traccia.
- `--launch` per specificare l'applicazione da profilare.
  Deve includere il percorso dell'eseguibile e può includere le relative opzioni.

<br/>

### Esempio

Il comando qui sotto è stato usato per profilare gemc con il template Time Profiler:

```shell

 rm -rf cpu.trace ; xcrun xctrace record \
  --template 'Time Profiler' \
  --output cpu.trace \
  --target-stdout gemc.log \
  --env C12BFIELDS=/opt/projects/ceInstall/macosx15-clang17/clas12_cmag/1.1 \
  --env CLAS12_CMAG=/opt/projects/ceInstall/macosx15-clang17/clas12_cmag/1.1 \
  --env DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH \
  --env FIELD_DIR=/opt/projects/ceInstall/noarch/data/magfield  \
  --env G4ABLADATA=$G4ABLADATA \
  --env G4DATA_DIR=$G4DATA_DIR \
  --env G4ENSDFSTATEDATA=$G4ENSDFSTATEDATA \
  --env G4INCLDATA=$G4INCLDATA \
  --env G4LEDATA=$G4LEDATA \
  --env G4LEVELGAMMADATA=$G4LEVELGAMMADATA \
  --env G4LIB=$G4LIB \
  --env G4NEUTRONHPDATA=$G4NEUTRONHPDATA \
  --env G4PARTICLEXSDATA=$G4PARTICLEXSDATA \
  --env G4PIIDATA=$G4PIIDATA \
  --env G4RADIOACTIVEDATA=$G4RADIOACTIVEDATA \
  --env G4REALSURFACEDATA=$G4REALSURFACEDATA \
  --env G4SAIDXSDATA=$G4SAIDXSDATA \
  --env G4TENDLDATA=$G4TENDLDATA \
  --env GEMC_DATA_DIR=$GEMC_DATA_DIR \
  --launch -- /opt/projects/gemc/clas12Tags/source/gemc \
    /Users/ungaro/rga_spring2019.gcard \
    -USE_GUI=0 -N=100 -PRINT_EVENT=1 -BEAM_P="e-, 4*GeV, 20*deg, 20*deg"
```

<br/>

---

<br/><br/>

# Profiling su Linux con valgrind
<hr style="height:4px;border:0;background:#4a90e2;">
<br/><br/>

## Prerequisiti

Assicurati che l'eseguibile sia compilato con i seguenti flag per abilitare il profiling:

- `-g` : informazioni complete sui simboli
- `-O2`: ottimizza in modo che gli hot spot siano realistici
- `-fno-omit-frame-pointer`: necessario per uno stack unwinding accurato
- `-fno-optimize-sibling-calls`:  mantiene visibili le chiamate in coda

<br/>

---

<br/>

## Uso di Valgrind

Valgrind può essere usato per profilare applicazioni C++ su Linux:

```shell
valgrind --tool=callgrind --callgrind-out-file=callgrind.out.%p \
  --dump-instr=yes --skip-plt=yes \
  /path/to/your/application options
```


### Spiegazione delle opzioni

- %p viene sostituito con il PID, così da consentire più
- il dump delle istruzioni correla meglio il tempo impiegato con il tempo CPU reale rispetto ai semplici conteggi delle chiamate.
- skip-plt: 

<br/>

---

<br/>


## Visualizzazione dei risultati

```shell
qcachegrind callgrind.out.<PID>
```

I seguenti accorgimenti possono rendere l'output più leggibile:

- Clic destro in Call Graph ▸Graph ▸Min node cost
- Raggruppa per nome della classe
- Pulsante “%” nella barra degli strumenti: valori relativi al nodo padre

<br/>

---

<br/>
