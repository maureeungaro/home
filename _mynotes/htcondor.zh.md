---
layout: default
title: "HTCondor"
permalink: /mynotes/htcondor.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# HTCondor
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## 检查站点配置

查询收集器，查看资源池中有哪些可用站点，以及这些站点是否提供作业所需的 CVMFS
存储库。下面两条命令会列出各站点的 `GLIDEIN_Site` 以及
`HAS_CVMFS_oasis_opensciencegrid_org` 和 `HAS_CVMFS_jlab_opensciencegrid_org` 标志，然后对
不同的结果行分组并统计数量。

对于 JLab CHTC 资源池，仅查询 `clas12` GlideinWMS 组：

```shell
condor_status -startd -pool jlab-cm.osg.chtc.io -const 'GLIDEClient_Group == "clas12"' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

对于 OSPool：

```shell
condor_status -startd -pool cm-1.ospool.osg-htc.org -const 'OSPool' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

<br/>

## 修改已提交作业的资源要求

编辑提交文件只会影响以后提交的作业。要修改已经在队列中的作业，请以作业所有者的身份，
在提交主机上使用 `condor_qedit`。下面的命令适用于 Bash 和 zsh。
参见 [condor_qedit 参考文档](https://htcondor.readthedocs.io/en/25.x/man-pages/condor_qedit.html)。

诸如 `9291` 这样的作业簇 ID 会选中该簇中所有仍在队列中的子作业；`9291.10` 则只选中子作业 `10`。
如果不指定状态约束，`condor_qedit` 会修改空闲、挂起和运行中的作业。它不会挂起或释放
作业。修改会影响后续的资源匹配，不会影响运行中作业当前的执行或资源分配。

### 检查资源要求和作业状态

`Requirements` 是属性名；在这些检查命令中，不要将其替换为其他值。
使用 `-long` 查看单个作业所存储的表达式：

```shell
condor_q 9291.10 -long -attributes Requirements
```

对于整个作业簇，请同时输出作业 ID（这可能产生大量输出）：

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

直接使用 `-af Requirements` 会对表达式求值，而不是输出其文本。在缺少工作节点
属性的情况下，即使所存储的表达式包含有效的匹配条件，结果也可能是 `false`。
这种输出并不表示所存储的资源要求表达式本身就是 `false`，也不表示作业无法匹配资源。
不要根据这种输出覆盖资源要求。如果 `-long` 显示表达式本身确实为
`false`，那么它确实不会匹配任何工作节点。

要按状态统计作业数量，而不输出数千行内容：

```shell
condor_q 9291 -af JobStatus | sort | uniq -c
```

第一列是数量；第二列是状态：`1` 表示空闲，`2` 表示运行中，`5` 表示挂起。
例如，`2560 1`、`301 2` 和 `1 5` 分别表示 2,560 个空闲作业、301 个运行中作业和 1 个挂起作业。
这些数量不能用于诊断资源要求是否存在问题。

将表达式读入 shell 变量时，请使用 `-af:r Requirements`：其中的 `r` 要求输出未经
求值的原始内容。参见
[condor_q 参考文档](https://htcondor.readthedocs.io/en/24.x/man-pages/condor_q.html)。

### 为作业簇中的所有作业设置资源要求

在决定是否修改之前，请先按上述方法检查所存储的表达式。

下面的命令会为作业簇 `9291` 中每个仍在队列中的作业设置资源要求。它要求工作节点提供 JLab
CVMFS 存储库，并移除之前对 Oasis 可用性和修订版本的要求：

```shell
condor_qedit 9291 Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

双引号和行尾反斜杠会将表达式作为单个参数传递，且不包含实际的换行符。
每个反斜杠都必须位于该行的最末尾，其后不能有空格。不要将双引号
替换为单引号：反斜杠加换行符的续行方式在单引号内不起作用。

这会替换整个表达式。如果原始提交还包含其他资源、体系结构
或文件传输要求，请从提交文件或资源要求完整的等效作业中提取这些条件，并将其包含在表达式中。
上述四个条件不会自动恢复 HTCondor 生成的资源要求。另外，请检查
作业脚本是否使用了预期的 `/cvmfs/` 路径；修改资源要求不会改变这些路径。

验证结果：

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

空闲作业会在下一次资源匹配时使用新的资源要求。挂起作业仍保持挂起状态。运行中的作业会继续
当前这次执行，并在需要再次匹配资源时使用新的资源要求。

只有在打算中断并重新启动运行中作业时，才应在编辑**之前**运行 `condor_hold 9291`，
确认作业已挂起（`JobStatus == 5`），然后在验证修改后运行 `condor_release 9291`。
挂起运行中的作业可能丢失进度或工作节点本地的输出；如果没有检查点机制，作业将从头开始。
挂起空闲作业也能防止它们在一系列修改尚未完成时启动。

### 仅为作业簇中的挂起作业设置资源要求

要让空闲和运行中的作业保持不变，请同时指定作业簇和挂起状态（`JobStatus == 5`）。
预览选中的作业：

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

仅对执行修改时处于挂起状态的作业应用替换：

```shell
condor_qedit -constraint 'ClusterId == 9291 && JobStatus == 5' Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

上文关于完整表达式的注意事项同样适用。无需先挂起整个作业簇：
这条命令只针对已经挂起的作业，并让它们保持挂起状态。验证修改：

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

准备好重试此作业簇中的挂起作业后：

```shell
condor_release -constraint 'ClusterId == 9291 && JobStatus == 5'
```

每条命令都会独立计算其约束条件。如果另一个作业在修改与
释放之间变为挂起状态，释放命令也会选中它。如果需要只释放已修改的那组作业，请使用明确的作业 ID。

下面的内存和站点示例针对单个作业 `8897.10`；请将其替换为目标作业 ID。

### 修改请求的内存大小

如果测得所需内存为 4 GiB，请将 `RequestMemory` 设置为 `4096` MB：

```shell
condor_qedit 8897.10 RequestMemory 4096
condor_q 8897.10 -long -attributes RequestMemory,Requirements
```

通常自动生成的资源要求 `TARGET.Memory >= RequestMemory` 会自动使用更新后的请求值。
如果表达式包含的是固定内存阈值，也请检查该条件。请求更多内存可能
增加等待时间，而且无法修复内存泄漏。它会在下一次资源分配时生效，不会影响
当前这次运行。对于以后的提交，请更新提交文件中的 `request_memory = 4096`。

### 排除有问题的站点

使用资源池公布的准确 `GLIDEIN_Site` 值，如上面的站点查询结果所示。将下面的
`SITE_TO_AVOID` 替换为该值。读取最新表达式，以保留之前的修改：

```bash
requirements=$(condor_q 8897.10 -af:r Requirements)
printf '%s\n' "$requirements"
```

如果查询失败或未返回表达式，请停止操作。然后追加排除条件：

```bash
condor_qedit 8897.10 Requirements \
  "($requirements) && (TARGET.GLIDEIN_Site =!= \"SITE_TO_AVOID\")"
```

ClassAd 运算符 `=!=` 也允许匹配未定义 `GLIDEIN_Site` 的工作节点。要要求站点信息已定义，
请另加一个条件 `!isUndefined(TARGET.GLIDEIN_Site)`。排除站点不会驱逐已在该站点
执行的作业；请使用挂起、编辑、释放的流程，使其在其他站点重新启动。

### 验证并释放

对于单个作业的示例，请检查每次修改是否成功，并查看最终值。只有在
作业处于挂起状态且已准备好重试时，才释放它：

```shell
condor_q 8897.10 -long -attributes JobStatus,Requirements,RequestMemory
condor_release 8897.10
condor_q 8897.10
condor_q 8897.10 -better-analyze
```

作业会重新进入资源匹配流程，并可能等待合适的工作节点。使用 `-better-analyze` 调查
未满足的资源要求。请将相同的预期修改应用到提交文件中，以供以后的作业使用。

<br/>

## 调试挂起作业

在提交主机上运行以下命令，例如 `scosg2202`。将 `8897.10` 替换为
作业的簇 ID 和进程 ID。这些示例针对单个作业，而不是其整个作业簇。

### 查看挂起原因和资源使用情况

```shell
condor_q 8897.10
condor_q 8897.10 -long \
  -attributes JobStatus,HoldReason,HoldReasonCode,HoldReasonSubCode,RequestMemory,MemoryUsage
```

检查 `HoldReason` 时也要检查 `JobStatus`：释放后，之前的挂起原因可能仍然保留。
常见状态值为 `1`（空闲）、`2`（运行中）和 `5`（挂起）。

事件日志记录调度器活动，与应用程序的标准输出和标准错误分开。查找
`012`（挂起）、`013`（释放）、`004`（驱逐）和 `001`（执行）。
发生驱逐后再次执行，并不一定意味着作业曾被挂起。

例如，作业 `8897.10` 在 2026 年 9 月 15 日记录了以下挂起信息：

```text
memory usage exceeded request_memory
Code 21 Subcode 102
Memory (MB): Usage 2440   Request 2311   Allocated 2432
```

该作业的内存使用量超过了分配的额度。释放后，后续的一次执行达到了 17,712 MB，
且在运行过程的大部分时间里，内存持续以每五分钟约 60 MB 的速度增长。这表明可能存在内存
泄漏或数据不断累积，但仅凭事件日志无法确定是哪个程序造成的。
所提供的日志以一次内存更新结束，没有记录第二次挂起。

略微增加请求的内存大小或反复释放作业，都无法解决内存持续
增长的问题。应先确定具体进程和流水线步骤，再测量其内存需求。

### 在作业运行时检查输出

```shell
condor_tail -maxbytes 20000 8897.10
condor_tail -stderr -maxbytes 20000 8897.10
```

查找最后一条 `Running ...` 消息，以确定当前执行的流水线步骤。应用程序的输出缓冲
可能延迟输出。这些命令要求作业正在运行且可以连接；它们无法在某次执行
结束后恢复原工作节点上的文件。

检查队列中作业的实际日志设置：

```shell
condor_q 8897.10 -long \
  -attributes Iwd,Out,Err,WhenToTransferOutput,StreamOut,StreamErr
```

门户目前生成的设置为 `when_to_transfer_output = ON_EXIT`，且未显式启用
标准输出和标准错误的流式传输。在这些设置下，应用程序输出可能一直留在工作节点上，直到作业退出。
因此，调度器的 `.log` 可能持续更新，而本地的 `.out` 和 `.err` 尚不存在或为空。
被中断的一次执行可能不会传回输出。

### 当 condor_tail 无法连接到 starter 时

```text
Failed to peek at file from starter: Failed to connect to starter
```

这表示 `condor_tail` 无法连接到工作节点上的 HTCondor starter。它不能说明
标准输出或标准错误文件是否存在。请以作业所有者的身份，在提交主机上检查当前状态：

```shell
condor_q 8897.10 -long \
  -attributes JobStatus,RemoteHost,LastRemoteHost,HoldReason,RequestMemory,MemoryUsage
tail -80 log/job.8897.10.log
```

请在提交目录中运行 `tail` 命令，或使用事件日志的完整路径。

| JobStatus | 含义 | 下一步 |
| --- | --- | --- |
| `5` | 挂起 | 通常没有正在运行的 starter；为诊断性重试准备日志设置。 |
| `1` | 空闲 | 等待工作节点；当前没有正在执行的作业输出可供检查。 |
| `2` | 运行中 | 尝试访问工作节点，并检查最新事件中是否有连接断开或驱逐记录。 |

对于运行中的作业，请尝试：

```shell
condor_ssh_to_job 8897.10
```

这也可能因相同的连接问题而失败。可能的原因包括工作节点无法访问、
网络或连接代理（CCB）出现问题，或工作节点在调度器
更新作业状态之前就已消失。仅凭连接错误无法区分这些原因。

在挂起或重新启动运行中的作业之前，请记录其状态和最新的事件日志条目：
停止本次执行可能导致无法再访问其当前的临时文件。

如果作业已经挂起，请按照下面的流式传输重试说明操作。流式传输可能在
再次失败之前将输出保存在提交主机上，但仍依赖网络连接和
应用程序的缓冲行为。它无法恢复上一次执行的输出，也无法解决内存增长问题。

### 确定消耗内存的进程

如果站点支持访问运行中的作业：

```shell
condor_ssh_to_job 8897.10
```

在工作节点会话中检查进程，并在一分钟后重复检查：

```shell
ps -eo pid,ppid,rss,vsz,etime,pcpu,args --sort=-rss | head -25
```

`RSS` 是以 KB 为单位的驻留内存；`VSZ` 是以 KB 为单位的虚拟内存。根据 PID、命令和 RSS 的变化，
区分生成器、GEMC、重建程序或其他进程。事件日志中的进程映像大小
与驻留内存不是同一种测量值。

在作业的临时工作目录中，通常可以通过以下方式查看标准输出和标准错误的捕获文件：

```shell
tail -100 _condor_stdout
tail -100 _condor_stderr
```

门户脚本在 `output/` 子目录中运行流水线，而捕获文件通常
保留在其上一级的临时工作目录中。

### 为诊断性重试启用流式传输

对于挂起作业，为下一次执行启用标准输出和标准错误的流式传输：

```shell
condor_qedit 8897.10 StreamOut True
condor_qedit 8897.10 StreamErr True
```

准备好重新启动作业后：

```shell
condor_release 8897.10
```

这会改变日志记录方式，不会改变内存请求或应用程序行为。诊断性重试可能遇到
同样的内存限制；其目的是在失败前捕获当前执行的步骤和输出。
如果应用程序没有检查点机制，流水线将从头开始。

修改原始提交文件不会更新已经在队列中的作业。请使用 `condor_qedit`
修改队列中的作业属性，并用 `condor_q -long` 确认结果。

### 修改 nodescript.sh

编辑提交端的脚本无法改变已经在工作节点上运行的副本。对于后续
执行，普通输入文件可能会重新传输，但 HTCondor 可能已保留提交时的
可执行文件副本。不要指望通过原地编辑 `nodescript.sh` 并释放作业来替换该副本。
编辑共享输入也可能影响之后启动的其他作业。

为了使测试行为可预期，请在单独的目录中准备一次全新的诊断性提交：

1. 复制生成的提交文件、`nodescript.sh`、`functions.sh` 以及其他所有必需的输入文件。
2. 保留失败作业的参数，包括子作业索引 `10` 及其 Lund URI（如果适用）。
   新的单作业提交中，`$(Process) = 0`；复现原作业时，请显式设置原始索引。
3. 将原来的 queue 语句替换为 `queue 1`，并移除对原有 queue 变量的依赖。
4. 检查可执行文件、输入文件、工作目录和日志路径，确保它们指向诊断文件。
5. 将最终上传重定向到单独的目标位置，或禁用上传，以免覆盖现有输出。
6. 在诊断用提交文件中添加以下设置：

```javascript
stream_output = True
stream_error = True
```

要启用 Bash 命令跟踪，请在诊断脚本开头附近、shebang 之后添加：

```bash
PS4='+ ${BASH_SOURCE}:${LINENO}: '
set -x
```

命令跟踪会将命令和展开后的参数写入标准错误。它可以确定调用了哪条命令，但
不会显示已编译程序内部发生的情况。避免跟踪会暴露凭据的命令。

检查诊断文件及其单作业 queue 设置后，在该目录中提交：

```shell
condor_submit debug.condor
```

将新的作业 ID 用于 `condor_tail` 和 `condor_ssh_to_job`。如果内存持续增长，请用
较小的输入复现已确定的流水线命令，并调查该程序的内存使用情况。
