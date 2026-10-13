---
layout: default
title: "Assertions in C++"
permalink: /mynotes/static_assertions.html
lang: ja
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# 静的アサーション
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

| **カテゴリ**               | **`static_assert( … )` マクロ**              | **保証内容**                                                         | **アサートする場面・理由**                                                                                     | **典型的な失敗シナリオ**                                                    |
|----------------------------|---------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **生存期間 / 破棄** | ``std::is_nothrow_destructible_v<T>``       | デストラクタが&nbsp;`noexcept` として宣言されている → 例外を送出できない。                 | オブジェクトはスタックの巻き戻し中やワーカースレッド上で破棄される可能性があり、例外を送出するデストラクタは `std::terminate` を呼び出す。 | 誰かが `~T() { if(err) throw; }` を追加する、またはデストラクタが例外を送出し得るメンバを追加する。  |
|                            | ``std::is_trivially_destructible_v<T>``     | コンパイラがデストラクタで*何もしない*（ビット単位での破棄）。         | 極めて低レベルな POD / ロックフリーコードでのみ必要（例: `std::atomic<T>` に格納する場合）。                             | `std::vector`、スマートポインタ、またはユーザー定義のデストラクタを追加する。              |
| **ムーブ**               | ``std::is_nothrow_move_constructible_v<T>`` | `T` のムーブが例外を送出しない。                                            | コンテナ（`std::vector`、`std::optional`）が強い例外安全性を保ち、コピーを回避できることを保証する。                   | ムーブコンストラクタから `noexcept` を削除する、またはムーブ時に例外を送出するメンバを追加する。 |
|                            | ``std::is_nothrow_move_assignable_v<T>``    | ムーブ代入が `noexcept` である。                                        | 上記と同じ理由。加えて、高速な `swap` に依存するアルゴリズムを高速化する。                                         | 前の列と同じ。                                                        |
| **コピー防止**        | ``!std::is_copy_constructible_v<T>``        | コピー構築が*削除されている*。                                       | 大きなオブジェクトや一意であるべきオブジェクトは、誤ってコピーされることが**決してあってはならない**（例: 変換テーブル）。                            | 開発者が `= delete` を削除し、意図せず高コストなコピーを有効化してしまう。       |
|                            | ``!std::is_copy_assignable_v<T>``           | コピー代入が*削除されている*。                                         | 上記と同じ。                                                                                                     | 同上。                                                                          |
| **コピーコスト / POD 性**   | ``std::is_trivially_copyable_v<T>``         | オブジェクトを生の `memcpy` で移動できる（独自のコピー／ムーブ／デストラクタがない）。 | 高頻度で値渡しされる小さな値型、ロックフリーキュー内のデータ。                                      | スマートポインタ、またはユーザー定義のコピー／ムーブ／デストラクタを追加する。                              |
| **スワップ可能性** (C++17)   | ``std::is_nothrow_swappable_v<T>``          | `swap(a,b)` が `noexcept` かつ低コストである。                                  | STL アルゴリズムが高速なスワップ処理を使えるようにする（例: `std::sort`、`std::map::insert` の内部）。                             | 独自の `swap()` が `noexcept` を失う、またはムーブ操作が例外を送出するようになる。            |

---

<br/>

## 適用方法

```cpp
#include <type_traits>
#include <utility>          // for std::is_nothrow_swappable_v

static_assert(std::is_nothrow_move_constructible_v<GTranslationTable>,
              "GTranslationTable move-ctor must be noexcept for vector reallocation!");

static_assert(!std::is_copy_constructible_v<GTranslationTable>,
              "Copying a translation table is disallowed — use move or shared_ptr.");

```

<br/>

## 適切なアサートの選び方


| 意図                                   | 推奨する型特性                                   |
| ---------------------------------------- | ---------------------------------------------------- |
| **パフォーマンスが重要な値型**      | `std::is_trivially_copyable_v<T>`                    |
| **リソースを保持し、*ムーブ*のみを行う型** | コピー操作を削除し、例外を送出しないムーブに関する 2 つの型特性をアサートする |
| **スレッド間で共有されるオブジェクト**         | 少なくとも `std::is_nothrow_destructible_v<T>`         |
| **独自の `swap` / 順序付きマップで使用** | `std::is_nothrow_swappable_v<T>` を追加する                 |


<br/>
