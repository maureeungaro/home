---
layout: default
title: "HTCondor"
permalink: /mynotes/htcondor.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# HTCondor
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

## サイト構成の確認

コレクターに問い合わせて、プール内でどのサイトを利用できるか、またそれらのサイトがジョブに必要な
CVMFS リポジトリを公開しているかを確認します。以下の 2 つのコマンドは、各サイトの `GLIDEIN_Site` と
`HAS_CVMFS_oasis_opensciencegrid_org` および `HAS_CVMFS_jlab_opensciencegrid_org` フラグを
表示し、同一の行をまとめて件数を付けます。

JLab CHTC プールで、`clas12` GlideinWMS グループに限定する場合:

```shell
condor_status -startd -pool jlab-cm.osg.chtc.io -const 'GLIDEClient_Group == "clas12"' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

OSPool の場合:

```shell
condor_status -startd -pool cm-1.ospool.osg-htc.org -const 'OSPool' \
  -af:h GLIDEIN_Site HAS_CVMFS_oasis_opensciencegrid_org HAS_CVMFS_jlab_opensciencegrid_org \
  | sort | uniq -c | sort -n | sort -u
```

<br/>

## 投入済みジョブの要件を変更する

投入ファイルの編集は、以降の投入にのみ影響します。すでにキューに入っているジョブを変更するには、
投入ホスト上で、ジョブの所有者として `condor_qedit` を使用します。以下のコマンドは Bash と zsh の
両方で動作します。
[condor_qedit リファレンス](https://htcondor.readthedocs.io/en/25.x/man-pages/condor_qedit.html)を参照してください。

`9291` のようなクラスタ ID は、そのクラスタのキューに入っているすべてのサブジョブを選択します。
`9291.10` はサブジョブ `10` のみを選択します。ステータス制約がない場合、`condor_qedit` はアイドル、
ホールド中、実行中のジョブを編集します。ジョブのホールドやリリースは行いません。変更は以降の
マッチメイキングに影響し、実行中のジョブの現在の実行やリソース割り当てには影響しません。

### 要件とジョブステータスの確認

`Requirements` は属性名です。これらの確認コマンドで別の値に置き換えないでください。
1 つのジョブに格納された式を見るには `-long` を使用します:

```shell
condor_q 9291.10 -long -attributes Requirements
```

クラスタ全体については、ジョブ ID を含めます（大量の出力が生成される可能性があります）:

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

単に `-af Requirements` を指定すると、式のテキストを出力するのではなく、式を評価します。ワーカーの
属性がない場合、格納された式に有効なマッチング条件が含まれていても、結果が `false` になることがあります。
その出力は、格納された要件が文字どおり `false` であることや、ジョブがマッチできないことを意味する
ものではありません。その出力に基づいて要件を上書きしないでください。`-long` で式自体が文字どおり
`false` と表示される場合は、どのワーカーにもマッチしません。

何千行もの出力を避けつつ、ステータス別にジョブ数を数えるには:

```shell
condor_q 9291 -af JobStatus | sort | uniq -c
```

1 列目は件数、2 列目はステータスです。`1` はアイドル、`2` は実行中、`5` はホールド中を意味します。
たとえば、`2560 1`、`301 2`、`1 5` は、2,560 件のアイドルジョブ、301 件の実行中ジョブ、1 件の
ホールド中ジョブを意味します。これらの件数だけでは、要件に問題があるかどうかは診断できません。

式をシェル変数に読み込む場合は `-af:r Requirements` を使用します。`r` は評価せずに式をそのまま
出力するよう指定します。
[condor_q リファレンス](https://htcondor.readthedocs.io/en/24.x/man-pages/condor_q.html)を参照してください。

### クラスタ内のすべてのジョブに要件を設定する

変更するかどうかを決める前に、上記のように格納された式を確認してください。

以下のコマンドは、クラスタ `9291` 内のキューに入っているすべてのジョブに要件を設定します。これは JLab
CVMFS リポジトリを必須とし、従来の Oasis の利用可否およびリビジョンに関する要件を削除します:

```shell
condor_qedit 9291 Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

二重引用符と行末のバックスラッシュによって、改行文字を含めずに式を 1 つの引数として渡します。
各バックスラッシュは、末尾にスペースを付けず、必ず行の最後に置いてください。二重引用符を単一引用符に
置き換えないでください。単一引用符の内側では、バックスラッシュと改行による行継続は機能しません。

これは式全体を置き換えます。元の投入ファイルに追加のリソース、アーキテクチャ、またはファイル転送の
要件があった場合は、投入ファイルまたは要件が変更されていない同等のジョブから、それらの条件式を
取り込んでください。上記の 4 つの条件式は、HTCondor が生成した要件を自動的に復元しません。また、
ジョブのスクリプトが意図した `/cvmfs/` パスを使用していることも確認してください。要件を変更しても、
それらのパスは変わりません。

