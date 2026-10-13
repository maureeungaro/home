---
layout: default
title: "Debugging C++"
permalink: /mynotes/debugging_c++.html
lang: it
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Debug del codice C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## Dipendenze delle librerie

- macOS: `otool -L <executable>` per elencare le librerie condivise collegate a un eseguibile.
- Linux: `ldd <executable>` per elencare le librerie condivise collegate a un eseguibile.

- `nm <options> <executable/library> | grep LZ4_compress_fast` per verificare se un determinato 
   simbolo è presente nel file binario o nella libreria.

   Opzioni per macOS:
     - `-g`: solo simboli esterni (globali) 
     - `-U`: omette i simboli non definiti
     - `-m`: informazioni dettagliate in stile Mach-O<br/><br/>

   Opzioni per Linux:
     - `-D`: simboli dinamici (interfaccia esportata)
     - `--defined-only`: solo i simboli definiti dalla libreria (esclude i simboli importati non definiti)<br/><br/>

   Tipo di simbolo:
     - `T/t`: simbolo definito nella sezione di codice (funzione)
     - `D/d`: simbolo definito nella sezione dati
     - `U`: non definito 

<br/>

# Uso di lldb (macOS)

- Avvia lldb con l'eseguibile:
```shell
lldb my_executable
```

- Imposta i breakpoint. Puoi usare virgolette e parametri, aggiungere numeri di riga o usare condizioni (-c).
  Nota che, se la funzione si trova in un oggetto condiviso, potresti dover caricare prima la libreria condivisa (ad esempio con `process launch`).
```shell
break set -n my_function_name
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- Esegui il programma senza argomenti:
```shell
run arg1 arg2
```

- Esegui il programma con argomenti (più flessibile)
```shell
process launch -- arg1 arg2 ...
```

- Seleziona un frame dello stack (una specifica invocazione di una funzione)
```shell
frame select 1
```
	- `0` corrisponde al puntatore all'istruzione in esecuzione nel thread selezionato al momento dell'arresto.
      In genere è il punto in cui si è verificato l'errore (o è stata sollevata un'eccezione o raggiunto un breakpoint).
	- `1` è il chiamante immediato del frame #0.
	- `2` è il chiamante del frame #1, e così via risalendo lo stack.

- Mostra cosa sta facendo il programma subito prima di terminare in modo anomalo.
```shell
disassemble -f
```
<br/>



- Ispeziona / Stampa i valori delle variabili:
```shell
frame variable    # show all variables in the current frame
p variable_name   # print a specific variable value
p *variable_name  # if they're pointers
```

- Procedi passo passo nel codice:
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

# Uso di gdb (Linux)

- Avvia gdb con l'eseguibile:

```shell
gdb my_executable
```

- Imposta i breakpoint (puoi usare nomi di funzione, file:line o condizioni):

```shell
break my_function_name
break 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break hipo_output.cc:<line_number>
break GOptions::getVerbosityFor if tag.size() == 0
```

- Imposta le opzioni di utilità (potresti dover inserire questi comandi uno alla volta)

```shell
set pagination off
set print thread-events off

catch throw
catch catch
```

- Esegui il programma con argomenti:

```shell
run arg1 arg2 ...
```

- Visualizza il backtrace e ispeziona lo stato del programma

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

- Procedi passo passo nel codice:

```shell
step     # Step into the next line (enter function)
next     # Step over the next line (skip into function)
finish   # Step out of the current function
```

<br/>
<br/>
<br/>
<br/>
