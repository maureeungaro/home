---
layout: default
title: "Using Git"
permalink: /mynotes/git.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}



# Git の使い方
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>


## 1 つのブランチまたはタグを、履歴なしで、サブモジュールも履歴なしでクローンする（シャロークローン）

```shell
git clone -b v1.2.3 --recurse-submodules --shallow-submodules --depth 1 [repo] 
```

<br/>

## Git LFS（Large File Storage）

Git LFS をインストールし、ユーザーアカウントに対して一度だけ初期化します。

```shell
# macOS
brew install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs

git lfs install
```

リポジトリで Git LFS を有効にし、LFS で保存するファイルの種類を選択します。

```shell
cd path/to/repository
git lfs track "*.zip"       # use a pattern or a specific file path
git add .gitattributes      # commit the tracking rules
git add path/to/archive.zip
git commit -m "Track ZIP files with Git LFS"
git push
```

`git lfs ls-files` を実行すると、追跡対象のファイルが一覧表示されます。パターンによる追跡は、新しく追加されるファイルにのみ適用されます。
すでに通常の Git にコミット済みのファイルを LFS に移すには `git lfs migrate` が必要で、これはリポジトリの履歴を書き換えます。

<br/>

## 不変のリリースを公開し、メジャーバージョンタグを移動する

バージョン付きの GitHub Action やその他のプロジェクトでは、2 つのタグを使用します。

* `v1.0.1` は不変のリリースタグです。移動したり再利用したりしないでください。
* `v1` は移動する互換性タグです。`uses: owner/repository@v1` を指定するユーザーには、最新の互換性のある
  `v1.x.x` リリースが提供されます。

GitHub Release は `v1.0.1` に紐づいたままにしておく必要があります。移動するのは `v1` タグのみで、移動する
GitHub Release を別途作成することはありません。

#### 1) GitHub Release を公開する

リポジトリの GitHub ページで次を行います。

1. **Releases** を開き、**Draft a new release** を選択します。
2. `v1.0.1` タグを作成（または選択）します。
3. リリースのタイトル、ノート、各種アセットを追加します。


#### 2) メジャーバージョンタグを作成または更新する

不変のバージョンと移動するメジャーバージョンを設定します。

```shell
version=v1.0.1
major=v1
```

`v1.0.1` の GitHub Release を公開してから、`v1` をそのリリースに向けます。最初のリリースではこれで
`v1` が作成され、以降のリリース（`v1.0.2`、`v1.1.2`、...）では同じコマンドで `v1` が最新の不変タグに更新されます。
GitHub が作成したばかりのタグをフェッチし、ローカルの `v1` タグを `$version` が参照するコミットに向け、
そのタグだけを GitHub 上で強制更新します。

```shell
git fetch origin tag "$version"
git tag -f "$major" "$version^{}"
git push --force origin "refs/tags/$major"
```

`^{}` サフィックスはバージョンタグを参照先まで解決するため、`v1` はリリースコミットを直接指します。タグの移動は
non-fast-forward な更新になるため強制更新が必要です（`v1` がまだ存在しない初回でも問題ありません）。`v*.*.*` のような不変タグは
GitHub のタグルールセットで保護し、移動を想定しているメジャーバージョンタグの更新は許可してください。

<br/>

## タグ／リリースを更新する（既存のタグを書き換える）

**次の変数を使用します**

* `tag`: GitHub のタグ名（例: `v1.2.3`）
* `btag`: タグから作成する一時ブランチ名
* `rtag`: タグの完全な ref パス（`refs/tags/<tag>`）。リモートでの削除に使用する

例: `tag=v1.2.3`

```shell
btag="b$tag"
rtag="refs/tags/$tag"
```

#### 1) 既存のタグから一時ブランチを作成して切り替える

```shell
git fetch origin --tags
git switch -c "$btag" "$tag"
```

#### 2) 変更を加え、コミットし、一時ブランチをプッシュする

```shell
git commit -am "Fixes for $tag"
git push -u origin "$btag"
```

#### 3) 古いコミットを指す古いローカルタグを削除し、新しい HEAD でローカルにタグを再作成する

（すでに `$btag` 上にいるため、追加の `git switch "$btag"` は冗長です。）

```shell
git tag -d "$tag"
git tag "$tag"
```

#### 4) リモートタグを新しいコミットを指すように置き換える

まず古いリモートタグを削除してから、新しいものをプッシュします。
タグは慣例上不変であり、多くのサーバーは強制しない限り non-fast-forward なタグ更新を拒否するため、リモートタグを明示的に強制更新します。

