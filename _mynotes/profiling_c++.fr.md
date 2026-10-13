---
layout: default
title: "Profiling C++"
permalink: /mynotes/profiling_c++.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Profilage sur macOS avec Instruments et xctrace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

### Variables d'environnement

L'environnement est transmis à la commande `xctrace`[^1] au moyen des options `--env`.
À partir d'un fichier `env.dat` contenant les valeurs des variables d'environnement (par exemple issues d'`export`),
la commande suivante, sur une seule ligne, permet d'obtenir les options à passer à `xctrace` :

[^1]:  assurez-vous que `xctrace` pointe bien vers celui de Xcode :
```shell
xcrun --find xctrace
```

```shell
 awk '{print "--env "$0" \\"}' env.dat
```

<br/>

### Modèles

Le modèle le plus couramment utilisé pour le profilage est `Time Profiler`, qui permet de profiler l'utilisation
du CPU.

Pour lister tous les modèles disponibles, utilisez :

```
xcrun xctrace list templates
```

L'option `--template` permet de sélectionner un modèle. Par exemple :

```shell
 --template 'Time Profiler'  
```

<br/>

### Autres options

- `--output` pour spécifier le fichier de sortie des données de trace.
- `--launch` pour spécifier l'application à profiler.
  Cette option doit inclure le chemin vers l'exécutable et peut inclure les options de celui-ci.

<br/>

### Exemple

La commande ci-dessous a été utilisée pour profiler gemc avec le modèle Time Profiler :

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

# Profilage sur Linux avec valgrind
<hr style="height:4px;border:0;background:#4a90e2;">
<br/><br/>

## Prérequis

Assurez-vous que l'exécutable est compilé avec les options suivantes afin d'activer le profilage :

- `-g` : symboles de débogage complets
- `-O2`: optimisation pour que les points chauds soient réalistes
- `-fno-omit-frame-pointer`: nécessaire pour une remontée précise de la pile d'appels
- `-fno-optimize-sibling-calls`: conserve la visibilité des appels terminaux

<br/>

---

<br/>

## Utilisation de Valgrind

Valgrind peut être utilisé pour profiler des applications C++ sous Linux :

```shell
valgrind --tool=callgrind --callgrind-out-file=callgrind.out.%p \
  --dump-instr=yes --skip-plt=yes \
  /path/to/your/application options
```


### Explication des options

- %p est remplacé par le PID, ce qui permet d'en gérer plusieurs
- le relevé des instructions permet de mieux relier le temps passé au temps CPU réel que le simple nombre d'appels.
- skip-plt : 

<br/>

---

<br/>


## Visualisation des résultats

```shell
qcachegrind callgrind.out.<PID>
```

Les actions suivantes peuvent rendre l'affichage plus lisible :

- Clic droit dans Graphe d'appels ▸ Graphe ▸ Coût minimal des nœuds
- Regrouper par nom de classe
- Bouton « % » dans la barre d'outils : relatif au parent

<br/>

---

<br/>
