---
layout: default
title: "Cernlib on macOS"
permalink: /mynotes/paw_cernlib_macos.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# 在 macOS 上使用 Cernlib 和 Paw
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

下面介绍在 macOS 上通过 Docker 容器运行 Cernlib 的 Paw 的一种快捷方法[^1]。
该方法使用一个基于 Debian 的容器，其中通过系统包管理器（即 apt-get）安装了 paw、paw++ 和 Cernlib。

[^1]: 感谢 [David Lawrence 的原始博客文章](https://davidljlab.wordpress.com/2018/10/03/cernlib-paw-docker/)。

## 环境要求

安装 Docker 和 X11（XQuartz）应用：

- [Docker](https://www.docker.com)
- [XQuartz](https://www.xquartz.org)

安装 XQuartz 后，请务必在“偏好设置 > 安全性”选项卡中启用“Allow connections from network clients”（允许来自网络客户端的连接）。
设置应如下图所示：

{% include figure.html
   src="/assets/images/notes/xquartz.png"
   alt="xquartz security preferences"
   caption="<br/>
   Allow connections from network clients. You may need to 
   restart XQuartz for the change to take effect."
   width="800"
%}

在终端中运行以下命令，以允许来自 Docker 容器的 X11 连接：

```shell
xhost +
```

## 在 Docker 中运行 Paw/Cernlib

在以下说明中，我们假设你使用的是一台
搭载 Apple Silicon CPU（M1/M2/M3 等）的 Mac。
如果你使用的是 Intel CPU，请从下面的 `docker run` 命令中移除 `--platform linux/amd64` 选项。


在终端中运行以下命令，创建一个脚本 `dsh`，用于在容器中启动交互式
shell：

```shell
docker pull jeffersonlab/cernlib:2004
docker run --rm -it --platform linux/amd64 jeffersonlab/cernlib:2004 cat /container/image/dsh | tr -d "\r" > dsh
chmod +x dsh
```

现在你可以在 Docker 中运行 Paw/Cernlib 了。
在终端中运行以下命令，在容器中启动交互式 shell，然后启动 `paw++`：

```shell
./dsh jeffersonlab/cernlib:2004
paw++
```



<br/><br/>

<hr>

<br/><br/>