結果を確認します:

```shell
condor_q 9291 -long -attributes ClusterId,ProcId,JobStatus,Requirements
```

アイドルジョブは、次にマッチされるときに新しい要件を使用します。ホールド中のジョブはホールドされた
ままです。実行中のジョブは現在の試行を続け、再度マッチングが必要になった場合に新しい要件を使用します。

実行中のジョブを中断して再起動する意図がある場合に限り、編集の**前に** `condor_hold 9291` を
実行し、ジョブがホールドされていること（`JobStatus == 5`）を確認してから、編集を検証した後に
`condor_release 9291` を実行してください。実行中のジョブをホールドすると、進捗やワーカー上の
ローカル出力が失われることがあります。チェックポイントがない場合は、最初からの再実行を想定してください。
アイドルジョブをホールドすると、一連の編集の途中でそれらのジョブが開始されるのも防げます。

### クラスタ内のホールド中のジョブのみに要件を設定する

アイドルジョブと実行中のジョブをそのままにするには、クラスタとホールドステータス（`JobStatus == 5`）
の両方を指定します。選択されるジョブを事前に確認します:

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

編集実行時にホールドされているジョブにのみ置換を適用します:

```shell
condor_qedit -constraint 'ClusterId == 9291 && JobStatus == 5' Requirements \
  "(TARGET.HAS_SINGULARITY =?= TRUE) && \
   (TARGET.HAS_CVMFS_jlab_opensciencegrid_org =?= TRUE) && \
   (TARGET.OSG_HOST_KERNEL_VERSION >= 21700) && \
   (TARGET.OSG_GLIDEIN_VERSION >= 534)"
```

上記の式全体の置換に関する注意事項が、ここでも適用されます。先にクラスタをホールドする必要はありません。
このコマンドはすでにホールドされているジョブを対象とし、それらをホールドしたままにします。編集を
確認します:

```shell
condor_q -constraint 'ClusterId == 9291 && JobStatus == 5' \
  -long -attributes ClusterId,ProcId,Requirements
```

このクラスタ内のホールド中のジョブを再試行する準備ができたら:

```shell
condor_release -constraint 'ClusterId == 9291 && JobStatus == 5'
```

各コマンドはその制約を独立して評価します。編集とリリースの間に別のジョブがホールドされた場合、
リリースはそのジョブも選択します。編集したジョブだけをリリースする必要がある場合は、明示的な
ジョブ ID を使用してください。

以下のメモリとサイトの例は、1 つのジョブ `8897.10` を対象としています。対象のジョブ ID に
置き換えてください。

### 要求メモリを変更する

実測した必要メモリ量が 4 GiB の場合、`RequestMemory` を `4096` MB に設定します:

```shell
condor_qedit 8897.10 RequestMemory 4096
condor_q 8897.10 -long -attributes RequestMemory,Requirements
```

通常生成される要件 `TARGET.Memory >= RequestMemory` は、更新された要求値を自動的に使用します。
式に固定のメモリしきい値が含まれている場合は、その条件式も確認してください。要求量を増やすと待ち時間が
長くなる可能性があり、メモリリークは解決しません。これは現在実行中の試行ではなく、次のリソース割り当てで
有効になります。今後の投入については、投入ファイルを更新して `request_memory = 4096` を設定してください。

### 問題のあるサイトを除外する

上記のサイトクエリで示されたとおり、プールが公開する正確な `GLIDEIN_Site` の値を使用します。
以下の `SITE_TO_AVOID` をその値に置き換えてください。以前の編集が保持されるように、最新の式を
読み込みます:

```bash
requirements=$(condor_q 8897.10 -af:r Requirements)
printf '%s\n' "$requirements"
```

クエリが失敗した場合や式が返されなかった場合は中止してください。その後、除外条件を追加します:

```bash
condor_qedit 8897.10 Requirements \
  "($requirements) && (TARGET.GLIDEIN_Site =!= \"SITE_TO_AVOID\")"
```

ClassAd 演算子 `=!=` は、`GLIDEIN_Site` が未定義のワーカーも許可します。サイトが既知であることを
必須とするには、別の条件式として `!isUndefined(TARGET.GLIDEIN_Site)` を含めてください。サイトを
除外しても、そこで実行中のジョブがワーカーから排除されることはありません。別の場所で再起動するには、
ホールド/編集/リリースのワークフローを使用してください。

### 確認とリリース

単一ジョブの例については、各編集が成功したことを確認し、最終的な値を調べてください。ジョブがホールド
されていて再試行の準備ができている場合にのみリリースしてください:

```shell
condor_q 8897.10 -long -attributes JobStatus,Requirements,RequestMemory
condor_release 8897.10
condor_q 8897.10
condor_q 8897.10 -better-analyze
```

