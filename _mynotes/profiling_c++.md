---
layout: default
title: "Profiling C++"
---

{% include mynotes.html %}


# Profiling on MacOS using Instruments and xctrace
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

### Environment Variables

The environment is passed to the `xctrace`[^1] command with `--env` options.
Provided a file `env.dat`with the environment variables settings (for example from `export`),
the following one liner can be used to get options needed to be passed to `xctrace`:

[^1]:  make sure `xctrace` points to the Xcode one:
```shell
xcrun --find xctrace
```

```shell
 awk '{print "--env "$0" \\"}' env.dat
```

<br/>

### Templates

The most used template for profiling is `Time Profiler`, which can be used to profile CPU usage.

To list all available templates, use:

```
xcrun xctrace list templates
```

The `--template` option can be used to select a template. For example:

```shell
 --template 'Time Profiler'  
```

<br/>

### Other options

- `--output` to specify the output file for the trace data.
- `--launch` to specify the application to be profiled.
  it must have the path to the executable and can include its options

<br/>

### Example

The command below was used to profile gemc with the Time Profiler template:

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

# Profiling on Linux using valgrind
<hr style="height:4px;border:0;background:#4a90e2;">
<br/><br/>

## Pre-requisites

Make sure the executable is compiled with the following flags to enable profiling:

- `-g` : full symbols
- `-O2`: optimise so hot spots are realistic
- `-fno-omit-frame-pointer`: needed for accurate stack unwinding
- `-fno-optimize-sibling-calls`:  keeps tail‑calls visible

<br/>

---

<br/>

## Using Valgrind

Valgrind can be used to profile C++ applications on Linux:

```shell
valgrind --tool=callgrind --callgrind-out-file=callgrind.out.%p \
  --dump-instr=yes --skip-plt=yes \
  /path/to/your/application options
```


### Options explained

- %p expands to the PID so multiple
- the instruction dums correlates better time spent with real‑world CPU time than raw call counts.
- skip-plt: 

<br/>

---

<br/>


## Viewing the results

```shell
qcachegrind callgrind.out.<PID>
```

The following can make the output more readable:

- Right‑click in Call Graph ▸Graph ▸Min node cost
- Group by class name
- “%” button in toolbar: relative to parent

<br/>

---

<br/>