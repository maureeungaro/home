---
layout: default
title: "Profiling C++"
permalink: /mynotes/profiling_c++.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Instruments と xctrace を使った macOS でのプロファイリング
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

### 環境変数

環境変数は `--env` オプションを使って `xctrace`[^1] コマンドに渡されます。
環境変数の設定（たとえば `export` で出力したもの）を記述したファイル `env.dat` がある場合、
`xctrace` に渡す必要のあるオプションを生成するには、次のワンライナーを使えます:

[^1]:  `xctrace` が Xcode のものを指していることを確認してください:
```shell
xcrun --find xctrace
```

```shell
 awk '{print "--env "$0" \\"}' env.dat
```

<br/>

### テンプレート

プロファイリングで最もよく使われるテンプレートは `Time Profiler` で、CPU 使用状況のプロファイリングに利用できます。

利用可能なすべてのテンプレートを一覧表示するには、次を使います:

```
xcrun xctrace list templates
```

`--template` オプションでテンプレートを選択できます。たとえば:

```shell
 --template 'Time Profiler'  
```

<br/>

### その他のオプション

- `--output` でトレースデータの出力ファイルを指定します。
- `--launch` でプロファイリング対象のアプリケーションを指定します。
  実行ファイルへのパスが必要で、アプリケーションのオプションを含めることもできます。

<br/>

### 例

以下のコマンドは、Time Profiler テンプレートで gemc をプロファイリングするために使用したものです:

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

# valgrind を使った Linux でのプロファイリング
<hr style="height:4px;border:0;background:#4a90e2;">
<br/><br/>

## 前提条件

プロファイリングを有効にするため、実行ファイルが以下のフラグ付きでコンパイルされていることを確認してください:

- `-g` : 完全なデバッグシンボル
- `-O2`: ホットスポットが実際の実行状況を反映するように最適化する
- `-fno-omit-frame-pointer`: 正確なスタックアンワインドに必要
- `-fno-optimize-sibling-calls`:  末尾呼び出しを確認できるように保つ

<br/>

---

<br/>

## Valgrind の使い方

Valgrind は Linux 上で C++ アプリケーションをプロファイリングするために使えます:

```shell
valgrind --tool=callgrind --callgrind-out-file=callgrind.out.%p \
  --dump-instr=yes --skip-plt=yes \
  /path/to/your/application options
```


### オプションの説明

- %p は PID に展開されるため、複数の
- 命令ダンプは、単純な呼び出し回数よりも、処理に費やされた時間を実際の CPU 時間によりよく対応づけます。
- skip-plt: 

<br/>

---

<br/>


## 結果の表示

```shell
qcachegrind callgrind.out.<PID>
```

次の操作で出力をより読みやすくできます:

- Call Graph 内で右クリック ▸Graph ▸Min node cost
- クラス名でグループ化する
- ツールバーの「%」ボタン: 親に対する相対表示

<br/>

---

<br/>
