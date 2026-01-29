---
layout: default
title: "Profiling C++"
---

{% include mynotes.html %}


# Debugging C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## Library dependencies

- macOS: `otool -L <executable>` to list shared libraries linked to an executable.
- Linux: `ldd <executable>` to list shared libraries linked to an executable.

- `nm <options> <executable/library> | grep LZ4_compress_fast` to check if a specific 
   symbol is present in the binary/library.

   MacOS options:
     - `-g`: external (global) symbols only 
     - `-U`: undefined symbols suppressed
     - `-m`: verbose Mach-O style info<br/><br/>

   Linux options:
     - `-D`: dynamic symbols (exported interface)
     - `--defined-only`: only symbols the library defines (not undefined imports)<br/><br/>

   Type of Symbol:
     - `T/t`: text (function) defined
     - `D/d`: data defined
     - `U`: undefined 

<br/>

# Using lldb (MacOS)

- Start lldb with the executable:
```shell
lldb my_executable
```

- Set breakpoints. Can use quotes and parameters or add line numbers, use conditions (-c)
  Notice that if the function is inside a shared object, you may need to load the shared library first (e.g. with `process launch`).
```shell
break set -n my_function_name
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- Run the program without arguments:
```shell
run arg1 arg2
```

- Run the program with arguments (more flexible)
```shell
process launch -- arg1 arg2 ...
```

- Change focus to a stack frame (a specific invocation of a function)
```shell
frame select 1
```
	- `0` is the currently executing instruction pointer for the selected thread at the stop moment.
      That is typically where the fault occurred (or where an exception/breakpoint was raised).
	- `1` is the immediate caller of frame #0.
	- `2` is the caller of frame #1, and so on up the stack.

<br/>



- Inspect / Print variable values:
```shell
frame variable    # show all variables in the current frame
p variable_name   # print a specific variable value
p *variable_name  # if they're pointers
```

- Step through the code:
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

# Using gdb (Linux)

- Start gdb with the executable:

```shell
gdb my_executable
```

- Set breakpoints (can use function names, file:line, or conditions):

```shell
break my_function_name
break 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break hipo_output.cc:<line_number>
break GOptions::getVerbosityFor if tag.size() == 0
```

- Set utilities (may have to entere these one by one)

```shell
set pagination off
set print thread-events off

catch throw
catch catch
```

- Run the program with arguments:

```shell
run arg1 arg2 ...
```

- Backtrace, inspect program state

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

- Step through the code:

```shell
step     # Step into the next line (enter function)
next     # Step over the next line (skip into function)
finish   # Step out of the current function
```

<br/>
<br/>
<br/>
<br/>
