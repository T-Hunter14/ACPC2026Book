# ACPC 2026 Competitive Programming Handbook

## Book Style Guide

- Use a clear hierarchy: chapter (`##`) → topic (`###`) → details (`####`/`#####`).
- Keep every technique in one canonical snippet first, then add variants.
- Every major topic should keep: **When to use**, **Complexity**, **Notes/Tricks**.
- Use `cpp` fenced blocks for C++ and keep variable naming consistent (`n, m, u, v, dist, par`).
- Prefer compact contest-ready snippets that stay readable (no unnecessary blank lines).
- Keep examples minimal and focused on one idea per block.

## Table of Contents

- [1) Foundations & Utilities](#1-foundations--utilities)
- [2) Graph Algorithms](#2-graph-algorithms)
- [3) Trees & Binary Lifting](#3-trees--binary-lifting)
- [4) Strings](#4-strings)
- [5) Range Query Data Structures](#5-range-query-data-structures)
- [6) STL, Two Pointers & Monotonic Techniques](#6-stl-two-pointers--monotonic-techniques)
- [7) Math & Number Theory](#7-math--number-theory)
- [8) Dynamic Programming](#8-dynamic-programming)
- [9) Missing Topics (Added)](#9-missing-topics-added)
- [10) Comprehensive Missing Tricks & Function Ideas](#10-comprehensive-missing-tricks--function-ideas)
- [11) Bit Manipulation & Bitset](#11-bit-manipulation--bitset)

### Foundation quick links

- [General Template (clean)](#general-template-clean)
- [Coordinate Compression (Restore Values)](#coordinate-compression-restore-values)
- [Binary Search Template (First True)](#binary-search-template-first-true)
- [Ternary Search](#ternary-search)

### Graph quick links

- [BFS (Breadth First Search)](#bfs-breadth-first-search)
- [DFS (Depth First Search)](#dfs-depth-first-search)
- [Topological Sort](#topological-sort)
- [Dijkstra](#dijkstra)
- [Kruskal (Minimum Spanning Tree)](#kruskal-minimum-spanning-tree)
- [Bellman Ford](#bellman-ford)
- [Floyd Warshall](#floyd-warshall)

### Trees / Strings / Data structures quick links

- [Binary Lifting](#binary-lifting)
- [LCA (Lowest Common Ancestor)](#lca-lowest-common-ancestor)
- [KMP (Knuth-Morris-Pratt)](#kmp-knuth-morris-pratt)
- [Segment Tree](#segment-tree)
- [Lazy Segment Tree](#lazy-segment-tree)
- [Sparse Table](#sparse-table)

### Algorithmic patterns quick links

- [Two Pointers Advanced Patterns](#two-pointers-advanced-patterns)
- [Sliding Window Advanced Patterns](#sliding-window-advanced-patterns)
- [Monotonic Stack](#monotonic-stack)
- [Monotonic Queue (Deque Tricks)](#monotonic-queue-deque-tricks)
- [Modular Arithmetic](#modular-arithmetic)
- [DP Mindset](#dp-mindset)

---




## 1) Foundations & Utilities

### General Template (clean)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Custom Sort

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

- Sort struct.
- Multi-key sorting.

##### Complexity

- `O(n log n)`

---

### Coordinate Compression (Restore Values)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Build : O(n log n)
Query : O(log n)
Memory : O(n)
```

##### Notes

- Use when original values are needed.
- Common with Fenwick Tree, Segment Tree, Sweep Line.

---

### Coordinate Compression (In-place)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(n log n)`

##### Notes

- Cannot restore original values.
- Faster to write during contests.

---

### Debug

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Notes

- Disabled automatically on Online Judge.

---

### Random (RNG helper)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(1)`

##### Notes

- Stress testing
- Randomized algorithms

---

### Shuffle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(n)`

##### Notes

- Generate random permutation.
- Useful for anti-hack.

---

### ckmin / ckmax

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(1)`

##### Notes

- Very common in DP and Graphs.

---

### Next / Previous Permutation

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(n)`

##### Notes

- Generate permutations.
- Useful in brute force.

---

### Useful STL Tricks

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

| Function | Complexity |
| --- | --- |
| max_element | O(n) |
| min_element | O(n) |
| accumulate | O(n) |
| reverse | O(n) |
| rotate | O(n) |
| iota | O(n) |

---

### Binary Search Template (First True)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(log Range)`

##### Notes

- Finds first valid value.

---

### Binary Search Template (Last True)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(log Range)`

##### Notes

- Finds last valid value.

---

### Ternary Search

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

- `O(log Range)`

##### Notes

- Convex / Concave functions only.
- Usually for optimization problems.

---


## 2) Graph Algorithms

### DSU (Standard)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Features

- Path Compression
- Union By Size
- Component Count
- Component Size Query

##### Complexity

| Operation | Complexity |
| --- | --- |
| find | O(α(n)) |
| unite | O(α(n)) |
| same | O(α(n)) |
| size | O(α(n)) |

##### Memory

```
O(n)
```

##### Common Uses

#### Connectivity

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Merge Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Component Size

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Number of Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Cycle Detection

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Kruskal MST

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### DSU (Component Tracking)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Features

- Path Compression
- Union By Size
- Component Count
- Component Size Query
- Get All Members of a Component
- Get All Components

##### Complexity

| Operation | Complexity |
| --- | --- |
| find | O(α(n)) |
| same | O(α(n)) |
| size | O(α(n)) |
| unite | O(log n) amortized |
| members | O(1) |

##### Memory

```
O(n)
```

##### Common Uses

#### Get Members of Component

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Print All Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Merge Small Into Large

```
Uses Small-To-Large Merging
Each node moves at most O(log n) times
```

##### When To Use

```
Need actual vertices of each component
Need to print components
Need to process all nodes inside a component
Need offline merging with component contents
```

##### When NOT To Use

```
Connectivity only
Kruskal
Cycle Detection
Standard DSU problems
```

Use Standard DSU by default.
Use Tracking DSU only when component members are explicitly required.

### BFS (Breadth First Search)

#### When To Use

```
Unweighted Graph
Shortest Path (all edges = 1)
Minimum Moves
Grid Problems
State Graphs
Multi Source Expansion
```

---

### Normal BFS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### BFS With Parent (Restore Path)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Restore Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Print shortest path
Find route
```

---

### Multi Source BFS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Nearest Hospital
Nearest Police Station
Nearest Special Node
Spread Problems
```

##### Complexity

```
O(V + E)
```

---

### Grid BFS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(N * M)
```

##### Tricks

```
8 Directions => add diagonals
Knight Moves => custom dx,dy
Maze Problems
```

---

### BFS On State Graph

#### Example

```
(node , mask)
(node , parity)
(node , coins)
(node , fuel)
```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Collect Keys
Visit Special Nodes
Bitmask BFS
Shortest State Transition
```

---

### 0-1 BFS

#### Condition

```
Edge Weight = 0 or 1 only
```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

##### Use

```
Reverse Edges
Minimum Cost Direction Changes
Binary Weight Graphs
```

---

### Useful Snippets

#### Count Connected Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Find Farthest Node

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Tree Diameter
```

---

### Common BFS Tricks

```
dist = -1  => unvisited

BFS always gives shortest path
in unweighted graph

Multi Source BFS
= add all sources initially

Grid BFS
= graph on cells

0-1 BFS
= Dijkstra replacement
for weights {0,1}

State BFS
= shortest path on states
not nodes
```

---

### Common Problems

```
Labyrinth
Monsters
Message Route
Police Stations
Nearest Special Node
Collect Keys
Binary Maze
Minimum Moves
Shortest Transformation
```

### DFS (Depth First Search)

#### When To Use

```
Connected Components
Tree Problems
Cycle Detection
Subtree Queries
Entry / Exit Time
Tree Diameter
Topological Sort
Bridges
Articulation Points
```

---

### Normal DFS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Connected Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Count Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

---

### DFS With Parent

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Tree DFS
Avoid Going Back To Parent
```

---

### Subtree Size

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Number Of Nodes In Subtree(u)
```

---

### Entry / Exit Time

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Check Ancestor

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Ancestor Queries
Euler Tour
Subtree Queries
LCA
```

---

### Euler Tour (Flatten Tree)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Subtree Range

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Segment Tree On Tree
Fenwick On Tree
Subtree Queries
```

---

### Cycle Detection (Undirected)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

---

### Cycle Detection (Directed)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### States

```
0 = Unvisited
1 = In Stack
2 = Finished
```

##### Use

```
Detect Directed Cycle
Check DAG
```

---

### Topological Sort (DFS)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Build Topological Order

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

---

### Tree Diameter

#### First DFS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Find farthest node:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Second DFS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Find farthest node:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Diameter Length

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(N)
```

---

### DFS Order

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Tree Traversal
Euler Variants
Offline Queries
```

---

### Bipartite Check (DFS)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

---

### Useful Snippets

#### Collect Nodes Of Component

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Leaf Detection

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Count Leaves

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common DFS Tricks

```
DFS = Explore Entire Component

Subtree Size
=> Post Order

tin/tout
=> Ancestor Queries

Euler Tour
=> Tree To Array

Directed Cycle
=> 3 Colors

Tree Diameter
=> Two DFS

Topo Sort
=> Reverse DFS Order
```

---

### Common Problems

```
Connected Components

Cycle Detection

Tree Diameter

Subtree Queries

Ancestor Queries

Topological Sort

Bipartite Graph

Tree DP

Bridges

Articulation Points

SCC
```

### Topological Sort

#### When To Use

```
DAG (Directed Acyclic Graph)

Task Scheduling
Course Prerequisites
Dependency Graphs
DP On DAG
Longest Path In DAG
```

---

### Kahn's Algorithm (BFS)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

---

### Check If DAG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Idea

```
A graph has a topological order
iff it is a DAG.
```

---

### Lexicographically Smallest Topological Order

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O((V + E) log V)
```

##### Use

```
Smallest Valid Ordering
```

---

### DFS Topological Sort

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Build Order

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

---

### Cycle Detection In DAG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### States

```
0 = Unvisited
1 = In Stack
2 = Finished
```

---

### Longest Path In DAG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

##### Use

```
AtCoder DP G
Longest Dependency Chain
```

---

### Shortest Path In DAG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V + E)
```

##### Notes

```
Works even with negative weights
(as long as graph is DAG)
```

---

### Count Number Of Paths In DAG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Count Paths
DP On DAG
```

---

### Path Restoration In DAG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Restore Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Useful Snippets

#### Sources (Indegree = 0)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Sinks (Outdegree = 0)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Check Unique Topological Order

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
More than one valid order exists.
```

---

### Common Tricks

```
Kahn => BFS Topological Sort

DFS Topo => Reverse DFS Finish Order

topo.size() != n
=> cycle exists

DAG DP
=> process nodes in topo order

Shortest Path In DAG
=> O(V + E)

Longest Path In DAG
=> O(V + E)

Negative Edges Allowed
if graph is DAG
```

---

### Common Problems

```
Course Schedule

Fox And Names

Hierarchy Problems

Task Scheduling

Dependency Resolution

AtCoder DP G

Longest Path In DAG

Count Paths

DAG Shortest Path

Build Order
```

### Dijkstra

#### When To Use

```
Shortest Path
Positive Edge Weights
Weighted Graphs
State Graphs
Multi Source Shortest Path
```

---

### Standard Dijkstra

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Time  : O((V + E) log V)
Memory: O(V)
```

##### Requirements

```
All weights >= 0
```

---

### Path Restore

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Restore Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Multi Source Dijkstra

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Nearest Hospital
Nearest Special Node
Spread Problems
```

---

### State Graph Dijkstra

#### Example States

```
(node , fuel)

(node , mask)

(node , coupons)

(node , parity)
```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Fuel Problems
Discount Coupons
Bitmask States
Extended Graphs
```

---

### Dense Graph Dijkstra

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V²)
```

##### Use

```
Dense Graph
n <= 5000 تقريبًا
Adjacency Matrix
```

---

### Count Number Of Shortest Paths

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
CSES Investigation
Count Shortest Paths
```

---

### Shortest Path DAG After Dijkstra

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
All Shortest Paths
DP On Shortest Paths
```

---

### Dijkstra On Grid

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Weighted Grid
Minimum Cost Path
```

---

### K Shortest Paths (Intro)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
CSES Flight Routes
K Shortest Paths
```

---

### Useful Snippets

#### Unreachable Nodes

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Farthest Reachable Node

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Shortest Path Length

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Check Negative Edge

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

```
Weights >= 0
=> Dijkstra

Weights 0/1
=> 0-1 BFS

Negative Edge
=> Bellman Ford

Multi Source
=> Push all sources initially

Path Restore
=> parent array

State Graph
=> expand state dimension

Count Paths
=> ways array

Shortest Path DAG
=> dist[v] = dist[u] + w
```

---

### Common Problems

```
Shortest Routes I

Message Route (weighted)

Flight Discount

Investigation

Flight Routes

Road Reparation Variants

Weighted Grid

Fuel Problems

Coupon Problems

State Graph Problems
```

### Kruskal (Minimum Spanning Tree)

#### When To Use

```
Minimum Spanning Tree (MST)

Connect all nodes
Minimum total cost

Build MST from weighted graph
```

---

### DSU Required

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Standard Kruskal

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Sorting : O(E log E)

DSU     : O(E α(N))

Total   : O(E log E)
```

##### Memory

```
O(E)
```

---

### Check If MST Exists

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Graph is disconnected
No spanning tree exists
```

---

### Store MST Edges

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Need actual MST
Need MST graph
Second MST
LCA on MST
```

---

### Build MST Graph

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
LCA
Max Edge Query
Second MST
Tree Queries
```

---

### Maximum Spanning Tree

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Everything else remains the same.

##### Use

```
Maximum total weight tree
```

---

### Number Of Connected Components

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Forest Cost

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Minimum Spanning Forest
```

##### Use

```
Disconnected Graph
```

---

### Second MST Idea

#### Observation

```
MST + One Extra Edge
```

For every non-MST edge:

```
Add edge

Find maximum edge
on path(u,v) inside MST

Replace it
```

Usually solved using:

```
LCA
Binary Lifting
Maximum Edge Query
```

##### Complexity

```
O(E log N)
```

---

### Useful Snippets

#### Sort Edges

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### MST Cost

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Number Of MST Edges

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Should be:

```
n - 1
```

for connected graph.

---

#### Check Same Component

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Detect Cycle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

```
Sort edges by weight

Take smallest valid edge

Skip edge creating cycle

DSU handles connectivity

Used edges = n - 1

MST always forms a tree

MST may not be unique

Negative edges are allowed

Self loops never help
```

---

### Common Problems

```
Road Reparation

Minimum Spanning Tree

Road Construction

Connect Cities

Building Roads

Second MST

MST Queries

Network Design

Satellite Network
```

---

### Prim vs Kruskal

| Feature | Kruskal | Prim |
| --- | --- | --- |
| Core DS | DSU | Priority Queue |
| Sort Edges | Yes | No |
| Dense Graph | Worse | Better |
| Sparse Graph | Excellent | Excellent |
| Most CP Problems | ✅ | Less Common |

##### Rule

```
Sparse Graph
=> Kruskal

Dense Graph
=> Prim
```

### Bellman Ford

#### When To Use

```
Negative Edge Weights

Shortest Path

Negative Cycle Detection

Difference Constraints

When Dijkstra Cannot Be Used
```

---

### Edge Structure

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Standard Bellman Ford

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Time  : O(V * E)

Memory: O(V)
```

---

### Negative Cycle Detection

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
There exists a reachable negative cycle.
```

---

### Path Restore

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Restore Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Restore Negative Cycle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### No Cycle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Move Inside Cycle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Extract Cycle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(V * E)
```

---

### Difference Constraints

#### Constraints

```
x[v] - x[u] <= w
```

Convert to edge:

```
u -> v (weight w)
```

Then run:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Scheduling
Inequalities
Constraint Systems
```

---

### Detect Any Negative Cycle

Sometimes source is unknown.

Create super source:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Detect cycle anywhere in graph
```

---

### Longest Path Trick

If graph has no positive cycle:

```
maximize path
```

Convert:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Warning

```
Need cycle handling
```

---

### Reachability From Negative Cycle

After detecting cycle nodes:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

from cycle vertices.

##### Use

```
Infinite Profit
Infinite Path
CSES High Score
```

---

### Useful Snippets

#### Unreachable Node

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Reachable Node

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Early Stop Optimization

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Benefit

```
Much faster in practice
```

---

### Common Tricks

```
Negative Edge
=> Bellman Ford

Negative Cycle
=> nth relaxation

Unknown Source
=> Super Source

Difference Constraints
=> Bellman Ford

Path Restore
=> parent array

Infinite Profit
=> detect cycle then DFS
```

---

### Common Problems

```
Cycle Finding

High Score

Difference Constraints

Wormholes

Time Machine

Negative Cycle Detection

System Of Inequalities
```

---

### Dijkstra vs Bellman

| Feature | Dijkstra | Bellman |
| --- | --- | --- |
| Negative Edge | ❌ | ✅ |
| Negative Cycle | ❌ | ✅ |
| Complexity | O(E log V) | O(VE) |
| Path Restore | ✅ | ✅ |

##### Rule

```
Weights >= 0
=> Dijkstra

Negative Edge Exists
=> Bellman Ford
```

### Floyd Warshall

#### When To Use

```
All Pairs Shortest Path (APSP)

Small Graph

Transitive Closure

Reachability

Path Restoration

Minimum Cycle

Character Transformations
```

---

### Standard Floyd Warshall

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Main Floyd

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
Time  : O(N³)

Memory: O(N²)
```

---

### Undirected Graph

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Multiple Edges

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Query Distance

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Unreachable Nodes

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Negative Cycle Detection

After Floyd:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Why?

```
Shortest path
from node to itself

must be 0

unless negative cycle exists
```

---

### Path Restoration

#### Parent Matrix

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Initialization

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Floyd Update

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Restore Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### No Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Transitive Closure

Instead of shortest path:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Initialization

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Floyd

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Can i reach j from i ?
```

---

### Minimum Directed Cycle

After Floyd:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Note

```
Works if cycle exists
```

---

### Character Conversion Problems

Example:

```
a -> b cost 3

b -> c cost 5

Find minimum cost
to convert strings
```

---

##### Build Graph

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Run Floyd.

##### Use

```
26 letters only

Perfect Floyd problem
```

---

### Floyd On States

Example:

```
Digits
Letters
Small DP States
```

Whenever:

```
nodes <= 500
```

Think about:

```
Floyd Warshall
```

---

### APSP Queries

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Total

```
Preprocess : O(N³)

Query      : O(1)
```

---

### Useful Snippets

#### Check Reachability

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Check Same SCC (small graph)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Mutually reachable
```

---

#### Count Reachable Nodes

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

```
APSP
=> Floyd

Reachability
=> Floyd Boolean

Negative Cycle
=> dist[i][i] < 0

Path Restore
=> nxt matrix

Character Conversion
=> Floyd

Many Queries
=> Floyd

Small Graph
=> Floyd
```

---

### Common Problems

```
Shortest Routes II

Greg and Graph

Character Conversion

Transitive Closure

Reachability Queries

All Pairs Shortest Path

Minimum Cycle

String Transformation
```

---

### Dijkstra vs Floyd

| Feature | Dijkstra | Floyd |
| --- | --- | --- |
| Single Source | ✅ | ❌ |
| All Pairs | ❌ | ✅ |
| Negative Edge | ❌ | ✅ |
| Negative Cycle Detection | ❌ | ✅ |
| Complexity | O(E log V) | O(N³) |

##### Rule

```
One Source
=> Dijkstra

All Pairs
=> Floyd
```

---

### Bellman vs Floyd

| Feature | Bellman | Floyd |
| --- | --- | --- |
| Single Source | ✅ | ❌ |
| All Pairs | ❌ | ✅ |
| Negative Cycle | ✅ | ✅ |
| Complexity | O(VE) | O(N³) |

##### Rule

```
Need all pairs
=> Floyd

Need one source
=> Bellman
```


## 3) Trees & Binary Lifting

### Binary Lifting

#### When To Use

```
Kth Ancestor

Jump Up K Levels

Tree Queries

LCA Preparation

Fast Ancestor Queries
```

---

### Idea

Instead of moving:

```
1 step
1 step
1 step
1 step
...
```

Precompute:

```
2^0 ancestor
2^1 ancestor
2^2 ancestor
2^3 ancestor
...
```

Then jump using binary representation of k.

---

### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Jump K Levels

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log N)
```

---

### Kth Ancestor

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Example

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Meaning:

```
3rd ancestor of node 10
```

---

### Check Ancestor

Needs Euler Tour.

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(1)
```

---

### Lift To Same Depth

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
LCA
Path Queries
```

---

### Distance To Root

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Number of edges
from root to u
```

---

### Build Complexity

```
O(N log N)
```

---

### Query Complexity

```
Jump
Ancestor
Lift

O(log N)
```

---

### Memory

```
O(N log N)
```

---

### Useful Snippets

#### Parent

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Grand Parent

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### 4th Ancestor

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

because:

```
2² = 4
```

---

#### Move Up One Level

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Move Up 13 Levels

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Root Check

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

```
up[u][j]
=
2^j ancestor

jump(u,k)
=
binary representation of k

depth difference
=
jump larger node upward

LCA
=
Binary Lifting + Depth

Distance
=
Depth + LCA
```

---

### Common Problems

```
Company Queries I

Company Queries II

Kth Ancestor

Tree Queries

Jump Queries

LCA

Path Queries
```

---

### Maximum N Guide

| N | LG |
| --- | --- |
| 1e5 | 17 |
| 2e5 | 18 |
| 5e5 | 19 |
| 1e6 | 20 |

##### Safe Choice

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

for:

```
N <= 1e6
```

---

### Common Mistakes

#### Wrong

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

may be accessed.

---

#### Safer

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Wrong LG

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

while:

```
N = 2e5
```

---

#### Safe

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Notes

```
Binary Lifting alone does NOT solve LCA.

It is only the preprocessing layer.

Next topic:
LCA
```

### LCA (Lowest Common Ancestor)

#### When To Use

```
Tree Queries

Distance Between Nodes

Path Queries

Kth Node On Path

Common Ancestor

Query On Path
```

---

### Idea

```
LCA(u,v)

=
deepest node

that is ancestor of both
```

Example:

```
     1
   /   \
  2     3
 / \
4   5
```

```
LCA(4,5) = 2

LCA(4,3) = 1
```

---

### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### LCA Query

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log N)
```

---

### Distance Between Two Nodes

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log N)
```

---

### Kth Ancestor

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Check Ancestor

Needs Euler Tour.

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(1)
```

---

### Kth Node On Path

Path:

```
u -------- v
```

Suppose:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Lengths

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Query

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
SPOJ QTREE2
```

---

### Length Of Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

returns:

```
number of edges
```

---

### Number Of Nodes On Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Check If Node Lies On Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log N)
```

---

### Find Parent

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Find Root Distance

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Path Through LCA

Every path:

```
u -> lca

+

lca -> v
```

Remember this.

Used everywhere.

---

### Useful Snippets

#### LCA

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Distance

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Parent

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Grand Parent

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Jump 10 Levels

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Same Depth

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

```
Distance

=
depth[u]
+
depth[v]
-
2 * depth[lca]
```

---

```
Path

=
u -> lca -> v
```

---

```
Nodes On Path

=
Distance + 1
```

---

```
Node On Path

=
dist(a,x)
+
dist(x,b)
=
dist(a,b)
```

---

```
Kth Ancestor

=
jump()
```

---

```
Kth Node On Path

=
LCA + Jump
```

---

### Complexity Summary

| Operation | Complexity |
| --- | --- |
| Build | O(N log N) |
| LCA | O(log N) |
| Distance | O(log N) |
| Jump | O(log N) |
| Kth Ancestor | O(log N) |
| Kth Node Path | O(log N) |

---

### Memory

```
O(N log N)
```

---

### Common Problems

```
Distance Queries

Company Queries II

LCA Queries

Tree Distance

Kth Ancestor

QTREE2

Path Queries

Tree Navigation
```

---

### ACPC Notes

Most common formulas:

#### Distance

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Number Of Nodes

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Node On Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Path

```
u -> lca -> v
```

If you remember only these four,
you can solve a huge number of tree problems.


## 4) Strings

### KMP (Knuth-Morris-Pratt)

#### When To Use

```
Pattern Matching

Find occurrences of a string

Borders

Prefix = Suffix

Periodicity

String DP
```

---

### Prefix Function

#### Definition

```
pi[i]

=
length of longest proper prefix

which is also suffix

for s[0...i]
```

---

Example

```
s = "ababaca"

pi =

0 0 1 2 3 0 1
```

---

### Prefix Function Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(N)
```

##### Memory

```
O(N)
```

---

### Pattern Matching

Find all occurrences of:

```
pattern p

inside

text t
```

---

##### Build String

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Compute Prefix

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Occurrences

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(N + M)
```

---

### KMP Search Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Longest Border

Border means:

```
Prefix

=

Suffix
```

but not entire string.

---

##### Answer

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(N)
```

---

### All Borders

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(N)
```

---

### Count Occurrences Of Every Prefix

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
cnt[len]

=

number of occurrences
of prefix length len
```

---

### String Period

Example:

```
abcabcabcabc
```

Period:

```
abc
```

Length:

```
3
```

---

##### Formula

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Check

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Smallest Period

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Prefix Automaton Jump

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Meaning

```
Go to next valid border
```

This is the whole magic of KMP.

---

### Distinct Prefix-Suffix Chain

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Use

```
Borders Problems
```

---

### Useful Snippets

#### Prefix Array

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Longest Border

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Check Border Length K

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Number Of Occurrences

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### First Occurrence

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

```
Longest Border

=
pi.back()
```

---

```
All Borders

=
follow pi chain
```

---

```
Pattern Matching

=
pattern#text
```

---

```
String Period

=
n - pi.back()
```

---

```
Occurrences Of Prefix

=
count over pi
```

---

```
KMP

=
linear time matching
```

---

### Complexity Summary

| Operation | Complexity |
| --- | --- |
| Prefix Function | O(N) |
| Pattern Matching | O(N+M) |
| Borders | O(N) |
| Period | O(N) |

---

### Common Problems

```
Finding Borders

Pattern Matching

Password (CF)

Periodic String

Prefix Occurrences

Text Search

String Compression

Prefix-Suffix Problems
```

---

### ACPC Notes

Most used formulas:

#### Longest Border

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Smallest Period

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Pattern Matching

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Border Chain

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

These four cover the majority of KMP problems.


## 5) Range Query Data Structures

### Segment Tree

#### Basic Segment Tree

##### Operation

```
Point Update
```

##### Query

```
Range Minimum
```

##### Complexity

| Operation | Complexity |
| --- | --- |
| Build | O(n) |
| Update | O(log n) |
| Query | O(log n) |
| Memory | O(n) |

---

##### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Common Modifications

##### Range Sum

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Identity:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Range Maximum

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Identity:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Range GCD

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Identity:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Range XOR

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Identity:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Notes

```
Most Segment Trees
only change:

Node

merge()

identity value
```

### Lazy Segment Tree

#### Range Assign + Range Minimum

##### Operation

```
Assign value to range
```

##### Query

```
Minimum on range
```

##### Complexity

| Operation | Complexity |
| --- | --- |
| Build | O(n) |
| Update | O(log n) |
| Query | O(log n) |
| Memory | O(n) |

---

##### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Other Important Lazy Versions

```
Range Add + Sum

Range Add + Min

Range Assign + Sum

Range Assign + Min
```

---

#### Rule

```
Lazy Segment Tree

=

Basic Segment Tree

+

Lazy Operation
```

Usually only:

Node

merge()

propagate()

change.

### Sparse Table

#### Usage

```
Static Array

No Updates

Many Queries
```

Works best for:

```
Range Minimum Query (RMQ)

Range Maximum Query

GCD Query

AND / OR Query
```

---

#### Complexity

| Operation | Complexity |
| --- | --- |
| Build | O(n log n) |
| Query | O(1) |
| Memory | O(n log n) |

---

#### Requirement

```
Operation must be idempotent

Examples:

min(a,a)=a
max(a,a)=a
gcd(a,a)=a

Works ✅
```

```
sum

xor

product

Do NOT work with O(1) sparse table
```

---

### Range Minimum Query

##### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Query

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(1)
```

---

### Range Maximum Query

Change only:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Range GCD Query

Change only:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

#### Maximum Frequency Of Query

Many problems:

```
Q = 2e5

N = 2e5
```

Sparse Table is usually better than Segment Tree.

Reason:

```
O(1)

instead of

O(log n)
```

---

#### Binary Search + Sparse Table

Very common.

Example:

```
Find first position

such that

min(l,pos) <= x
```

Use:

```
Binary Search

+

Sparse Table
```

---

#### GCD Segment Problems

Common pattern:

```
gcd(l,r)
```

inside binary search.

Sparse Table is ideal.

---

### Memory

```
n log n
```

For:

```
n = 2e5
```

About:

```
3.6 million integers
```

Safe.

---

### Limitations

```
No Updates

Static Array Only
```

If updates exist:

```
Use Segment Tree
```

---

### Most Common Uses

```
RMQ

Maximum Query

GCD Query

Binary Search + RMQ

Binary Search + GCD

LCA (Euler Tour + Sparse Table)
```


## 6) STL, Two Pointers & Monotonic Techniques

### Ordered Set (PBDS)

#### Include

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Create

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Insert

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log n)
```

---

#### Erase

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log n)
```

---

#### Count Elements Smaller Than x

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Example:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Returns:

```
count of elements < 10
```

##### Complexity

```
O(log n)
```

---

#### K-th Element

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Example:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Returns:

```
smallest element
```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Returns:

```
second smallest
```

##### Complexity

```
O(log n)
```

---

#### Size

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Exists

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Common Tricks

#### Count <= x

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Count > x

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Count >= x

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Ordered Multiset

Duplicates Allowed

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Insert Duplicate

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Erase One Occurrence

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Complexity

| Operation | Complexity |
| --- | --- |
| Insert | O(log n) |
| Erase | O(log n) |
| order_of_key | O(log n) |
| find_by_order | O(log n) |

---

### Most Common Uses

```
K-th Smallest

Inversion Count

Order Statistics

Online Ranking

Dynamic Median

Dynamic K-th Element
```

### STL Advanced Tricks

---

### Set As Next Pointer

#### Idea

Store all alive positions.

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Remove Segment

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(total_removed * log n)
```

Each element removed once.

---

#### Uses

```
Destroy Array

Paint Segments

Offline Updates

Next Alive Position

Skip Processed Nodes
```

---

### Dynamic Mex

#### Idea

Store all missing values.

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Answer

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Update

Insert number:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Remove number:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(log n)
```

---

#### Uses

```
Online Mex

Dynamic Mex

Replacement Operations
```

---

### Difference Map

#### Idea

Coordinates too large.

```
1e18
```

Use:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

instead of:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Sweep

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Intervals

Coverage

Huge Coordinates

Sweep Line
```

---

### Frequency Of Frequency

#### Idea

Store:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

and

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

where:

```
cnt[f]
=
how many numbers appear exactly f times
```

---

#### Update

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Query

Check if frequency exists:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Mo Algorithm

Frequency Queries

Maximum Frequency

Equal Frequencies
```

---

### Lazy Deletion

#### Problem

Priority Queue has no:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Solution

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Delete:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Clean Top

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Sliding Window Maximum

Dynamic Maximum

Median Problems
```

---

### Coordinate Compression

#### Important Rule

Compress:

```
Array

Queries

Updates

Endpoints
```

Together.

---

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Compress

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Recover

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Fenwick

Segtree

Sweep Line

Offline Queries
```

---

### Offline Sort Trick

#### Idea

Sort:

```
Values

Queries
```

by same key.

---

#### Example

Count elements:

```
> k
```

inside range.

---

#### Process

```
Sort values descending

Sort queries descending by k

Insert values gradually
```

---

#### Uses

```
Fenwick

Segment Tree

DSU

Range Queries
```

---

### Small To Large

#### Idea

Always merge smaller container.

---

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n log² n)
```

instead of

```
O(n²)
```

---

#### Uses

```
DSU On Tree

Map Merge

Set Merge

Color Frequency Problems
```

---

### Custom Hash

#### Problem

unordered_map

can be hacked.

---

#### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Usage

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Codeforces Hacks

Large Hash Tables

Fast Frequency Maps
```

---

### Multiset Median Trick

#### Idea

Maintain:

```
Left Half

Right Half
```

---

#### Invariant

```
|left|

=
|right|

or

|left| = |right| + 1
```

---

#### Median

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Sliding Window Median

Running Median
```

---

### Order Statistics Trick

#### Count Inside Range

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### K-th Element

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Dynamic Ranking

K-th Smallest

Online Queries
```

---

### Multiset Min-Max Window

#### Idea

Maintain window values.

---

#### Maximum

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Minimum

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Window Difference

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Longest Window

Max-Min <= K

Sliding Window Constraints
```

---

### Set + Binary Search

#### Idea

Nearest Element

---

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Check:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

and

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Closest Number

Nearest Tower

Nearest Value
```

---

### Top 5 Must-Know STL Tricks

```
Set As Next Pointer

Frequency Of Frequency

Lazy Deletion

Coordinate Compression

Small To Large
```

These appear repeatedly in:

```
ECPC

ACPC

Codeforces Div2/Div1
```

### Two Pointers Advanced Patterns

---

### Recognition Checklist

Think about Two Pointers if you see:

```
Subarray

Contiguous Segment

Longest

Shortest

At Most

Exactly

Distinct

Window
```

---

### Longest Valid Segment

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Longest Distinct Subarray

Longest Sum <= K

Longest Window
```

---

### Shortest Valid Segment

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Minimum Window

Shortest Sum >= K

Cover All Characters
```

---

### Count Subarrays Trick

#### Observation

When window:

```
[l,r]
```

is valid.

Then all:

```
[l,r]

[l+1,r]

[l+2,r]

...

[r,r]
```

are valid.

---

#### Formula

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Count Subarrays

At Most K Distinct

At Most K Odd

At Most K Zeros
```

---

### Exactly K Trick

#### Formula

```
Exactly(K)

=

AtMost(K)

-

AtMost(K-1)
```

---

#### Uses

```
Exactly K Distinct

Exactly K Odd

Exactly K Ones

Exactly K Special Elements
```

---

### Distinct Elements Window

#### State

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Add

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Remove

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
K Distinct

Unique Window

Longest Distinct
```

---

### Positive Sum Window

#### Condition

Array must be:

```
Positive
```

or

```
Non Negative
```

---

#### Works

```
sum <= k

sum < k

sum >= k
```

---

#### Doesn't Work

```
Negative Numbers
```

---

### Binary Array Trick

#### Maintain

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Common Problems

```
Flip K Zeros

Longest Ones

At Most K Zeros

Maximum Consecutive Ones
```

---

### Circular Array Trick

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Then run:

```
Two Pointers
```

on:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Circular Window

Circular Subarray

Ring Problems
```

---

### Two Pointers On Sorted Array

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Two Sum

Closest Pair

Difference Constraints

Pair Counting
```

---

### Pair Sum = X

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Pair Difference >= K

#### Observation

Sort.

Move:

```
r only forward
```

---

Complexity:

```
O(n)
```

instead of:

```
O(n²)
```

---

### Merge Two Sorted Arrays

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Move smaller pointer.

---

#### Complexity

```
O(n+m)
```

---

### Common Mistakes

#### Negative Numbers

Usually break:

```
Sliding Window

Two Pointers
```

---

#### Non-Monotonic Conditions

Condition must become valid again by:

```
moving l
```

Otherwise:

```
Two Pointers ❌
```

---

### Top 5 Patterns

```
Longest Valid Segment

Shortest Valid Segment

Count Subarrays

Exactly K Trick

Two Pointers On Sorted Array
```

These alone solve a huge percentage of Two Pointer problems.

### Sliding Window Advanced Patterns

---

### Recognition Checklist

Think about Sliding Window if you see:

```
Subarray

Contiguous Segment

Window

Longest

Shortest

Fixed Length

Distinct

Frequency Constraint
```

---

### Fixed Length Window

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

#### Uses

```
Maximum Sum Length K

Minimum Sum Length K

Average Queries

Fixed Window Problems
```

---

### Variable Length Window

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Longest Window

Shortest Window

Distinct Constraints
```

---

### Minimum Cover Window

#### Problem

Find smallest segment containing:

```
all characters

all colors

all values
```

---

#### Pattern

Expand:

```
r
```

until valid.

Shrink:

```
l
```

while still valid.

---

#### Uses

```
Minimum Window Substring

Cover All Types

Smallest Valid Segment
```

---

### Frequency Window

#### State

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

or

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Add

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Remove

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Distinct

Most Frequent

Frequency Constraints
```

---

### Distinct Count Window

#### State

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Add

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Remove

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
At Most K Distinct

Exactly K Distinct

Longest Distinct
```

---

### At Most K Trick

#### Count

```
Subarrays
```

with:

```
At Most K
```

---

#### Formula

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Why

All windows ending at:

```
r
```

are valid.

---

### Exactly K Trick

#### Formula

```
Exactly(K)

=

AtMost(K)

-

AtMost(K-1)
```

---

#### Uses

```
Distinct

Odd Numbers

Special Values
```

---

### Window Maximum

#### Naive

```
O(nk)
```

---

#### Better

Use:

```
Monotonic Queue
```

---

Complexity:

```
O(n)
```

---

### Window Minimum

Same idea.

Use:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Min Window

Max Window

DP Optimization
```

---

### Sliding Median

#### Idea

Maintain:

```
Left Half

Right Half
```

using:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(log n)
```

per operation.

---

#### Uses

```
Median Window

Online Median
```

---

### Sliding Mex

#### Idea

Maintain:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

and:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Answer:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(log n)
```

---

### Binary Array Window

#### State

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Common Problems

```
Flip K Zeros

Longest Ones

At Most K Zeros

Maximum Consecutive Ones
```

---

### Circular Window

#### Trick

Duplicate array.

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Run window on:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Circular Array

Ring Problems
```

---

### Monotonic Condition

Sliding Window works when:

```
Adding elements

can only make condition worse

or better

monotonically
```

---

Examples

```
Distinct <= K

Sum <= K

Zeros <= K
```

---

Usually NOT

```
Negative Numbers

Non-monotonic Constraints
```

---

### Common Hidden Observation

If:

```
l only moves forward

r only moves forward
```

Then:

```
O(n)
```

even if there is:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

inside loop.

---

### Most Important Patterns

```
Fixed Length Window

Minimum Cover Window

At Most K

Exactly K

Window Maximum

Window Minimum

Sliding Median

Sliding Mex
```

---

### Contest Checklist

If problem contains:

```
Subarray

Longest

Shortest

At Most

Exactly

Window

Distinct
```

Check:

```
Sliding Window
```

before trying:

```
Binary Search

Segment Tree

DP
```

### Monotonic Stack

---

### Recognition Checklist

Think about Monotonic Stack if you see:

```
Nearest

First Greater

First Smaller

Contribution

Histogram

Subarray Minimum

Subarray Maximum
```

---

### Next Greater Element

#### Problem

For every index:

```
First Greater To The Right
```

---

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

### Previous Greater Element

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Next Smaller Element

#### Pattern

Replace:

```
<=
```

with

```
>=
```

---

#### Uses

```
Histogram

Subarray Minimum
```

---

### Previous Smaller Element

Same idea.

---

### Strict vs Non Strict

Very Important

For duplicates:

```
<
<=
>
>=
```

changes answer.

---

Common choice:

```
Left  -> Strict

Right -> Non Strict
```

or opposite.

---

Used in:

```
Contribution Problems
```

---

### Largest Rectangle In Histogram

#### Idea

Find:

```
Previous Smaller

Next Smaller
```

---

Width

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Area

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

### Contribution Technique

#### Problem

Sum of:

```
Subarray Minimums
```

---

Observation:

Count how many subarrays use:

```
a[i]
```

as minimum.

---

Contribution

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Where

```
left
=
choices on left

right
=
choices on right
```

---

#### Uses

```
Subarray Minimums

Subarray Maximums

Range Contributions
```

---

### Sum Of Subarray Minimums

#### Formula

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

### Sum Of Subarray Maximums

Same idea.

Use:

```
Greater
```

instead of:

```
Smaller
```

---

### Max-Min Of All Subarrays

#### Formula

```
Contribution As Maximum

-

Contribution As Minimum
```

---

Very common trick.

---

### Monotonic Increasing Stack

Stack contains:

```
Increasing Values
```

---

Pop while:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Used for:

```
Minimums

Smaller Elements
```

---

### Monotonic Decreasing Stack

Stack contains:

```
Decreasing Values
```

---

Pop while:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Used for:

```
Maximums

Greater Elements
```

---

### Remove K Digits

Classic problem.

---

Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Uses

```
Greedy + Stack
```

---

### Valid Parentheses

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Push:

```
(
[
{
```

Pop:

```
)
]
}
```

---

Uses

```
Bracket Problems
```

---

### Next Greater Circular

#### Trick

Loop:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Use:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

### Common Observation

Every element:

```
Push Once

Pop Once
```

Therefore:

```
O(n)
```

not:

```
O(n²)
```

---

### Most Important Patterns

```
Next Greater

Next Smaller

Histogram

Contribution Technique

Subarray Minimums

Subarray Maximums

Max-Min Contribution
```

---

### Contest Checklist

If problem asks:

```
Nearest Greater

Nearest Smaller

First Bigger

Histogram

Contribution

Subarray Minimum

Subarray Maximum
```

Think:

```
Monotonic Stack
```

before:

```
Segment Tree

Sparse Table
```

### Monotonic Queue (Deque Tricks)

---

### Recognition Checklist

Think about Monotonic Queue if you see:

```
Sliding Window Maximum

Sliding Window Minimum

Fixed Length Window

Range Maximum

Range Minimum

DP Optimization
```

---

### Why Not Multiset?

Window Max using:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Complexity:

```
O(n log n)
```

---

Monotonic Queue:

```
O(n)
```

---

### Sliding Window Maximum

#### Problem

For every window:

```
length = k
```

find:

```
maximum
```

---

#### Pattern

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

### Sliding Window Minimum

#### Pattern

Replace:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

with:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Answer:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Complexity

```
O(n)
```

---

### Understanding The Queue

Queue stores:

```
indices
```

not values.

---

Values are:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Why O(n)?

Every index:

```
Enter Once

Leave Once
```

---

Total:

```
O(n)
```

---

### Fixed Window Max

#### Example

```
Maximum of every subarray
length k
```

---

Classic application.

---

### Fixed Window Min

Same idea.

---

### Min-Max Window

Maintain:

```
One Max Queue

One Min Queue
```

---

Window Difference:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Uses

```
Max - Min <= K

Longest Valid Window
```

---

### Longest Window With

#### Condition

```
max(window)
-
min(window)
<= k
```

---

#### Pattern

Two Pointers

- 

Monotonic Queue

---

#### Complexity

```
O(n)
```

---

### DP Optimization

#### Form

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

inside window.

---

Example

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

for

```
i-k <= j < i
```

---

Use:

```
Monotonic Queue
```

---

Complexity

```
O(n)
```

instead of:

```
O(nk)
```

---

### Shortest Subarray >= K

#### Famous Problem

Contains:

```
Prefix Sum

Deque
```

---

Pattern

Store prefix sums in:

```
Increasing Order
```

---

Uses

```
Negative Numbers
```

where normal sliding window fails.

---

### Queue Types

#### Maximum Queue

Pop:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Answer

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Minimum Queue

Pop:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Answer

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Circular Array Trick

Duplicate:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Run deque normally.

---

Uses

```
Circular Window Maximum

Circular Window Minimum
```

---

### Common Mistakes

#### Store Values

Wrong.

Store:

```
indices
```

---

Because we need:

```
window expiration
```

---

#### Forget Removing Old Index

Must remove:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

when outside window.

---

Otherwise:

```
Wrong Answer
```

---

### Comparison

```
Multiset

O(n log n)
```

---

```
Monotonic Queue

O(n)
```

---

### Most Important Patterns

```
Sliding Window Maximum

Sliding Window Minimum

Max-Min Window

DP Optimization

Shortest Subarray >= K
```

---

### Contest Checklist

If problem contains:

```
Window Maximum

Window Minimum

Range Max In Sliding Window

Range Min In Sliding Window

DP Window Transition
```

Think:

```
Monotonic Queue
```

before:

```
Segment Tree

Sparse Table

Multiset
```

---

### Top 3 Uses In Contests

```
Sliding Window Maximum

Sliding Window Minimum

DP Optimization
```

These appear much more often than the rest.

### Number Theory Handbook (ACPC)

---

### Core Functions

#### GCD

##### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log(min(a,b)))
```

##### Uses

- Coprime checking
- Fractions
- Number theory
- LCM

##### Facts

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### LCM

##### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log(min(a,b)))
```

##### Facts

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Warning

Bad

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Good

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Binary Power

##### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log b)
```

##### Uses

- Powers
- Modular arithmetic
- Combinatorics

---

#### Modular Power

##### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log b)
```

---

### Extended Euclid

#### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Returns

```
ax+by=gcd(a,b)
```

##### Complexity

```
O(log n)
```

##### Uses

- Modular inverse
- Diophantine equations
- CRT

---


## 7) Math & Number Theory

### Modular Arithmetic

#### Normalize Mod

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Addition

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Subtraction

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Multiplication

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Division

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Never:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Modular Inverse

#### Fermat

##### Condition

```
mod must be prime
```

##### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log mod)
```

---

#### Recursive Inverse

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log mod)
```

---

#### Extended Euclid Inverse

##### Condition

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Works For

```
Non-prime mod
```

---

#### Generate All Inverses

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(n)
```

---

#### Facts

##### Inverse Exists iff

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Product

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Factorials

#### Build Factorial

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(n)
```

---

#### Inverse Factorials

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(n)
```

---

#### nCr

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(1)
```

---

### Legendre Formula

#### Power Of Prime Inside n!

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(logp(n))
```

##### Uses

- Trailing zeros
- Factorial divisibility
- nCr factorization

---

#### Trailing Zeros In n!

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Why?

```
2s are always more than 5s
```

---

#### Prime Exponent In nCr

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Check m | n!

Factorize:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Check

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

for every prime.

---

### Diophantine Equations

#### Equation

```
ax+by=c
```

---

#### Solution Exists iff

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### One Solution

From

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Multiply by

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### General Solution

Let

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Positive Solutions

Move

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

until

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Euler Phi

#### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(sqrt(n))
```

---

#### Meaning

Count numbers

```
1 <= x <= n
```

such that

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Facts

##### Prime

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Prime Power

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Multiplicative

If

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Divisor Identity

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

over all divisors d of n.

---

#### Euler Theorem

If

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Prime Testing

#### Trial Division

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(sqrt(n))
```

---

#### Miller Rabin

##### Complexity

```
O(log³ n)
```

##### Range

```
up to 1e18
```

---

### Linear Sieve

#### Function

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(n)
```

##### Gives

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

smallest prime factor.

---

### Prime Factorization

#### Using SPF

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(log n)
```

---

### Divisors

#### Number Of Divisors

If

```
n=p1^a1*p2^a2...
```

Then

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Sum Of Divisors

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Product Of Divisors

If

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Harmonic Lemma

#### Fact

Distinct values of

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

are only

```
O(sqrt(n))
```

---

#### Loop

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

##### Complexity

```
O(sqrt(n))
```

---

### Important Facts

#### Coprime

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Consecutive Numbers

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Count Multiples In [1,n]

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Count Multiples In [l,r]

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

#### Distinct Prime Factors

Maximum for

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

is

```
15
```

---

#### Maximum Number Of Divisors

For

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

maximum is approximately

```
103680
```

---

#### Factorization Limits

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

usually acceptable.

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

not acceptable.

Use

```
Miller Rabin
Pollard Rho
```

---

### Must Know For ACPC

1. gcd
2. lcm
3. binary power
4. modular power
5. exgcd
6. modular inverse
7. factorial
8. inverse factorial
9. nCr
10. Legendre
11. phi
12. linear sieve
13. SPF factorization
14. divisor formulas
15. harmonic lemma
16. Miller Rabin

### Dynamic Programming - ACPC Reference

---


## 8) Dynamic Programming

### DP Mindset

Every DP problem has:

```
State      -> What defines the subproblem?
Transition -> How to move to next states?
Base Case  -> Smallest solvable state?
Answer     -> Which state contains final answer?
```

General Memoization Template:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Complexity Formula

Always calculate:

```
Time = States × Transitions
```

Example:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

States:

```
N × SUM
```

Transition:

```
2
```

Complexity:

```
O(N × SUM)
```

---

### 1D DP

---

### Fibonacci

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Transition:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Complexity:

```
O(N)
```

---

### Tricks

##### Rolling Memory

Instead of:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Use:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Memory:

```
O(1)
```

---

### Stair DP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Transition:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Used in:

```
Ways
Counting
Paths
```

---

### Prefix DP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Meaning:

```
Answer for first i elements
```

Common form:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

where

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Examples:

```
LIS
Partition DP
Word Break
```

---

### 0/1 Knapsack

---

### State

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Meaning:

```
Current item
Remaining capacity
```

---

### Recursive

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Iterative

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Important Tricks

##### Trick 1

Backward loop:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

means

```
Take Once
```

---

##### Trick 2

Forward loop:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

means

```
Take Infinite Times
```

---

##### Trick 3

Recover Solution

Store:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Then backtrack.

---

##### Trick 4

When:

```
W ≤ 1e5
```

Use capacity DP.

When:

```
Value ≤ 1e5
```

Use value DP.

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Complexity:

```
O(NW)
```

---

### Subset Sum

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Recursive

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Iterative

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### Count Solutions

Replace:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

with

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Find One Solution

Store:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Bitset Optimization

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Complexity:

```
O(N*S/64)
```

Huge optimization.

---

### Coin Change

---

### Count Ways

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### Combination

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Permutation

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

after choosing.

Very common trap.

---

### LCS

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Recursive

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### Recover String

Store choices.

---

##### SCS

```
Shortest Common Supersequence
```

Formula:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Edit Distance Relation

```
Insert/Delete only
```

Answer:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Complexity:

```
O(NM)
```

---

### LIS

---

### O(N²)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### O(N log N)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### Strict LIS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Non-Decreasing LIS

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Recover LIS

Store:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Count LIS

Need another DP.

---

### Grid DP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Recursive

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### Obstacles

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Minimum Cost

Replace:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

with

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Maximum Cost

Use:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Path Recovery

Store direction.

---

Complexity:

```
O(NM)
```

---

### DAG DP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Longest Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### Count Paths

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Longest Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Shortest Path

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Complexity:

```
O(V+E)
```

---

### Tree DP

---

### Independent Set

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tree DP Tricks

##### Subtree DP

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Rerooting

Need:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Diameter DP

Keep:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

largest depths.

---

##### Tree Matching

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

common.

---

Complexity:

```
O(N)
```

---

### Range DP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Recursive

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Recognition

Keywords:

```
Interval
Segment
Palindrome
Merge
Split
```

---

### Tricks

##### Length Order

Always build:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Partition Point

Usually:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Palindrome DP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

Complexity:

```
O(N³)
```

---

### Bitmask DP

Use when:

```
N ≤ 20
```

---

### Assignment DP

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Bit Tricks

Check:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Set:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Remove:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Count:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Submask Enumeration

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Tricks

##### TSP

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Assignment

State:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Partition DP

Enumerate submasks.

---

Complexity:

```
O(N*2^N)
```

---

### Digit DP

Use when:

```
Count numbers
between L and R
satisfying property
```

---

### State

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Template

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Most Important Digit DP Tricks

##### Count [L,R]

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Always.

---

##### Leading Zeros

Add state:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Divisibility

Add:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Digit Sum

Add:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Used Digits

Add:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

##### Binary Digit DP

Convert to bits.

Same idea.

---

Complexity

```
Digits × States
```

---

### DP Optimizations

---

### Rolling Array

Before:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

After:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

Memory:

```
O(M)
```

---

### State Compression

Before:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

After:

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Prefix Optimization

Before:

```
O(N²)
```

After:

```
O(N)
```

using prefix sums.

---

### Memory Estimate

```
1e6 int       = 4 MB
1e6 long long = 8 MB
```

---

### DP Recognition Cheat Sheet

| Pattern | State |
| --- | --- |
| Prefix | dp[i] |
| Grid | dp[i][j] |
| Strings | dp[i][j] |
| Interval | dp[l][r] |
| Tree | dp[u] |
| Tree Take/Leave | dp[u][2] |
| Subset | dp[mask] |
| TSP | dp[mask][last] |
| Digit | dp[pos][tight] |
| Counting | dp[state] += dp[next] |
| Min Cost | min(...) |
| Max Profit | max(...) |

---

### Most Important ACPC DP Topics

1. Knapsack
2. Subset Sum
3. Coin Change
4. LIS
5. LCS
6. Edit Distance
7. Grid DP
8. DAG DP
9. Tree DP
10. Range DP
11. Bitmask DP
12. Digit DP
13. Reconstruction
14. Rolling Array
15. Bitset DP
## 9) Missing Topics (Added)

### Fenwick Tree (BIT)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Complexity

- `add / prefix / range`: `O(log n)`

---

### SCC (Kosaraju)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### 2-SAT (Implication Graph)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Note

- Build SCC on implication graph; variable `x` is true if `comp[id(x,true)] > comp[id(x,false)]`.

---

### Dinic (Max Flow)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Note

- Use level graph BFS + blocking flow DFS.

---

### Trie (Lowercase)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Aho-Corasick (Pattern Matching)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Heavy-Light Decomposition (HLD)

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Mo's Algorithm

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Meet in the Middle

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

## 10) Comprehensive Missing Tricks & Function Ideas

### Foundations & Utilities: extra useful functions

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Extra ideas

- Coordinate-compress pairs/tuples when a value alone is not enough.
- Prefer `long long` in weighted/DP transitions by default.
- Keep one reusable `restore_path(par, target)` helper for graph and DP reconstructions.

---

### Graphs: missed patterns and tricks

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Common graph problem recognition

- **Shortest path + 0/1 edges** → 0-1 BFS.
- **Topological order + DAG transitions** → DAG DP.
- **Connectivity under edge additions** → DSU.
- **Offline connectivity with removals** → reverse process + DSU.
- **Constraints of form `x - y <= c`** → Bellman-Ford / SPFA model.

---

### Trees: missed ideas

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

---

### Strings: missed functions and patterns

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### String problem recognition

- Many pattern queries in one text → Aho-Corasick.
- Prefix/suffix border questions → prefix-function / Z-function.
- Need lexicographic cyclic operations → suffix-array / Booth-style ideas.

---

### Data Structures (DS): missed important functions

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### DS problem-type checklist

- Point update + prefix/range sum → Fenwick.
- Range update + range query → lazy segtree or two-BIT trick.
- Static idempotent range query (min/gcd/max) → sparse table.
- Order statistics with updates → PBDS / segtree over compressed values.

---

### Number Theory (NS): missed functions and ideas

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Number theory recognition

- Congruence system with multiple mods → CRT.
- Huge exponent with mod prime/composite → Euler/Fermat + fast power.
- Frequent factorization queries up to N → SPF sieve.

---

### Dynamic Programming (DP): missed important patterns

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### DP problem-type recognition (high-value)

- Sequence with local transitions → 1D DP.
- Partition into k groups with cost interval → D&C / Knuth candidates.
- State depends on subset of used elements → bitmask DP.
- Count strings/numbers with digit constraints → digit DP.
- Tree answer requiring include/exclude node states → tree DP with 2-state transitions.

---

### Final quick ACPC checklist by topic

- **Graphs:** shortest path family, SCC/2-SAT, flow, bridges/articulation, DSU offline.
- **DS:** Fenwick variants, segtree lazy, sparse table, PBDS/compression workflow.
- **Strings:** KMP + Z + Aho, hashing for O(1) substring compare.
- **Number theory (NS):** gcd/ext-gcd, inverses, CRT, sieve/SPF, modular power.
- **DP:** state design, transition proof, memory compression, reconstruction, optimization conditions.
- **Bits:** masks, subset iteration, popcount/parity, bitset acceleration, XOR basis patterns.

## 11) Bit Manipulation & Bitset

### Bit Operations Cheat Sheet

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Notes

- Use unsigned shifts for bit-heavy logic to avoid sign issues.
- For 64-bit masks, always shift with `1LL << i`.
- `x & (x-1)` removes the lowest set bit.

---

### Submask / Supmask Iteration Tricks

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Use Cases

- Subset DP transitions.
- Meet-in-the-middle state filtering.
- Inclusion-exclusion over selected features.

---

### Important Bit Tricks

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Problem Recognition

- `n <= 20` and "choose subset" → bitmask brute force / DP.
- Need to count enabled features fast → popcount.
- Need nearest differing state by one element → toggle one bit.

---

### Bitmask DP Starter Patterns

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### Complexity

- Bitmask DP over subsets: usually `O(n * 2^n)` or `O(n^2 * 2^n)`.
- SOS DP: `O(n * 2^n)`.

---

### std::bitset: How To Use

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### When bitset is strong

- Dense boolean DP states.
- Many OR/AND/XOR operations on big binary vectors.
- Fast subset-sum feasibility queries.

---

### XOR Basis (Linear Basis) – important bit module

```cpp\n#include <bits/stdc++.h>\nusing namespace std;\nusing ll = long long;\nconstexpr ll INF = (ll)4e18;\nconstexpr int MOD = 1'000'000'007;\n#define all(x) (x).begin(), (x).end()\n\nvoid solve() {\n // ...\n}\n\nint main() {\n ios::sync_with_stdio(false);\n cin.tie(nullptr);\n int t = 1; cin >> t;\n while (t--) solve();\n return 0;\n}\n```

#### XOR Basis Use Cases

- Maximum subset xor.
- Check if xor target is representable.
- Offline queries on xor-space (with prefix basis variants).

---

### Common Bit Problems Checklist

- Subset count / subset optimization.
- Min operations using toggles.
- Pair xor max/min.
- Gaussian elimination over GF(2) / xor basis.
- Profile DP on grids (state per row/column mask).





