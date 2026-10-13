---
layout: default
title: "Debugging C++"
permalink: /mynotes/debugging_c++.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# C++ のデバッグ
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## ライブラリの依存関係

- macOS: `otool -L <executable>` で、実行ファイルにリンクされている共有ライブラリを一覧表示します。
- Linux: `ldd <executable>` で、実行ファイルにリンクされている共有ライブラリを一覧表示します。

- `nm <options> <executable/library> | grep LZ4_compress_fast` で、特定のシンボルがバイナリ／ライブラリに
   存在するかどうかを確認します。

   macOS のオプション:
     - `-g`: 外部（グローバル）シンボルのみ
     - `-U`: 未定義シンボルを非表示にする
     - `-m`: 詳細な Mach-O 形式の情報<br/><br/>

   Linux のオプション:
     - `-D`: 動的シンボル（エクスポートされたインターフェース）
     - `--defined-only`: ライブラリが定義するシンボルのみ（未定義のインポートは除く）<br/><br/>

   シンボルの種類:
     - `T/t`: テキスト（関数）が定義されている
     - `D/d`: データが定義されている
     - `U`: 未定義

<br/>

# lldb の使用（macOS）

- 実行ファイルを指定して lldb を起動します:
```shell
lldb my_executable
```

- ブレークポイントを設定します。引用符やパラメータ、行番号、条件（-c）を使用できます。
  関数が共有オブジェクト内にある場合は、先に共有ライブラリを読み込む必要があることがあります（例: `process launch` を使用）。
```shell
break set -n my_function_name
break set -n 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break set --file hipo_output.cc --line <line_number>
break set -n "GOptions::getVerbosityFor" -c "tag.size() == 0"
```

- 引数なしでプログラムを実行します:
```shell
run arg1 arg2
```

- 引数を指定してプログラムを実行します（より柔軟）
```shell
process launch -- arg1 arg2 ...
```

- スタックフレーム（特定の関数呼び出し）にフォーカスを移します
```shell
frame select 1
```
	- `0` は、停止時点で選択されているスレッドの、現在実行中の命令ポインタです。
      通常、ここが障害の発生箇所（または例外／ブレークポイントによる停止箇所）です。
	- `1` はフレーム #0 の直接の呼び出し元です。
	- `2` はフレーム #1 の呼び出し元で、以降スタックを上にたどります。

- プログラムがクラッシュする直前に何をしているかを表示します。
```shell
disassemble -f
```
<br/>



- 変数の値を確認／表示します:
```shell
frame variable    # show all variables in the current frame
p variable_name   # print a specific variable value
p *variable_name  # if they're pointers
```

- コードをステップ実行します:
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

# gdb の使用（Linux）

- 実行ファイルを指定して gdb を起動します:

```shell
gdb my_executable
```

- ブレークポイントを設定します（関数名、file:line、または条件を使用可能）:

```shell
break my_function_name
break 'hipo_output::writeHeader(outputContainer*, std::map<std::string, double>, gBank)'
break hipo_output.cc:<line_number>
break GOptions::getVerbosityFor if tag.size() == 0
```

- ユーティリティを設定します（1つずつ入力する必要がある場合があります）

```shell
set pagination off
set print thread-events off

catch throw
catch catch
```

- 引数を指定してプログラムを実行します:

```shell
run arg1 arg2 ...
```

- バックトレースとプログラムの状態を確認します

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

- コードをステップ実行します:

```shell
step     # Step into the next line (enter function)
next     # Step over the next line (skip into function)
finish   # Step out of the current function
```

<br/>
<br/>
<br/>
<br/>
