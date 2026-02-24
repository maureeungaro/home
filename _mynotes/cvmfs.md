---
layout: default
title: "CVMFS on Macos"
---

{% include mynotes.html %}


# CVMFS
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>
<br/>


To use **CernVM File System** mount points on a Mac, two packages are needed:

- [macFuse](https://macfuse.github.io)
- [CernVM-FS](https://cernvm.cern.ch/fs/)

<br/>

> [!IMPORTANT] MacFuse permissions
> During installation a prompt should appear to allow `Ben Fisher` extension. <br/>
> This can also be checked with the command: <br/>
> `sudo kmutil load -p /Library/Filesystems/macfuse.fs/Contents/Extensions/26/macfuse.kext`
> (replace 26 with the OS Versions)<br/>
> If they are not approved to load, go to `Settings > Privacy and Security > Security`, allow and restart.