```shell
git push origin ":$rtag"
git push --force origin "$rtag"
```

#### 5) 必要に応じて GitHub Release（およびアセット）を更新する
* リリースアセット（バイナリ／独自の .tar.gz など）をアップロードしていた場合:
   既存のリリースを更新し、古いアセットを削除して新しいものをアップロードします（またはリリースを削除して再作成します）。
   タグを移動してもアップロード済みのアセットは置き換わりません。
* GitHub が生成するソースアーカイブ（「Source code (tar.gz/zip)」）のみを使用している場合:
  通常はリリースをそのままにしておけます。引き続き「$tag のリリース」のまま残り、生成されるアーカイブは
  更新されたタグに追従します（キャッシュのため少し時間がかかる場合があります）。
* リリースノート／変更履歴を変更する必要がある場合:
  既存のリリースノートを編集するか、$tag のリリースを削除して再作成します。

#### 6) 後片付け: 一時ブランチを削除する（リモート＋ローカル）

```shell
git push origin --delete "$btag"
git switch main
git branch -D "$btag"
```


<br/>

## ブランチ

新しいブランチを作成して切り替える:

```shell
git checkout -b branchname
```

既存のブランチに切り替える:

```shell
git checkout branchname
```

branch1 の変更を branch2 にマージする（どちらか一方が main でも構いません）。きれいな履歴にするには `rebase` を使います。
あるいは `merge` を使って両方のブランチの履歴を残すこともできます。
```shell
git checkout branch2
git merge/rebase branch1 
```

ブランチをリモートにプッシュする:

```shell
git push -u origin branchname
```

リモートブランチを削除する:

```shell
git push origin --delete branchname
```

すべてのリモートブランチを一覧表示する:

- `git branch -r`: すべてのリモートブランチを一覧表示します
- `git branch -a`: すべてのブランチ（ローカルとリモート）を一覧表示します
- `git branch -vv`: すべてのブランチを最新のコミットとともに一覧表示します
- `git branch --merged`: 現在のブランチにマージ済みのブランチを一覧表示します
- `git branch --no-merged`: 現在のブランチにまだマージされていないブランチを一覧表示します


<br/>

## 既存のプルリクエストまたはマージリクエストを修正する

**フォーク**からの GitHub プルリクエスト（PR）または GitLab マージリクエスト（MR）は、**そのフォーク内のソースブランチ**を
追跡し、それを**元のリポジトリのターゲットブランチ**（多くの場合 `main`）にマージすることを提案します。フォークは
別個のリポジトリであり、その中にもブランチがあります。同じフォーク内の同じブランチにコミットを追加すれば、
ブラウザからでもローカルクローンからのプッシュでも、開いているリクエストは自動的に更新されます。
別のリクエストを作成する必要はありません。

### ブラウザでコードを更新する

フォークをクローンする必要はありません。ただし、そのソースブランチを更新する権限は必要です。作成者は自分のフォークを
編集でき、メンテナは作成者が GitHub で **Allow edits from maintainers** を、GitLab で **Allow contributions from members** を
有効にしている場合に変更を加えられます。

1. 既存の PR または MR を開き、その**ソースフォークとソースブランチ**を特定します。
2. ブラウザでそのフォークを開き、ソースブランチ（例: `my-feature`）を選択します。
3. ファイルを開いて Web エディタを使用します。複数ファイルにまたがる変更には、GitHub の Web エディタまたは
   GitLab の Web IDE を使用します。
4. 変更をレビューし、**既存のソースブランチ**に直接コミットします。選択肢が提示された場合は、新しいブランチや
   リクエストを作成するのではなく、そのブランチを選びます。

既存の PR または MR にそれらのコミットが自動的に含まれます。リクエストのページで更新された差分とチェック結果を
確認してください。

ソースブランチを更新する権限がある場合は、レビューコメントの変更提案を PR または MR 上で直接適用することもできます。
提案を適用すると、そのブランチにコミットが作成されます。権限を持たないレビュアーは、作成者または権限を持つメンテナが
適用できるように変更を提案できます。

### ローカルクローンからコードを更新する

#### 1) フォークとそのソースブランチを特定する

リクエストのページでソースフォークとブランチ（例: `your-user/repository` と `my-feature`）を確認します。
そのフォークのソースブランチへの書き込み権限が必要です。別のフォークを作成したり別のブランチにプッシュしたりしても、
既存のリクエストは更新されません。

