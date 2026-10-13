---
layout: default
title: "Debugging C++"
permalink: /mynotes/debugging_c++.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# 调试 C++
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## 库依赖

- macOS：使用 `otool -L <executable>` 列出可执行文件链接的共享库。
- Linux：使用 `ldd <executable>` 列出可执行文件链接的共享库。

- `nm <options> <executable/library> | grep LZ4_compress_fast` 用于检查某个特定符号是否
   存在于二进制文件/库中。

   macOS 选项：
     - `-g`：仅显示外部（全局）符号
     - `-U`：不显示未定义符号
     - `-m`：以 Mach-O 风格显示详细信息<br/><br/>

   Linux 选项：
     - `-D`：动态符号（导出接口）
     - `--defined-only`：仅显示库所定义的符号（而非未定义的导入符号）<br/><br/>

   符号类型：
     - `T/t`：已定义的代码段（函数）符号
     - `D/d`：已定义的数据符号
     - `U`：未定义符号

<br/>

# 使用 lldb（macOS）

- 指定可执行文件并启动 lldb：
```shell
lldb my_executable
```

- 设置断点。可以使用引号和参数，或指定行号，也可以使用条件（-c）。
  注意，如果函数位于共享对象中，可能需要先加载共享库（例如通过 `process launch`）。
```shell
break set -n my_function_name
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- 不带参数运行程序：
```shell
run arg1 arg2
```

- 带参数运行程序（更灵活）
```shell
process launch -- arg1 arg2 ...
```

- 将焦点切换到某个栈帧（函数的某次具体调用）
```shell
frame select 1
```
	- `0` 是所选线程在停止时刻当前正在执行的指令指针。
      这通常就是发生故障（或触发异常/断点）的位置。
	- `1` 是栈帧 #0 的直接调用者。
	- `2` 是栈帧 #1 的调用者，依此类推沿调用栈向上。

- 显示程序在崩溃前正在执行的指令。
```shell
disassemble -f
```
<br/>



- 检查/打印变量值：
```shell
frame variable    # show all variables in the current frame
p variable_name   # print a specific variable value
p *variable_name  # if they're pointers
```

- 单步执行代码：
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

# 使用 gdb（Linux）

- 指定可执行文件并启动 gdb：

```shell
gdb my_executable
```

- 设置断点（可以使用函数名、file:line 或条件）：

```shell
break my_function_name
break 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break hipo_output.cc:<line_number>
break GOptions::getVerbosityFor if tag.size() == 0
```

- 设置辅助功能（可能需要逐条输入）

```shell
set pagination off
set print thread-events off

catch throw
catch catch
```

- 带参数运行程序：

```shell
run arg1 arg2 ...
```

- 查看调用栈回溯，检查程序状态

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

- 单步执行代码：

```shell
step     # Step into the next line (enter function)
next     # Step over the next line (skip into function)
finish   # Step out of the current function
```

<br/>
<br/>
<br/>
<br/>
