---
layout: default
title: "Profiling C++"
---

{% include mynotes.html %}

---

<br/>


# Debugging C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/><br/>

## Library dependencies

- `otool -L <executable>` to list shared libraries linked to an executable.
- `nm <executable> | grep LZ4_compress_fast` to check if a specific 
   symbol is present in the binary.
- `nm -u <executable> ` to list undefined symbols in the binary. 
   Notice: this may include symbols from libraries that are not linked to the binary, 
   but are available in the system.

<br/>

# Using lldb (MacOS)

- Start lldb with the executable:
```bash
lldb my_executable
```

- Set breakpoints. Can use quotes and parameters or add line numbers, use conditions (-c)
  Notice that if the function is inside a shared object, you may need to load the shared library first (e.g. with `process launch`).
```bash
break set -n my_function_name
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- Run the program with arguments[^1]:
```bash
process launch -- arg1 arg2 ...
```

[^1]: For simpler lldb options `run arg1 arg2` also works, but `process launch` is more flexible.

- Step through the code:
```bash
step        # or just 's'. Step into the next line of code
next        # or just 'n'. Step over the next line of code
frame info  # Show current frame information
list        # Show the current source code around the current line
bt          # Backtrace to see the call stack
finish      # Step out of the current function
```

- Inspect / Print variable values:
```bash
frame variable    # show all variables in the current frame
p variable_name   # print a specific variable value
p *variable_name  # if they're pointers
```


<br/>

# Using gdb (Linux)

- Start gdb with the executable:

```bash
gdb my_executable
```

- Set breakpoints (can use function names, file:line, or conditions):


```bash
break my_function_name
break 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break hipo_output.cc:<line_number>
break GOptions::getVerbosityFor if tag.size() == 0
```

- Run the program with arguments:

```bash
run arg1 arg2 ...
```

- Step through the code:

```bash
step     # Step into the next line (enter function)
next     # Step over the next line (skip into function)
finish   # Step out of the current function
```

- Inspect program state:

```bash
backtrace       # Show call stack
info locals     # Show local variables
info args       # Show function arguments
print var       # Print value of variable
print *ptr      # Dereference a pointer
list            # Show source around current line
```


<br/>
<br/>
<br/>
<br/>
