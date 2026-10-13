---
layout: default
title: Docker, Apptainer
permalink: /mynotes/docker.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# Docker 与 Apptainer
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

使用 Docker 运行 Docker 镜像：

```shell
docker run -it --rm <image> command
```

其中：

- `-it`：让你能够像操作 shell 一样与容器交互
- `--rm`：容器退出时自动将其删除。
- `command`：在容器内运行的命令，通常为 `bash`

通过 `-v` 绑定可以将本地目录挂载到容器中以实现持久化存储。
例如，下面的命令会让本地的 `~/mywork` 以 `/usr/local/mywork` 的形式在容器中可用：

```shell
docker run -it --rm  -v ~/mywork:/usr/local/mywork <image> command
```

<br/>

## 常用命令

Dockerfile 关键字 `CMD` 可以指向一个脚本，如果未在
Docker `run` 命令中指定要执行的命令，该脚本就会运行。

关键字 `ENTRYPOINT` 定义了一个始终会在容器中运行的脚本，
无论是否指定 `command` 参数。

可以在运行时用下面的选项覆盖入口点（此处以 `sh` 为例）：

```shell
--entrypoint /bin/sh
```
<br/>

### 检查镜像：

```shell
docker image inspect <image> 
```

<br/><br/>

## Apptainer

Linux 主机上提供了 `apptainer`（原名 Singularity），其用法与 Docker 类似。
它使用一个缓存目录来存储镜像，因此我建议将该缓存设置到
磁盘容量较大的位置。在下面的示例中使用 `/path/to/user/cache`：

```shell
export sif_cache=/path/to/$USER/sif
```

然后：

```shell
export APPTAINER_CACHEDIR=$sif_cache/apptainer-cache 
export APPTAINER_TMPDIR=$sif_cache/apptainer-tmp 
export TMPDIR=$sif_cache/apptainer-tmp 

apptainer exec --cleanenv --bind ~/mywork:/usr/local/mywork \
  <image> command
```



<br/>
<br/>
<br/>
<br/>
