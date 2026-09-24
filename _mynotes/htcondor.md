---
layout: default
title: "HTCondor"
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# HTCondor
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## Checking site configurations

Query the collector to see which sites are available in a pool and whether they expose the CVMFS
repositories the jobs need. The two commands below report each site's `GLIDEIN_Site` along with the
`HAS_CVMFS_oasis_opensciencegrid_org` and `HAS_CVMFS_jlab_opensciencegrid_org` flags, then group the
distinct rows with a count.

For the JLab CHTC pool, restricted to the `clas12` GlideinWMS group:

```shell
condor_status -startd -pool jlab-cm.osg.chtc.io -const 'GLIDEClient_Group == "clas12"' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

For the OSPool:

```shell
condor_status -startd -pool cm-1.ospool.osg-htc.org -const 'OSPool' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

<br/>

## Debugging held jobs

Run the following commands on the submission host, such as `scosg2202`. Replace `8897.10` with the
job's cluster and process ID. These examples target one job, not its entire cluster.

### Read the hold reason and resource usage

```shell
condor_q 8897.10
condor_q 8897.10 -long \
  -attributes JobStatus,HoldReason,HoldReasonCode,HoldReasonSubCode,RequestMemory,MemoryUsage
```

Check `JobStatus` along with `HoldReason`: a previous hold reason may remain after a release.
Common status values are `1` (idle), `2` (running), and `5` (held).

The event log records scheduler activity separately from application stdout and stderr. Look for
`012` (held), `013` (released), `004` (evicted), and `001` (executing).
An eviction followed by another execution is not necessarily a hold.

For example, job `8897.10` recorded this hold on September 15, 2026:

```text
memory usage exceeded request_memory
Code 21 Subcode 102
Memory (MB): Usage 2440   Request 2311   Allocated 2432
```

The job exceeded its memory allocation. After release, a later attempt reached 17,712 MB, with
sustained growth of roughly 60 MB every five minutes for much of the run. This suggests a memory
leak or accumulating data, but the event log alone cannot identify the responsible program.
The supplied log ended with a memory update, not a second hold.

Increasing the request slightly or repeatedly releasing the job does not resolve sustained memory
growth. Identify the process and pipeline step first, then measure its memory requirements.

### Inspect output while the job is running

```shell
condor_tail -maxbytes 20000 8897.10
condor_tail -stderr -maxbytes 20000 8897.10
```

Look for the last `Running ...` message to identify the active pipeline step. Application buffering
can delay output. These commands require a running, reachable job; they do not recover an old worker's
files after that attempt has ended.

Check the queued job's actual logging settings:

```shell
condor_q 8897.10 -long \
  -attributes Iwd,Out,Err,WhenToTransferOutput,StreamOut,StreamErr
```

The portal currently generates `when_to_transfer_output = ON_EXIT` and does not explicitly enable
stdout/stderr streaming. With those settings, application output can remain on the worker until exit.
The scheduler's `.log` can therefore keep updating while `.out` and `.err` are absent or empty locally.
An interrupted attempt may not return its output.

### When condor_tail cannot connect to the starter

```text
Failed to peek at file from starter: Failed to connect to starter
```

This means `condor_tail` cannot reach the worker's HTCondor starter. It does not establish whether
stdout or stderr files exist. On the submission host, as the job owner, check the current state:

```shell
condor_q 8897.10 -long \
  -attributes JobStatus,RemoteHost,LastRemoteHost,HoldReason,RequestMemory,MemoryUsage
tail -80 log/job.8897.10.log
```

Run the `tail` command from the submission directory, or use the full path to its event log.

| JobStatus | Meaning | Next step |
| --- | --- | --- |
| `5` | Held | There is usually no running starter; prepare logging for a diagnostic retry. |
| `1` | Idle | Wait for a worker; there is no active output to inspect. |
| `2` | Running | Try worker access and check the latest events for disconnection or eviction. |

For a running job, try:

```shell
condor_ssh_to_job 8897.10
```

This may fail for the same connectivity reason. Possible causes include an unreachable worker,
a network or connection-broker (CCB) problem, or a worker that disappeared before the scheduler
updated the job's state. The connection error alone does not distinguish these causes.

Capture the status and latest event-log entries before holding or restarting a running job:
stopping the attempt can lose access to its current scratch files.

If the job is already held, follow the streaming retry instructions below. Streaming may preserve
output on the submission host before another failure, but still depends on connectivity and
application buffering. It cannot recover output from the previous attempt or fix memory growth.

### Identify the process consuming memory

If the site supports access to running jobs:

```shell
condor_ssh_to_job 8897.10
```

Inside the worker session, inspect processes and repeat after a minute:

```shell
ps -eo pid,ppid,rss,vsz,etime,pcpu,args --sort=-rss | head -25
```

`RSS` is resident memory in KB; `VSZ` is virtual memory in KB. Use the PID, command, and changing RSS
to distinguish the generator, GEMC, reconstruction, or another process. The event log's image size
is not the same measurement as resident memory.

In the job's scratch directory, the stdout/stderr capture files are usually available as:

```shell
tail -100 _condor_stdout
tail -100 _condor_stderr
```

The portal script runs its pipeline in an `output/` subdirectory, while the capture files normally
remain in the scratch directory above it.

### Enable streaming for a diagnostic retry

For a held job, enable stdout/stderr streaming for the next attempt:

```shell
condor_qedit 8897.10 StreamOut True
condor_qedit 8897.10 StreamErr True
```

When ready to restart the job:

```shell
condor_release 8897.10
```

This changes logging, not the memory request or application behavior. The diagnostic retry can hit
the same memory limit; its purpose is to capture the active step and output before failure.
Without application checkpointing, expect the pipeline to start again.

Changing the original submission file does not update an already queued job. Use `condor_qedit`
for queued job attributes, and confirm the result with `condor_q -long`.

### Changing nodescript.sh

Editing the submit-side script cannot change the copy already running on a worker. For a later
attempt, ordinary input files may be transferred again, but HTCondor may have retained a submitted
copy of the executable. Do not rely on editing `nodescript.sh` in place and releasing to replace it.
Editing shared inputs can also affect other jobs that start afterward.

For a predictable test, prepare one fresh diagnostic submission in a separate directory:

1. Copy the generated submission file, `nodescript.sh`, `functions.sh`, and any other required inputs.
2. Preserve the failing job's arguments, including subjob index `10` and its Lund URI if applicable.
   A new single-job submission has `$(Process) = 0`; set the original index explicitly when reproducing it.
3. Replace the original queue statement with `queue 1`, and remove dependencies on its old queue variables.
4. Check executable, input, working-directory, and log paths so they refer to the diagnostic files.
5. Redirect the final upload to a separate destination, or disable it, to avoid replacing existing output.
6. Add the following settings to the diagnostic submission file:

```condor
stream_output = True
stream_error = True
```

For Bash command tracing, add this near the beginning of the diagnostic script, after the shebang:

```bash
PS4='+ ${BASH_SOURCE}:${LINENO}: '
set -x
```

Tracing writes commands and expanded arguments to stderr. It identifies the invoked command but
does not show what happens inside a compiled program. Avoid tracing commands that expose credentials.

After reviewing the diagnostic file and its single-job queue, submit from that directory:

```shell
condor_submit debug.condor
```

Use the new job ID with `condor_tail` and `condor_ssh_to_job`. If memory keeps growing, reproduce the
identified pipeline command with a smaller input and investigate that program's memory use.
