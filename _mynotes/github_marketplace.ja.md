---
layout: default
title: "GitHub Actions Marketplace"
permalink: /mynotes/github_marketplace.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}

# GitHub Marketplace へのアクションの公開
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

このノートでは [ThreadScale](https://github.com/gemc/ThreadScale) を例として使用します。
リポジトリのルートで定義されたアクションは [Marketplace の ThreadScale](https://github.com/marketplace/actions/threadscale)
として公開されており、ワークフローから `uses: gemc/ThreadScale@v1` で呼び出します。

## リポジトリの準備

アクション専用のパブリックリポジトリを使用し、そのルートに `action.yml` または `action.yaml` を 1 つ配置します。
Marketplace の既存の名前や GitHub の予約名と重複しない、一意のアクション名を選びます。

ThreadScale のメタデータには次のフィールドが含まれています。完全な `action.yml` では入力と出力も宣言されています。

```yaml
name: ThreadScale
description: Measure strong scaling, speedup, throughput, and parallel efficiency across application threads.
author: GEMC Collaboration

branding:
  color: blue
  icon: activity

runs:
  using: node24
  main: src/main.js
```

自分のアクションでは、名前、説明、ブランディング、エントリポイントを置き換えてください。`runs.main` が参照する
コード、使用方法と入力を説明する README、ライセンスを含めます。ThreadScale は MIT ライセンスを採用しており、
実行時の依存関係やビルド手順なしで JavaScript を直接実行します。ローカルでのチェックは次のとおりです。

```shell
npm run check
npm test
```

ThreadScale は `.github/workflows/` 以下に再利用可能なワークフローも提供しています。Marketplace への掲載には
ルートの `action.yml` が使用されます。

<br/>

## GitHub を通じた公開

1. GitHub 上でリポジトリのルートにある `action.yml` を開き、リリースバナーからリリースの下書きを作成します。
2. リリースフォームで Marketplace 公開のチェックボックスをオンにします。
3. チェックボックスが無効になっている場合は、リポジトリの所有者または組織の所有者がリリースページから
   Marketplace 開発者契約に同意する必要があります。公開には二要素認証も必要です。
4. メタデータの検証エラーをすべて解消し、メインカテゴリと、必要に応じて 2 つ目のカテゴリを選択します。
5. 公開するコードに対応する固定バージョンタグを選択し、リリースのタイトルとリリースノートを追加します。
   - 既存の `v1.0.0` を掲載する場合は、そのタグを選択します。対応する GitHub Release がすでに存在する場合は、
     そのリリースを編集し、そこで Marketplace 公開を有効にします。
   - 更新したコードをリリースする場合は、テスト済みのコミットを指す `v1.0.1` を作成または選択します。タグを
     作成する際は、リリースの対象がテストしたコミットであることを確認してください。
   - リリースには固定バージョンタグを使用し、`v1` は利用者向けに参照先を更新していくタグとして維持します。
6. リリースを公開し、Marketplace の掲載内容を確認します。掲載条件を満たすアクションは、別途審査を受けることなく
   すぐに表示されます。

現在の要件とインターフェースについては [GitHub の公開手順][publishing] を参照してください。

<br/>

## バージョンタグの保守

`v1` が現在 `v1.0.0` と同じコミットを指しているとします。この既存バージョンを Marketplace に公開する際に、
タグの変更は不要です。Marketplace への掲載を追加するためだけに `v1.0.1` を作成する必要はありません。

更新したコードの準備が整ったら、Marketplace 公開を有効にして、`v1.0.1` に紐付けた新しい GitHub Release を
公開します。その後、`v1` の参照先を `v1.0.1` と同じコミットに移動します。新しいリリースを作成しても、これは
**自動では行われません**。タグを自分で更新するか、更新を行うようにリリースの自動化を設定してください。

`v1.0.1` を公開したら、アクションのリポジトリで次のコマンドを実行します。

```shell
git fetch origin tag v1.0.1
git tag -f v1 'v1.0.1^{}'
git push --force origin refs/tags/v1
```

接尾辞 `^{}` は、バージョンタグが指すコミットを取得します。参照先が移動するのは `v1` のみです。`v1.0.0`、`v1.0.1`、
および対応する GitHub Release の参照先は変わりません。`@v1` を使う利用者には次回以降の実行で更新されたコードが
提供され、`@v1.0.0` を使う利用者は引き続きそのバージョンを使用します。詳細は
[リリースタグに関する Git のノート][tags] を参照してください。

ThreadScale の再利用可能なワークフローも内部で `gemc/ThreadScale@v1` を参照するため、利用者が実行する前に
そのタグが存在している必要があります。利用者は、互換性のある更新を受け取るために `@v1` を選択するか、
完全なコミット SHA を指定して固定できます。

以降のバージョンでも、Marketplace 公開を有効にして新しいバージョンのリリースを公開し、互換性のある変更であれば
メジャーバージョンタグを更新します。以前のバージョンタグはそのまま残します。

<br/>

## アクションを見つけてもらい、試してもらう

- README の冒頭に、解決する課題、動作する簡潔なワークフロー、結果のスクリーンショットを示します。
  ThreadScale のスケーリングチャートは、掲載する内容の良い例です。
- 分かりやすいリポジトリの説明、`github-action`、`benchmark`、
  `performance` などの関連トピック、Marketplace へのリンクを追加します。自分のホームページや関連プロジェクトのドキュメントからアクションにリンクします。
- 実際のアプリケーションを使った短いチュートリアルを、ワークフローと生成されたレポートを含めて公開します。
  関連する科学技術計算コミュニティや共同研究者と共有し、LinkedIn にも投稿します。
- 継続的に管理されている GitHub Actions や科学技術ソフトウェアの一覧の対象範囲に合う場合は、掲載を提案します。
  各一覧への投稿手順に従ってください。
- 初期の利用者に利用事例の報告を呼びかけ、許可を得たうえで採用プロジェクトの簡潔な一覧を追加します。
  大きなリリースは、改善の具体例とともに告知します。

## 役立つ README バッジの追加

ThreadScale にはすでに Marketplace、テスト状況、ライセンスのバッジがあります。スター数のバッジを追加すると、
関心の度合いを公開の指標として示せます。次の Markdown をアクションの README にコピーし、必要に応じてリポジトリ名とワークフロー名を置き換えてください。

```markdown
[![Marketplace][market-badge]][market]
[![Stars][stars-badge]][repo]
[![Tests][tests-badge]][tests]

[market-badge]: https://img.shields.io/badge/Marketplace-ThreadScale-2088FF
[stars-badge]: https://img.shields.io/github/stars/gemc/ThreadScale?style=flat
[tests-badge]: https://img.shields.io/github/actions/workflow/status/gemc/ThreadScale/test.yml
[market]: https://github.com/marketplace/actions/threadscale
[repo]: https://github.com/gemc/ThreadScale
[tests]: https://github.com/gemc/ThreadScale/actions/workflows/test.yml
```

[スター数のバッジ][stars-docs] はスター数を表示し、[ワークフローバッジ][tests-docs] はアクションのリポジトリの
テスト状況を示します。どちらも、他のプロジェクトがそのアクションを実行する頻度を測るものではありません。
Marketplace バッジは静的なリンクです。リリースアセットのダウンロード数やリポジトリのクローン数も、
アクションの実行回数として示すべきではありません。

## 採用実績の根拠を示す

有用な利用状況バッジを作るには、**そのアクションを使用していることが確認できたパブリックリポジトリ**の数を
管理し、その根拠へのリンクを付けます。手作業で確認した一覧から始め、管理が煩雑になった場合にのみ更新を自動化します。
呼び出し元の候補を見つけるには [GitHub コード検索][search-docs] を使います。

```text
"gemc/ThreadScale@" path:.github/workflows/ NOT repo:gemc/ThreadScale
"gemc/ThreadScale/.github/workflows/thread-scaling.yml@" path:.github/workflows/ NOT repo:gemc/ThreadScale
```

検索結果を確認して現在使用されている `uses:` 参照を見つけ、両方の検索結果に含まれるリポジトリの重複を除き、
独立した採用事例に当たらないフォークやコピーされた例を除外します。日付と集計方法を記録します。
これは一部のみを対象とした集計です。プライベートリポジトリや、検索インデックスに登録されていない呼び出し元、
間接的な呼び出し元は含まれません。また、ワークフロー内の参照だけでは、実際に実行されたことは証明できません。

確認済みの件数を表示するには、小さな JSON ファイルを自分のウェブサイトに公開し、
[Shields エンドポイントバッジ][endpoint-docs] を使います。たとえば、次の JSON では **N をプレースホルダーとして**
使用しています。公開前に、確認済みの件数に置き換えてください。

```json
{
  "schemaVersion": 1,
  "label": "known public users",
  "message": "N repositories",
  "color": "blue"
}
```

続いて、次の README テンプレートを使い、例示された 2 つの URL を自分の JSON エンドポイントと根拠を示すページに置き換えます。

```markdown
[![Known public users][usage-badge]][usage-evidence]

[usage-badge]: https://img.shields.io/endpoint?url=https%3A%2F%2Fexample.org%2Fusage.json
[usage-evidence]: https://example.org/adopters
```

広報活動の効果を確認するために、リポジトリのメンテナーは **Insights → Traffic** で訪問者数、
クローン数、参照元サイトを調べることもできます。GitHub の [トラフィック表示][traffic-docs] では、過去 14 日間の
訪問者数と完全なクローンの数を確認できます。これらはリポジトリのトラフィックを測る指標であり、アクションの実行回数ではありません。

[tags]: /home/mynotes/git#publish-an-immutable-release-and-move-its-major-version-tag
[publishing]:
  https://docs.github.com/en/actions/how-tos/create-and-publish-actions/publish-in-github-marketplace
[stars-docs]: https://shields.io/badges/git-hub-repo-stars
[tests-docs]: https://shields.io/badges/git-hub-actions-workflow-status
[endpoint-docs]: https://shields.io/badges/endpoint-badge
[search-docs]:
  https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
[traffic-docs]:
  https://docs.github.com/articles/viewing-traffic-to-a-repository