ローカルクローンで、各リモートがどのリポジトリを指しているか確認します。

```shell
git remote -v
```

以下のコマンドでは、リクエストのソースフォークを指す `fork` という名前のリモートを使用します。そのフォークがすでに
`origin` の場合は、全体を通して `fork` を `origin` に置き換えてください。それを指すリモートがない場合は、GitHub または
GitLab に表示される、そのフォークの SSH または HTTPS クローン URL を使って追加します。

```shell
git remote add fork <fork-clone-url>
```

#### 2) フォークのソースブランチに切り替える

作業ツリーをクリーンな状態にしてから始めます。ブランチを切り替える前に、関係のない変更はコミットするか、一時退避しておきます。

```shell
git status
git fetch fork
git switch my-feature
# If the branch does not exist locally, use this instead:
# git switch --track fork/my-feature
git pull --ff-only fork my-feature
```

プル時にブランチの分岐が報告された場合は、続行する前にローカルとリモートのコミットの分岐を解消してください。

#### 3) ファイルを編集し、変更をレビューし、コミットして、フォークにプッシュする

要求された変更を加えて関連するチェックを実行し、その後、次を実行します。

```shell
git diff
git add path/to/file path/to/another-file
git diff --cached
git commit -m "Address review feedback"
git push fork HEAD:my-feature
```

`HEAD:my-feature` は現在のコミットをフォークの既存のソースブランチにプッシュします。元のリポジトリの
PR または MR に新しいコミットが含まれます。そのページで更新された差分とチェック結果を確認してください。

#### 4) 必要に応じてタイトルや説明を更新する

GitHub または GitLab で既存のリクエストを開き、タイトルや説明を編集します。これらの編集に Git のコミットは
必要ありません。変更の範囲が変わった場合は、レビュアーが理解できるように最終的な変更内容を説明してください。

#### コミットを修正したりソースブランチをリベースしたりした場合

すでにプッシュしたコミットを修正したりリベースしたりすると、その履歴が書き換えられます。ブランチを共有している人と
調整したうえで、`git push --force-with-lease fork HEAD:my-feature` を使って同じリクエストを更新します。lease のチェックで
プッシュが拒否された場合は、再試行する前にリモートの変更をフェッチしてレビューしてください。ブランチ保護により
強制プッシュが禁止されている場合があります。新しいコミットを追加すれば履歴の書き換えを回避できます。

リクエストがマージされた後は、新しいブランチと新しい PR または MR を通じて追加の変更を提出してください。

<br/>

## 別のブランチから特定のファイルだけを取り込む（ブランチ全体はマージしない）

別のブランチ（またはコミット／タグ）から 1 つまたは数個のファイルだけが必要な場合は、ブランチ全体をマージせず、
それらのパスだけを現在の作業ツリーに取り込みます。

> ⚠️ これらのコマンドは、指定されたパスのローカルコピーを**上書き**します。それらに対する未コミットの変更は
> 失われます。不安な場合はまず `git status` を実行してください。

#### まず差分をプレビューする

```shell
git diff main..otherbranch -- path/to/file        # what would change in that file
git show otherbranch:path/to/file                 # print the file as it is on otherbranch
```

#### ファイルをコピーする（ローカル版を置き換える）

```shell
# Modern (recommended). --source can be a branch, tag, or commit SHA.
git restore --source=otherbranch --staged --worktree -- path/to/file [more/files...]

# Classic equivalent (also stages the result):
git checkout otherbranch -- path/to/file [more/files...]
```

`git checkout <branch> -- <path>` は作業ツリーとインデックスの両方を更新します（変更はステージング済みになります）。
`git restore --source=<ref> -- <path>` はデフォルトでは作業ツリーのみを更新します。ステージングもするには（上記のように）
`--staged` を追加します。その後は通常どおりコミットします。

```shell
git add path/to/file        # only needed if the file is not already staged
git commit -m "Bring path/to/file from otherbranch"
```

#### ファイル内の一部の変更だけを取り込む（対話的、ハンク単位）

これは 1 つのファイルを「マージする」のに最も近い方法です。どのハンクを取り込むかを選べます。

```shell
git restore -p --source=otherbranch -- path/to/file   # or: git checkout -p otherbranch -- path/to/file
```

#### 1 つのファイルの真の 3 ウェイマージ

`checkout`／`restore` はファイルを*置き換える*のであって、その内容を自分のファイルの内容とマージするわけではありません。
2 つのバージョン間で 1 つのファイルを実際に行単位でマージするには、`git merge-file` を使用します。

