---
layout: default
title: "Profiling C++"
permalink: /mynotes/profiling_c++.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# 在 macOS 上使用 Instruments 和 xctrace 进行性能分析
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

### 环境变量

环境变量通过 `--env` 选项传递给 `xctrace`[^1] 命令。
给定一个包含环境变量设置的文件 `env.dat`（例如来自 `export` 的输出），
可以使用下面的一行命令来生成需要传递给 `xctrace` 的选项：

[^1]:  请确保 `xctrace` 指向 Xcode 自带的版本：
```shell
xcrun --find xctrace
```

```shell
 awk '{print "--env "$0" \\"}' env.dat
```

<br/>

### 模板

最常用的性能分析模板是 `Time Profiler`，可用于分析 CPU 使用情况。

要列出所有可用的模板，请使用：

```
xcrun xctrace list templates
```

可以使用 `--template` 选项来选择模板。例如：

```shell
 --template 'Time Profiler'  
```

<br/>

### 其他选项

- `--output` 用于指定跟踪数据的输出文件。
- `--launch` 用于指定要分析的应用程序。
  必须提供可执行文件的路径，也可以包含该应用程序的选项。

<br/>

### 示例

下面的命令曾用于使用 Time Profiler 模板对 gemc 进行性能分析：

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

# 在 Linux 上使用 valgrind 进行性能分析
<hr style="height:4px;border:0;background:#4a90e2;">
<br/><br/>

## 前置条件

请确保可执行文件使用以下标志编译，以启用性能分析：

- `-g` : 完整的符号信息
- `-O2`: 进行优化，使热点更贴近真实情况
- `-fno-omit-frame-pointer`: 准确的栈展开所需
- `-fno-optimize-sibling-calls`:  保持尾调用可见

<br/>

---

<br/>

## 使用 Valgrind

Valgrind 可用于在 Linux 上对 C++ 应用程序进行性能分析：

```shell
valgrind --tool=callgrind --callgrind-out-file=callgrind.out.%p \
  --dump-instr=yes --skip-plt=yes \
  /path/to/your/application options
```


### 选项说明

- %p 会展开为 PID，因此可以支持多个
- 指令转储比原始调用计数更能将耗时与真实的 CPU 时间关联起来。
- skip-plt: 

<br/>

---

<br/>


## 查看结果

```shell
qcachegrind callgrind.out.<PID>
```

以下操作可以让输出更易读：

- 在 Call Graph 中右击 ▸Graph ▸Min node cost
- 按类名分组
- 工具栏中的 “%” 按钮：相对于父级显示

<br/>

---

<br/>