ジョブはマッチメイキングに戻り、適切なワーカーを待つことがあります。満たされていない要件を調査するには
`-better-analyze` を使用してください。今後のジョブのために、今回意図した変更を投入ファイルにも適用して
ください。

<br/>

## ホールド中のジョブのデバッグ

以下のコマンドは `scosg2202` などの投入ホスト上で実行してください。`8897.10` をジョブのクラスタ ID と
プロセス ID に置き換えてください。これらの例は、クラスタ全体ではなく 1 つのジョブを対象としています。

### ホールド理由とリソース使用量を確認する

```shell
condor_q 8897.10
condor_q 8897.10 -long \
  -attributes JobStatus,HoldReason,HoldReasonCode,HoldReasonSubCode,RequestMemory,MemoryUsage
```

`JobStatus` を `HoldReason` とともに確認してください。リリース後も、以前のホールド理由が残っている
ことがあります。一般的なステータス値は `1`（アイドル）、`2`（実行中）、`5`（ホールド中）です。

イベントログは、アプリケーションの stdout および stderr とは別にスケジューラの動作を記録します。
`012`（ホールド）、`013`（リリース）、`004`（ワーカーからの排除）、`001`（実行）を探してください。
排除の後に再度実行されても、必ずしもホールドされたとは限りません。

たとえば、ジョブ `8897.10` は 2026 年 9 月 15 日に以下のホールドを記録しました:

```text
memory usage exceeded request_memory
Code 21 Subcode 102
Memory (MB): Usage 2440   Request 2311   Allocated 2432
```

このジョブは割り当てられたメモリ量を超過しました。リリース後の試行では、メモリ使用量が 17,712 MB に達し、
実行時間の大部分にわたって、5 分ごとにおよそ 60 MB ずつ増加し続けました。これはメモリリークまたは
データの蓄積を示唆しますが、イベントログだけでは原因となったプログラムを特定できません。提供された
ログは、2 回目のホールドではなくメモリ使用量の更新で終わっていました。

要求量をわずかに増やしたり、ジョブを繰り返しリリースしたりしても、持続的なメモリ使用量の増加は解決しません。
まずプロセスとパイプラインのステップを特定し、その必要メモリ量を測定してください。

### ジョブ実行中に出力を調べる

```shell
condor_tail -maxbytes 20000 8897.10
condor_tail -stderr -maxbytes 20000 8897.10
```

実行中のパイプラインステップを特定するために、最後の `Running ...` メッセージを探してください。
アプリケーションのバッファリングによって出力が遅れることがあります。これらのコマンドを使用するには、
ジョブが実行中で接続可能である必要があります。その試行が終了した後に、以前のワーカーのファイルを
復元することはできません。

キューに入っているジョブの実際のログ設定を確認します:

```shell
condor_q 8897.10 -long \
  -attributes Iwd,Out,Err,WhenToTransferOutput,StreamOut,StreamErr
```

ポータルは現在 `when_to_transfer_output = ON_EXIT` を生成し、stdout/stderr のストリーミングを明示的に
有効にしていません。これらの設定では、アプリケーションの出力が終了までワーカー上に残ることがあります。
そのため、スケジューラの `.log` は更新され続ける一方で、`.out` と `.err` はローカルに存在しないか空の
ままになることがあります。中断された試行では、出力が返されないことがあります。

### condor_tail が starter に接続できない場合

```text
Failed to peek at file from starter: Failed to connect to starter
```

これは `condor_tail` がワーカーの HTCondor starter に接続できないことを意味します。stdout または
stderr のファイルが存在するかどうかは、このエラーだけでは判断できません。投入ホスト上で、ジョブの
所有者として現在の状態を確認します:

```shell
condor_q 8897.10 -long \
  -attributes JobStatus,RemoteHost,LastRemoteHost,HoldReason,RequestMemory,MemoryUsage
tail -80 log/job.8897.10.log
```

`tail` コマンドは投入ディレクトリから実行するか、イベントログへのフルパスを使用してください。

| JobStatus | 意味 | 次のステップ |
| --- | --- | --- |
| `5` | ホールド中 | 通常、実行中の starter はありません。診断用の再試行に向けてログ設定を準備します。 |
| `1` | アイドル | ワーカーを待ちます。確認できる実行中の出力はありません。 |
| `2` | 実行中 | ワーカーへのアクセスを試み、切断や排除がないか最新のイベントを確認します。 |

実行中のジョブの場合は、次を試します:

```shell
condor_ssh_to_job 8897.10
```

これも同じ接続上の理由で失敗することがあります。考えられる原因には、接続できないワーカー、ネットワーク
または接続ブローカー（CCB）の問題、スケジューラがジョブの状態を更新する前に利用できなくなったワーカー
などがあります。接続エラーだけでは、これらの原因を区別できません。