```shell
git show otherbranch:path/to/file > /tmp/theirs       # their version
git show $(git merge-base HEAD otherbranch):path/to/file > /tmp/base   # common ancestor
git merge-file path/to/file /tmp/base /tmp/theirs     # merges into path/to/file, marks conflicts
```


<br/>

## コンフリクト

### 1. コンフリクトを解決する

- 何がコンフリクトしているか確認する:

```shell
git status
```

* **テキストのコンフリクト（`UU` など）**: ファイルを開いて `<<<<<<< ======= >>>>>>>` を修正し、その後:

```shell
git add path
```

* **一方の側を採用する**（ours か theirs を選ぶ）:

```shell
git checkout --ours  path   # keep our version (rebase source)
git checkout --theirs path  # keep their version (rebase target)
git add path
```

* **ファイルを削除したい場合（例: `DU` / 削除と変更のコンフリクト）**:

```shell
git rm -- path
# if the file is already gone locally:
git rm --cached -- path
git add -u
```

### 2. リベースまたはマージを完了する

```shell
git rebase --continue   # repeat until it finishes
git push origin branch2
```

または
```shell
git commit -m "merge branch1 into branch2"
git push origin branch2
```

<br/>


### 未マージのステータスコード

* `DD` 双方で削除
* `AU` こちらで追加
* `UD` 相手側で削除
* `UA` 相手側で追加
* `DU` こちらで削除 *(多くの場合: 残すか削除するかを決める。削除するには `git rm` を使う)*
* `AA` 双方で追加
* `UU` 双方で変更

<br/>


## 履歴

### 特定のファイルのコミットと差分を表示する

```shell
git log -p -- path/to/file
```

### コンパクトな 1 行履歴
```shell
git log --follow --date=short --pretty=format:"%h %ad %an %s" -- path/to/file
```

### リポジトリからすべての履歴を削除するには:

```shell
	git checkout --orphan new-main
	git add -A
	git commit -m 'new files'
	git branch -D main
	git branch -m main
	git push -f origin main
	git branch --set-upstream-to=origin/main main
```

<br/>

## 直近のコミットをリバートする／取り消す

直近のコミットを「取り消す」には、まったく異なる 2 つの方法があります。コミットがすでにプッシュされているか
どうかで選びます。

#### すでにプッシュ済み → `git revert`（安全、履歴を保持）

`git revert` はコミットを削除しません。その変更を打ち消す**新しい**コミットを作成します。履歴は保持され、
強制プッシュも不要なので、共有ブランチやプッシュ済みのブランチに適した選択です。

```shell
git revert HEAD          # opens an editor for the revert message
git revert --no-edit HEAD   # reuse the default message, no editor
git push
```

リバート自体を取り消すには、そのリバートをさらにリバートする（`git revert HEAD`）か、まだローカルにしかないうちに、
以下のリセットコマンドで破棄します。

#### ローカルのみ → `git reset`（履歴を書き換える）

コミットがまだプッシュされて**いない**場合は、ブランチポインタを 1 コミット戻します。変更内容がどうなるかは
フラグによって異なります。

```shell
git reset --soft  HEAD~1   # undo the commit, keep changes staged
git reset --mixed HEAD~1   # undo the commit, keep changes in the working tree (default)
git reset --hard  HEAD~1   # undo the commit AND discard the changes
```

> ⚠️ `--hard` はそのコミットの作業ツリー上の変更を永久に破棄します。まず `git status`（不安なら
> `git stash`）を実行してください。

よくあるケース: 作業は残しつつコミットをやり直す — `git reset --soft HEAD~1` の後、必要に応じて再ステージング／コミットします。

リセットせずに、メッセージだけを修正したり、忘れていたファイルを直近のコミットに追加したりする:

```shell
git commit --amend            # edit message and/or fold in staged changes
git commit --amend --no-edit  # keep the message, just add the staged changes
```

#### すでにプッシュ済みだった場合

プッシュ済みのコミットをリセットすると履歴が書き換えられるため、プッシュは non-fast-forward となり、強制する必要があります。
他の誰かがその間にプッシュしていた場合に拒否する `--force-with-lease` を優先してください。

```shell
git reset --hard HEAD~1
git push --force-with-lease
```

> ⚠️ これは自分が管理するブランチでのみ行ってください。共有履歴を書き換えると他のクローンとの整合性が崩れます。
> 共有ブランチでは代わりに `git revert` を使用してください。

