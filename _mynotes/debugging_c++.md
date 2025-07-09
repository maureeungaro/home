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

## Using lldb

- Start lldb with the executable:
```bash
lldb ./my_executable
```

- Set breakpoints. Can use quotes and parameters or add line numbers, use conditions (-c)
```bash
breakpoint set --name my_function
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- Run the program:
```bash
run <options>
```

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