実行中のジョブをホールドまたは再起動する前に、ステータスと最新のイベントログエントリを記録してください。
試行を停止すると、その試行で使用中のスクラッチファイルへのアクセスが失われることがあります。

ジョブがすでにホールドされている場合は、以下のストリーミングを有効にして再試行する手順に従ってください。
ストリーミングによって、次の失敗が起きる前に投入ホスト上で出力を保存できることがありますが、これも
接続状態とアプリケーションのバッファリングに依存します。前の試行の出力を復元したり、メモリ使用量の
増加を解消したりすることはできません。

### メモリを消費しているプロセスを特定する

サイトが実行中のジョブへのアクセスをサポートしている場合:

```shell
condor_ssh_to_job 8897.10
```

ワーカー上のセッションでプロセスを調べ、1 分後にもう一度確認します:

```shell
ps -eo pid,ppid,rss,vsz,etime,pcpu,args --sort=-rss | head -25
```

`RSS` は常駐メモリ量（KB）、`VSZ` は仮想メモリ量（KB）です。PID、コマンド、RSS の変化を使って、
ジェネレーター、GEMC、再構成処理、またはその他のプロセスを区別してください。イベントログの
イメージサイズは、常駐メモリ量と同じ測定値ではありません。

ジョブのスクラッチディレクトリでは、stdout/stderr のキャプチャファイルは通常、次の名前で利用できます:

```shell
tail -100 _condor_stdout
tail -100 _condor_stderr
```

ポータルスクリプトはパイプラインを `output/` サブディレクトリ内で実行しますが、キャプチャファイルは
通常その親のスクラッチディレクトリに残ります。

### 診断用の再試行のためにストリーミングを有効にする

ホールド中のジョブについて、次の試行のために stdout/stderr のストリーミングを有効にします:

```shell
condor_qedit 8897.10 StreamOut True
condor_qedit 8897.10 StreamErr True
```

ジョブを再起動する準備ができたら:

```shell
condor_release 8897.10
```

これはログ設定を変更するものであり、メモリ要求やアプリケーションの動作は変更しません。
診断用の再試行でも同じメモリ上限に達する可能性があります。その目的は、失敗の前に実行中のステップと
出力を記録することです。アプリケーションのチェックポイント機能がなければ、パイプラインは最初から
やり直しになると想定してください。

元の投入ファイルを変更しても、すでにキューに入っているジョブは更新されません。キューに入っている
ジョブの属性を変更するには `condor_qedit` を使用し、`condor_q -long` で結果を確認してください。

### nodescript.sh を変更する

投入側のスクリプトを編集しても、すでにワーカー上で実行されているコピーを変更することはできません。
次回以降の試行では、通常の入力ファイルは再転送されることがありますが、HTCondor は投入時の実行ファイルの
コピーを保持している場合があります。`nodescript.sh` をその場で編集してリリースすれば置き換えられると
考えないでください。共有入力を編集すると、その後に開始する他のジョブにも影響する可能性があります。

意図した条件で確実にテストするには、別のディレクトリに新しい診断用の投入を 1 つ用意します:

1. 生成された投入ファイル、`nodescript.sh`、`functions.sh`、およびその他の必要な入力をコピーします。
2. サブジョブインデックス `10` と、該当する場合は Lund URI を含め、失敗したジョブの引数を保持します。
   新しい単一ジョブの投入では `$(Process) = 0` になるため、再現時には元のインデックスを明示的に設定してください。
3. 元の queue 文を `queue 1` に置き換え、古い queue 変数への依存を削除します。
4. 実行ファイル、入力、作業ディレクトリ、ログのパスが、診断用のファイルやディレクトリを参照していることを確認します。
5. 最終アップロードの宛先を別の場所に変更するか、アップロードを無効にして、既存の出力の上書きを防ぎます。
6. 診断用の投入ファイルに以下の設定を追加します:

```javascript
stream_output = True
stream_error = True
```

Bash のコマンドトレースを有効にするには、診断用スクリプトの先頭付近で、シバンの後に以下を追加します:

```bash
PS4='+ ${BASH_SOURCE}:${LINENO}: '
set -x
```

トレースはコマンドと展開された引数を stderr に書き出します。呼び出されたコマンドは特定できますが、
コンパイル済みプログラムの内部で何が起きているかは示しません。認証情報が露出するコマンドのトレースは
避けてください。

診断用ファイルと、queue 文が単一ジョブを指定していることを確認した後、そのディレクトリから投入します:

```shell
condor_submit debug.condor
```

新しいジョブ ID を `condor_tail` および `condor_ssh_to_job` で使用してください。メモリ使用量が
増加し続ける場合は、特定したパイプラインコマンドをより小さな入力で再現し、そのプログラムのメモリ使用量を
調査してください。
