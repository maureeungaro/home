---
layout: default
title: "Assertions in C++"
permalink: /mynotes/static_assertions.html
lang: zh
human_reviewed: false
---

{% include directory.html data=site.data.mynotes columns=5 section_breaks=2 %}


# 静态断言
<hr style="height:4px;border:0;background:#4a90e2;">


<br/>

| **类别**               | **`static_assert( … )` 宏**              | **保证**                                                         | **何时 / 为何需要此断言**                                                                                     | **典型的失败场景**                                                    |
|----------------------------|---------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **生命周期 / 析构** | ``std::is_nothrow_destructible_v<T>``       | 析构函数声明为&nbsp;`noexcept` → 不会抛出异常。                 | 对象可能在栈展开期间或工作线程上被销毁；抛出异常的析构函数会导致调用 `std::terminate`。 | 有人添加了 `~T() { if(err) throw; }`，或添加了析构函数可能抛出异常的成员。  |
|                            | ``std::is_trivially_destructible_v<T>``     | 编译器在析构函数中*什么都不做*（按位销毁）。         | 仅在极底层的 POD / 无锁代码中需要（例如存入 `std::atomic<T>`）。                             | 添加了 `std::vector`、智能指针或用户自定义的析构函数。              |
| **移动**               | ``std::is_nothrow_move_constructible_v<T>`` | 移动 `T` 不会抛出异常。                                            | 确保容器（`std::vector`、`std::optional`）维持强异常安全保证并避免拷贝。                   | 从移动构造函数中移除了 `noexcept`，或添加了移动操作会抛出异常的成员。 |
|                            | ``std::is_nothrow_move_assignable_v<T>``    | 移动赋值为 `noexcept`。                                        | 原因同上；同时也能加速依赖快速 `swap` 的算法。                                         | 同上一列。                                                        |
| **拷贝保护**        | ``!std::is_copy_constructible_v<T>``        | 拷贝构造函数被*删除*。                                       | 大型 / 具有唯一性的对象**绝不能**被意外拷贝（例如转换表）。                            | 某位贡献者移除了 `= delete`，意外启用了代价高昂的拷贝。       |
|                            | ``!std::is_copy_assignable_v<T>``           | 拷贝赋值运算符被*删除*。                                         | 同上。                                                                                                     | 同上。                                                                          |
| **拷贝成本 / POD 性质**   | ``std::is_trivially_copyable_v<T>``         | 对象可以直接用 `memcpy` 移动（没有自定义的拷贝 / 移动 / 析构函数）。 | 高频按值传递的小型值类型、无锁队列中的数据。                                      | 添加了智能指针或用户自定义的拷贝 / 移动 / 析构函数。                              |
| **可交换性** (C++17)   | ``std::is_nothrow_swappable_v<T>``          | `swap(a,b)` 是 `noexcept` 且开销小。                                  | 让 STL 算法能够使用快速交换路径（例如在 `std::sort`、`std::map::insert` 内部）。                             | 自定义的 `swap()` 失去了 `noexcept`，或移动操作开始抛出异常。            |

---

<br/>

## 如何使用

```cpp
#include <type_traits>
#include <utility>          // for std::is_nothrow_swappable_v

static_assert(std::is_nothrow_move_constructible_v<GTranslationTable>,
              "GTranslationTable move-ctor must be noexcept for vector reallocation!");

static_assert(!std::is_copy_constructible_v<GTranslationTable>,
              "Copying a translation table is disallowed — use move or shared_ptr.");

```

<br/>

## 选择合适的断言


| 意图                                   | 建议使用的类型特征                                   |
| ---------------------------------------- | ---------------------------------------------------- |
| **对性能要求严格的值类型**      | `std::is_trivially_copyable_v<T>`                    |
| **只进行*移动*操作的资源持有对象** | 删除拷贝操作 + 对两个无异常移动类型特征进行断言 |
| **跨线程共享的对象**         | 至少断言 `std::is_nothrow_destructible_v<T>`         |
| **自定义 `swap` / 用于有序映射容器** | 添加 `std::is_nothrow_swappable_v<T>`                 |


<br/>
