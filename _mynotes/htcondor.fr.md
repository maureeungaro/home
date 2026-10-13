---
layout: default
title: "HTCondor"
permalink: /mynotes/htcondor.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# HTCondor
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## Vérification des configurations des sites

Interrogez le collecteur pour voir quels sites sont disponibles dans un pool et s'ils donnent accès aux dépôts
CVMFS dont les jobs ont besoin. Les deux commandes ci-dessous indiquent, pour chaque site, son `GLIDEIN_Site`
ainsi que les indicateurs `HAS_CVMFS_oasis_opensciencegrid_org` et `HAS_CVMFS_jlab_opensciencegrid_org`, puis
regroupent les lignes distinctes en indiquant leur nombre d'occurrences.

Pour le pool CHTC de JLab, restreint au groupe GlideinWMS `clas12` :

```shell
condor_status -startd -pool jlab-cm.osg.chtc.io -const 'GLIDEClient_Group == "clas12"' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

Pour l'OSPool :

```shell
condor_status -startd -pool cm-1.ospool.osg-htc.org -const 'OSPool' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

<br/>

## Modification des exigences des jobs soumis

La modification d'un fichier de soumission n'affecte que les soumissions futures. Utilisez `condor_qedit`
sur l'hôte de soumission, en tant que propriétaire du job, pour modifier les jobs déjà dans la file d'attente.
Les commandes ci-dessous fonctionnent sous Bash et zsh.
Consultez la [référence de condor_qedit](https://htcondor.readthedocs.io/en/25.x/man-pages/condor_qedit.html).

Un identifiant de cluster tel que `9291` sélectionne tous ses sous-jobs présents dans la file d'attente ;
`9291.10` sélectionne uniquement le sous-job `10`.
Sans contrainte de statut, `condor_qedit` modifie les jobs en attente, bloqués et en cours d'exécution. Il
ne bloque ni ne débloque les jobs. Les changements affectent les appariements ultérieurs, mais pas l'exécution
ou l'allocation de ressources en cours d'un job.

### Inspecter les exigences et le statut d'un job

`Requirements` est le nom de l'attribut ; ne le remplacez pas par une autre valeur dans ces commandes
d'inspection. Utilisez `-long` pour voir l'expression stockée pour un job :

```shell
condor_q 9291.10 -long -attributes Requirements
```

Pour l'ensemble du cluster, incluez les identifiants des jobs (cela peut produire une sortie volumineuse) :

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

Un simple `-af Requirements` évalue l'expression au lieu d'en afficher le texte. Sans les attributs d'un
nœud de calcul, le résultat peut valoir `false` même lorsque l'expression stockée contient des conditions
d'appariement valides. Cette sortie ne signifie pas que les exigences stockées valent littéralement `false`,
ni que les jobs ne peuvent pas être appariés à un nœud. Ne remplacez pas les exigences sur la base de cette
sortie. Si `-long` montre que l'expression elle-même vaut littéralement `false`, alors elle ne correspond
à aucun nœud de calcul.

Pour compter les jobs par statut sans afficher des milliers de lignes :

```shell
condor_q 9291 -af JobStatus | sort | uniq -c
```

La première colonne est le nombre de jobs ; la seconde est le statut : `1` signifie en attente, `2` en cours
d'exécution et `5` bloqué. Par exemple, `2560 1`, `301 2` et `1 5` signifient 2 560 jobs en attente,
301 jobs en cours d'exécution et un job bloqué. Ces décomptes ne permettent pas de diagnostiquer un problème
d'exigences.

Lorsque vous lisez une expression dans une variable shell, utilisez `-af:r Requirements` : le `r` demande
une sortie brute, non évaluée. Consultez la
[référence de condor_q](https://htcondor.readthedocs.io/en/24.x/man-pages/condor_q.html).

### Définir les exigences pour tous les jobs d'un cluster

Inspectez les expressions stockées ci-dessus avant de décider de les modifier.

La commande suivante définit les exigences pour chaque job présent dans la file d'attente du cluster `9291`.
Elle exige le dépôt CVMFS de JLab et supprime les anciennes exigences de disponibilité et de révision d'Oasis :

```shell
condor_qedit 9291 Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

Les guillemets doubles et les barres obliques inverses en fin de ligne transmettent l'expression comme un seul
argument, sans sauts de ligne littéraux. Placez chaque barre oblique inverse tout à la fin de sa ligne, sans
espaces après elle. Ne remplacez pas les guillemets doubles par des guillemets simples : la continuation de
ligne par une barre oblique inverse suivie d'un saut de ligne ne fonctionne pas entre guillemets simples.

Cela remplace l'expression entière. Si la soumission d'origine comportait des exigences supplémentaires de
ressources, d'architecture ou de transfert de fichiers, reprenez ces clauses depuis la soumission ou un job
équivalent intact. Les quatre clauses ci-dessus ne restaurent pas automatiquement les exigences générées par
HTCondor. Vérifiez également que les scripts du job utilisent les chemins `/cvmfs/` prévus ; modifier les
exigences ne change pas ces chemins.

Vérifiez le résultat :

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

Les jobs en attente utilisent les nouvelles exigences lors de leur prochain appariement. Les jobs bloqués
restent bloqués. Les jobs en cours d'exécution poursuivent leur tentative actuelle et utilisent les nouvelles
exigences s'ils ont besoin d'un nouvel appariement.

Uniquement si vous avez l'intention d'interrompre et de relancer des jobs en cours d'exécution, exécutez
`condor_hold 9291` **avant** la modification, confirmez que les jobs sont bloqués (`JobStatus == 5`), puis
exécutez `condor_release 9291` après avoir vérifié les modifications. Bloquer des jobs en cours d'exécution
peut entraîner la perte du travail effectué ou des sorties stockées localement sur le nœud de calcul ; sans
points de reprise, attendez-vous à un redémarrage. Bloquer des jobs en attente les empêche aussi de démarrer
pendant une série de modifications.

### Définir les exigences uniquement pour les jobs bloqués d'un cluster

Pour laisser les jobs en attente et en cours d'exécution inchangés, sélectionnez à la fois le cluster et le
statut bloqué (`JobStatus == 5`). Affichez les jobs sélectionnés :

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

Appliquez le remplacement uniquement aux jobs bloqués au moment de la modification :

```shell
condor_qedit -constraint 'ClusterId == 9291 && JobStatus == 5' Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

Les mêmes considérations sur le remplacement de l'expression entière évoquées ci-dessus s'appliquent. Vous
n'avez pas besoin de bloquer le cluster au préalable : cette commande cible les jobs déjà bloqués et les
laisse bloqués. Vérifiez les modifications :

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

Lorsque vous êtes prêt à relancer les jobs bloqués de ce cluster :

```shell
condor_release -constraint 'ClusterId == 9291 && JobStatus == 5'
```

Chaque commande évalue sa contrainte indépendamment. Si un autre job devient bloqué entre la modification
et le déblocage, la commande de déblocage le sélectionne aussi. Utilisez des identifiants de job explicites
si vous devez débloquer exactement l'ensemble modifié.

Les exemples de mémoire et de site ci-dessous ciblent un seul job, `8897.10` ; remplacez-le par
l'identifiant du job visé.

### Modifier la mémoire demandée

Pour un besoin mesuré de 4 Gio, réglez `RequestMemory` sur `4096` Mo :

```shell
condor_qedit 8897.10 RequestMemory 4096
condor_q 8897.10 -long -attributes RequestMemory,Requirements
```

L'exigence générée habituelle, `TARGET.Memory >= RequestMemory`, utilise automatiquement la demande mise à
jour. Si l'expression contient plutôt un seuil de mémoire fixe, examinez également cette clause. Une demande
plus importante peut augmenter le temps d'attente et ne corrige pas une fuite mémoire. Elle prend effet lors
de la prochaine allocation, pas pour la tentative en cours d'exécution. Pour les soumissions futures,
mettez à jour `request_memory = 4096` dans le fichier de soumission.

### Exclure un site problématique

Utilisez la valeur `GLIDEIN_Site` exacte annoncée par le pool, telle qu'affichée dans les requêtes sur les
sites ci-dessus. Remplacez `SITE_TO_AVOID` ci-dessous par cette valeur. Lisez l'expression la plus récente
afin de préserver les modifications précédentes :

```bash
requirements=$(condor_q 8897.10 -af:r Requirements)
printf '%s\n' "$requirements"
```

Arrêtez-vous si la requête a échoué ou n'a renvoyé aucune expression. Ajoutez ensuite l'exclusion :

```bash
condor_qedit 8897.10 Requirements \
  "($requirements) && (TARGET.GLIDEIN_Site =!= \"SITE_TO_AVOID\")"
```

L'opérateur ClassAd `=!=` autorise aussi les nœuds de calcul où `GLIDEIN_Site` est indéfini. Pour exiger un
site connu, incluez `!isUndefined(TARGET.GLIDEIN_Site)` comme clause supplémentaire. Exclure un site n'évince
pas une tentative en cours sur ce site ; utilisez la procédure de blocage, modification et déblocage pour
la relancer ailleurs.

### Vérifier et débloquer

Pour les exemples portant sur un seul job, vérifiez que chaque modification a réussi et inspectez les
valeurs finales. Ne débloquez le job que s'il est bloqué et que vous êtes prêt à le relancer :

```shell
condor_q 8897.10 -long -attributes JobStatus,Requirements,RequestMemory
condor_release 8897.10
condor_q 8897.10
condor_q 8897.10 -better-analyze
```

Le job revient dans le processus d'appariement et peut attendre un nœud de calcul approprié. Utilisez
`-better-analyze` pour examiner les exigences non satisfaites. Appliquez les mêmes modifications souhaitées
au fichier de soumission pour les jobs futurs.

<br/>

## Débogage des jobs bloqués

Exécutez les commandes suivantes sur l'hôte de soumission, tel que `scosg2202`. Remplacez `8897.10` par
l'identifiant de cluster et de processus du job. Ces exemples ciblent un seul job, pas l'ensemble de son
cluster.

### Lire le motif du blocage et l'utilisation des ressources

```shell
condor_q 8897.10
condor_q 8897.10 -long \
  -attributes JobStatus,HoldReason,HoldReasonCode,HoldReasonSubCode,RequestMemory,MemoryUsage
```

Vérifiez `JobStatus` en même temps que `HoldReason` : un motif de blocage antérieur peut subsister après un
déblocage. Les valeurs de statut courantes sont `1` (en attente), `2` (en cours d'exécution) et `5` (bloqué).

Le journal d'événements enregistre l'activité de l'ordonnanceur séparément des flux stdout et stderr de
l'application. Recherchez `012` (bloqué), `013` (débloqué), `004` (évincé) et `001` (en exécution).
Une éviction suivie d'une autre exécution n'est pas nécessairement un blocage.

Par exemple, le job `8897.10` a enregistré ce blocage le 15 septembre 2026 :

```text
memory usage exceeded request_memory
Code 21 Subcode 102
Memory (MB): Usage 2440   Request 2311   Allocated 2432
```

Le job a dépassé son allocation mémoire. Après déblocage, une tentative ultérieure a atteint 17 712 Mo,
avec une augmentation soutenue d'environ 60 Mo toutes les cinq minutes pendant une grande partie de
l'exécution. Cela suggère une fuite mémoire ou une accumulation de données, mais le journal d'événements
seul ne peut pas identifier le programme responsable. Le journal fourni se terminait par une mise à jour
de l'utilisation mémoire, et non par un second blocage.

Augmenter légèrement la demande ou débloquer le job de façon répétée ne résout pas une augmentation soutenue
de l'utilisation mémoire. Identifiez d'abord le processus et l'étape du pipeline, puis mesurez ses besoins
en mémoire.

### Inspecter la sortie pendant l'exécution du job

```shell
condor_tail -maxbytes 20000 8897.10
condor_tail -stderr -maxbytes 20000 8897.10
```

Recherchez le dernier message `Running ...` pour identifier l'étape active du pipeline. La mise en tampon
de l'application peut retarder la sortie. Ces commandes nécessitent un job en cours d'exécution et
joignable ; elles ne récupèrent pas les fichiers d'un ancien nœud de calcul après la fin de cette tentative.

Vérifiez les paramètres de journalisation effectifs du job présent dans la file d'attente :

```shell
condor_q 8897.10 -long \
  -attributes Iwd,Out,Err,WhenToTransferOutput,StreamOut,StreamErr
```

Le portail génère actuellement `when_to_transfer_output = ON_EXIT` et n'active pas explicitement la
transmission en continu de stdout/stderr. Avec ces paramètres, la sortie de l'application peut rester sur
le nœud de calcul jusqu'à la fin de l'exécution. Le `.log` de l'ordonnanceur peut donc continuer à se mettre
à jour tandis que `.out` et `.err` sont absents ou vides localement. Une tentative interrompue peut ne pas
renvoyer sa sortie.

### Lorsque condor_tail ne peut pas se connecter au starter

```text
Failed to peek at file from starter: Failed to connect to starter
```

Cela signifie que `condor_tail` ne peut pas joindre le starter HTCondor du nœud de calcul. Cela ne permet
pas de déterminer si les fichiers stdout ou stderr existent. Sur l'hôte de soumission, en tant que
propriétaire du job, vérifiez l'état actuel :

```shell
condor_q 8897.10 -long \
  -attributes JobStatus,RemoteHost,LastRemoteHost,HoldReason,RequestMemory,MemoryUsage
tail -80 log/job.8897.10.log
```

Exécutez la commande `tail` depuis le répertoire de soumission, ou utilisez le chemin complet vers son
journal d'événements.

| JobStatus | Signification | Étape suivante |
| --- | --- | --- |
| `5` | Bloqué | Il n'y a généralement pas de starter en cours d'exécution ; préparez la journalisation pour une nouvelle tentative de diagnostic. |
| `1` | En attente | Attendez un nœud de calcul ; il n'y a pas de sortie en cours à inspecter. |
| `2` | En cours d'exécution | Essayez d'accéder au nœud de calcul et recherchez une déconnexion ou une éviction dans les derniers événements. |

Pour un job en cours d'exécution, essayez :

```shell
condor_ssh_to_job 8897.10
```

Cela peut échouer pour la même raison de connectivité. Les causes possibles incluent un nœud de calcul
injoignable, un problème de réseau ou de courtier de connexions (CCB), ou un nœud de calcul qui a disparu
avant que l'ordonnanceur n'ait mis à jour l'état du job. L'erreur de connexion seule ne permet pas de
distinguer ces causes.

Enregistrez le statut et les dernières entrées du journal d'événements avant de bloquer ou de relancer un
job en cours d'exécution : arrêter la tentative peut faire perdre l'accès à ses fichiers temporaires actuels.

Si le job est déjà bloqué, suivez les instructions de relance avec transmission en continu ci-dessous.
La transmission en continu peut préserver la sortie sur l'hôte de soumission avant un nouvel échec, mais
dépend toujours de la connectivité et de la mise en tampon de l'application. Elle ne peut pas récupérer
la sortie de la tentative précédente ni corriger l'augmentation de l'utilisation mémoire.

### Identifier le processus qui consomme la mémoire

Si le site prend en charge l'accès aux jobs en cours d'exécution :

```shell
condor_ssh_to_job 8897.10
```

Dans la session sur le nœud de calcul, inspectez les processus et recommencez après une minute :

```shell
ps -eo pid,ppid,rss,vsz,etime,pcpu,args --sort=-rss | head -25
```

`RSS` est la mémoire résidente en Ko ; `VSZ` est la mémoire virtuelle en Ko. Utilisez le PID, la commande et
l'évolution de RSS pour distinguer le générateur, GEMC, la reconstruction ou un autre processus. La taille
de l'image du processus dans le journal d'événements n'est pas la même mesure que la mémoire résidente.

Dans le répertoire temporaire du job, les fichiers de capture stdout/stderr sont généralement accessibles
comme suit :

```shell
tail -100 _condor_stdout
tail -100 _condor_stderr
```

Le script du portail exécute son pipeline dans un sous-répertoire `output/`, tandis que les fichiers de
capture restent normalement dans le répertoire temporaire parent.

### Activer la transmission en continu pour une nouvelle tentative de diagnostic

Pour un job bloqué, activez la transmission en continu de stdout/stderr pour la prochaine tentative :

```shell
condor_qedit 8897.10 StreamOut True
condor_qedit 8897.10 StreamErr True
```

Lorsque vous êtes prêt à relancer le job :

```shell
condor_release 8897.10
```

Cela change la journalisation, pas la demande de mémoire ni le comportement de l'application. La nouvelle
tentative de diagnostic peut atteindre la même limite de mémoire ; son but est de capturer l'étape active
et la sortie avant l'échec. Sans points de reprise dans l'application, attendez-vous à ce que le pipeline
recommence depuis le début.

Modifier le fichier de soumission d'origine ne met pas à jour un job déjà présent dans la file d'attente.
Utilisez `condor_qedit` pour les attributs des jobs dans la file, et confirmez le résultat avec `condor_q -long`.

### Modification de nodescript.sh

Modifier le script côté soumission ne peut pas changer la copie déjà en cours d'exécution sur un nœud de
calcul. Pour une tentative ultérieure, les fichiers d'entrée ordinaires peuvent être transférés à nouveau,
mais HTCondor peut avoir conservé une copie de l'exécutable fournie lors de la soumission. Ne comptez pas
sur la modification de `nodescript.sh` sur place suivie d'un déblocage pour le remplacer. Modifier des
entrées partagées peut aussi affecter d'autres jobs qui démarrent par la suite.

Pour un test au comportement prévisible, préparez une nouvelle soumission de diagnostic dans un répertoire
séparé :

1. Copiez le fichier de soumission généré, `nodescript.sh`, `functions.sh` et toutes les autres entrées requises.
2. Conservez les arguments du job défaillant, y compris l'indice du sous-job `10` et son URI Lund le cas échéant.
   Une nouvelle soumission à un seul job a `$(Process) = 0` ; définissez explicitement l'indice d'origine
   lorsque vous reproduisez le problème.
3. Remplacez l'instruction de mise en file d'origine par `queue 1`, et supprimez les dépendances à ses anciennes
   variables de mise en file.
4. Vérifiez les chemins de l'exécutable, des entrées, du répertoire de travail et des journaux pour qu'ils
   pointent vers les fichiers de diagnostic.
5. Redirigez le transfert final vers une destination séparée, ou désactivez-le, pour éviter de remplacer
   la sortie existante.
6. Ajoutez les paramètres suivants au fichier de soumission de diagnostic :

```javascript
stream_output = True
stream_error = True
```

Pour le traçage des commandes Bash, ajoutez ceci près du début du script de diagnostic, après le shebang :

```bash
PS4='+ ${BASH_SOURCE}:${LINENO}: '
set -x
```

Le traçage écrit les commandes et les arguments après expansion sur stderr. Il identifie la commande
invoquée mais ne montre pas ce qui se passe à l'intérieur d'un programme compilé. Évitez de tracer des
commandes qui exposent des informations d'authentification.

Après avoir vérifié le fichier de diagnostic et sa mise en file d'un seul job, soumettez depuis ce répertoire :

```shell
condor_submit debug.condor
```

Utilisez le nouvel identifiant de job avec `condor_tail` et `condor_ssh_to_job`. Si l'utilisation mémoire
continue d'augmenter, reproduisez la commande du pipeline identifiée avec une entrée plus petite et
examinez l'utilisation mémoire de ce programme.
