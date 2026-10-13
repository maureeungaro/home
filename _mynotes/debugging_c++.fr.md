---
layout: default
title: "Debugging C++"
permalink: /mynotes/debugging_c++.html
lang: fr
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Débogage en C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## Dépendances en bibliothèques

- macOS : `otool -L <executable>` pour lister les bibliothèques partagées liées à un exécutable.
- Linux : `ldd <executable>` pour lister les bibliothèques partagées liées à un exécutable.

- `nm <options> <executable/library> | grep LZ4_compress_fast` pour vérifier si un symbole particulier
   est présent dans le binaire ou la bibliothèque.

   Options macOS :
     - `-g` : uniquement les symboles externes (globaux)
     - `-U` : ne pas afficher les symboles non définis
     - `-m` : informations détaillées au format Mach-O<br/><br/>

   Options Linux :
     - `-D` : symboles dynamiques (interface exportée)
     - `--defined-only` : uniquement les symboles définis par la bibliothèque (sans les symboles importés non définis)<br/><br/>

   Type de symbole :
     - `T/t` : symbole défini dans la section de code (fonction)
     - `D/d` : symbole de données défini
     - `U` : non défini

<br/>

# Utilisation de lldb (macOS)

- Démarrer lldb avec l'exécutable :
```shell
lldb my_executable
```

- Définir des points d'arrêt. Utiliser des guillemets et des paramètres, des numéros de ligne ou des conditions (-c)
  Si la fonction se trouve dans un objet partagé, il peut être nécessaire de charger d'abord la bibliothèque partagée (par exemple avec `process launch`).
```shell
break set -n my_function_name
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- Lancer le programme sans arguments :
```shell
run arg1 arg2
```

- Lancer le programme avec des arguments (plus flexible)
```shell
process launch -- arg1 arg2 ...
```

- Sélectionner un cadre de pile (une invocation particulière d'une fonction)
```shell
frame select 1
```
	- `0` correspond au pointeur d'instruction courant du thread sélectionné au moment de l'arrêt.
      C'est généralement là que l'erreur s'est produite (ou qu'une exception a été levée ou un point d'arrêt atteint).
	- `1` est l'appelant immédiat du cadre de pile nº 0.
	- `2` est l'appelant du cadre de pile nº 1, et ainsi de suite en remontant la pile.

- afficher ce qu'il fait juste avant de planter.
```shell
disassemble -f
```
<br/>



- Inspecter / afficher les valeurs des variables :
```shell
frame variable    # show all variables in the current frame
p variable_name   # print a specific variable value
p *variable_name  # if they're pointers
```

- Parcourir le code pas à pas :
```shell
step        # or just 's'. Step into the next line of code
next        # or just 'n'. Step over the next line of code
frame info  # Show current frame information
list        # Show the current source code around the current line
bt          # Backtrace to see the call stack
bt all      # Full backtrace with arguments
finish      # Step out of the current function
```

<br/>

# Utilisation de gdb (Linux)

- Démarrer gdb avec l'exécutable :

```shell
gdb my_executable
```

- Définir des points d'arrêt (on peut utiliser des noms de fonction, file:line ou des conditions) :

```shell
break my_function_name
break 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break hipo_output.cc:<line_number>
break GOptions::getVerbosityFor if tag.size() == 0
```

- Configurer les outils (il peut être nécessaire de saisir ces commandes une par une)

```shell
set pagination off
set print thread-events off

catch throw
catch catch
```

- Lancer le programme avec des arguments :

```shell
run arg1 arg2 ...
```

- Afficher la pile des appels et inspecter l'état du programme

```shell
backtrace       # Show call stack
bt full
thread apply all bt full
info threads
frame N         # Change focus to a stack frame
info locals     # Show local variables
info args       # Show function arguments
print var       # Print value of variable
print *ptr      # Dereference a pointer
list            # Show source around current line
```

- Parcourir le code pas à pas :

```shell
step     # Step into the next line (enter function)
next     # Step over the next line (skip into function)
finish   # Step out of the current function
```

<br/>
<br/>
<br/>
<br/>