#### 誤って取り除いたコミットを復元する

`reset` はコミットを即座に削除するわけではありません。以前の先端コミットはしばらく reflog に残ります。

```shell
git reflog                 # find the SHA of the lost commit
git reset --hard <sha>     # or: git cherry-pick <sha>
```

<br/>

## トークン（個人アクセストークン）

**個人アクセストークン（PAT）**は、リポジトリではなく**あなたの個人アカウント**に紐づく認証情報です。
常に次の場所で作成します。

```
Personal Settings > Developer Settings > Personal access tokens
```

間違えやすい重要な 2 点:

* トークンは**それを作成したアカウントの権限を継承**します。あるリポジトリに対して操作する（そのワークフローを
  トリガーする、プッシュする、プライベートイメージをプルする）には、そのアカウントが**そのリポジトリ**に対応するアクセス権を持っている必要があります。
* GitHub はトークン文字列を作成時に**一度だけ**表示します。後から読み出すことはできません（設定からも、
  貼り付けたシークレットからも）。紛失した場合は再生成してください。

既存のトークンを `regenerate`（新しい値を生成）するか、クラシックトークンのスコープをその場で編集（値は変わらない）できます。
どちらも同じページで行います。常にカスタムの有効期限を設定してください。

### どのスコープ／権限が必要か？

トークンが存在するリポジトリではなく、トークンが**行う**べきことに対応する行を選びます。

| 目的                                      | クラシックのスコープ     | きめ細かなトークンの権限         |
|-------------------------------------------|------------------------|--------------------------------|
| 別のリポジトリのワークフローを**トリガー**する（API） | `repo` / `public_repo` | **Actions → Read and write**   |
| `.github/workflows/*` ファイルを追加／編集する | `workflow`             | **Workflows → Read and write** |
| プライベートコンテナイメージをプルする        | `read:packages`        | **Packages → Read**            |

> ⚠️ よくある間違い: `workflow` スコープはワークフローファイルをコミットするため**だけ**のものです。実行を
> *トリガーする*ことは**できません**。`workflow_dispatch` / `repository_dispatch` を発火させるには、クラシックトークンでは `repo`
> （パブリックリポジトリでは `public_repo`）、きめ細かなトークンでは **Actions: Read and write** が
> 必要です。

### 直接リンク

* きめ細かなトークン: <https://github.com/settings/personal-access-tokens/new>
  → 所有者 `gemc`、リポジトリの例 `gemc/clas12-systems`、権限 **Actions: Read and write**
* クラシックトークン: <https://github.com/settings/tokens/new>
  → スコープ: ✅ `repo`（`public_repo` を含む）、プライベートイメージには `read:packages` を追加

（ワークフローではなく）ローカルツールが使用するトークンは、そのツールが読み込むファイルに保存してください。通常はホームディレクトリ内の
ファイルで、たとえば `.bob` です。


<br/>

## シークレット

**GitHub Actions のシークレット**は、リポジトリの設定に保存される暗号化された変数です。そのリポジトリのワークフローは
実行時に {% raw %}`${{ secrets.SECRET_NAME }}`{% endraw %} 経由でそれを読み取ります。値がログに出力されたり、
リポジトリを閲覧する人に表示されたりすることはありません。

2 つの要素は別物として扱ってください。これらは別の場所に存在します。

* **トークン**（`ghp_…` / `github_pat_…` という文字列）は、**あなたの個人アカウント**で作成します（上記参照）。
* **シークレット**は、そのトークン文字列の*コピー*で、**それを使用するワークフローが存在するリポジトリ**に保存されます。
  つまり、トリガーを行うリポジトリであり、トリガーされるリポジトリでは**ありません**。

### 作成して保存する方法

1. **あなたの個人アカウント**（Developer settings）で**トークンを生成**し、ワークフローに操作させたい
   **ターゲット**リポジトリに対応するスコープ／権限を選びます（上記の表を参照）。そのアカウントはターゲットリポジトリへの書き込み権限を持っている必要があります。

2. 画面に表示された**トークンの値をコピー**します（表示されるのは一度だけ）。

3. **それを使用するワークフローが存在するリポジトリにシークレットを追加する**
   - そのリポジトリ → **Settings → Secrets and variables → Actions** に移動します
     （例: <https://github.com/gemc/pygemc/settings/secrets/actions>）
   - **New repository secret** をクリックします
   - 名前: 例 `GEMC_SRC_PAT`（ワークフロー YAML で参照される名前と一致させる必要があります）
   - 値: トークンを貼り付けます
   - **Add secret** をクリックします


