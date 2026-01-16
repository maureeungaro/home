---
layout: default
title: "jekyll"
---
{% include mynotes.html %}


# C++ Sanitizers
<hr style="height:4px;border:0;background:#4a90e2;">

<br/>

Below is the recommended list of useful, portable, low-friction, multi-distro sanitizers.

Other sanitizers like `integer`, `memory`, `HWASan` did not make the list as they are not as useful 
or their implementation could be not supported, or give different results, for different distros / compilers, etc. 

## `address`: ASan — AddressSanitizer (`-fsanitize=address`)

**Purpose:** Detects **memory safety** bugs at runtime.

* out-of-bounds reads/writes (heap/stack/global)
* use-after-free
* double free / invalid free
* some use-after-return/use-after-scope modes (toolchain-dependent)

Typical use: “find crashes/corruption fast.”

**Typical findings**

* Heap buffer overflows / underflows
* Stack buffer overflows / underflows
* Use-after-free
* Use-after-return / use-after-scope (depending on compiler options)
* Double free, invalid free, some allocator misuse

**How it works (conceptually)**

* Instruments loads/stores and uses **shadow memory** plus poisoned red-zones around allocations to catch out-of-bounds and UAF quickly.

**Caveats**

* Overhead: usually moderate (often 1.5–3× slower, higher memory use).
* Incompatibilities: **ASan and TSan cannot be combined** in the same binary in practice; treat them as separate build modes.
* False positives: rare, but can happen with custom allocators / low-level tricks unless properly annotated.

<br/>

## `thread`: San — ThreadSanitizer (`-fsanitize=thread`)

Detects **data races** and other concurrency issues:

* unsynchronized concurrent accesses (at least one write)
* reports race stacks and synchronization context

Typical use: “validate thread safety.”
Note: Usually run as a separate build from ASan.

**Purpose:** Detects **data races** and some other concurrency bugs.

**Typical findings**

* Data races (unsynchronized concurrent accesses, at least one write)
* Misuse patterns around mutexes/atomics (depending on runtime)
* Some deadlock-related diagnostics can appear, but the core value is races.

**How it works**

* Instruments memory accesses and synchronization operations, builds a happens-before model, and reports conflicting accesses.

**Caveats**

* Overhead: significant (often 5–15× slower, large memory overhead).
* Incompatibilities: not generally combined with ASan/LSan/UBSan in a single build; use a dedicated “tsan” configuration.
* Requires that most of your code (and ideally key third-party libs) are built with TSan instrumentation to be effective.

<br/>

## `undefined` UBSan — UndefinedBehaviorSanitizer (`-fsanitize=undefined` plus subchecks)

Detects **undefined behavior** in C/C++:

* signed integer overflow (when enabled)
* invalid shifts (negative or too large)
* misaligned accesses
* invalid vptr (some modes), out-of-range enum, etc.

Typical use: “catch UB that may not crash but is wrong.”

**Purpose:** Detects **undefined behavior** at runtime (language/ABI rules violations).

**Typical findings** (examples)

* Signed integer overflow (if enabled)
* Invalid shifts (shift by negative or ≥ bit-width)
* Misaligned pointer dereference
* Null pointer issues in some contexts (depending on options)
* Invalid enum values, vptr checks, etc. (depending on flags)

**How it works**

* Inserts checks for specific UB categories and traps or reports at runtime.

**Caveats**

* “UBSan” is really a **suite of checks**; what you get depends on the exact flags.
* Some checks can be noisy in codebases that intentionally rely on “benign UB” patterns.

<br/>

## `leak` LSan — LeakSanitizer (`-fsanitize=leak` or ASan leak detection)

Detects **memory leaks** (unfreed allocations that become unreachable at program end).

Typical use: “keep long-running services/tests from silently leaking.”
Often used as part of ASan on Linux.

**Purpose:** Detects **memory leaks** (objects that are allocated but not reachable at program end).

**Typical findings**

* Leaked heap allocations
* Leaks from certain allocation APIs if intercepted

**How it works**

* At process exit (or on request), scans reachable memory roots and reports allocations that were never freed and are not reachable.

**Caveats**

* Leak detection is most reliable when the program exits “cleanly” and when allocations are from interceptable allocators.
* Often used **as part of ASan** workflows on Linux; many teams simply run ASan with leak detection enabled rather than separate “leak-only” builds.

<br/>




