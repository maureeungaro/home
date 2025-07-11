---
layout: default
title: "Static Assertions in C++"
---

{% include mynotes.html %}

---

<br/>

| **Category**               | **`static_assert( … )` macro**              | **Guarantee**                                                         | **When / Why you’d assert it**                                                                                     | **Typical failure scenario**                                                    |
|----------------------------|---------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Lifetime / destruction** | ``std::is_nothrow_destructible_v<T>``       | Destructor is declared&nbsp;`noexcept` → can’t throw.                 | Objects may be destroyed during stack-unwinding or on worker threads; a throwing dtor would call `std::terminate`. | Someone adds `~T() { if(err) throw; }` or a member whose destructor can throw.  |
|                            | ``std::is_trivially_destructible_v<T>``     | Compiler does *nothing* in the destructor (bit-wise destroy).         | Needed only for ultra-low-level POD / lock-free code (e.g. store in `std::atomic<T>`).                             | Adding a `std::vector`, smart pointer, or user-written destructor.              |
| **Movement**               | ``std::is_nothrow_move_constructible_v<T>`` | Moving a `T` cannot throw.                                            | Ensures containers (`std::vector`, `std::optional`) keep strong exception-safety & avoid copies.                   | Removing `noexcept` from the move-ctor or adding a member with a throwing move. |
|                            | ``std::is_nothrow_move_assignable_v<T>``    | Move-assignment is `noexcept`.                                        | Same reasons as above; also speeds up algorithms that rely on fast `swap`.                                         | Same as previous column.                                                        |
| **Copy-protection**        | ``!std::is_copy_constructible_v<T>``        | Copy-construction is *deleted*.                                       | Large / unique objects must **never** be copied accidentally (e.g. translation tables).                            | A contributor removes `= delete`, accidentally enabling expensive copies.       |
|                            | ``!std::is_copy_assignable_v<T>``           | Copy-assignment is *deleted*.                                         | Same as above.                                                                                                     | Ditto.                                                                          |
| **Copy cost / POD-ness**   | ``std::is_trivially_copyable_v<T>``         | Object can be moved with raw `memcpy` (no custom copy / move / dtor). | Tiny value types passed by value at high frequency, data in lock-free queues.                                      | Adding a smart pointer or user copy / move / dtor.                              |
| **Swappability** (C++17)   | ``std::is_nothrow_swappable_v<T>``          | `swap(a,b)` is `noexcept` and cheap.                                  | Lets STL algorithms use fast swap paths (e.g. inside `std::sort`, `std::map::insert`).                             | Custom `swap()` loses `noexcept`, or move operations start throwing.            |

---

<br/>

## How to apply one

```cpp
#include <type_traits>
#include <utility>          // for std::is_nothrow_swappable_v

static_assert(std::is_nothrow_move_constructible_v<GTranslationTable>,
              "GTranslationTable move-ctor must be noexcept for vector reallocation!");

static_assert(!std::is_copy_constructible_v<GTranslationTable>,
              "Copying a translation table is disallowed — use move or shared_ptr.");

```
<br/>