<br/>

## 別のリポジトリのワークフローをトリガーする

組み込みの `GITHUB_TOKEN` は別のリポジトリのワークフローを開始**できない**ため、リポジトリ間のトリガーには
シークレットとして保存した PAT を使用します。**リポジトリ A** のワークフローが GitHub API を呼び出して
**リポジトリ B** のワークフローをディスパッチする、という形です。

必要なものは 3 つです。

1. **リポジトリ B への書き込み権限**を持つアカウントが所有し、Actions をトリガーするスコープを持つ **PAT**
   （クラシックの `repo`、または B に対するきめ細かなトークンの **Actions: Read and write**）。上記のトークンの表を参照してください。
2. その PAT を保持する**シークレット**。**リポジトリ A**（トリガー元）に保存します。
3. **リポジトリ B のワークフローにディスパッチ可能なトリガー**。ターゲットのワークフローの `on:` ブロックに
   `workflow_dispatch:`（任意で `inputs:`）を追加します。そうしないと API 呼び出しが `404`/`422` を返します。

### ディスパッチ呼び出し（リポジトリ A のワークフロー内）

{% raw %}
```yaml
      - name: Trigger workflow_dispatch on repo B
        run: |
          curl --fail-with-body -X POST \
            -H "Accept: application/vnd.github+json" \
            -H "Authorization: Bearer ${{ secrets.B_PAT }}" \
            -H "X-GitHub-Api-Version: 2022-11-28" \
            https://api.github.com/repos/<owner>/<repoB>/actions/workflows/test.yml/dispatches \
            -d '{"ref":"main","inputs":{"triggered_by":"repo A"}}'
```
{% endraw %}

`inputs` のキーは、リポジトリ B のワークフローの `workflow_dispatch:` の下で宣言された `inputs:` と
一致させる必要があります。

### セキュリティ: `workflow_run` で連鎖するトリガーを保護する

`on: workflow_run` を持つワークフローは**特権付き**で実行され（シークレット／PAT を参照できる）、フォークからの PR
イベントでも起動するため、ジョブの実行条件を設けてください。そうしないと、フォークからの PR が特権付きステップに到達し、
`workflow_run.head_sha` 経由でチェックアウトされたコードがその特権で実行されるおそれがあります。これが CodeQL が
「特権コンテキストでの信頼できないコードのチェックアウト」を指摘する理由でもあります。

**どのフィールドをチェックするかは連鎖上の位置によって異なります** — 間違えやすい点です。

* **1 段目** — `push`/`pull_request` によって*直接*トリガーされるワークフローの完了を待ち受ける場合（例: `Test` の完了を
  `on: workflow_run` で受けて実行される `Deploy`）: `github.event.workflow_run.event` は元のイベントなので、
  `event == 'push'` でガードします。

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.event == 'push'
        }}
  ```
  {% endraw %}

* **2 段目** — それ*自体*が `workflow_run` でトリガーされるワークフローの完了を待ち受ける場合（例: すでに
  `on: workflow_run` で実行される `Deploy` の後に実行されるジョブ）: ここでは `workflow_run.event` は**常に
  `workflow_run`**であり、`push` になることはありません。`event == 'push'` を使うとジョブは一度も実行されず、
  `event == 'workflow_run'` を使うと常に条件を満たします（保護になりません）。代わりにソースリポジトリをチェックしてガードします。
  `head_*` フィールドが元のソース情報を連鎖を通じて引き継ぎます。

  {% raw %}
  ```yaml
      if: >-
        ${{
          github.event.workflow_run.conclusion == 'success' &&
          github.event.workflow_run.head_repository.full_name == github.repository
        }}
  ```
  {% endraw %}

  `head_repository.full_name == github.repository` は同一リポジトリのプッシュでは true、フォークからの PR の連鎖では
  false になります。これにより、信頼できないコードのチェックアウトを防ぐために必要な保護が得られます。

### このプロジェクトでの例

| トリガー元（リポジトリ A） | シークレット名（A 内） | ターゲット（リポジトリ B） | トークンに必要な権限（B 上） |
|-------------------------|-----------------------|----------------------|-------------------------|
| `gemc/pygemc`           | `GEMC_SRC_PAT`        | `gemc/src`           | src 上で Actions をトリガーする |
| `gemc/src`              | `CLAS12_SYSTEMS_PAT`  | `gemc/clas12-systems`| clas12-systems 上で Actions をトリガーする |
