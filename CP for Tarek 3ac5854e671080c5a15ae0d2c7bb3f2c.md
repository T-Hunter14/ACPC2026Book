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

- [General Template (clean)](#11-general-template-clean)
- [Coordinate Compression (Restore Values)](#13-coordinate-compression-restore-values)
- [Binary Search Template (First True)](#112-binary-search-template-first-true)
- [Ternary Search](#114-ternary-search)

### Graph quick links

- [BFS (Breadth First Search)](#25-bfs-breadth-first-search)
- [DFS (Depth First Search)](#217-dfs-depth-first-search)
- [Topological Sort](#238-topological-sort)
- [Dijkstra](#252-dijkstra)
- [Kruskal (Minimum Spanning Tree)](#268-kruskal-minimum-spanning-tree)
- [Bellman Ford](#284-bellman-ford)
- [Floyd Warshall](#298-floyd-warshall)

### Trees / Strings / Data structures quick links

- [Binary Lifting](#31-binary-lifting)
- [LCA (Lowest Common Ancestor)](#321-lca-lowest-common-ancestor)
- [KMP (Knuth-Morris-Pratt)](#41-kmp-knuth-morris-pratt)
- [Segment Tree](#51-segment-tree)
- [Lazy Segment Tree](#55-lazy-segment-tree)
- [Sparse Table](#57-sparse-table)

### Algorithmic patterns quick links

- [Two Pointers Advanced Patterns](#622-two-pointers-advanced-patterns)
- [Sliding Window Advanced Patterns](#638-sliding-window-advanced-patterns)
- [Monotonic Stack](#657-monotonic-stack)
- [Monotonic Queue (Deque Tricks)](#677-monotonic-queue-deque-tricks)
- [Modular Arithmetic](#71-modular-arithmetic)
- [DP Mindset](#81-dp-mindset)

### Newly added techniques quick links

**Foundations**
- [Overflow-Safe Multiplication (`__int128`)](#115-overflow-safe-multiplication-__int128)
- [Fixed-Precision Output](#116-fixed-precision-output)
- [Fast Input For Large N](#117-fast-input-for-large-n)
- [Reading Until EOF](#118-reading-until-eof)
- [Local Benchmark Timer](#119-local-benchmark-timer)

**Graphs**
- [DSU With Rollback](#23-dsu-with-rollback)
- [Weighted / Parity DSU](#24-weighted-parity-dsu)
- [Bipartite Check (BFS)](#215-bipartite-check-bfs)
- [Count Number Of Shortest Paths (BFS)](#216-count-number-of-shortest-paths-bfs)
- [Print The Actual Cycle (Undirected)](#226-print-the-actual-cycle-undirected)
- [Print The Actual Cycle (Directed)](#227-print-the-actual-cycle-directed)
- [Iterative DFS (Stack-Based)](#228-iterative-dfs-stack-based)
- [Articulation Points (Cut Vertices)](#229-articulation-points-cut-vertices)
- [Bridges (Cut Edges)](#230-bridges-cut-edges)
- [Minimum Time To Finish All Tasks](#251-minimum-time-to-finish-all-tasks)
- [SPFA (Queue-Optimized Bellman-Ford)](#265-spfa-queue-optimized-bellman-ford)
- [Count Number Of Shortest Paths (Dijkstra)](#266-count-number-of-shortest-paths-dijkstra)
- [Johnson's Algorithm (All-Pairs, Negative Edges Allowed)](#267-johnsons-algorithm-all-pairs-negative-edges-allowed)
- [Minimum Bottleneck Spanning Tree Fact](#282-minimum-bottleneck-spanning-tree-fact)
- [Kruskal Reconstruction Tree](#283-kruskal-reconstruction-tree)
- [Graph Diameter Via Floyd-Warshall](#2116-graph-diameter-via-floyd-warshall)
- [Kuhn's Algorithm (Bipartite Matching)](#95-kuhns-algorithm-bipartite-matching)
- [Hopcroft-Karp (Faster Bipartite Matching)](#96-hopcroft-karp-faster-bipartite-matching)
- [Min-Cost Max-Flow](#97-min-cost-max-flow)

**Trees**
- [Weighted Binary Lifting (Max/Min Edge On Path)](#318-weighted-binary-lifting-maxmin-edge-on-path)
- [O(1) LCA (Euler Tour + Sparse Table)](#341-o1-lca-euler-tour-sparse-table)
- [Centroid Decomposition](#342-centroid-decomposition)
- [DSU On Tree (Small-To-Large Over Subtrees)](#343-dsu-on-tree-small-to-large-over-subtrees)
- [Rerooting DP (Change Of Root Technique)](#344-rerooting-dp-change-of-root-technique)

**Strings**
- [Z-Function](#420-z-function)
- [String Hashing (Polynomial Rolling Hash)](#421-string-hashing-polynomial-rolling-hash)
- [Manacher's Algorithm (Longest Palindromic Substring)](#423-manachers-algorithm-longest-palindromic-substring)

**Range Query Data Structures**
- [Iterative Segment Tree (Bottom-Up)](#53-iterative-segment-tree-bottom-up)
- [Persistent Segment Tree](#515-persistent-segment-tree)
- [Merge Sort Tree](#516-merge-sort-tree)
- [Sqrt Decomposition (Block Decomposition)](#517-sqrt-decomposition-block-decomposition)

**STL / Two Pointers**
- [Merge / Partial Sum Tricks](#111-merge-partial-sum-tricks)
- [Tie-Breaking On Equal Values](#683-tie-breaking-on-equal-values)
- [`lower_bound` / `upper_bound` With Custom Comparator](#620-lower_bound-upper_bound-with-custom-comparator)

**Math & Number Theory**
- [Matrix Exponentiation](#6101-matrix-exponentiation)
- [Chinese Remainder Theorem (CRT)](#710-chinese-remainder-theorem-crt)
- [Euler Totient Sieve (φ For All 1..N)](#712-euler-totient-sieve-φ-for-all-1n)
- [Möbius Function + Sieve](#715-möbius-function-sieve)
- [Lucas' Theorem (nCr mod small prime p)](#74-lucas-theorem-ncr-mod-small-prime-p)
- [Catalan Numbers](#75-catalan-numbers)
- [Stars And Bars](#76-stars-and-bars)
- [Derangements](#77-derangements)

**Dynamic Programming**
- [Kadane's Algorithm (Maximum Subarray Sum)](#88-kadanes-algorithm-maximum-subarray-sum)
- [Bitset-Accelerated Feasibility (Knapsack Trick 5)](#trick-5-bitset-accelerated-feasibility)
- [Knuth's Optimization](#841-knuths-optimization)
- [Divide & Conquer DP Optimization](#855-divide-conquer-dp-optimization)

**Mo's Algorithm**
- [Mo's Algorithm With Point Updates](#912-mos-algorithm-with-point-updates)

**Bit Manipulation**
- [Brian Kernighan's Trick (Named)](#112-brian-kernighans-trick-named)
- [Gray Code](#113-gray-code)

---




## 1) Foundations & Utilities

### 1.1 General Template (clean)

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;
constexpr ll INF = (ll)4e18;
constexpr int MOD = 1'000'000'007;
#define all(x) (x).begin(), (x).end()
void solve() {
    // ...
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
```

---

### 1.2 Custom Sort

```cpp
struct node {
    int x, y;
};
sort(all(v), [](const node &a, const node &b) { return a.x != b.x ? a.x < b.x : a.y > b.y; });
```

##### Use

- Sort struct.
- Multi-key sorting.

##### Complexity

- `O(n log n)`

---

### 1.3 Coordinate Compression (Restore Values)

```cpp
struct compressor {
    vector<int> vals;
    void build(vector<int> v) {
        vals = move(v);
        sort(all(vals));
        vals.erase(unique(all(vals)), vals.end());
    }
    int get(int x) const { return lower_bound(all(vals), x) - vals.begin(); }
    int rev(int id) const { return vals[id]; }
};
```

##### Use

```cpp
compressor cp;
cp.build(a);
int id = cp.get(x);
int val = cp.rev(id);
```

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

### 1.4 Coordinate Compression (In-place)

```cpp
auto vals = a;
sort(all(vals));
vals.erase(unique(all(vals)), vals.end());
for (auto &x : a) x = lower_bound(all(vals), x) - vals.begin();
```

##### Complexity

- `O(n log n)`

##### Notes

- Cannot restore original values.
- Faster to write during contests.

---

### 1.5 Debug

```cpp
#ifndef ONLINE_JUDGE
template <class T>
void dbg(const vector<T> &v) {
    cerr << "[ ";
    for (const auto &x : v) cerr << x << ' ';
    cerr << "]\n";
}
#define debug(x) cerr << #x << " = " << (x) << '\n'
#else
#define debug(x) ((void)0)
#define dbg(v) ((void)0)
#endif
```

##### Use

```cpp
debug(n);
debug(ans);
dbg(v);
```

##### Notes

- Disabled automatically on Online Judge.

---

### 1.6 Random (RNG helper)

```cpp
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
long long rnd(long long l, long long r) { return uniform_int_distribution<long long>(l, r)(rng); }
```

##### Use

```cpp
long long x = rnd(1, 100);
```

##### Complexity

- `O(1)`

##### Notes

- Stress testing
- Randomized algorithms

---

### 1.7 Shuffle

```cpp
shuffle(all(v), rng);
```

##### Complexity

- `O(n)`

##### Notes

- Generate random permutation.
- Useful for anti-hack.

---

### 1.8 ckmin / ckmax

```cpp
template <class T>
bool ckmin(T &a, const T &b) {
    return b < a ? (a = b, true) : false;
}
template <class T>
bool ckmax(T &a, const T &b) {
    return a < b ? (a = b, true) : false;
}
```

##### Use

```cpp
ckmin(ans, cur);
ckmax(ans, cur);
```

##### Complexity

- `O(1)`

##### Notes

- Very common in DP and Graphs.

---

### 1.9 Next / Previous Permutation

```cpp
next_permutation(all(v));
prev_permutation(all(v));
```

##### Complexity

- `O(n)`

##### Notes

- Generate permutations.
- Useful in brute force.

---

### 1.10 Useful STL Tricks

```cpp
*max_element(all(v));
*min_element(all(v));
accumulate(all(v), 0LL);
reverse(all(v));
rotate(v.begin(), v.begin() + k, v.end());
iota(all(v), 0);
```

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

### 1.11 Merge / Partial Sum Tricks

```cpp
vector<int> merged(a.size() + b.size());
merge(all(a), all(b), merged.begin());             // a, b must already be sorted
inplace_merge(v.begin(), v.begin() + k, v.end());  // merge two sorted halves in place
vector<long long> pre(v.size());
partial_sum(all(v), pre.begin());  // pre[i] = v[0] + ... + v[i]
```

##### Use

- `merge`: combine two sorted ranges without a full re-sort (used inside merge-sort-style divide & conquer, and the Merge Sort Tree above).
- `inplace_merge`: merge sort's merge step without extra allocation.
- `partial_sum`: quick prefix-sum array construction.

---

### 1.12 Binary Search Template (First True)

```cpp
long long l = 0, r = (long long)1e18, ans = -1;
while (l <= r) {
    long long mid = (l + r) >> 1;
    if (check(mid))
        ans = mid, r = mid - 1;
    else
        l = mid + 1;
}
```

##### Complexity

- `O(log Range)`

##### Notes

- Finds first valid value.

---

### 1.13 Binary Search Template (Last True)

```cpp
long long l = 0, r = (long long)1e18, ans = -1;
while (l <= r) {
    long long mid = (l + r) >> 1;
    if (check(mid))
        ans = mid, l = mid + 1;
    else
        r = mid - 1;
}
```

##### Complexity

- `O(log Range)`

##### Notes

- Finds last valid value.

---

### 1.14 Ternary Search

```cpp
while (r - l > 3) {
    long long m1 = l + (r - l) / 3, m2 = r - (r - l) / 3;
    if (f(m1) < f(m2))
        r = m2;
    else
        l = m1;
}
```

##### Complexity

- `O(log Range)`

##### Notes

- Convex / Concave functions only.
- Usually for optimization problems.

---

### 1.15 Overflow-Safe Multiplication (`__int128`)

```cpp
long long safe_mul(long long a, long long b, long long cap = LLONG_MAX) {
    __int128 r = (__int128)a * b;
    if (r > cap) return cap;
    return (long long)r;
}
```

##### Use

- Multiply two `long long` values when the product may exceed `10^18`.
- Compare products without overflow: `(__int128)a * b < (__int128)c * d`.

---

### 1.16 Fixed-Precision Output

```cpp
cout << fixed << setprecision(9) << ans << "\n";
```

##### Use

- Geometry / probability / expected-value answers.
- `setprecision(k)` controls digits after the decimal point when combined with `fixed`.

---

### 1.17 Fast Input For Large N

```cpp
static char buf[1 << 25];
int bufPos = 0, bufLen = 0;
inline int gc() {
    if (bufPos == bufLen) {
        bufLen = fread(buf, 1, sizeof(buf), stdin);
        bufPos = 0;
        if (!bufLen) return -1;
    }
    return buf[bufPos++];
}
inline int readInt() {
    int c = gc(), sgn = 1, x = 0;
    while (c <= ' ') c = gc();
    if (c == '-') sgn = -1, c = gc();
    while (c >= '0') x = x * 10 + c - '0', c = gc();
    return x * sgn;
}
```

##### Use

- Input sizes around `10^7` or more where `cin`/`scanf` become too slow.

---

### 1.18 Reading Until EOF

```cpp
int x;
while (cin >> x) {
    // process x
}
```

##### Use

- Multi-testcase input with no explicit test count given.

---

### 1.19 Local Benchmark Timer

```cpp
auto start = chrono::high_resolution_clock::now();
// ... code ...
auto end = chrono::high_resolution_clock::now();
cerr << chrono::duration<double>(end - start).count() << "s\n";
```

##### Use

- Measure runtime locally before submitting; never leave in final submission.

---


## 2) Graph Algorithms

### 2.1 DSU (Standard)

```cpp
struct dsu {
    vector<int> p, sz;
    int cc;
    dsu() {}
    dsu(int n) { init(n); }
    void init(int n) {
        cc = n;
        p.resize(n + 1);
        sz.assign(n + 1, 1);
        iota(all(p), 0);
    }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    bool same(int a, int b) { return find(a) == find(b); }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a;
        sz[a] += sz[b];
        cc--;
        return true;
    }
    int size(int x) { return sz[find(x)]; }
};
```

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

```cpp
if (d.same(u, v)) 
```

#### Merge Components

```cpp
d.unite(u, v);
```

#### Component Size

```cpp
cout << d.size(u);
```

#### Number of Components

```cpp
cout << d.cc;
```

#### Cycle Detection

```cpp
if (!d.unite(u, v)) {
    // cycle found
}
```

#### Kruskal MST

```cpp
if (d.unite(u, v)) mst += w;
```

---

### 2.2 DSU (Component Tracking)

```cpp
struct dsu {
    int cc;
    vector<int> p, sz;
    vector<vector<int>> comp;
    dsu() {}
    dsu(int n) { init(n); }
    void init(int n) {
        cc = n;
        p.resize(n + 1);
        sz.assign(n + 1, 1);
        iota(all(p), 0);
        comp.assign(n + 1, {});
        for (int i = 1; i <= n; i++) comp[i].push_back(i);
    }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    bool same(int a, int b) { return find(a) == find(b); }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a;
        sz[a] += sz[b];
        if (comp[b].size() > comp[a].size()) swap(comp[a], comp[b]);
        comp[a].insert(comp[a].end(), comp[b].begin(), comp[b].end());
        comp[b].clear();
        cc--;
        return true;
    }
    int size(int x) { return sz[find(x)]; }
    vector<int> &members(int x) { return comp[find(x)]; }
    vector<vector<int>> get_all_components() {
        vector<vector<int>> res;
        for (int i = 1; i < (int)comp.size(); i++) {
            if (!comp[i].empty()) res.push_back(comp[i]);
        }
        return res;
    }
};
```

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

```cpp
for (auto u : d.members(x)) cout << u << ' ';
```

#### Print All Components

```cpp
auto comps = d.get_all_components();
for (auto &c : comps) {
    for (auto x : c) cout << x << ' ';
    cout << endl;
}
```

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

---

### 2.3 DSU With Rollback

```cpp
struct DsuRollback {
    vector<int> p, sz;
    vector<pair<int, int>> history;
    DsuRollback(int n) {
        p.resize(n + 1);
        iota(p.begin(), p.end(), 0);
        sz.assign(n + 1, 1);
    }
    int find(int x) { return p[x] == x ? x : find(p[x]); }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) {
            history.push_back({-1, -1});
            return false;
        }
        if (sz[a] < sz[b]) swap(a, b);
        history.push_back({b, p[b]});
        p[b] = a;
        sz[a] += sz[b];
        return true;
    }
    int snapshot() { return history.size(); }
    void rollback(int checkpoint) {
        while ((int)history.size() > checkpoint) {
            auto [b, oldp] = history.back();
            history.pop_back();
            if (b == -1) continue;
            sz[p[b]] -= sz[b];
            p[b] = oldp;
        }
    }
};
```

##### When To Use

- Offline dynamic connectivity (edges added/removed over time, e.g. divide-and-conquer on time).
- No path compression, union by size only, so undo is O(1) per operation.

##### Complexity

- `unite / find`: `O(log n)`
- `rollback`: `O(1)` per undone operation

---

### 2.4 Weighted / Parity DSU

```cpp
struct ParityDsu {
    vector<int> p, rnk, rel;  // rel[x] = parity of x relative to p[x]
    ParityDsu(int n) {
        p.resize(n + 1);
        iota(p.begin(), p.end(), 0);
        rnk.assign(n + 1, 0);
        rel.assign(n + 1, 0);
    }
    pair<int, int> find(int x) {
        if (p[x] == x) return {x, 0};
        auto [r, par] = find(p[x]);
        rel[x] ^= par;
        p[x] = r;
        return {r, rel[x]};
    }
    bool unite(int a, int b, int parity) {
        auto [ra, pa] = find(a);
        auto [rb, pb] = find(b);
        if (ra == rb) return (pa ^ pb) == parity;
        if (rnk[ra] < rnk[rb]) swap(ra, rb), swap(pa, pb);
        p[rb] = ra;
        rel[rb] = pa ^ pb ^ parity;
        if (rnk[ra] == rnk[rb]) rnk[ra]++;
        return true;
    }
};
```

##### Use

- Bipartiteness checking with edge additions (parity = 1 means "different side").
- Relative distance / offset constraints between nodes.

##### Complexity

- `O(log n)` per operation (near `O(alpha(n))` with rank + path compression).

---

### 2.5 BFS (Breadth First Search)

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

### 2.6 Normal BFS

```cpp
vector<int> bfs(int src, const vector<vector<int>> &adj) {
    int n = (int)adj.size() - 1;
    vector<int> dist(n + 1, -1);
    queue<int> q;
    q.push(src);
    dist[src] = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u])
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
    }
    return dist;
}
```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

##### Use

```cpp
auto dist = bfs(1, adj);
```

---

### 2.7 BFS With Parent (Restore Path)

```cpp
vector<int> dist(n + 1, -1);
vector<int> par(n + 1, -1);
queue<int> q;
q.push(src);
dist[src] = 0;
while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (auto v : adj[u]) {
        if (dist[v] != -1) continue;
        dist[v] = dist[u] + 1;
        par[v] = u;
        q.push(v);
    }
}
```

##### Restore Path

```cpp
vector<int> path;
for (int cur = dest; cur != -1; cur = par[cur]) path.push_back(cur);
reverse(all(path));
```

##### Use

```
Print shortest path
Find route
```

---

### 2.8 Multi Source BFS

```cpp
vector<int> dist(n + 1, -1);
queue<int> q;
for (auto src : sources) {
    q.push(src);
    dist[src] = 0;
}
while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (auto v : adj[u]) {
        if (dist[v] != -1) continue;
        dist[v] = dist[u] + 1;
        q.push(v);
    }
}
```

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

### 2.9 Grid BFS

```cpp
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
queue<pair<int, int>> q;
q.push({sx, sy});
dist[sx][sy] = 0;
while (!q.empty()) {
    auto [x, y] = q.front();
    q.pop();
    for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
        if (grid[nx][ny] == '#') continue;
        if (dist[nx][ny] != -1) continue;
        dist[nx][ny] = dist[x][y] + 1;
        q.push({nx, ny});
    }
}
```

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

### 2.10 BFS On State Graph

#### Example

```
(node , mask)
(node , parity)
(node , coins)
(node , fuel)
```

---

```cpp
queue<pair<int, int>> q;
vector<vector<int>> dist(n + 1, vector<int>(1 << k, -1));
q.push({src, 0});
dist[src][0] = 0;
while (!q.empty()) {
    auto [u, mask] = q.front();
    q.pop();
    for (auto v : adj[u]) {
        int nmask = mask;
        if (special[v]) nmask |= (1 << id[v]);
        if (dist[v][nmask] != -1) continue;
        dist[v][nmask] = dist[u][mask] + 1;
        q.push({v, nmask});
    }
}
```

##### Use

```
Collect Keys
Visit Special Nodes
Bitmask BFS
Shortest State Transition
```

---

### 2.11 0-1 BFS

#### Condition

```
Edge Weight = 0 or 1 only
```

---

```cpp
deque<int> dq;
vector<int> dist(n + 1, INF);
dist[src] = 0;
dq.push_front(src);
while (!dq.empty()) {
    int u = dq.front();
    dq.pop_front();
    for (auto [v, w] : adj[u]) {
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            if (w == 0)
                dq.push_front(v);
            else
                dq.push_back(v);
        }
    }
}
```

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

### 2.12 Useful Snippets

#### Count Connected Components

```cpp
int cc = 0;
for (int i = 1; i <= n; i++) {
    if (dist[i] != -1) continue;
    cc++;
    queue<int> q;
    q.push(i);
    dist[i] = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto v : adj[u]) {
            if (dist[v] != -1) continue;
            dist[v] = 0;
            q.push(v);
        }
    }
}
```

---

#### Find Farthest Node

```cpp
int mx = 0;
int node = src;
for (int i = 1; i <= n; i++) {
    if (dist[i] > mx) {
        mx = dist[i];
        node = i;
    }
}
```

##### Use

```
Tree Diameter
```

---

### 2.13 Common BFS Tricks

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

### 2.14 Common Problems

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

---

### 2.15 Bipartite Check (BFS)

```cpp
bool color[N];
bool vis2[N];
bool isBipartiteBFS(int src, vector<vector<int>> &adj) {
    queue<int> q;
    q.push(src);
    vis2[src] = true;
    color[src] = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (!vis2[v]) {
                vis2[v] = true;
                color[v] = !color[u];
                q.push(v);
            } else if (color[v] == color[u]) {
                return false;
            }
        }
    }
    return true;
}
```

##### Use

- Avoids recursion depth issues on large graphs compared to the DFS version.

---

### 2.16 Count Number Of Shortest Paths (BFS)

```cpp
vector<long long> cnt(N, 0);
vector<int> dist(N, -1);
void bfsCount(int src, vector<vector<int>> &adj, long long mod) {
    queue<int> q;
    q.push(src);
    dist[src] = 0;
    cnt[src] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                cnt[v] = cnt[u];
                q.push(v);
            } else if (dist[v] == dist[u] + 1) {
                cnt[v] = (cnt[v] + cnt[u]) % mod;
            }
        }
    }
}
```

##### Use

- Number of distinct shortest paths from `src` to every node, modulo `mod`.

---

### 2.17 DFS (Depth First Search)

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

### 2.18 Normal DFS

```cpp
vector<vector<int>> adj;
vector<int> vis;
void dfs(int u) {
    vis[u] = 1;
    for (int v : adj[u])
        if (!vis[v]) dfs(v);
}
```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

##### Use

```cpp
dfs(1);
```

---

### 2.19 Connected Components

```cpp
vector<int> vis;
void dfs(int u) {
    vis[u] = 1;
    for (auto v : adj[u]) {
        if (!vis[v]) dfs(v);
    }
}
```

##### Count Components

```cpp
int cc = 0;
for (int i = 1; i <= n; i++) {
    if (vis[i]) continue;
    cc++;
    dfs(i);
}
```

##### Complexity

```
O(V + E)
```

---

### 2.20 DFS With Parent

```cpp
void dfs(int u, int p) {
    for (auto v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
    }
}
```

##### Use

```
Tree DFS
Avoid Going Back To Parent
```

---

### 2.21 Subtree Size

```cpp
vector<int> sz;
void dfs(int u, int p) {
    sz[u] = 1;
    for (auto v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        sz[u] += sz[v];
    }
}
```

##### Use

```cpp
cout << sz[u];
```

##### Meaning

```
Number Of Nodes In Subtree(u)
```

---

### 2.22 Entry / Exit Time

```cpp
int timer = 0;
vector<int> tin, tout;
void dfs(int u, int p) {
    tin[u] = ++timer;
    for (auto v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
    }
    tout[u] = timer;
}
```

##### Check Ancestor

```cpp
bool is_ancestor(int u, int v) { return tin[u] <= tin[v] && tout[v] <= tout[u]; }
```

##### Use

```
Ancestor Queries
Euler Tour
Subtree Queries
LCA
```

---

### 2.23 Euler Tour (Flatten Tree)

```cpp
vector<int> tin;
vector<int> tout;
vector<int> flat;
int timer = 0;
void dfs(int u, int p) {
    tin[u] = timer++;
    flat.push_back(u);
    for (auto v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
    }
    tout[u] = timer - 1;
}
```

##### Subtree Range

```cpp
[ tin[u], tout[u] ]
```

##### Use

```
Segment Tree On Tree
Fenwick On Tree
Subtree Queries
```

---

### 2.24 Cycle Detection (Undirected)

```cpp
bool dfs(int u, int p) {
    vis[u] = 1;
    for (auto v : adj[u]) {
        if (v == p) continue;
        if (vis[v]) return true;
        if (dfs(v, u)) return true;
    }
    return false;
}
```

##### Complexity

```
O(V + E)
```

---

### 2.25 Cycle Detection (Directed)

```cpp
vector<int> vis;
bool dfs(int u) {
    vis[u] = 1;
    for (auto v : adj[u]) {
        if (vis[v] == 1) return true;
        if (vis[v] == 0 && dfs(v)) return true;
    }
    vis[u] = 2;
    return false;
}
```

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

### 2.26 Print The Actual Cycle (Undirected)

```cpp
vector<int> par, cyc;
bool findCycle(int u, int p, vector<vector<int>> &adj) {
    vis[u] = 1;
    par[u] = p;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (vis[v] == 1) {
            for (int x = u; x != v; x = par[x]) cyc.push_back(x);
            cyc.push_back(v);
            return true;
        }
        if (!vis[v] && findCycle(v, u, adj)) return true;
    }
    vis[u] = 2;
    return false;
}
```

##### Use

- Reconstructs the actual cycle nodes, not just a yes/no answer.

---

### 2.27 Print The Actual Cycle (Directed)

```cpp
vector<int> par2, cyc2;
bool findCycleDirected(int u, vector<vector<int>> &adj) {
    vis[u] = 1;
    for (int v : adj[u]) {
        if (vis[v] == 1) {
            for (int x = u; x != v; x = par2[x]) cyc2.push_back(x);
            cyc2.push_back(v);
            return true;
        }
        if (vis[v] == 0) {
            par2[v] = u;
            if (findCycleDirected(v, adj)) return true;
        }
    }
    vis[u] = 2;
    return false;
}
```

---

### 2.28 Iterative DFS (Stack-Based)

```cpp
void dfsIterative(int src, vector<vector<int>> &adj) {
    vector<int> stk = {src};
    vector<int> visited(adj.size(), 0);
    while (!stk.empty()) {
        int u = stk.back();
        stk.pop_back();
        if (visited[u]) continue;
        visited[u] = 1;
        // process u here
        for (int v : adj[u])
            if (!visited[v]) stk.push_back(v);
    }
}
```

##### Use

- Avoids stack overflow on deep graphs/trees (`n` around `10^5`–`10^6` with a chain shape).
- Order of visiting siblings is reversed vs. recursive DFS; reverse `adj[u]` first if exact order matters.

##### Complexity

- `O(V + E)`

---

### 2.29 Articulation Points (Cut Vertices)

```cpp
vector<vector<int>> g;
vector<int> tin, low;
vector<bool> visAP, isCut;
int timerAP = 0;
void dfsAP(int u, int p = -1) {
    visAP[u] = true;
    tin[u] = low[u] = timerAP++;
    int children = 0;
    for (int v : g[u]) {
        if (v == p) continue;
        if (visAP[v]) {
            low[u] = min(low[u], tin[v]);
        } else {
            dfsAP(v, u);
            low[u] = min(low[u], low[v]);
            if (low[v] >= tin[u] && p != -1) isCut[u] = true;
            children++;
        }
    }
    if (p == -1 && children > 1) isCut[u] = true;
}
```

##### When To Use

```
Find nodes whose removal disconnects the graph
Network reliability problems
Biconnected components
```

##### Complexity

```
O(V + E)
```

---

### 2.30 Bridges (Cut Edges)

```cpp
vector<vector<pair<int, int>>> gB;  // {to, edgeId}
vector<int> tinB, lowB;
vector<bool> visB;
vector<pair<int, int>> bridges;
int timerB = 0;
void dfsBridges(int u, int parentEdge = -1) {
    visB[u] = true;
    tinB[u] = lowB[u] = timerB++;
    for (auto [v, id] : gB[u]) {
        if (id == parentEdge) continue;
        if (visB[v]) {
            lowB[u] = min(lowB[u], tinB[v]);
        } else {
            dfsBridges(v, id);
            lowB[u] = min(lowB[u], lowB[v]);
            if (lowB[v] > tinB[u]) bridges.push_back({u, v});
        }
    }
}
```

##### When To Use

```
Find edges whose removal disconnects the graph
Critical connections in a network
```

##### Complexity

```
O(V + E)
```

---

### 2.31 Topological Sort (DFS)

```cpp
vector<int> vis;
vector<int> topo;
void dfs(int u) {
    vis[u] = 1;
    for (auto v : adj[u]) {
        if (!vis[v]) dfs(v);
    }
    topo.push_back(u);
}
```

##### Build Topological Order

```cpp
for (int i = 1; i <= n; i++) {
    if (!vis[i]) dfs(i);
}
reverse(all(topo));
```

##### Complexity

```
O(V + E)
```

---

### 2.32 Tree Diameter

#### First DFS

```cpp
dfs(1);
```

Find farthest node:

```cpp
int a = max_element(all(dist)) - dist.begin();
```

---

#### Second DFS

```cpp
dfs(a);
```

Find farthest node:

```cpp
int b = max_element(all(dist)) - dist.begin();
```

---

#### Diameter Length

```cpp
dist[b]
```

##### Complexity

```
O(N)
```

---

### 2.33 DFS Order

```cpp
vector<int> ord;
void dfs(int u, int p) {
    ord.push_back(u);
    for (auto v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
    }
}
```

##### Use

```
Tree Traversal
Euler Variants
Offline Queries
```

---

### 2.34 Bipartite Check (DFS)

```cpp
vector<int> color(n + 1, -1);
bool dfs(int u, int c) {
    color[u] = c;
    for (auto v : adj[u]) {
        if (color[v] == -1) {
            if (!dfs(v, c ^ 1)) return false;
        } else {
            if (color[v] == color[u]) return false;
        }
    }
    return true;
}
```

##### Complexity

```
O(V + E)
```

---

### 2.35 Useful Snippets

#### Collect Nodes Of Component

```cpp
vector<int> comp;
void dfs(int u) {
    vis[u] = 1;
    comp.push_back(u);
    for (auto v : adj[u]) {
        if (!vis[v]) dfs(v);
    }
}
```

---

#### Leaf Detection

```cpp
if (adj[u].size() == 1 && u != root) {
    // leaf
}
```

---

#### Count Leaves

```cpp
int leaves = 0;
for (int i = 2; i <= n; i++) {
    if (adj[i].size() == 1) leaves++;
}
```

---

### 2.36 Common DFS Tricks

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

### 2.37 Common Problems

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

### 2.38 Topological Sort

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

### 2.39 Kahn's Algorithm (BFS)

```cpp
vector<int> topo;
vector<int> indeg(n + 1);
for (int u = 1; u <= n; u++) {
    for (auto v : adj[u]) { indeg[v]++; }
}
queue<int> q;
for (int i = 1; i <= n; i++) {
    if (indeg[i] == 0) q.push(i);
}
while (!q.empty()) {
    int u = q.front();
    q.pop();
    topo.push_back(u);
    for (auto v : adj[u]) {
        indeg[v]--;
        if (indeg[v] == 0) q.push(v);
    }
}
```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

---

### 2.40 Check If DAG

```cpp
if ((int)topo.size() != n) {
    // cycle exists
}
```

##### Idea

```
A graph has a topological order
iff it is a DAG.
```

---

### 2.41 Lexicographically Smallest Topological Order

```cpp
priority_queue<int, vector<int>, greater<int>> pq;
for (int i = 1; i <= n; i++) {
    if (indeg[i] == 0) pq.push(i);
}
while (!pq.empty()) {
    int u = pq.top();
    pq.pop();
    topo.push_back(u);
    for (auto v : adj[u]) {
        indeg[v]--;
        if (indeg[v] == 0) pq.push(v);
    }
}
```

##### Complexity

```
O((V + E) log V)
```

##### Use

```
Smallest Valid Ordering
```

---

### 2.42 DFS Topological Sort

```cpp
vector<int> vis;
vector<int> topo;
void dfs(int u) {
    vis[u] = 1;
    for (auto v : adj[u]) {
        if (!vis[v]) dfs(v);
    }
    topo.push_back(u);
}
```

##### Build Order

```cpp
for (int i = 1; i <= n; i++) {
    if (!vis[i]) dfs(i);
}
reverse(all(topo));
```

##### Complexity

```
O(V + E)
```

---

### 2.43 Cycle Detection In DAG

```cpp
vector<int> vis;
bool dfs(int u) {
    vis[u] = 1;
    for (auto v : adj[u]) {
        if (vis[v] == 1) return true;
        if (vis[v] == 0 && dfs(v)) return true;
    }
    vis[u] = 2;
    return false;
}
```

##### States

```
0 = Unvisited
1 = In Stack
2 = Finished
```

---

### 2.44 Longest Path In DAG

```cpp
vector<int> dp(n + 1, 0);
for (auto u : topo) {
    for (auto v : adj[u]) { dp[v] = max(dp[v], dp[u] + 1); }
}
```

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

### 2.45 Shortest Path In DAG

```cpp
vector<int> dist(n + 1, INF);
dist[src] = 0;
for (auto u : topo) {
    if (dist[u] == INF) continue;
    for (auto [v, w] : adj[u]) { dist[v] = min(dist[v], dist[u] + w); }
}
```

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

### 2.46 Count Number Of Paths In DAG

```cpp
vector<int> dp(n + 1);
dp[src] = 1;
for (auto u : topo) {
    for (auto v : adj[u]) {
        dp[v] += dp[u];
        dp[v] %= MOD;
    }
}
```

##### Use

```
Count Paths
DP On DAG
```

---

### 2.47 Path Restoration In DAG

```cpp
vector<int> par(n + 1, -1);
for (auto u : topo) {
    for (auto v : adj[u]) {
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            par[v] = u;
        }
    }
}
```

##### Restore Path

```cpp
vector<int> path;
for (int cur = dest; cur != -1; cur = par[cur]) { path.push_back(cur); }
reverse(all(path));
```

---

### 2.48 Useful Snippets

#### Sources (Indegree = 0)

```cpp
vector<int> srcs;
for (int i = 1; i <= n; i++) {
    if (indeg[i] == 0) srcs.push_back(i);
}
```

---

#### Sinks (Outdegree = 0)

```cpp
vector<int> sinks;
for (int i = 1; i <= n; i++) {
    if (adj[i].empty()) sinks.push_back(i);
}
```

---

#### Check Unique Topological Order

```cpp
bool unique_order = true;
while (!q.empty()) {
    if ((int)q.size() > 1) unique_order = false;
    int u = q.front();
    q.pop();
    ...
}
```

##### Meaning

```
More than one valid order exists.
```

---

### 2.49 Common Tricks

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

### 2.50 Common Problems

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

---

### 2.51 Minimum Time To Finish All Tasks

```cpp
vector<long long> minFinishTime(int n, vector<vector<int>> &adj, vector<long long> &dur) {
    vector<int> indeg(n + 1, 0);
    for (int u = 1; u <= n; u++)
        for (int v : adj[u]) indeg[v]++;
    vector<long long> finish(n + 1, 0);
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (!indeg[i]) q.push(i), finish[i] = dur[i];
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            finish[v] = max(finish[v], finish[u] + dur[v]);
            if (--indeg[v] == 0) q.push(v);
        }
    }
    return finish;
}
```

##### Use

- Each task `i` takes `dur[i]` time and must wait for all its dependencies to finish first.
- `finish[i]` = earliest completion time of task `i`; answer is `max(finish)`.

##### Complexity

- `O(V + E)`

---

### 2.52 Dijkstra

#### When To Use

```
Shortest Path
Positive Edge Weights
Weighted Graphs
State Graphs
Multi Source Shortest Path
```

---

### 2.53 Standard Dijkstra

```cpp
vector<long long> dijkstra(int src, const vector<vector<pair<int, int>>> &adj) {
    int n = (int)adj.size() - 1;
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>,
        greater<pair<long long, int>>>
        pq;
    dist[src] = 0;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d != dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[v] > d + w) {
                dist[v] = d + w;
                pq.push({dist[v], v});
            }
    }
    return dist;
}
```

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

### 2.54 Path Restore

```cpp
vector<int> dist(n + 1, INF);
vector<int> par(n + 1, -1);
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
dist[src] = 0;
pq.push({0, src});
while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();
    if (d != dist[u]) continue;
    for (auto [v, w] : adj[u]) {
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            par[v] = u;
            pq.push({dist[v], v});
        }
    }
}
```

##### Restore Path

```cpp
vector<int> path;
for (int cur = dest; cur != -1; cur = par[cur]) { path.push_back(cur); }
reverse(all(path));
```

---

### 2.55 Multi Source Dijkstra

```cpp
vector<int> dist(n + 1, INF);
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
for (auto src : sources) {
    dist[src] = 0;
    pq.push({0, src});
}
while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();
    if (d != dist[u]) continue;
    for (auto [v, w] : adj[u]) {
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            pq.push({dist[v], v});
        }
    }
}
```

##### Use

```
Nearest Hospital
Nearest Special Node
Spread Problems
```

---

### 2.56 State Graph Dijkstra

#### Example States

```
(node , fuel)

(node , mask)

(node , coupons)

(node , parity)
```

---

```cpp
priority_queue<array<int, 3>, vector<array<int, 3>>, greater<array<int, 3>>> pq;
vector<vector<int>> dist(n + 1, vector<int>(K, INF));
dist[src][0] = 0;
pq.push({0, src, 0});
while (!pq.empty()) {
    auto [d, u, state] = pq.top();
    pq.pop();
    if (d != dist[u][state]) continue;
    ...
}
```

##### Use

```
Fuel Problems
Discount Coupons
Bitmask States
Extended Graphs
```

---

### 2.57 Dense Graph Dijkstra

```cpp
vector<int> dist(n + 1, INF);
vector<int> vis(n + 1);
dist[src] = 0;
for (int it = 1; it <= n; it++) {
    int u = -1;
    for (int i = 1; i <= n; i++) {
        if (vis[i]) continue;
        if (u == -1 || dist[i] < dist[u]) { u = i; }
    }
    vis[u] = 1;
    for (auto [v, w] : adj[u]) { dist[v] = min(dist[v], dist[u] + w); }
}
```

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

### 2.58 Count Number Of Shortest Paths

```cpp
vector<int> dist(n + 1, INF);
vector<int> ways(n + 1, 0);
dist[src] = 0;
ways[src] = 1;
while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();
    if (d != dist[u]) continue;
    for (auto [v, w] : adj[u]) {
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            ways[v] = ways[u];
            pq.push({dist[v], v});
        } else if (dist[v] == dist[u] + w) {
            ways[v] += ways[u];
            ways[v] %= MOD;
        }
    }
}
```

##### Use

```
CSES Investigation
Count Shortest Paths
```

---

### 2.59 Shortest Path DAG After Dijkstra

```cpp
if (dist[v] == dist[u] + w) { dag[u].push_back(v); }
```

##### Use

```
All Shortest Paths
DP On Shortest Paths
```

---

### 2.60 Dijkstra On Grid

```cpp
priority_queue<array<int, 3>, vector<array<int, 3>>, greater<array<int, 3>>> pq;
dist[sx][sy] = 0;
pq.push({0, sx, sy});
```

##### Use

```
Weighted Grid
Minimum Cost Path
```

---

### 2.61 K Shortest Paths (Intro)

```cpp
vector<int> cnt(n + 1);
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
pq.push({0, src});
while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();
    cnt[u]++;
    if (cnt[u] > k) continue;
    for (auto [v, w] : adj[u]) { pq.push({d + w, v}); }
}
```

##### Use

```
CSES Flight Routes
K Shortest Paths
```

---

### 2.62 Useful Snippets

#### Unreachable Nodes

```cpp
if (dist[u] == INF) {
    // unreachable
}
```

---

#### Farthest Reachable Node

```cpp
int mx = -1;
int node = -1;
for (int i = 1; i <= n; i++) {
    if (dist[i] == INF) continue;
    if (dist[i] > mx) {
        mx = dist[i];
        node = i;
    }
}
```

---

#### Shortest Path Length

```cpp
cout << dist[dest];
```

---

#### Check Negative Edge

```cpp
if (w < 0) {
// DON'T use Dijkstra\n}\n
```

---

### 2.63 Common Tricks

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

### 2.64 Common Problems

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

---

### 2.65 SPFA (Queue-Optimized Bellman-Ford)

```cpp
vector<long long> spfa(int src, int n, vector<vector<pair<int, int>>> &adj) {
    vector<long long> dist(n + 1, INF);
    vector<bool> inQueue(n + 1, false);
    dist[src] = 0;
    queue<int> q;
    q.push(src);
    inQueue[src] = true;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        inQueue[u] = false;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (!inQueue[v]) {
                    q.push(v);
                    inQueue[v] = true;
                }
            }
        }
    }
    return dist;
}
```

##### Use

- Bellman-Ford variant that only relaxes nodes queued after being updated; often faster in practice on sparse graphs.
- Still handles negative edges; worst case is `O(VE)` same as plain Bellman-Ford.

##### Note

- Can be adapted for negative-cycle detection by tracking relaxation counts per node (like Bellman-Ford's `n-1` pass rule).

---

### 2.66 Count Number Of Shortest Paths (Dijkstra)

```cpp
vector<long long> cntPaths(int src, int n, vector<vector<pair<int, int>>> &adj, long long mod) {
    vector<long long> dist(n + 1, INF), cnt(n + 1, 0);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    dist[src] = 0;
    cnt[src] = 1;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                cnt[v] = cnt[u];
                pq.push({dist[v], v});
            } else if (dist[u] + w == dist[v]) {
                cnt[v] = (cnt[v] + cnt[u]) % mod;
            }
        }
    }
    return cnt;
}
```

##### Use

- Number of distinct shortest paths from `src` to every node, modulo `mod`.

---

### 2.67 Johnson's Algorithm (All-Pairs, Negative Edges Allowed)

```cpp
// 1) Add a virtual node 0 connected to all nodes with weight 0.
// 2) Run Bellman-Ford from node 0 to get h[v] (fails if a negative cycle exists).
// 3) Reweight every edge (u,v,w) -> w + h[u] - h[v] (now all weights are >= 0).
// 4) Run Dijkstra from every node on the reweighted graph.
// 5) True distance: dist(u,v) = dijkstraDist(u,v) - h[u] + h[v].
```

##### Use

- All-pairs shortest paths on sparse graphs with negative edges (but no negative cycle).
- Faster than running Floyd-Warshall (`O(V^3)`) when the graph is sparse: `O(VE log V)` total.

---

### 2.68 Kruskal (Minimum Spanning Tree)

#### When To Use

```
Minimum Spanning Tree (MST)

Connect all nodes
Minimum total cost

Build MST from weighted graph
```

---

### 2.69 DSU Required

```cpp
struct dsu {
    vector<int> p, sz;
    dsu(int n) {
        p.resize(n + 1);
        sz.assign(n + 1, 1);
        iota(all(p), 0);
    }
    int find(int x) { return p[x] == x ? x : p[x] = find(p[x]); }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a;
        sz[a] += sz[b];
        return true;
    }
};
```

---

### 2.70 Standard Kruskal

```cpp
struct edge {
    int u, v, w;
    bool operator<(const edge &other) const { return w < other.w; }
};
vector<edge> edges;
sort(all(edges));
dsu d(n);
int mst = 0;
for (auto [u, v, w] : edges) {
    if (d.unite(u, v)) { mst += w; }
}
```

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

### 2.71 Check If MST Exists

```cpp
int used = 0;
for (auto [u, v, w] : edges) {
    if (d.unite(u, v)) {
        mst += w;
        used++;
    }
}
if (used != n - 1) { cout << "IMPOSSIBLE"; }
```

##### Meaning

```
Graph is disconnected
No spanning tree exists
```

---

### 2.72 Store MST Edges

```cpp
vector<edge> mst_edges;
for (auto [u, v, w] : edges) {
    if (d.unite(u, v)) {
        mst += w;
        mst_edges.push_back({u, v, w});
    }
}
```

##### Use

```
Need actual MST
Need MST graph
Second MST
LCA on MST
```

---

### 2.73 Build MST Graph

```cpp
vector<vector<pair<int, int>>> mst_adj(n + 1);
for (auto [u, v, w] : edges) {
    if (d.unite(u, v)) {
        mst_adj[u].push_back({v, w});
        mst_adj[v].push_back({u, w});
    }
}
```

##### Use

```
LCA
Max Edge Query
Second MST
Tree Queries
```

---

### 2.74 Maximum Spanning Tree

```cpp
sort(all(edges), [&](auto a, auto b) { return a.w > b.w; });
```

Everything else remains the same.

##### Use

```
Maximum total weight tree
```

---

### 2.75 Number Of Connected Components

```cpp
dsu d(n);
for (auto [u, v, w] : edges) d.unite(u, v);
int cc = 0;
for (int i = 1; i <= n; i++) {
    if (d.find(i) == i) cc++;
}
```

---

### 2.76 Forest Cost

```cpp
int cost = 0;
for (auto [u, v, w] : edges) {
    if (d.unite(u, v)) cost += w;
}
```

##### Meaning

```
Minimum Spanning Forest
```

##### Use

```
Disconnected Graph
```

---

### 2.77 Second MST Idea

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

### 2.78 Useful Snippets

#### Sort Edges

```cpp
sort(all(edges));
```

---

#### MST Cost

```cpp
cout << mst;
```

---

#### Number Of MST Edges

```cpp
cout << mst_edges.size();
```

Should be:

```
n - 1
```

for connected graph.

---

#### Check Same Component

```cpp
if (d.find(u) == d.find(v)) {}
```

---

#### Detect Cycle

```cpp
if (!d.unite(u, v)) {
    // cycle edge
}
```

---

### 2.79 Common Tricks

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

### 2.80 Common Problems

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

### 2.81 Prim vs Kruskal

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

---

### 2.82 Minimum Bottleneck Spanning Tree Fact

```
The MST also minimizes the maximum edge weight
on the unique tree path between any two nodes u, v.

=> "min possible max-edge on any path between u and v"
   is answered by the MST path between u and v.
```

---

### 2.83 Kruskal Reconstruction Tree

```cpp
struct KruskalTree {
    int n;
    vector<int> par, val, dsuP;
    vector<vector<int>> children;
    int find(int x) { return dsuP[x] == x ? x : dsuP[x] = find(dsuP[x]); }
    void build(int n_, vector<array<int, 3>> &edges) {  // edges: {w, u, v}
        n = n_;
        sort(edges.begin(), edges.end());
        int cur = n;
        dsuP.resize(2 * n);
        iota(dsuP.begin(), dsuP.end(), 0);
        val.assign(2 * n, 0);
        children.assign(2 * n, {});
        for (auto &[w, u, v] : edges) {
            int ru = find(u), rv = find(v);
            if (ru == rv) continue;
            cur++;
            val[cur] = w;
            children[cur] = {ru, rv};
            dsuP[ru] = dsuP[rv] = dsuP[cur] = cur;
        }
    }
};
```

##### Use

- Answers "minimum possible maximum edge weight on a path between `u` and `v`" as `val[LCA(u, v)]` in the reconstruction tree, using the existing Binary Lifting / LCA section on top of it.

##### Complexity

- Build: `O(E log E)`; query: `O(log n)` per LCA once binary lifting is built on the reconstruction tree.

---

### 2.84 Bellman Ford

#### When To Use

```
Negative Edge Weights

Shortest Path

Negative Cycle Detection

Difference Constraints

When Dijkstra Cannot Be Used
```

---

### 2.85 Edge Structure

```cpp
struct edge {
    int u, v, w;
};
```

---

### 2.86 Standard Bellman Ford

```cpp
vector<int> dist(n + 1, INF);
dist[src] = 0;
for (int i = 1; i <= n - 1; i++) {
    bool changed = false;
    for (auto [u, v, w] : edges) {
        if (dist[u] == INF) continue;
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            changed = true;
        }
    }
    if (!changed) break;
}
```

##### Complexity

```
Time  : O(V * E)

Memory: O(V)
```

---

### 2.87 Negative Cycle Detection

```cpp
bool neg_cycle = false;
for (auto [u, v, w] : edges) {
    if (dist[u] == INF) continue;
    if (dist[v] > dist[u] + w) { neg_cycle = true; }
}
```

##### Meaning

```
There exists a reachable negative cycle.
```

---

### 2.88 Path Restore

```cpp
vector<int> dist(n + 1, INF);
vector<int> par(n + 1, -1);
dist[src] = 0;
for (int i = 1; i <= n - 1; i++) {
    for (auto [u, v, w] : edges) {
        if (dist[u] == INF) continue;
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            par[v] = u;
        }
    }
}
```

##### Restore Path

```cpp
vector<int> path;
for (int cur = dest; cur != -1; cur = par[cur]) { path.push_back(cur); }
reverse(all(path));
```

---

### 2.89 Restore Negative Cycle

```cpp
int x = -1;
for (int i = 1; i <= n; i++) {
    x = -1;
    for (auto [u, v, w] : edges) {
        if (dist[u] == INF) continue;
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            par[v] = u;
            x = v;
        }
    }
}
```

##### No Cycle

```cpp
if (x == -1) {
    // no negative cycle
}
```

---

##### Move Inside Cycle

```cpp
for (int i = 1; i <= n; i++) x = par[x];
```

---

##### Extract Cycle

```cpp
vector<int> cyc;
int cur = x;
do {
    cyc.push_back(cur);
    cur = par[cur];
} while (cur != x);
cyc.push_back(x);
reverse(all(cyc));
```

##### Complexity

```
O(V * E)
```

---

### 2.90 Difference Constraints

#### Constraints

```
x[v] - x[u] <= w
```

Convert to edge:

```
u -> v (weight w)
```

Then run:

```cpp
Bellman Ford
```

##### Use

```
Scheduling
Inequalities
Constraint Systems
```

---

### 2.91 Detect Any Negative Cycle

Sometimes source is unknown.

Create super source:

```cpp
for (int i = 1; i <= n; i++) edges.push_back({0, i, 0});
```

Then:

```cpp
Bellman Ford(0)
```

##### Meaning

```
Detect cycle anywhere in graph
```

---

### 2.92 Longest Path Trick

If graph has no positive cycle:

```
maximize path
```

Convert:

```cpp
w = -w;
```

Then:

```cpp
Bellman Ford
```

##### Warning

```
Need cycle handling
```

---

### 2.93 Reachability From Negative Cycle

After detecting cycle nodes:

```cpp
BFS / DFS
```

from cycle vertices.

##### Use

```
Infinite Profit
Infinite Path
CSES High Score
```

---

### 2.94 Useful Snippets

#### Unreachable Node

```cpp
if (dist[u] == INF) {}
```

---

#### Reachable Node

```cpp
if (dist[u] != INF) {}
```

---

#### Early Stop Optimization

```cpp
bool changed = false;
... if (!changed) break;
```

##### Benefit

```
Much faster in practice
```

---

### 2.95 Common Tricks

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

### 2.96 Common Problems

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

### 2.97 Dijkstra vs Bellman

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

### 2.98 Floyd Warshall

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

### 2.99 Standard Floyd Warshall

```cpp
vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));
for (int i = 1; i <= n; i++) dist[i][i] = 0;
for (auto [u, v, w] : edges) { dist[u][v] = min(dist[u][v], w); }
```

---

##### Main Floyd

```cpp
for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) { dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]); }
    }
}
```

##### Complexity

```
Time  : O(N³)

Memory: O(N²)
```

---

### 2.100 Undirected Graph

```cpp
dist[u][v] = dist[v][u] = w;
```

---

### 2.101 Multiple Edges

```cpp
dist[u][v] = min(dist[u][v], w);
```

---

### 2.102 Query Distance

```cpp
cout << dist[u][v];
```

---

### 2.103 Unreachable Nodes

```cpp
if (dist[u][v] == INF) {}
```

---

### 2.104 Negative Cycle Detection

After Floyd:

```cpp
for (int i = 1; i <= n; i++) {
    if (dist[i][i] < 0) {
        // negative cycle
    }
}
```

##### Why?

```
Shortest path
from node to itself

must be 0

unless negative cycle exists
```

---

### 2.105 Path Restoration

#### Parent Matrix

```cpp
vector<vector<int>> nxt(n + 1, vector<int>(n + 1, -1));
```

---

##### Initialization

```cpp
for (auto [u, v, w] : edges) {
    dist[u][v] = w;
    nxt[u][v] = v;
}
```

---

##### Floyd Update

```cpp
if (dist[i][j] > dist[i][k] + dist[k][j]) {
    dist[i][j] = dist[i][k] + dist[k][j];
    nxt[i][j] = nxt[i][k];
}
```

---

##### Restore Path

```cpp
vector<int> path;
int cur = u;
while (cur != v) {
    path.push_back(cur);
    cur = nxt[cur][v];
}
path.push_back(v);
```

##### No Path

```cpp
if (nxt[u][v] == -1) {}
```

---

### 2.106 Transitive Closure

Instead of shortest path:

```cpp
vector<vector<int>> reach(n + 1, vector<int>(n + 1));
```

---

##### Initialization

```cpp
reach[u][v] = 1;
```

---

##### Floyd

```cpp
for (int k = 1; k <= n; k++) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) { reach[i][j] |= reach[i][k] && reach[k][j]; }
    }
}
```

##### Meaning

```
Can i reach j from i ?
```

---

### 2.107 Minimum Directed Cycle

After Floyd:

```cpp
int ans = INF;
for (int i = 1; i <= n; i++) { ans = min(ans, dist[i][i]); }
```

##### Note

```
Works if cycle exists
```

---

### 2.108 Character Conversion Problems

Example:

```
a -> b cost 3

b -> c cost 5

Find minimum cost
to convert strings
```

---

##### Build Graph

```cpp
dist[a][b] = cost;
```

Run Floyd.

##### Use

```
26 letters only

Perfect Floyd problem
```

---

### 2.109 Floyd On States

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

### 2.110 APSP Queries

```cpp
run Floyd once
```

Then:

```cpp
answer Q queries O(1)
```

##### Total

```
Preprocess : O(N³)

Query      : O(1)
```

---

### 2.111 Useful Snippets

#### Check Reachability

```cpp
if (dist[u][v] != INF) {}
```

---

#### Check Same SCC (small graph)

```cpp
if (dist[u][v] != INF && dist[v][u] != INF) {}
```

##### Meaning

```
Mutually reachable
```

---

#### Count Reachable Nodes

```cpp
int cnt = 0;
for (int v = 1; v <= n; v++) {
    if (dist[u][v] != INF) cnt++;
}
```

---

### 2.112 Common Tricks

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

### 2.113 Common Problems

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

### 2.114 Dijkstra vs Floyd

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

### 2.115 Bellman vs Floyd

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

---

### 2.116 Graph Diameter Via Floyd-Warshall

```cpp
long long graphDiameter(int n, vector<vector<long long>> &dist) {
    long long diam = 0;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (dist[i][j] < INF) diam = max(diam, dist[i][j]);
    return diam;
}
```

##### Use

- Once `dist[][]` is computed by Floyd-Warshall, the graph diameter is just the max finite entry.
- Counting the number of shortest paths between every pair can be tracked alongside with an extra `cnt[i][j]` matrix updated the same way as the BFS/Dijkstra path-count tricks.

---

### 2.117 Shortest Paths — Recommended Practice

```
CSES - Shortest Routes I (Dijkstra)
CSES - Shortest Routes II (Floyd-Warshall)
CSES - High Score (Bellman-Ford, negative cycle detection)
CSES - Cycle Finding (Bellman-Ford negative cycle)
CSES - Flight Discount (modified Dijkstra, one discounted edge)
CSES - Investigation (shortest path count + min/max edges on shortest path)
Codeforces - Dijkstra? (classic Dijkstra warm-up)
Classic - 0-1 BFS on a grid with weighted 0/1 edges
Classic - Cheapest Flights Within K Stops (Bellman-Ford with a hop limit)
```


## 3) Trees & Binary Lifting

### 3.1 Binary Lifting

#### When To Use

```
Kth Ancestor

Jump Up K Levels

Tree Queries

LCA Preparation

Fast Ancestor Queries
```

---

### 3.2 Idea

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

### 3.3 Template

```cpp
const int LG = 20;
vector<vector<int>> up;
vector<int> dep;
vector<vector<int>> adj;
void dfs(int u, int p) {
    up[u][0] = p;
    for (int j = 1; j < LG; j++) { up[u][j] = up[up[u][j - 1]][j - 1]; }
    for (auto v : adj[u]) {
        if (v == p) continue;
        dep[v] = dep[u] + 1;
        dfs(v, u);
    }
}
void build(int n, int root = 1) {
    up.assign(n + 1, vector<int>(LG));
    dep.assign(n + 1, 0);
    dfs(root, root);
}
```

---

### 3.4 Jump K Levels

```cpp
int jump(int u, int k) {
    for (int j = 0; j < LG; j++) {
        if (k & (1LL << j)) u = up[u][j];
    }
    return u;
}
```

##### Complexity

```
O(log N)
```

---

### 3.5 Kth Ancestor

```cpp
int kth_ancestor(int u, int k) { return jump(u, k); }
```

##### Example

```cpp
cout << kth_ancestor(10, 3);
```

Meaning:

```
3rd ancestor of node 10
```

---

### 3.6 Check Ancestor

Needs Euler Tour.

```cpp
bool is_ancestor(int u, int v) { return tin[u] <= tin[v] && tout[v] <= tout[u]; }
```

##### Complexity

```
O(1)
```

---

### 3.7 Lift To Same Depth

```cpp
if (dep[u] < dep[v]) swap(u, v);
u = jump(u, dep[u] - dep[v]);
```

##### Use

```
LCA
Path Queries
```

---

### 3.8 Distance To Root

```cpp
dep[u]
```

##### Meaning

```
Number of edges
from root to u
```

---

### 3.9 Build Complexity

```
O(N log N)
```

---

### 3.10 Query Complexity

```
Jump
Ancestor
Lift

O(log N)
```

---

### 3.11 Memory

```
O(N log N)
```

---

### 3.12 Useful Snippets

#### Parent

```cpp
up[u][0]
```

---

#### Grand Parent

```cpp
up[u][1]
```

---

#### 4th Ancestor

```cpp
up[u][2]
```

because:

```
2² = 4
```

---

#### Move Up One Level

```cpp
u = up[u][0];
```

---

#### Move Up 13 Levels

```cpp
u = jump(u, 13);
```

---

#### Root Check

```cpp
if (u == root) {}
```

---

### 3.13 Common Tricks

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

### 3.14 Common Problems

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

### 3.15 Maximum N Guide

| N | LG |
| --- | --- |
| 1e5 | 17 |
| 2e5 | 18 |
| 5e5 | 19 |
| 1e6 | 20 |

##### Safe Choice

```cpp
const int LG = 20;
```

for:

```
N <= 1e6
```

---

### 3.16 Common Mistakes

#### Wrong

```cpp
dfs(root, 0);
```

Then:

```cpp
up[0][j]
```

may be accessed.

---

#### Safer

```cpp
dfs(root, root);
```

---

#### Wrong LG

```cpp
const int LG = 17;
```

while:

```
N = 2e5
```

---

#### Safe

```cpp
const int LG = 20;
```

---

### 3.17 Notes

```
Binary Lifting alone does NOT solve LCA.

It is only the preprocessing layer.

Next topic:
LCA
```

---

### 3.18 Weighted Binary Lifting (Max/Min Edge On Path)

```cpp
int up[LG][N];
long long mxEdge[LG][N];
void buildWeighted(int n, vector<int> &par, vector<long long> &edgeToParent) {
    for (int v = 1; v <= n; v++) {
        up[0][v] = par[v];
        mxEdge[0][v] = edgeToParent[v];
    }
    for (int k = 1; k < LG; k++)
        for (int v = 1; v <= n; v++) {
            up[k][v] = up[k - 1][up[k - 1][v]];
            mxEdge[k][v] = max(mxEdge[k - 1][v], mxEdge[k - 1][up[k - 1][v]]);
        }
}
long long maxEdgeToKthAncestor(int v, int k) {
    long long best = 0;
    for (int i = 0; i < LG; i++)
        if (k >> i & 1) {
            best = max(best, mxEdge[i][v]);
            v = up[i][v];
        }
    return best;
}
```

##### Use

- "Max/min edge weight on the path to the kth ancestor" or, combined with LCA, "max/min edge on the path between `u` and `v`".
- Same jump table as plain binary lifting, with an extra array carried alongside `up[k][v]`.

##### Complexity

- Build: `O(n log n)`; query: `O(log n)`.

---

### 3.19 Binary Lifting On Functional Graphs (Successor Arrays)

```cpp
int up[LG][N];  // up[0][i] = nxt[i], given some functional array "next pointer" nxt[]
void buildFunctional(int n, vector<int> &nxt) {
    for (int i = 0; i < n; i++) up[0][i] = nxt[i];
    for (int k = 1; k < LG; k++)
        for (int i = 0; i < n; i++) up[k][i] = up[k - 1][up[k - 1][i]];
}
int jump(int i, long long k) {
    for (int b = 0; b < LG && k; b++, k >>= 1)
        if (k & 1) i = up[b][i];
    return i;
}
```

##### Use

- The same binary-lifting jump table as tree LCA, but applied to an arbitrary array `nxt[i]` that isn't necessarily a tree — e.g. "where do you end up after k steps of `i = nxt[i]`", used for functional graph problems, cycle detection, and permutation-power queries.
- Since `nxt[i]` can point anywhere (including forming cycles), this works even when the "graph" isn't a tree, unlike the tree-only LCA binary lifting above.
- Detecting the cycle a node eventually falls into: binary-search on `k` using `jump(i, k)` combined with Floyd's cycle detection, or just jump `up to LOG(maxK)` steps directly once `LG` covers the needed range.

##### Complexity

- Build: `O(n log MAXK)`; query: `O(log k)` per jump.

---

### 3.20 Binary Lifting — Recommended Practice

```
CSES - Planets Queries I (binary lifting on a functional graph)
CSES - Planets Queries II (functional graph + cycle detection)
CSES - Company Queries I (kth ancestor)
CSES - Company Queries II (LCA)
Codeforces - Kth Ancestor (offline binary lifting variant)
Classic - Permutation applied k times (cycle decomposition + binary lifting)
```

---

### 3.21 LCA (Lowest Common Ancestor)

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

### 3.22 Idea

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

### 3.23 Template

```cpp
const int LG = 20;
vector<vector<int>> adj;
vector<vector<int>> up;
vector<int> dep;
void dfs(int u, int p) {
    up[u][0] = p;
    for (int j = 1; j < LG; j++) { up[u][j] = up[up[u][j - 1]][j - 1]; }
    for (auto v : adj[u]) {
        if (v == p) continue;
        dep[v] = dep[u] + 1;
        dfs(v, u);
    }
}
void build(int n, int root = 1) {
    up.assign(n + 1, vector<int>(LG));
    dep.assign(n + 1, 0);
    dfs(root, root);
}
```

---

### 3.24 LCA Query

```cpp
int lca(int u, int v) {
    if (dep[u] < dep[v]) swap(u, v);
    int diff = dep[u] - dep[v];
    for (int j = 0; j < LG; j++) {
        if (diff & (1LL << j)) u = up[u][j];
    }
    if (u == v) return u;
    for (int j = LG - 1; j >= 0; j--) {
        if (up[u][j] != up[v][j]) {
            u = up[u][j];
            v = up[v][j];
        }
    }
    return up[u][0];
}
```

##### Complexity

```
O(log N)
```

---

### 3.25 Distance Between Two Nodes

```cpp
int dist(int u, int v) {
    int p = lca(u, v);
    return dep[u] + dep[v] - 2 * dep[p];
}
```

##### Complexity

```
O(log N)
```

---

### 3.26 Kth Ancestor

```cpp
int jump(int u, int k) {
    for (int j = 0; j < LG; j++) {
        if (k & (1LL << j)) u = up[u][j];
    }
    return u;
}
```

---

### 3.27 Check Ancestor

Needs Euler Tour.

```cpp
bool is_ancestor(int u, int v) { return tin[u] <= tin[v] && tout[v] <= tout[u]; }
```

##### Complexity

```
O(1)
```

---

### 3.28 Kth Node On Path

Path:

```
u -------- v
```

Suppose:

```cpp
int p = lca(u, v);
```

---

##### Lengths

```cpp
int left = dep[u] - dep[p];
int right = dep[v] - dep[p];
```

---

##### Query

```cpp
int kth(int u, int v, int k) {
    int p = lca(u, v);
    int left = dep[u] - dep[p];
    if (k <= left) return jump(u, k);
    k -= left;
    int right = dep[v] - dep[p];
    return jump(v, right - k);
}
```

##### Use

```
SPOJ QTREE2
```

---

### 3.29 Length Of Path

```cpp
dist(u, v)
```

returns:

```
number of edges
```

---

### 3.30 Number Of Nodes On Path

```cpp
dist(u, v) + 1
```

---

### 3.31 Check If Node Lies On Path

```cpp
dist(u, x) + dist(x, v) == dist(u, v)
```

##### Complexity

```
O(log N)
```

---

### 3.32 Find Parent

```cpp
up[u][0]
```

---

### 3.33 Find Root Distance

```cpp
dep[u]
```

---

### 3.34 Path Through LCA

Every path:

```
u -> lca

+

lca -> v
```

Remember this.

Used everywhere.

---

### 3.35 Useful Snippets

#### LCA

```cpp
int p = lca(u, v);
```

---

#### Distance

```cpp
cout << dist(u, v);
```

---

#### Parent

```cpp
cout << up[u][0];
```

---

#### Grand Parent

```cpp
cout << up[u][1];
```

---

#### Jump 10 Levels

```cpp
cout << jump(u, 10);
```

---

#### Same Depth

```cpp
u = jump(u, dep[u] - dep[v]);
```

---

### 3.36 Common Tricks

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

### 3.37 Complexity Summary

| Operation | Complexity |
| --- | --- |
| Build | O(N log N) |
| LCA | O(log N) |
| Distance | O(log N) |
| Jump | O(log N) |
| Kth Ancestor | O(log N) |
| Kth Node Path | O(log N) |

---

### 3.38 Memory

```
O(N log N)
```

---

### 3.39 Common Problems

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

### 3.40 ACPC Notes

Most common formulas:

#### Distance

```cpp
dep[u] + dep[v] - 2 * dep[lca(u, v)]
```

---

#### Number Of Nodes

```cpp
dist(u, v) + 1
```

---

#### Node On Path

```cpp
dist(u, x) + dist(x, v) == dist(u, v)
```

---

#### Path

```
u -> lca -> v
```

If you remember only these four,
you can solve a huge number of tree problems.

---

### 3.41 O(1) LCA (Euler Tour + Sparse Table)

```cpp
vector<int> euler, first_occ, eulerDepth;
void dfsEuler(int u, int p, int d, vector<vector<int>> &adj) {
    first_occ[u] = euler.size();
    euler.push_back(u);
    eulerDepth.push_back(d);
    for (int v : adj[u])
        if (v != p) {
            dfsEuler(v, u, d + 1, adj);
            euler.push_back(u);
            eulerDepth.push_back(d);
        }
}
// Build a min-Sparse-Table over eulerDepth (see Sparse Table section) storing the
// euler index of the minimum, then:
int lcaO1(int u, int v, SparseTable &st) {  // SparseTable built on (eulerDepth, index)
    int l = first_occ[u], r = first_occ[v];
    if (l > r) swap(l, r);
    int idx = st.query(l, r);  // index of min depth in [l, r]
    return euler[idx];
}
```

##### Use

- Alternative to Binary Lifting LCA: `O(n log n)` build, `O(1)` per query instead of `O(log n)`.
- Reuses the existing Sparse Table section directly (min-query over `(depth, eulerIndex)` pairs).

##### Complexity

- Build: `O(n log n)`; query: `O(1)`.

---

### 3.42 Centroid Decomposition

```cpp
vector<int> subSz, removed;
int getSz(int u, int p, vector<vector<int>> &adj) {
    subSz[u] = 1;
    for (int v : adj[u])
        if (v != p && !removed[v]) subSz[u] += getSz(v, u, adj);
    return subSz[u];
}
int getCentroid(int u, int p, int treeSz, vector<vector<int>> &adj) {
    for (int v : adj[u])
        if (v != p && !removed[v] && subSz[v] > treeSz / 2) return getCentroid(v, u, treeSz, adj);
    return u;
}
void decompose(int u, vector<vector<int>> &adj) {
    int treeSz = getSz(u, -1, adj);
    int c = getCentroid(u, -1, treeSz, adj);
    removed[c] = true;
    // process paths through centroid c here
    for (int v : adj[c])
        if (!removed[v]) decompose(v, adj);
}
```

##### When To Use

```
Count / query paths in a tree (path length k, path sum, etc.)
Divide and conquer over tree structure
Distance-related aggregate queries
```

##### Complexity

- Build: `O(n log n)`; each level processes `O(n)` nodes total across `O(log n)` levels.

---

### 3.43 DSU On Tree (Small-To-Large Over Subtrees)

```cpp
vector<int> sz, bigChild, cnt;
void calcSz(int u, int p, vector<vector<int>> &adj) {
    sz[u] = 1;
    bigChild[u] = -1;
    int mx = 0;
    for (int v : adj[u])
        if (v != p) {
            calcSz(v, u, adj);
            sz[u] += sz[v];
            if (sz[v] > mx) mx = sz[v], bigChild[u] = v;
        }
}
void addSubtree(int u, int p, int val, vector<vector<int>> &adj) {
    cnt[val]++;  // update whatever aggregate you're tracking
    for (int v : adj[u])
        if (v != p) addSubtree(v, u, val, adj);
}
void dsuOnTree(int u, int p, bool keep, vector<vector<int>> &adj, vector<int> &color) {
    for (int v : adj[u])
        if (v != p && v != bigChild[u]) dsuOnTree(v, u, false, adj, color);
    if (bigChild[u] != -1) dsuOnTree(bigChild[u], u, true, adj, color);
    for (int v : adj[u])
        if (v != p && v != bigChild[u]) addSubtree(v, u, color[v], adj);
    cnt[color[u]]++;
    // answer for subtree(u) can be read from cnt[] here
    if (!keep) {
        // roll back: remove this subtree's contribution from cnt[]
    }
}
```

##### Use

- Answer per-subtree aggregate queries (e.g. "number of distinct colors in subtree") in `O(n log n)` total instead of `O(n^2)`.
- Distinct from the generic "Small To Large" merging trick already in the STL chapter — this specifically merges child subtree *data structures* while keeping the heavy child's structure to avoid rebuilding it.

##### Complexity

- `O(n log n)`

---

### 3.44 Rerooting DP (Change Of Root Technique)

```cpp
vector<long long> down, up_, ans;
void dfsDown(int u, int p, vector<vector<int>> &adj) {
    down[u] = 0;
    for (int v : adj[u])
        if (v != p) {
            dfsDown(v, u, adj);
            down[u] += down[v] + subSz[v];  // example: sum of distances inside subtree
        }
}
void dfsUp(int u, int p, int n, vector<vector<int>> &adj) {
    ans[u] = down[u] + up_[u];
    for (int v : adj[u])
        if (v != p) {
            // combine everything except v's own contribution, then add edge (u,v)
            up_[v] = (ans[u] - (down[v] + subSz[v])) + (n - subSz[v]);
            dfsUp(v, u, n, adj);
        }
}
```

##### Use

- Computes an answer for *every* node as root in `O(n)` total instead of running an `O(n)` DFS from each node separately (`O(n^2)`).
- Classic applications: sum of distances to all other nodes, maximum distance from each node, subtree-dependent counts re-evaluated per root.

##### Complexity

- `O(n)` total (two DFS passes).


## 4) Strings

### 4.1 KMP (Knuth-Morris-Pratt)

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

### 4.2 Prefix Function

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

### 4.3 Prefix Function Template

```cpp
vector<int> prefix_function(string s) {
    int n = s.size();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j]) { j = pi[j - 1]; }
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    return pi;
}
```

##### Complexity

```
O(N)
```

##### Memory

```
O(N)
```

---

### 4.4 Pattern Matching

Find all occurrences of:

```
pattern p

inside

text t
```

---

##### Build String

```cpp
string s = p + "#" + t;
```

---

##### Compute Prefix

```cpp
auto pi = prefix_function(s);
```

---

##### Occurrences

```cpp
vector<int> pos;
int m = p.size();
for (int i = m + 1; i < s.size(); i++) {
    if (pi[i] == m) { pos.push_back(i - 2 * m); }
}
```

##### Complexity

```
O(N + M)
```

---

### 4.5 KMP Search Template

```cpp
vector<int> kmp(string t, string p) {
    string s = p + "#" + t;
    auto pi = prefix_function(s);
    vector<int> pos;
    int m = p.size();
    for (int i = m + 1; i < s.size(); i++) {
        if (pi[i] == m) { pos.push_back(i - 2 * m); }
    }
    return pos;
}
```

---

### 4.6 KMP Automaton + DP Over Automaton States

```cpp
vector<array<int, 26>> buildAutomaton(const string &p) {
    int m = p.size();
    auto pi = prefix_function(p);
    vector<array<int, 26>> aut(m + 1);
    for (int state = 0; state <= m; state++) {
        for (int c = 0; c < 26; c++) {
            if (state < m && p[state] - 'a' == c) {
                aut[state][c] = state + 1;
            } else if (state == 0) {
                aut[state][c] = 0;
            } else {
                aut[state][c] = aut[pi[state - 1]][c];
            }
        }
    }
    return aut;
}
// dp[i][state] = number of strings of length i whose KMP-matching progress against
// pattern p is exactly `state`, without ever reaching state == m (pattern found).
long long countAvoiding(int n, string &p, long long mod) {
    int m = p.size();
    auto aut = buildAutomaton(p);
    vector<long long> dp(m, 0), ndp(m, 0);
    dp[0] = 1;
    for (int i = 0; i < n; i++) {
        fill(ndp.begin(), ndp.end(), 0);
        for (int state = 0; state < m; state++) {
            if (!dp[state]) continue;
            for (int c = 0; c < 26; c++) {
                int ns = aut[state][c];
                if (ns == m) continue;  // pattern matched, discard this branch
                ndp[ns] = (ndp[ns] + dp[state]) % mod;
            }
        }
        dp = ndp;
    }
    long long total = 0;
    for (long long x : dp) total = (total + x) % mod;
    return total;
}
```

##### Use

```
Count strings of length n over an alphabet that never contain pattern p as a substring
Count strings that contain p as a substring exactly k times (extend the DP with a count dimension)
Build automaton once in O(M * alphabet), then any "state transition" DP runs in O(N * M * alphabet)
```

##### Note

- Precomputing `aut[state][c]` for every state/char turns "follow failure links until match or state 0" into an O(1) transition, which is what makes the DP over states run fast.
- Reuses the existing `prefix_function` from the KMP section directly.

##### Complexity

```
Build automaton : O(M * alphabet)
DP over states  : O(N * M * alphabet)
```

---

### 4.7 KMP — Recommended Practice

```
CSES - Finding Borders
CSES - Finding Periods
CSES - String Matching
Codeforces - Password (double technique: KMP + Z-function)
Classic - Count strings of length n avoiding a given pattern (KMP automaton DP)
Classic - Count occurrences of pattern as substring (including overlaps)
```

---

### 4.8 Longest Border

Border means:

```
Prefix

=

Suffix
```

but not entire string.

---

##### Answer

```cpp
auto pi = prefix_function(s);
cout << pi.back();
```

##### Complexity

```
O(N)
```

---

### 4.9 All Borders

```cpp
auto pi = prefix_function(s);
vector<int> borders;
int cur = pi.back();
while (cur > 0) {
    borders.push_back(cur);
    cur = pi[cur - 1];
}
```

##### Complexity

```
O(N)
```

---

### 4.10 Count Occurrences Of Every Prefix

```cpp
auto pi = prefix_function(s);
vector<int> cnt(s.size() + 1);
for (auto x : pi) cnt[x]++;
for (int i = s.size(); i > 0; i--) { cnt[pi[i - 1]] += cnt[i]; }
for (int i = 0; i <= s.size(); i++) { cnt[i]++; }
```

##### Meaning

```
cnt[len]

=

number of occurrences
of prefix length len
```

---

### 4.11 String Period

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

```cpp
int n = s.size();
auto pi = prefix_function(s);
int len = n - pi.back();
```

---

##### Check

```cpp
if (n % len == 0) {
    // periodic
}
```

---

### 4.12 Smallest Period

```cpp
int n = s.size();
auto pi = prefix_function(s);
int len = n - pi.back();
if (n % len == 0)
    cout << len;
else
    cout << n;
```

---

### 4.13 Prefix Automaton Jump

```cpp
j = pi[j - 1];
```

##### Meaning

```
Go to next valid border
```

This is the whole magic of KMP.

---

### 4.14 Distinct Prefix-Suffix Chain

```cpp
int cur = pi.back();
while (cur > 0) {
    cout << cur << endl;
    cur = pi[cur - 1];
}
```

##### Use

```
Borders Problems
```

---

### 4.15 Useful Snippets

#### Prefix Array

```cpp
auto pi = prefix_function(s);
```

---

#### Longest Border

```cpp
cout << pi.back();
```

---

#### Check Border Length K

```cpp
if (pi.back() >= k) {}
```

---

#### Number Of Occurrences

```cpp
auto pos = kmp(text, pattern);
cout << pos.size();
```

---

#### First Occurrence

```cpp
if (!pos.empty()) { cout << pos[0]; }
```

---

### 4.16 Common Tricks

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

### 4.17 Complexity Summary

| Operation | Complexity |
| --- | --- |
| Prefix Function | O(N) |
| Pattern Matching | O(N+M) |
| Borders | O(N) |
| Period | O(N) |

---

### 4.18 Common Problems

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

### 4.19 ACPC Notes

Most used formulas:

#### Longest Border

```cpp
pi.back()
```

---

#### Smallest Period

```cpp
n - pi.back()
```

---

#### Pattern Matching

```cpp
pattern + "#" + text
```

---

#### Border Chain

```cpp
cur = pi[cur - 1]
```

These four cover the majority of KMP problems.

---

### 4.20 Z-Function

```cpp
vector<int> z_function(const string &s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
    }
    return z;
}
```

##### When To Use

```
Pattern matching (pattern + '#' + text, same as KMP)
Finding all borders / periods
Counting distinct substrings variants
```

##### Complexity

```
O(N)
```

##### Notes

- `z[i]` = length of the longest common prefix between `s` and `s[i..]`.
- Same "pattern + separator + text" trick as KMP for search: matches occur where `z[i] == len(pattern)`.

---

### 4.21 String Hashing (Polynomial Rolling Hash)

```cpp
struct StringHash {
    vector<long long> h, pw;
    long long mod, base;
    StringHash(const string &s, long long mod_ = 1'000'000'007, long long base_ = 131) {
        mod = mod_;
        base = base_;
        int n = s.size();
        h.assign(n + 1, 0);
        pw.assign(n + 1, 1);
        for (int i = 0; i < n; i++) {
            h[i + 1] = (h[i] * base + s[i]) % mod;
            pw[i + 1] = pw[i] * base % mod;
        }
    }
    long long get(int l, int r) const {  // hash of s[l..r], 0-indexed inclusive
        long long res = (h[r + 1] - h[l] * pw[r - l + 1]) % mod;
        return (res + mod) % mod;
    }
};
```

##### When To Use

```
O(1) substring comparison after O(N) build
Palindrome checks (compare hash of s[l..r] vs reversed s[l..r])
Duplicate / repeated substring detection
Binary search on longest common prefix between two positions
```

##### Complexity

```
Build : O(N)
Query : O(1)
```

##### Notes

- Use two independent hashes (different `mod`/`base`) and compare both to avoid collisions in adversarial problems.
- To compare `s[l1..r1]` with `s[l2..r2]`: equal length and `get(l1, r1) == get(l2, r2)`.

---

### 4.22 Hashing — Recommended Practice

```
CSES - Finding Similar Substrings
CSES - String Matching (hashing alternative to KMP)
Codeforces - Palindromic Characteristics (Manacher + hashing combo)
Classic - Count distinct substrings of a string
Classic - Longest common substring of two strings (binary search + hashing)
Classic - Check if string A's rotation equals string B
```

---

### 4.23 Manacher's Algorithm (Longest Palindromic Substring)

```cpp
vector<int> manacher(const string &s) {
    string t = "^";
    for (char c : s) t += string("#") + c;
    t += "#$";
    int n = t.size();
    vector<int> p(n, 0);
    int c = 0, r = 0;
    for (int i = 1; i < n - 1; i++) {
        if (i < r) p[i] = min(r - i, p[2 * c - i]);
        while (t[i + p[i] + 1] == t[i - p[i] - 1]) p[i]++;
        if (i + p[i] > r) c = i, r = i + p[i];
    }
    return p;  // p[i] = radius of palindrome centered at t[i]
}
```

##### When To Use

```
Longest palindromic substring
Counting all palindromic substrings
Palindrome-related DP preprocessing
```

##### Complexity

```
O(N)
```

##### Notes

- Works uniformly for odd and even length palindromes via the transformed string `t`.
- Longest palindromic substring length = `max(p[i])`; its center in the original string is `(i - 1) / 2` (integer division after removing the transform offset).


## 5) Range Query Data Structures

### 5.1 Segment Tree

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

```cpp
#define LNode(n) (2 * (n) + 1)
#define RNode(n) (2 * (n) + 2)
#define md(lx, rx) ((lx) + ((rx) - (lx)) / 2)
struct Node {
    int val;
    Node() { val = INF; }
    Node(int x) { val = x; }
};
struct SegTree {
    int tree_size;
    vector<Node> seg_data;
    SegTree(int n) {
        tree_size = 1;
        while (tree_size < n) tree_size *= 2;
        seg_data.resize(2 * tree_size);
    }
    Node merge(Node &a, Node &b) {
        Node res;
        res.val = min(a.val, b.val);
        return res;
    }
    void init(vector<int> &nums, int ni, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < nums.size()) seg_data[ni] = Node(nums[lx]);
            return;
        }
        init(nums, LNode(ni), lx, md(lx, rx));
        init(nums, RNode(ni), md(lx, rx), rx);
        seg_data[ni] = merge(seg_data[LNode(ni)], seg_data[RNode(ni)]);
    }
    void init(vector<int> &nums) { init(nums, 0, 0, tree_size); }
    void update(int idx, int val, int ni, int lx, int rx) {
        if (rx - lx == 1) {
            seg_data[ni] = Node(val);
            return;
        }
        if (idx < md(lx, rx)) {
            update(idx, val, LNode(ni), lx, md(lx, rx));
        } else {
            update(idx, val, RNode(ni), md(lx, rx), rx);
        }
        seg_data[ni] = merge(seg_data[LNode(ni)], seg_data[RNode(ni)]);
    }
    void update(int idx, int val) { update(idx, val, 0, 0, tree_size); }
    Node query(int l, int r, int ni, int lx, int rx) {
        if (lx >= r || rx <= l) { return Node(); }
        if (lx >= l && rx <= r) { return seg_data[ni]; }
        Node lf = query(l, r, LNode(ni), lx, md(lx, rx));
        Node ri = query(l, r, RNode(ni), md(lx, rx), rx);
        return merge(lf, ri);
    }
    int query(int l, int r) { return query(l, r, 0, 0, tree_size).val; }
};
```

---

#### Common Modifications

##### Range Sum

```cpp
res.val = a.val + b.val;
```

Identity:

```cpp
val = 0;
```

---

##### Range Maximum

```cpp
res.val = max(a.val, b.val);
```

Identity:

```cpp
val = -INF;
```

---

##### Range GCD

```cpp
res.val = gcd(a.val, b.val);
```

Identity:

```cpp
val = 0;
```

---

##### Range XOR

```cpp
res.val = a.val ^ b.val;
```

Identity:

```cpp
val = 0;
```

---

### 5.2 Notes

```
Most Segment Trees
only change:

Node

merge()

identity value
```

---

### 5.3 Iterative Segment Tree (Bottom-Up)

```cpp
struct IterSegTree {
    int n;
    vector<long long> t;
    IterSegTree(int n_) {
        n = n_;
        t.assign(2 * n, 0);
    }
    void build(vector<long long> &a) {
        for (int i = 0; i < n; i++) t[n + i] = a[i];
        for (int i = n - 1; i > 0; i--) t[i] = min(t[2 * i], t[2 * i + 1]);
    }
    void update(int i, long long val) {
        for (t[i += n] = val; i > 1; i >>= 1) t[i >> 1] = min(t[i], t[i ^ 1]);
    }
    long long query(int l, int r) {  // [l, r)
        long long res = LLONG_MAX;
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l & 1) res = min(res, t[l++]);
            if (r & 1) res = min(res, t[--r]);
        }
        return res;
    }
};
```

##### Use

- Same point-update / range-query segment tree as the recursive version, but non-recursive with a smaller constant factor.
- Simplest to write for point update + range min/max/sum; harder to extend to lazy propagation (use the recursive version for that).

##### Complexity

```
Build : O(N)
Update : O(log N)
Query : O(log N)
```

---

### 5.4 Segment Tree — Recommended Practice

```
CSES - Dynamic Range Minimum Queries
CSES - Dynamic Range Sum Queries
CSES - Range Update Queries
CSES - Distinct Values Queries
Codeforces - Kth Number (persistent segment tree)
Classic - Count inversions with point updates
```

---

### 5.5 Lazy Segment Tree

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

```cpp
#define LNode(n) (2 * (n) + 1)
#define RNode(n) (2 * (n) + 2)
#define md(lx, rx) ((lx) + ((rx) - (lx)) / 2)
struct Node {
    int val;
    int lazy;
    bool is_lazy;
    Node() {
        val = INF;
        lazy = 0;
        is_lazy = false;
    }
    Node(int x) {
        val = x;
        lazy = 0;
        is_lazy = false;
    }
    void assign(int x) {
        val = x;
        lazy = x;
        is_lazy = true;
    }
};
struct SegTree {
    int tree_size;
    vector<Node> seg_data;
    SegTree(int n) {
        tree_size = 1;
        while (tree_size < n) tree_size *= 2;
        seg_data.resize(2 * tree_size);
    }
    Node merge(Node &a, Node &b) {
        Node res;
        res.val = min(a.val, b.val);
        return res;
    }
    void init(vector<int> &nums, int ni, int lx, int rx) {
        if (rx - lx == 1) {
            if (lx < nums.size()) seg_data[ni] = Node(nums[lx]);
            return;
        }
        init(nums, LNode(ni), lx, md(lx, rx));
        init(nums, RNode(ni), md(lx, rx), rx);
        seg_data[ni] = merge(seg_data[LNode(ni)], seg_data[RNode(ni)]);
    }
    void init(vector<int> &nums) { init(nums, 0, 0, tree_size); }
    void propagate(int ni, int lx, int rx) {
        if (rx - lx == 1 || !seg_data[ni].is_lazy) return;
        seg_data[LNode(ni)].assign(seg_data[ni].lazy);
        seg_data[RNode(ni)].assign(seg_data[ni].lazy);
        seg_data[ni].is_lazy = false;
    }
    void update(int l, int r, int val, int ni, int lx, int rx) {
        propagate(ni, lx, rx);
        if (lx >= l && rx <= r) {
            seg_data[ni].assign(val);
            return;
        }
        if (lx >= r || rx <= l) { return; }
        update(l, r, val, LNode(ni), lx, md(lx, rx));
        update(l, r, val, RNode(ni), md(lx, rx), rx);
        seg_data[ni] = merge(seg_data[LNode(ni)], seg_data[RNode(ni)]);
    }
    void update(int l, int r, int val) { update(l, r, val, 0, 0, tree_size); }
    Node query(int l, int r, int ni, int lx, int rx) {
        propagate(ni, lx, rx);
        if (lx >= r || rx <= l) { return Node(); }
        if (lx >= l && rx <= r) { return seg_data[ni]; }
        Node lf = query(l, r, LNode(ni), lx, md(lx, rx));
        Node ri = query(l, r, RNode(ni), md(lx, rx), rx);
        return merge(lf, ri);
    }
    int query(int l, int r) { return query(l, r, 0, 0, tree_size).val; }
};
```

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

---

### 5.6 Lazy Segment Tree — Recommended Practice

```
CSES - Range Update Queries
CSES - Polynomial Range Queries (range add, range sum of squares/cubes)
CSES - Forest Queries II (2D variant, harder extension)
Codeforces - Chtholly's request (range assign + range sum, segment tree beats style)
Classic - Range add, range max query
Classic - Range assign, range sum query
```

### 5.7 Sparse Table

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

### 5.8 Range Minimum Query

##### Template

```cpp
struct SparseTable {
    int n;
    vector<vector<int>> st;
    vector<int> lg;
    SparseTable() {}
    SparseTable(vector<int> &a) { build(a); }
    int merge(int a, int b) { return min(a, b); }
    void build(vector<int> &a) {
        n = a.size();
        lg.assign(n + 1, 0);
        for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
        int k = lg[n] + 1;
        st.assign(k, vector<int>(n));
        st[0] = a;
        for (int j = 1; j < k; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st[j][i] = merge(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
            }
        }
    }
    int query(int l, int r) {
        int k = lg[r - l + 1];
        return merge(st[k][l], st[k][r - (1 << k) + 1]);
    }
};
```

---

#### Query

```cpp
SparseTable sp(a);
cout << sp.query(l, r);
```

##### Complexity

```
O(1)
```

---

### 5.9 Range Maximum Query

Change only:

```cpp
int merge(int a, int b) { return max(a, b); }
```

---

### 5.10 Range GCD Query

Change only:

```cpp
int merge(int a, int b) { return gcd(a, b); }
```

---

### 5.11 Tricks

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

### 5.12 Memory

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

### 5.13 Limitations

```
No Updates

Static Array Only
```

If updates exist:

```
Use Segment Tree
```

---

### 5.14 Most Common Uses

```
RMQ

Maximum Query

GCD Query

Binary Search + RMQ

Binary Search + GCD

LCA (Euler Tour + Sparse Table)
```

---

### 5.15 Persistent Segment Tree

```cpp
struct PersistentSegTree {
    struct Node {
        int val;
        int l, r;
    };
    vector<Node> t;
    vector<int> roots;
    int n;
    PersistentSegTree(int n_) : n(n_) { roots.push_back(build(0, n - 1)); }
    int build(int lx, int rx) {
        int id = t.size();
        t.push_back({0, -1, -1});
        if (lx == rx) return id;
        int m = (lx + rx) / 2;
        t[id].l = build(lx, m);
        t[id].r = build(m + 1, rx);
        return id;
    }
    int update(int prev, int lx, int rx, int pos, int val) {
        int id = t.size();
        t.push_back(t[prev]);
        if (lx == rx) {
            t[id].val += val;
            return id;
        }
        int m = (lx + rx) / 2;
        if (pos <= m)
            t[id].l = update(t[prev].l, lx, m, pos, val);
        else
            t[id].r = update(t[prev].r, m + 1, rx, pos, val);
        t[id].val = t[t[id].l].val + t[t[id].r].val;
        return id;
    }
    int query(int node, int lx, int rx, int l, int r) {
        if (rx < l || r < lx) return 0;
        if (l <= lx && rx <= r) return t[node].val;
        int m = (lx + rx) / 2;
        return query(t[node].l, lx, m, l, r) + query(t[node].r, m + 1, rx, l, r);
    }
};
```

##### Use

- "Kth smallest value in range `[l, r]`" — build one version per prefix, query the difference between `roots[r]` and `roots[l-1]`.
- Historical / versioned range queries (query the array as it looked at any past point in time).

##### Complexity

```
Build : O(N)
Update : O(log N) new nodes per update
Query : O(log N)
Memory : O(N log N)
```

---

### 5.16 Merge Sort Tree

```cpp
vector<vector<int>> mergeTree;
void buildMergeTree(vector<int> &a, int node, int lx, int rx) {
    if (lx == rx) {
        mergeTree[node] = {a[lx]};
        return;
    }
    int m = (lx + rx) / 2;
    buildMergeTree(a, 2 * node, lx, m);
    buildMergeTree(a, 2 * node + 1, m + 1, rx);
    merge(mergeTree[2 * node].begin(), mergeTree[2 * node].end(), mergeTree[2 * node + 1].begin(),
        mergeTree[2 * node + 1].end(), back_inserter(mergeTree[node]));
}
int countLessEq(int node, int lx, int rx, int l, int r, int x) {
    if (rx < l || r < lx) return 0;
    if (l <= lx && rx <= r)
        return upper_bound(mergeTree[node].begin(), mergeTree[node].end(), x) -
               mergeTree[node].begin();
    int m = (lx + rx) / 2;
    return countLessEq(2 * node, lx, m, l, r, x) + countLessEq(2 * node + 1, m + 1, rx, l, r, x);
}
```

##### Use

- Offline queries: "count elements `<= x` in range `[l, r]`" in `O(log^2 N)` per query after `O(N log N)` build.

##### Complexity

```
Build : O(N log N)
Query : O(log^2 N)
Memory : O(N log N)
```

---

### 5.17 Sqrt Decomposition (Block Decomposition)

```cpp
struct SqrtDecomp {
    int n, blockSz;
    vector<long long> a, blockSum;
    void build(vector<long long> &arr) {
        a = arr;
        n = a.size();
        blockSz = max(1, (int)sqrt(n));
        blockSum.assign((n + blockSz - 1) / blockSz, 0);
        for (int i = 0; i < n; i++) blockSum[i / blockSz] += a[i];
    }
    void update(int i, long long val) {
        blockSum[i / blockSz] += val - a[i];
        a[i] = val;
    }
    long long query(int l, int r) {  // sum on [l, r]
        long long res = 0;
        int lb = l / blockSz, rb = r / blockSz;
        if (lb == rb) {
            for (int i = l; i <= r; i++) res += a[i];
            return res;
        }
        for (int i = l; i < (lb + 1) * blockSz; i++) res += a[i];
        for (int b = lb + 1; b < rb; b++) res += blockSum[b];
        for (int i = rb * blockSz; i <= r; i++) res += a[i];
        return res;
    }
};
```

##### Use

- Simpler alternative to Segment Tree for range update / range query when implementation speed matters more than the extra `O(sqrt N)` constant factor.
- Basis for Mo's Algorithm (already in the book) and many "block trick" offline techniques.

##### Complexity

```
Build : O(N)
Update : O(1)
Query : O(sqrt N)
```

---

### 5.18 Sqrt Decomposition — Range Add, Range Sum (Lazy Blocks)

```cpp
struct SqrtLazy {
    int n, blockSz;
    vector<long long> a, blockSum, blockLazy;
    void build(vector<long long> &arr) {
        a = arr;
        n = a.size();
        blockSz = max(1, (int)sqrt(n));
        int nb = (n + blockSz - 1) / blockSz;
        blockSum.assign(nb, 0);
        blockLazy.assign(nb, 0);
        for (int i = 0; i < n; i++) blockSum[i / blockSz] += a[i];
    }
    void updateRange(int l, int r, long long val) {  // add val to a[l..r]
        int lb = l / blockSz, rb = r / blockSz;
        if (lb == rb) {
            for (int i = l; i <= r; i++) a[i] += val, blockSum[lb] += val;
            return;
        }
        for (int i = l; i < (lb + 1) * blockSz; i++) a[i] += val, blockSum[lb] += val;
        for (int b = lb + 1; b < rb; b++) blockLazy[b] += val, blockSum[b] += val * blockSz;
        for (int i = rb * blockSz; i <= r; i++) a[i] += val, blockSum[rb] += val;
    }
    long long query(int l, int r) {
        long long res = 0;
        int lb = l / blockSz, rb = r / blockSz;
        if (lb == rb) {
            for (int i = l; i <= r; i++) res += a[i] + blockLazy[lb];
            return res;
        }
        for (int i = l; i < (lb + 1) * blockSz; i++) res += a[i] + blockLazy[lb];
        for (int b = lb + 1; b < rb; b++) res += blockSum[b];
        for (int i = rb * blockSz; i <= r; i++) res += a[i] + blockLazy[rb];
        return res;
    }
};
```

##### Use

- Range-update, range-query without recursion — the "lazy propagation" idea from the Lazy Segment Tree above, but done with flat blocks instead of a tree.
- Good fallback whenever a Lazy Segment Tree's recursion feels error-prone under time pressure.

##### Complexity

```
Update : O(sqrt N)
Query : O(sqrt N)
```

---

### 5.19 Sqrt Decomposition On Queries (Offline Query Buckets)

```
Split Q offline queries into blocks of size ~sqrt(Q) (or sqrt(N) depending on the problem).
Process each block by resetting/rebuilding only the state that block needs, reusing state
across queries inside the same block instead of recomputing from scratch per query.

Classic use: "add edge, then answer connectivity" offline problems where a full DSU
rebuild every query is too slow, but rebuilding once per sqrt(Q)-sized batch is fine.
```

##### Use

- General offline trick: whenever per-query recomputation is O(N) but the *total* work across a whole block can be amortized, chunk queries into `sqrt(Q)` batches.
- Same underlying idea as Mo's Algorithm, generalized beyond range queries.

---

### 5.20 Sqrt Decomposition — Recommended Practice

```
CSES - Range Update Queries (segment tree or sqrt decomposition both work)
Codeforces - Chef and Churu / generic "sqrt block" range update problems
Classic - Range add, range sum with sqrt decomposition instead of a Fenwick/segment tree
Classic - Offline "add edge, answer connectivity" with query-batching
```


## 6) STL, Two Pointers & Monotonic Techniques

### 6.1 Ordered Set (PBDS)

#### Include

```cpp
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
```

---

#### Template

```cpp
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
```

---

#### Create

```cpp
ordered_set<int> st;
```

---

#### Insert

```cpp
st.insert(x);
```

##### Complexity

```
O(log n)
```

---

#### Erase

```cpp
st.erase(x);
```

##### Complexity

```
O(log n)
```

---

#### Count Elements Smaller Than x

```cpp
st.order_of_key(x);
```

Example:

```cpp
st.order_of_key(10);
```

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

```cpp
*st.find_by_order(k)
```

Example:

```cpp
*st.find_by_order(0)
```

Returns:

```
smallest element
```

---

```cpp
*st.find_by_order(1)
```

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

```cpp
st.size()
```

---

#### Exists

```cpp
st.find(x) != st.end()
```

---

### 6.2 Common Tricks

#### Count <= x

```cpp
st.order_of_key(x + 1)
```

---

#### Count > x

```cpp
st.size() - st.order_of_key(x + 1)
```

---

#### Count >= x

```cpp
st.size() - st.order_of_key(x)
```

---

### 6.3 Ordered Multiset

Duplicates Allowed

```cpp
template <typename T>
using ordered_multiset = tree<pair<T, int>, null_type, less<pair<T, int>>, rb_tree_tag,
    tree_order_statistics_node_update>;
```

---

#### Insert Duplicate

```cpp
ms.insert({x, id});
```

---

#### Erase One Occurrence

```cpp
ms.erase(ms.lower_bound({x, 0}));
```

---

### 6.4 Complexity

| Operation | Complexity |
| --- | --- |
| Insert | O(log n) |
| Erase | O(log n) |
| order_of_key | O(log n) |
| find_by_order | O(log n) |

---

### 6.5 Most Common Uses

```
K-th Smallest

Inversion Count

Order Statistics

Online Ranking

Dynamic Median

Dynamic K-th Element
```

### 6.6 STL Advanced Tricks

---

### 6.7 Set As Next Pointer

#### Idea

Store all alive positions.

```cpp
set<int> st;
```

---

#### Remove Segment

```cpp
auto it = st.lower_bound(l);
while (it != st.end() && *it <= r) { it = st.erase(it); }
```

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

### 6.8 Dynamic Mex

#### Idea

Store all missing values.

```cpp
set<int> mex;
```

---

#### Answer

```cpp
*mex.begin()
```

---

#### Update

Insert number:

```cpp
freq[x]++;
if (freq[x] == 1) mex.erase(x);
```

Remove number:

```cpp
freq[x]--;
if (freq[x] == 0) mex.insert(x);
```

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

### 6.9 Difference Map

#### Idea

Coordinates too large.

```
1e18
```

Use:

```cpp
map<int, int> diff;
```

instead of:

```cpp
vector<int>
```

---

#### Pattern

```cpp
diff[l]++;
diff[r + 1]--;
```

---

#### Sweep

```cpp
int cur = 0;
for (auto [x, val] : diff) { cur += val; }
```

---

#### Uses

```
Intervals

Coverage

Huge Coordinates

Sweep Line
```

---

### 6.10 Frequency Of Frequency

#### Idea

Store:

```cpp
freq[x]
```

and

```cpp
cnt[f]
```

where:

```
cnt[f]
=
how many numbers appear exactly f times
```

---

#### Update

```cpp
cnt[freq[x]]--;
freq[x]++;
cnt[freq[x]]++;
```

---

#### Query

Check if frequency exists:

```cpp
cnt[k] > 0
```

---

#### Uses

```
Mo Algorithm

Frequency Queries

Maximum Frequency

Equal Frequencies
```

---

### 6.11 Lazy Deletion

#### Problem

Priority Queue has no:

```cpp
erase(x)
```

---

#### Solution

```cpp
priority_queue<int> pq;
map<int, int> bad;
```

Delete:

```cpp
bad[x]++;
```

---

#### Clean Top

```cpp
while (!pq.empty() && bad[pq.top()]) {
    bad[pq.top()]--;
    pq.pop();
}
```

---

#### Uses

```
Sliding Window Maximum

Dynamic Maximum

Median Problems
```

---

### 6.12 Coordinate Compression

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

```cpp
vector<int> comp;
for (auto x : a) comp.push_back(x);
for (auto q : queries) comp.push_back(q);
```

---

```cpp
sort(all(comp));
comp.erase(unique(all(comp)), comp.end());
```

---

#### Compress

```cpp
id = lower_bound(all(comp), x) - comp.begin();
```

---

#### Recover

```cpp
comp[id]
```

---

#### Uses

```
Fenwick

Segtree

Sweep Line

Offline Queries
```

---

### 6.13 Offline Sort Trick

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

### 6.14 Small To Large

#### Idea

Always merge smaller container.

---

#### Pattern

```cpp
if (a.size() > b.size()) swap(a, b);
```

---

```cpp
for (auto x : a) b.insert(x);
```

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

### 6.15 Custom Hash

#### Problem

unordered_map

can be hacked.

---

#### Template

```cpp
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};
```

---

#### Usage

```cpp
unordered_map<int, int, custom_hash> mp;
```

---

#### Uses

```
Codeforces Hacks

Large Hash Tables

Fast Frequency Maps
```

---

### 6.16 Multiset Median Trick

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

```cpp
*left.rbegin()
```

---

#### Uses

```
Sliding Window Median

Running Median
```

---

### 6.17 Order Statistics Trick

#### Count Inside Range

```cpp
os.order_of_key(r + 1) - os.order_of_key(l)
```

---

#### K-th Element

```cpp
*os.find_by_order(k)
```

---

#### Uses

```
Dynamic Ranking

K-th Smallest

Online Queries
```

---

### 6.18 Multiset Min-Max Window

#### Idea

Maintain window values.

---

#### Maximum

```cpp
*ms.rbegin()
```

---

#### Minimum

```cpp
*ms.begin()
```

---

#### Window Difference

```cpp
*ms.rbegin() - *ms.begin()
```

---

#### Uses

```
Longest Window

Max-Min <= K

Sliding Window Constraints
```

---

### 6.19 Set + Binary Search

#### Idea

Nearest Element

---

#### Pattern

```cpp
auto it = st.lower_bound(x);
```

Check:

```cpp
it
```

and

```cpp
prev(it)
```

---

#### Uses

```
Closest Number

Nearest Tower

Nearest Value
```

---

### 6.20 `lower_bound` / `upper_bound` With Custom Comparator

```cpp
struct Item {
    int key, id;
};
vector<Item> v;  // sorted by .key ascending
auto it = lower_bound(all(v), target, [](const Item &a, int val) { return a.key < val; });
// it -> first element with .key >= target
auto it2 = upper_bound(all(v), target, [](int val, const Item &a) { return val < a.key; });
// it2 -> first element with .key > target
```

##### Note

- The comparator's argument order matters: for `lower_bound` compare `(element, value)`; for `upper_bound` compare `(value, element)`.
- Works the same way on `vector`/`array`, unlike `set::lower_bound` which needs the container's own comparator instead.

---

### 6.21 Top 5 Must-Know STL Tricks

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

### 6.22 Two Pointers Advanced Patterns

---

### 6.23 Recognition Checklist

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

### 6.24 Longest Valid Segment

#### Pattern

```cpp
int l = 0;
for (int r = 0; r < n; r++) {
    add(a[r]);
    while (!valid) {
        remove(a[l]);
        l++;
    }
    ans = max(ans, r - l + 1);
}
```

---

#### Uses

```
Longest Distinct Subarray

Longest Sum <= K

Longest Window
```

---

### 6.25 Shortest Valid Segment

#### Pattern

```cpp
int l = 0;
for (int r = 0; r < n; r++) {
    add(a[r]);
    while (valid) {
        ans = min(ans, r - l + 1);
        remove(a[l]);
        l++;
    }
}
```

---

#### Uses

```
Minimum Window

Shortest Sum >= K

Cover All Characters
```

---

### 6.26 Count Subarrays Trick

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

```cpp
ans += r - l + 1;
```

---

#### Uses

```
Count Subarrays

At Most K Distinct

At Most K Odd

At Most K Zeros
```

---

### 6.27 Exactly K Trick

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

### 6.28 Distinct Elements Window

#### State

```cpp
map<int, int> freq;
int distinct;
```

---

#### Add

```cpp
if (++freq[x] == 1) distinct++;
```

---

#### Remove

```cpp
if (--freq[x] == 0) distinct--;
```

---

#### Uses

```
K Distinct

Unique Window

Longest Distinct
```

---

### 6.29 Positive Sum Window

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

### 6.30 Binary Array Trick

#### Maintain

```cpp
cnt0 cnt1
```

---

#### Common Problems

```
Flip K Zeros

Longest Ones

At Most K Zeros

Maximum Consecutive Ones
```

---

### 6.31 Circular Array Trick

#### Pattern

```cpp
vector<int> b = a;
for (auto x : a) b.push_back(x);
```

---

Then run:

```
Two Pointers
```

on:

```cpp
b
```

---

#### Uses

```
Circular Window

Circular Subarray

Ring Problems
```

---

### 6.32 Two Pointers On Sorted Array

#### Pattern

```cpp
int l = 0;
int r = n - 1;
```

---

#### Uses

```
Two Sum

Closest Pair

Difference Constraints

Pair Counting
```

---

### 6.33 Pair Sum = X

```cpp
while (l < r) {
    if (a[l] + a[r] == x) {
        ...
    } else if (a[l] + a[r] < x) {
        l++;
    } else {
        r--;
    }
}
```

---

### 6.34 Pair Difference >= K

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

### 6.35 Merge Two Sorted Arrays

#### Pattern

```cpp
i = 0;
j = 0;
```

Move smaller pointer.

---

#### Complexity

```
O(n+m)
```

---

### 6.36 Common Mistakes

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

### 6.37 Top 5 Patterns

```
Longest Valid Segment

Shortest Valid Segment

Count Subarrays

Exactly K Trick

Two Pointers On Sorted Array
```

These alone solve a huge percentage of Two Pointer problems.

### 6.38 Sliding Window Advanced Patterns

---

### 6.39 Recognition Checklist

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

### 6.40 Fixed Length Window

#### Pattern

```cpp
int sum = 0;
for (int i = 0; i < k; i++) sum += a[i];
for (int r = k; r < n; r++) {
    sum += a[r];
    sum -= a[r - k];
}
```

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

### 6.41 Variable Length Window

#### Pattern

```cpp
int l = 0;
for (int r = 0; r < n; r++) {
    add(a[r]);
    while (!valid) {
        remove(a[l]);
        l++;
    }
}
```

---

#### Uses

```
Longest Window

Shortest Window

Distinct Constraints
```

---

### 6.42 Minimum Cover Window

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

### 6.43 Frequency Window

#### State

```cpp
map<int, int> freq;
```

or

```cpp
vector<int> freq;
```

---

#### Add

```cpp
freq[x]++;
```

---

#### Remove

```cpp
freq[x]--;
```

---

#### Uses

```
Distinct

Most Frequent

Frequency Constraints
```

---

### 6.44 Distinct Count Window

#### State

```cpp
int distinct;
```

---

#### Add

```cpp
if (++freq[x] == 1) distinct++;
```

---

#### Remove

```cpp
if (--freq[x] == 0) distinct--;
```

---

#### Uses

```
At Most K Distinct

Exactly K Distinct

Longest Distinct
```

---

### 6.45 At Most K Trick

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

```cpp
ans += r - l + 1;
```

---

#### Why

All windows ending at:

```
r
```

are valid.

---

### 6.46 Exactly K Trick

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

### 6.47 Window Maximum

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

### 6.48 Window Minimum

Same idea.

Use:

```cpp
deque<int>
```

---

#### Uses

```
Min Window

Max Window

DP Optimization
```

---

### 6.49 Sliding Median

#### Idea

Maintain:

```
Left Half

Right Half
```

using:

```cpp
multiset
```

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

### 6.50 Sliding Mex

#### Idea

Maintain:

```cpp
freq[x]
```

and:

```cpp
set<int> missing;
```

---

Answer:

```cpp
*missing.begin()
```

---

#### Complexity

```
O(log n)
```

---

### 6.51 Binary Array Window

#### State

```cpp
cnt0 cnt1
```

---

#### Common Problems

```
Flip K Zeros

Longest Ones

At Most K Zeros

Maximum Consecutive Ones
```

---

### 6.52 Circular Window

#### Trick

Duplicate array.

```cpp
vector<int> b = a;
for (auto x : a) b.push_back(x);
```

---

Run window on:

```cpp
b
```

---

#### Uses

```
Circular Array

Ring Problems
```

---

### 6.53 Monotonic Condition

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

### 6.54 Common Hidden Observation

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

```cpp
while (...) 
```

inside loop.

---

### 6.55 Most Important Patterns

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

### 6.56 Contest Checklist

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

### 6.57 Monotonic Stack

---

### 6.58 Recognition Checklist

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

### 6.59 Next Greater Element

#### Problem

For every index:

```
First Greater To The Right
```

---

#### Pattern

```cpp
vector<int> ans(n, -1);
stack<int> st;
for (int i = n - 1; i >= 0; i--) {
    while (!st.empty() && a[st.top()] <= a[i]) st.pop();
    if (!st.empty()) ans[i] = st.top();
    st.push(i);
}
```

---

#### Complexity

```
O(n)
```

---

### 6.60 Previous Greater Element

#### Pattern

```cpp
for (int i = 0; i < n; i++) {
    while (!st.empty() && a[st.top()] <= a[i]) st.pop();
    if (!st.empty()) ans[i] = st.top();
    st.push(i);
}
```

---

### 6.61 Next Smaller Element

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

### 6.62 Previous Smaller Element

Same idea.

---

### 6.63 Strict vs Non Strict

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

### 6.64 Largest Rectangle In Histogram

#### Idea

Find:

```
Previous Smaller

Next Smaller
```

---

Width

```cpp
r[i] - l[i] - 1
```

---

Area

```cpp
a[i] * (r[i] - l[i] - 1)
```

---

#### Complexity

```
O(n)
```

---

### 6.65 Contribution Technique

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

```cpp
a[i] * left *right
```

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

### 6.66 Sum Of Subarray Minimums

#### Formula

```cpp
ans += a[i] * left[i] * right[i];
```

---

#### Complexity

```
O(n)
```

---

### 6.67 Sum Of Subarray Maximums

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

### 6.68 Max-Min Of All Subarrays

#### Formula

```
Contribution As Maximum

-

Contribution As Minimum
```

---

Very common trick.

---

### 6.69 Monotonic Increasing Stack

Stack contains:

```
Increasing Values
```

---

Pop while:

```cpp
st.top() >= current
```

---

Used for:

```
Minimums

Smaller Elements
```

---

### 6.70 Monotonic Decreasing Stack

Stack contains:

```
Decreasing Values
```

---

Pop while:

```cpp
st.top() <= current
```

---

Used for:

```
Maximums

Greater Elements
```

---

### 6.71 Remove K Digits

Classic problem.

---

Pattern

```cpp
while (k && !st.empty() && st.back() > x) {
    st.pop_back();
    k--;
}
```

---

Uses

```
Greedy + Stack
```

---

### 6.72 Valid Parentheses

#### Pattern

```cpp
stack<char> st;
```

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

### 6.73 Next Greater Circular

#### Trick

Loop:

```cpp
for (int i = 2 * n - 1; i >= 0; i--) 
```

Use:

```cpp
a[i % n]
```

---

#### Complexity

```
O(n)
```

---

### 6.74 Common Observation

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

### 6.75 Most Important Patterns

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

### 6.76 Contest Checklist

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

### 6.77 Monotonic Queue (Deque Tricks)

---

### 6.78 Recognition Checklist

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

### 6.79 Why Not Multiset?

Window Max using:

```cpp
multiset
```

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

### 6.80 Sliding Window Maximum

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

```cpp
deque<int> dq;
for (int i = 0; i < n; i++) {
    while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
    dq.push_back(i);
    while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
    if (i >= k - 1) ans.push_back(a[dq.front()]);
}
```

---

#### Complexity

```
O(n)
```

---

### 6.81 Sliding Window Minimum

#### Pattern

Replace:

```cpp
<=
```

with:

```cpp
>=
```

---

Answer:

```cpp
a[dq.front()]
```

---

#### Complexity

```
O(n)
```

---

### 6.82 Understanding The Queue

Queue stores:

```
indices
```

not values.

---

Values are:

```cpp
a[dq.front()]
```

---

### 6.83 Tie-Breaking On Equal Values

```
Sliding Window Maximum:
  pop back while a[dq.back()] <= a[i]   (use <=, not <)
  keeps only the rightmost of equal values -> shorter, still-correct window

Sliding Window Minimum:
  pop back while a[dq.back()] >= a[i]   (use >=, not >)
```

##### Note

- Same strict-vs-non-strict choice as the Monotonic Stack section, applied to the deque: using `<=`/`>=` instead of `<`/`>` discards redundant equal-value entries and keeps the deque smaller without changing the answer for max/min queries.

---

### 6.84 Why O(n)?

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

### 6.85 Fixed Window Max

#### Example

```
Maximum of every subarray
length k
```

---

Classic application.

---

### 6.86 Fixed Window Min

Same idea.

---

### 6.87 Min-Max Window

Maintain:

```
One Max Queue

One Min Queue
```

---

Window Difference:

```cpp
mx - mn
```

---

#### Uses

```
Max - Min <= K

Longest Valid Window
```

---

### 6.88 Longest Window With

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

### 6.89 DP Optimization

#### Form

```cpp
dp[i] = max(dp[j])
```

inside window.

---

Example

```cpp
dp[i] = max(dp[j]) + cost
```

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

### 6.90 Shortest Subarray >= K

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

### 6.91 Queue Types

#### Maximum Queue

Pop:

```cpp
while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
```

---

Answer

```cpp
a[dq.front()]
```

---

### 6.92 Minimum Queue

Pop:

```cpp
while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
```

---

Answer

```cpp
a[dq.front()]
```

---

### 6.93 Circular Array Trick

Duplicate:

```cpp
b = a;
for (auto x : a) b.push_back(x);
```

---

Run deque normally.

---

Uses

```
Circular Window Maximum

Circular Window Minimum
```

---

### 6.94 Common Mistakes

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

```cpp
dq.front()
```

when outside window.

---

Otherwise:

```
Wrong Answer
```

---

### 6.95 Comparison

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

### 6.96 Most Important Patterns

```
Sliding Window Maximum

Sliding Window Minimum

Max-Min Window

DP Optimization

Shortest Subarray >= K
```

---

### 6.97 Contest Checklist

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

### 6.98 Top 3 Uses In Contests

```
Sliding Window Maximum

Sliding Window Minimum

DP Optimization
```

These appear much more often than the rest.

### 6.99 Number Theory Handbook (ACPC)

---

### 6.100 Core Functions

#### GCD

##### Function

```cpp
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
```

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

```cpp
gcd(a, b) = gcd(b, a % b)
```

```cpp
gcd(a, b) = gcd(a - b, b)
```

```cpp
gcd(a, b, c) = gcd(gcd(a, b), c)
```

```cpp
gcd(n, n + 1) = 1
```

---

#### LCM

##### Function

```cpp
int lcm(int a, int b) { return a / gcd(a, b) * b; }
```

##### Complexity

```
O(log(min(a,b)))
```

##### Facts

```cpp
gcd(a, b) * lcm(a, b) = a * b
```

##### Warning

Bad

```cpp
a *b / gcd(a, b)
```

Good

```cpp
a / gcd(a, b) * b
```

---

#### Binary Power

##### Function

```cpp
int power(int a, int b) {
    int res = 1;
    while (b) {
        if (b & 1) res *= a;
        a *= a;
        b >>= 1;
    }
    return res;
}
```

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

```cpp
int power(int a, int b, int mod) {
    int res = 1;
    while (b) {
        if (b & 1) res = 1LL * res * a % mod;
        a = 1LL * a * a % mod;
        b >>= 1;
    }
    return res;
}
```

##### Complexity

```
O(log b)
```

---

### 6.101 Matrix Exponentiation

```cpp
typedef vector<vector<long long>> Matrix;
Matrix multiply(const Matrix &a, const Matrix &b, long long mod) {
    int n = a.size(), m = b[0].size(), k = b.size();
    Matrix c(n, vector<long long>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < k; j++)
            if (a[i][j])
                for (int l = 0; l < m; l++) c[i][l] = (c[i][l] + a[i][j] * b[j][l]) % mod;
    return c;
}
Matrix matPow(Matrix a, long long p, long long mod) {
    int n = a.size();
    Matrix res(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) res[i][i] = 1;
    while (p) {
        if (p & 1) res = multiply(res, a, mod);
        a = multiply(a, a, mod);
        p >>= 1;
    }
    return res;
}
```

##### Use

- Same repeated-squaring idea as `power()` above, applied to matrices instead of numbers.
- Linear recurrences: `f(n) = c1*f(n-1) + c2*f(n-2) + ...` computed in `O(k^3 log n)` via the recurrence's transition matrix (`k` = recurrence order).
- Classic example: generalized Fibonacci `[[1,1],[1,0]]^n`.

##### Complexity

```
O(k^3 log n) for a k x k matrix raised to the n-th power
```

---

### 6.102 Extended Euclid

#### Function

```cpp
int exgcd(int a, int b, int &x, int &y) {
    if (!b) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int g = exgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return g;
}
```

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

### 7.1 Modular Arithmetic

#### Normalize Mod

```cpp
x %= mod;
if (x < 0) x += mod;
```

---

#### Addition

```cpp
(a + b) % mod
```

---

#### Subtraction

```cpp
((a - b) % mod + mod) % mod
```

---

#### Multiplication

```cpp
1LL * a *b % mod
```

---

#### Division

```cpp
a *inv(b) % mod
```

Never:

```cpp
a / b % mod
```

---

### 7.2 Modular Inverse

#### Fermat

##### Condition

```
mod must be prime
```

##### Function

```cpp
int inv(int x) { return power(x, mod - 2, mod); }
```

##### Complexity

```
O(log mod)
```

---

#### Recursive Inverse

```cpp
int inv(int x) { return x == 1 ? 1 : mod - 1LL * (mod / x) * inv(mod % x) % mod; }
```

##### Complexity

```
O(log mod)
```

---

#### Extended Euclid Inverse

##### Condition

```cpp
gcd(a, m) == 1
```

##### Function

```cpp
int inv(int a) {
    int x, y;
    exgcd(a, mod, x, y);
    return (x % mod + mod) % mod;
}
```

##### Works For

```
Non-prime mod
```

---

#### Generate All Inverses

```cpp
inv[1] = 1;
for (int i = 2; i <= n; i++) inv[i] = mod - (mod / i) * inv[mod % i] % mod;
```

##### Complexity

```
O(n)
```

---

#### Facts

##### Inverse Exists iff

```cpp
gcd(a, m) == 1
```

##### Product

```cpp
(a *b) ^ -1 = a ^ -1 * b ^ -1
```

---

### 7.3 Factorials

#### Build Factorial

```cpp
fac[0] = 1;
for (int i = 1; i <= n; i++) fac[i] = 1LL * fac[i - 1] * i % mod;
```

##### Complexity

```
O(n)
```

---

#### Inverse Factorials

```cpp
invfac[n] = power(fac[n], mod - 2);
for (int i = n; i >= 1; i--) invfac[i - 1] = 1LL * invfac[i] * i % mod;
```

##### Complexity

```
O(n)
```

---

#### nCr

```cpp
int C(int n, int r) {
    if (r < 0 || r > n) return 0;
    return 1LL * fac[n] * invfac[r] % mod * invfac[n - r] % mod;
}
```

##### Complexity

```
O(1)
```

---

### 7.4 Lucas' Theorem (nCr mod small prime p)

```cpp
long long Cmodp(long long n, long long r, long long p) {  // n, r can be huge; p is small prime
    if (r < 0 || r > n) return 0;
    if (r == 0) return 1;
    return C(n % p, r % p) * Cmodp(n / p, r / p, p) % p;  // C(a,b) here is nCr mod p for a,b < p
}
```

##### Use

- `nCr mod p` when `n, r` are up to `10^18` but `p` is a small prime (fits precomputed factorials up to `p`).
- Reduces the problem to standard `nCr mod p` on the base-`p` digits of `n` and `r`.

##### Complexity

```
O(log_p(n))
```

---

### 7.5 Catalan Numbers

```cpp
long long catalan(int n) {  // C_n = C(2n, n) / (n + 1)
    return C(2 * n, n) * power(n + 1, mod - 2, mod) % mod;
}
```

##### Use

```
Balanced parentheses of length 2n
Binary trees with n nodes
Triangulations of a convex (n+2)-gon
Paths on a grid that don't cross the diagonal
```

##### Formula

```
C_0 = 1
C_n = Σ_{i=0}^{n-1} C_i * C_(n-1-i)
C_n = C(2n, n) - C(2n, n+1)
```

---

### 7.6 Stars And Bars

```
Number of ways to write n as an ordered sum of k non-negative integers:
    C(n + k - 1, k - 1)

Number of ways with each part >= 1 (positive integers):
    C(n - 1, k - 1)
```

##### Use

- Distributing `n` identical items into `k` distinct bins.

---

### 7.7 Derangements

```cpp
long long derangement(int n) {
    vector<long long> d(n + 1);
    d[0] = 1;
    if (n >= 1) d[1] = 0;
    for (int i = 2; i <= n; i++) d[i] = (long long)(i - 1) * ((d[i - 1] + d[i - 2]) % mod) % mod;
    return d[n];
}
```

##### Use

- Permutations of `n` elements where no element stays in its original position.

##### Formula

```
D(n) = (n - 1) * (D(n-1) + D(n-2))
D(n) = n! * Σ_{i=0}^{n} (-1)^i / i!
```

---

### 7.8 Legendre Formula

#### Power Of Prime Inside n!

```cpp
int cnt(int n, int p) {
    int res = 0;
    while (n) {
        n /= p;
        res += n;
    }
    return res;
}
```

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

```cpp
cnt(n, 5)
```

##### Why?

```
2s are always more than 5s
```

---

#### Prime Exponent In nCr

```cpp
cnt(n, p) - cnt(r, p) - cnt(n - r, p)
```

---

#### Check m | n!

Factorize:

```cpp
m = p1 ^ a1 * p2 ^ a2...
```

Check

```cpp
cnt(n, pi) >= ai
```

for every prime.

---

### 7.9 Diophantine Equations

#### Equation

```
ax+by=c
```

---

#### Solution Exists iff

```cpp
c % gcd(a, b) == 0
```

---

#### One Solution

From

```cpp
ax + by = g
```

Multiply by

```cpp
c / g
```

---

#### General Solution

Let

```cpp
g = gcd(a, b)
```

Then

```cpp
x = x0 + k * (b / g) y = y0 - k * (a / g)
```

---

#### Positive Solutions

Move

```cpp
k
```

until

```cpp
x > 0 y > 0
```

---

### 7.10 Chinese Remainder Theorem (CRT)

```cpp
// x = a1 (mod m1), x = a2 (mod m2)  ->  merged into x = a (mod lcm(m1, m2))
pair<long long, long long> crt(long long a1, long long m1, long long a2, long long m2) {
    long long x, y;
    long long g = exgcd(m1, m2, x, y);
    if ((a2 - a1) % g != 0) return {-1, -1};  // no solution
    long long lcm = m1 / g * m2;
    long long mult = (a2 - a1) / g % (m2 / g);
    long long res = (a1 + m1 * ((mult * x) % (m2 / g) + m2 / g) % (m2 / g)) % lcm;
    if (res < 0) res += lcm;
    return {res, lcm};  // x = res (mod lcm)
}
```

##### Use

- Merge two congruences `x ≡ a1 (mod m1)` and `x ≡ a2 (mod m2)` into one `x ≡ a (mod lcm(m1,m2))`.
- To merge more than two congruences, fold them one at a time with the same function.
- Reuses the `exgcd` already defined above (Extended Euclid).

##### Complexity

```
O(log(min(m1, m2))) per merge
```

---

### 7.11 Euler Phi

#### Function

```cpp
int phi(int n) {
    int res = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) n /= i;
            res -= res / i;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}
```

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

```cpp
gcd(x, n) == 1
```

---

#### Facts

##### Prime

```cpp
phi(p) = p - 1
```

##### Prime Power

```cpp
phi(p ^ k) = p ^ k - p ^ (k - 1)
```

##### Multiplicative

If

```cpp
gcd(a, b) == 1
```

Then

```cpp
phi(ab) = phi(a) * phi(b)
```

##### Divisor Identity

```cpp
Σ phi(d) = n
```

over all divisors d of n.

---

#### Euler Theorem

If

```cpp
gcd(a, m) == 1
```

Then

```cpp
a ^ phi(m) = 1 mod m
```

---

### 7.12 Euler Totient Sieve (φ For All 1..N)

```cpp
vector<int> phiSieve(int n) {
    vector<int> phi(n + 1);
    iota(phi.begin(), phi.end(), 0);
    for (int i = 2; i <= n; i++)
        if (phi[i] == i)  // i is prime
            for (int j = i; j <= n; j += i) phi[j] -= phi[j] / i;
    return phi;
}
```

##### Use

- Computes `phi(i)` for every `1 <= i <= n` at once, instead of calling the O(sqrt(n)) `phi()` function n times.

##### Complexity

```
O(N log log N)
```

---

### 7.13 Prime Testing

#### Trial Division

```cpp
bool prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}
```

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

### 7.14 Linear Sieve

#### Function

```cpp
vector<int> lp(n + 1);
vector<int> primes;
for (int i = 2; i <= n; i++) {
    if (!lp[i]) {
        lp[i] = i;
        primes.push_back(i);
    }
    for (auto p : primes) {
        if (p > lp[i] || i * p > n) break;
        lp[i * p] = p;
    }
}
```

##### Complexity

```
O(n)
```

##### Gives

```cpp
lp[x]
```

smallest prime factor.

---

### 7.15 Möbius Function + Sieve

```cpp
vector<int> mobiusSieve(int n) {
    vector<int> mu(n + 1, 0), lp(n + 1, 0), primes;
    mu[1] = 1;
    for (int i = 2; i <= n; i++) {
        if (!lp[i]) {
            lp[i] = i;
            primes.push_back(i);
            mu[i] = -1;
        }
        for (int p : primes) {
            if (p > lp[i] || (long long)i * p > n) break;
            lp[i * p] = p;
            mu[i * p] = (p == lp[i]) ? 0 : -mu[i];
        }
    }
    return mu;
}
```

##### Use

- `mu[n] = 0` if `n` has a squared prime factor, else `(-1)^(number of distinct prime factors)`.
- Core building block for inclusion-exclusion over divisors: `Σ_{d|n} mu(d) = [n == 1]`.
- Common in "count coprime pairs" / "count squarefree numbers" style problems.

##### Complexity

```
O(N) build (piggybacks on the Linear Sieve above)
```

---

### 7.16 Prime Factorization

#### Using SPF

```cpp
vector<pair<int, int>> factor(int x) {
    vector<pair<int, int>> res;
    while (x > 1) {
        int p = lp[x];
        int cnt = 0;
        while (x % p == 0) {
            x /= p;
            cnt++;
        }
        res.push_back({p, cnt});
    }
    return res;
}
```

##### Complexity

```
O(log n)
```

---

### 7.17 Divisors

#### Number Of Divisors

If

```
n=p1^a1*p2^a2...
```

Then

```cpp
Π(ai + 1)
```

---

#### Sum Of Divisors

```cpp
Π((p ^ (a + 1) - 1) / (p - 1))
```

---

#### Product Of Divisors

If

```cpp
d = d(n)
```

Then

```cpp
n ^ (d / 2)
```

---

### 7.18 Harmonic Lemma

#### Fact

Distinct values of

```cpp
n / i
```

are only

```
O(sqrt(n))
```

---

#### Loop

```cpp
for (int l = 1, r; l <= n; l = r + 1) {
    int k = n / l;
    r = n / k;
}
```

##### Complexity

```
O(sqrt(n))
```

---

### 7.19 Important Facts

#### Coprime

```cpp
gcd(a, b) == 1
```

---

#### Consecutive Numbers

```cpp
gcd(n, n + 1) = 1
```

---

#### Count Multiples In [1,n]

```cpp
n / x
```

---

#### Count Multiples In [l,r]

```cpp
r / x - (l - 1) / x
```

---

#### Distinct Prime Factors

Maximum for

```cpp
n <= 1e18
```

is

```
15
```

---

#### Maximum Number Of Divisors

For

```cpp
n <= 1e18
```

maximum is approximately

```
103680
```

---

#### Factorization Limits

```cpp
sqrt(1e12) = 1e6
```

usually acceptable.

```cpp
sqrt(1e18) = 1e9
```

not acceptable.

Use

```
Miller Rabin
Pollard Rho
```

---

### 7.20 Must Know For ACPC

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

### 7.21 Dynamic Programming - ACPC Reference

---


## 8) Dynamic Programming

### 8.1 DP Mindset

Every DP problem has:

```
State      -> What defines the subproblem?
Transition -> How to move to next states?
Base Case  -> Smallest solvable state?
Answer     -> Which state contains final answer?
```

General Memoization Template:

```cpp
int solve(state) {
    if (base_case) return answer;
    int &ret = dp[state];
    if (ret != -1) return ret;
    ret = initial_value;
    for (all_possible_choices) { ret = combine(ret, solve(next_state)); }
    return ret;
}
```

---

### 8.2 Complexity Formula

Always calculate:

```
Time = States × Transitions
```

Example:

```cpp
dp[i][sum]
```

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

### 8.3 1D DP

---

### 8.4 Fibonacci

State:

```cpp
dp[n]
```

Transition:

```cpp
f(n) = f(n - 1) + f(n - 2)
```

```cpp
int solve(int n) {
    if (n <= 1) return n;
    int &ret = dp[n];
    if (ret != -1) return ret;
    return ret = solve(n - 1) + solve(n - 2);
}
```

Complexity:

```
O(N)
```

---

### 8.5 Tricks

##### Rolling Memory

Instead of:

```cpp
dp[n]
```

Use:

```cpp
a, b, c
```

Memory:

```
O(1)
```

---

### 8.6 Stair DP

State:

```cpp
dp[i]
```

Transition:

```cpp
dp[i] = dp[i - 1] + dp[i - 2]
```

Used in:

```
Ways
Counting
Paths
```

---

### 8.7 Prefix DP

State:

```cpp
dp[i]
```

Meaning:

```
Answer for first i elements
```

Common form:

```cpp
dp[i] = best(dp[j])
```

where

```cpp
j < i
```

Examples:

```
LIS
Partition DP
Word Break
```

---

### 8.8 Kadane's Algorithm (Maximum Subarray Sum)

```cpp
long long maxSubarray(vector<long long> &a) {
    long long best = a[0], cur = a[0];
    for (int i = 1; i < (int)a.size(); i++) {
        cur = max(a[i], cur + a[i]);
        best = max(best, cur);
    }
    return best;
}
```

##### State

```cpp
dp[i] = max subarray sum ending exactly at i dp[i] = max(a[i], dp[i - 1] + a[i])
```

##### Use

```
Maximum sum contiguous subarray
Maximum sum circular subarray (total - min subarray)
2D version: fix top/bottom rows, run 1D Kadane on column sums
```

##### Complexity

```
O(N)
```

---

### 8.9 0/1 Knapsack

---

### 8.10 State

```cpp
(i, rem)
```

Meaning:

```
Current item
Remaining capacity
```

---

### 8.11 Recursive

```cpp
int solve(int i, int rem) {
    if (i == n) return 0;
    int &ret = dp[i][rem];
    if (ret != -1) return ret;
    ret = solve(i + 1, rem);
    if (rem >= w[i]) ret = max(ret, val[i] + solve(i + 1, rem - w[i]));
    return ret;
}
```

---

### 8.12 Iterative

```cpp
for (int i = 0; i < n; i++) {
    for (int w = W; w >= cost[i]; w--) { dp[w] = max(dp[w], dp[w - cost[i]] + val[i]); }
}
```

---

### 8.13 Important Tricks

##### Trick 1

Backward loop:

```cpp
for (w = W; w >= cost; w--) 
```

means

```
Take Once
```

---

##### Trick 2

Forward loop:

```cpp
for (w = cost; w <= W; w++) 
```

means

```
Take Infinite Times
```

---

##### Trick 3

Recover Solution

Store:

```cpp
par[i][w]
```

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

```cpp
dp[value] = minimum weight
```

---

Complexity:

```
O(NW)
```

---

##### Trick 5: Bitset-Accelerated Feasibility

```cpp
bitset<100001> bs;
bs[0] = 1;
for (int w : weights) bs |= (bs << w);
// bs[s] == 1  <=>  sum s is achievable using a subset of weights
```

##### Use

```
"Is sum S reachable?" style knapsack, no need for the actual value dp[w].
Turns O(N * W) into O(N * W / 64) via word-level parallelism.
```

---

### 8.14 Subset Sum

State:

```cpp
(i, sum)
```

---

### 8.15 Recursive

```cpp
bool solve(int i, int sum) {
    if (sum == target) return true;
    if (i == n) return false;
    int &ret = dp[i][sum];
    if (ret != -1) return ret;
    return ret = solve(i + 1, sum) || solve(i + 1, sum + a[i]);
}
```

---

### 8.16 Iterative

```cpp
dp[0] = 1;
for (auto x : a) {
    for (int s = S; s >= x; s--) { dp[s] |= dp[s - x]; }
}
```

---

### 8.17 Tricks

##### Count Solutions

Replace:

```cpp
bool
```

with

```cpp
long long
```

---

##### Find One Solution

Store:

```cpp
take[i][sum]
```

---

##### Bitset Optimization

```cpp
bitset<MAX> bs;
bs[0] = 1;
for (auto x : a) bs |= (bs << x);
```

Complexity:

```
O(N*S/64)
```

Huge optimization.

---

### 8.18 Coin Change

---

### 8.19 Count Ways

```cpp
ll solve(int i, int rem) {
    if (rem == 0) return 1;
    if (i == n) return 0;
    ll &ret = dp[i][rem];
    if (ret != -1) return ret;
    ret = solve(i + 1, rem);
    if (rem >= coin[i]) ret += solve(i, rem - coin[i]);
    return ret;
}
```

---

### 8.20 Tricks

##### Combination

```cpp
solve(i, ...)
```

---

##### Permutation

```cpp
solve(0, ...)
```

after choosing.

Very common trap.

---

### 8.21 LCS

State:

```cpp
(i, j)
```

---

### 8.22 Recursive

```cpp
int solve(int i, int j) {
    if (i == n || j == m) return 0;
    int &ret = dp[i][j];
    if (ret != -1) return ret;
    if (a[i] == b[j]) return ret = 1 + solve(i + 1, j + 1);
    return ret = max(solve(i + 1, j), solve(i, j + 1));
}
```

---

### 8.23 Tricks

##### Recover String

Store choices.

---

##### SCS

```
Shortest Common Supersequence
```

Formula:

```cpp
n + m - LCS
```

---

##### Edit Distance Relation

```
Insert/Delete only
```

Answer:

```cpp
n + m - 2 * LCS
```

---

Complexity:

```
O(NM)
```

---

### 8.24 LIS

---

### 8.25 O(N²)

```cpp
for (int i = 0; i < n; i++) {
    dp[i] = 1;
    for (int j = 0; j < i; j++) {
        if (a[j] < a[i]) dp[i] = max(dp[i], dp[j] + 1);
    }
}
```

---

### 8.26 O(N log N)

```cpp
vector<int> lis;
for (auto x : a) {
    auto it = lower_bound(lis.begin(), lis.end(), x);
    if (it == lis.end())
        lis.push_back(x);
    else
        *it = x;
}
```

---

### 8.27 Tricks

##### Strict LIS

```cpp
lower_bound
```

---

##### Non-Decreasing LIS

```cpp
upper_bound
```

---

##### Recover LIS

Store:

```cpp
parent[]
```

---

##### Count LIS

Need another DP.

---

### 8.28 Grid DP

State:

```cpp
(i, j)
```

---

### 8.29 Recursive

```cpp
ll solve(int i, int j) {
    if (i == n - 1 && j == m - 1) return 1;
    if (i >= n || j >= m) return 0;
    ll &ret = dp[i][j];
    if (ret != -1) return ret;
    return ret = solve(i + 1, j) + solve(i, j + 1);
}
```

---

### 8.30 Tricks

##### Obstacles

```cpp
if (blocked) return 0;
```

---

##### Minimum Cost

Replace:

```cpp
+
```

with

```cpp
min(...)
```

---

##### Maximum Cost

Use:

```cpp
max(...)
```

---

##### Path Recovery

Store direction.

---

Complexity:

```
O(NM)
```

---

### 8.31 DAG DP

State:

```cpp
u
```

---

### 8.32 Longest Path

```cpp
int solve(int u) {
    int &ret = dp[u];
    if (ret != -1) return ret;
    ret = 0;
    for (auto v : adj[u]) { ret = max(ret, 1 + solve(v)); }
    return ret;
}
```

---

### 8.33 Tricks

##### Count Paths

```cpp
ret += solve(v);
```

---

##### Longest Path

```cpp
ret = max(...)
```

---

##### Shortest Path

```cpp
ret = min(...)
```

---

Complexity:

```
O(V+E)
```

---

### 8.34 Tree DP

---

### 8.35 Independent Set

State:

```cpp
(node, take)
```

---

```cpp
int solve(int u, int take, int p) {
    int &ret = dp[u][take];
    if (ret != -1) return ret;
    ret = take;
    for (auto v : adj[u]) {
        if (v == p) continue;
        if (take)
            ret += solve(v, 0, u);
        else
            ret += max(solve(v, 0, u), solve(v, 1, u));
    }
    return ret;
}
```

---

### 8.36 Tree DP Tricks

##### Subtree DP

```cpp
dp[u]
```

---

##### Rerooting

Need:

```cpp
dp_down dp_up
```

---

##### Diameter DP

Keep:

```cpp
mx1 mx2
```

largest depths.

---

##### Tree Matching

State:

```cpp
(u, take)
```

common.

---

Complexity:

```
O(N)
```

---

### 8.37 Range DP

State:

```cpp
(l, r)
```

---

### 8.38 Recursive

```cpp
int solve(int l, int r) {
    if (l == r) return 0;
    int &ret = dp[l][r];
    if (ret != -1) return ret;
    ret = INF;
    for (int k = l; k < r; k++) { ret = min(ret, solve(l, k) + solve(k + 1, r)); }
    return ret;
}
```

---

### 8.39 Recognition

Keywords:

```
Interval
Segment
Palindrome
Merge
Split
```

---

### 8.40 Tricks

##### Length Order

Always build:

```cpp
len = 1..n
```

---

##### Partition Point

Usually:

```cpp
for (k = l; k < r; k++) 
```

---

##### Palindrome DP

State:

```cpp
dp[l][r]
```

---

Complexity:

```
O(N³)
```

---

### 8.41 Knuth's Optimization

```cpp
long long dp[N][N];
int opt[N][N];
for (int len = 2; len <= n; len++)
    for (int l = 1; l + len - 1 <= n; l++) {
        int r = l + len - 1;
        dp[l][r] = LLONG_MAX;
        for (int k = opt[l][r - 1]; k <= opt[l + 1][r]; k++) {
            long long val = dp[l][k] + dp[k + 1][r] + cost(l, r);
            if (val < dp[l][r]) {
                dp[l][r] = val;
                opt[l][r] = k;
            }
        }
    }
```

##### When To Use

```
dp[l][r] = min_{l<=k<r} (dp[l][k] + dp[k+1][r] + cost(l,r))
cost(l,r) satisfies the quadrangle inequality (monotone/concave cost)
```

##### Note

- Requires proving `opt[l][r-1] <= opt[l][r] <= opt[l+1][r]` for the specific cost function before applying — same interval-DP shape as this Range DP section, sped up from `O(N^3)` to `O(N^2)`.

##### Complexity

```
O(N²)
```

---

### 8.42 Bitmask DP

Use when:

```
N ≤ 20
```

---

### 8.43 Assignment DP

```cpp
int solve(int mask) {
    if (mask == (1 << n) - 1) return 0;
    int &ret = dp[mask];
    if (ret != -1) return ret;
    ret = INF;
    int pos = __builtin_popcount(mask);
    for (int i = 0; i < n; i++) {
        if (mask & (1 << i)) continue;
        ret = min(ret, cost[pos][i] + solve(mask | (1 << i)));
    }
    return ret;
}
```

---

### 8.44 Bit Tricks

Check:

```cpp
mask & (1 << i)
```

Set:

```cpp
mask | (1 << i)
```

Remove:

```cpp
mask ^ (1 << i)
```

Count:

```cpp
__builtin_popcount(mask)
```

---

### 8.45 Submask Enumeration

```cpp
for (int sub = mask; sub; sub = (sub - 1) & mask) {}
```

---

### 8.46 Tricks

##### TSP

State:

```cpp
(mask, last)
```

---

##### Assignment

State:

```cpp
(mask)
```

---

##### Partition DP

Enumerate submasks.

---

Complexity:

```
O(N*2^N)
```

---

### 8.47 Bitmask DP — Recommended Practice

```
CSES - Elevator Rides
CSES - Counting Tilings
CSES - Hamiltonian Flights
CSES - Counting Numbers (bitmask variant)
Classic - Travelling Salesman Problem (TSP)
Classic - Assignment Problem (min cost bipartite assignment)
```

---

### 8.48 Digit DP

Use when:

```
Count numbers
between L and R
satisfying property
```

---

### 8.49 State

```cpp
(pos, tight, sum)
```

---

### 8.50 Template

```cpp
ll solve(int pos, int tight, int sum) {
    if (pos == num.size()) return condition;
    ll &ret = dp[pos][tight][sum];
    if (!tight && ret != -1) return ret;
    ll ans = 0;
    int mx = tight ? num[pos] - '0' : 9;
    for (int d = 0; d <= mx; d++) { ans += solve(pos + 1, tight && d == mx, sum + d); }
    if (!tight) ret = ans;
    return ret;
}
```

---

### 8.51 Most Important Digit DP Tricks

##### Count [L,R]

```cpp
f(R) - f(L - 1)
```

Always.

---

##### Leading Zeros

Add state:

```cpp
started
```

```cpp
dp[pos][tight][started]
```

---

##### Divisibility

Add:

```cpp
mod
```

```cpp
dp[pos][tight][mod]
```

---

##### Digit Sum

Add:

```cpp
sum
```

---

##### Used Digits

Add:

```cpp
mask
```

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

### 8.52 Digit DP — Recommended Practice

```
CSES - Counting Numbers
Codeforces - Beautiful Numbers (digit sum divisibility)
Codeforces - Number With The Given Amount Of Divisors (digit DP + factorization combo)
Classic - Count numbers in [L, R] with no two adjacent equal digits
Classic - Count numbers in [L, R] with digit sum in a given range
```

---

### 8.53 DP Optimizations

---

### 8.54 Rolling Array

Before:

```cpp
dp[n][m]
```

After:

```cpp
dp[2][m]
```

Memory:

```
O(M)
```

---

### 8.55 Divide & Conquer DP Optimization

```cpp
long long dp_prev[N], dp_cur[N];
void solve(int l, int r, int optL, int optR) {
    if (l > r) return;
    int mid = (l + r) / 2;
    pair<long long, int> best = {LLONG_MAX, -1};
    for (int k = optL; k <= min(mid, optR); k++)
        best = min(best, {dp_prev[k] + cost(k + 1, mid), k});
    dp_cur[mid] = best.first;
    int opt = best.second;
    solve(l, mid - 1, optL, opt);
    solve(mid + 1, r, opt, optR);
}
// call: solve(0, n - 1, 0, n - 1) once per DP layer, then swap dp_prev/dp_cur
```

##### When To Use

```
dp[i][j] = min_{k<j} (dp[i-1][k] + cost(k+1, j))
opt[i][j] is monotonic in j: opt[i][j] <= opt[i][j+1]
```

##### Complexity

```
O(N log N) per layer instead of O(N^2)
```

---

### 8.56 State Compression

Before:

```cpp
dp[i][j][k]
```

After:

```cpp
dp[j][k]
```

---

### 8.57 Prefix Optimization

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

### 8.58 Memory Estimate

```
1e6 int       = 4 MB
1e6 long long = 8 MB
```

---

### 8.59 DP Recognition Cheat Sheet

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

### 8.60 Most Important ACPC DP Topics

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

### 9.1 Fenwick Tree (BIT)

```cpp
struct Fenwick {
    int n;
    vector<long long> bit;
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    void add(int idx, long long val) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += val;
    }
    long long sumPrefix(int idx) const {
        long long r = 0;
        for (; idx > 0; idx -= idx & -idx) r += bit[idx];
        return r;
    }
    long long rangeSum(int l, int r) const { return sumPrefix(r) - sumPrefix(l - 1); }
};
```

#### Complexity

- `add / prefix / range`: `O(log n)`

---

### 9.2 SCC (Kosaraju)

```cpp
vector<vector<int>> g, rg;
vector<int> vis, order, comp;
void dfs1(int u) {
    vis[u] = 1;
    for (int v : g[u])
        if (!vis[v]) dfs1(v);
    order.push_back(u);
}
void dfs2(int u, int c) {
    comp[u] = c;
    for (int v : rg[u])
        if (comp[v] == -1) dfs2(v, c);
}
int kosaraju(int n) {
    vis.assign(n + 1, 0);
    order.clear();
    for (int i = 1; i <= n; i++)
        if (!vis[i]) dfs1(i);
    comp.assign(n + 1, -1);
    int scc = 0;
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        if (comp[u] == -1) dfs2(u, scc++);
    }
    return scc;
}
```

---

### 9.3 2-SAT (Implication Graph)

```cpp
struct TwoSAT {
    int n;
    vector<vector<int>> g, rg;
    vector<int> comp, order, vis, ans;
    TwoSAT(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        g.assign(2 * n, {});
        rg.assign(2 * n, {});
    }
    int id(int x, bool t) { return 2 * x + (t ? 1 : 0); }
    void addImp(int u, int v) {
        g[u].push_back(v);
        rg[v].push_back(u);
    }
    void imply(int a, bool av, int b, bool bv) { addImp(id(a, av), id(b, bv)); }
    void either(int a, bool av, int b, bool bv) {
        imply(a, !av, b, bv);
        imply(b, !bv, a, av);
    }
    void forceVar(int a, bool av) { imply(a, !av, a, av); }
    void dfs1(int u) {
        vis[u] = 1;
        for (int v : g[u])
            if (!vis[v]) dfs1(v);
        order.push_back(u);
    }
    void dfs2(int u, int c) {
        comp[u] = c;
        for (int v : rg[u])
            if (comp[v] == -1) dfs2(v, c);
    }
    bool satisfiable() {
        vis.assign(2 * n, 0);
        order.clear();
        for (int i = 0; i < 2 * n; i++)
            if (!vis[i]) dfs1(i);
        comp.assign(2 * n, -1);
        int c = 0;
        for (int i = 2 * n - 1; i >= 0; i--)
            if (comp[order[i]] == -1) dfs2(order[i], c++);
        ans.assign(n, 0);
        for (int i = 0; i < n; i++) {
            if (comp[id(i, false)] == comp[id(i, true)]) return false;
            ans[i] = comp[id(i, false)] < comp[id(i, true)];
        }
        return true;
    }
};
```

#### Note

- Build SCC on implication graph; variable `x` is true if `comp[id(x,true)] > comp[id(x,false)]`.

---

### 9.4 Dinic (Max Flow)

```cpp
struct Dinic {
    struct E {
        int to, rev;
        long long cap;
    };
    int n;
    vector<vector<E>> g;
    vector<int> lvl, it;
    Dinic(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        g.assign(n, {});
    }
    void addEdge(int u, int v, long long c) {
        E a{v, (int)g[v].size(), c}, b{u, (int)g[u].size(), 0};
        g[u].push_back(a);
        g[v].push_back(b);
    }
    bool bfs(int s, int t) {
        lvl.assign(n, -1);
        queue<int> q;
        q.push(s);
        lvl[s] = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto &e : g[u])
                if (e.cap > 0 && lvl[e.to] == -1) lvl[e.to] = lvl[u] + 1, q.push(e.to);
        }
        return lvl[t] != -1;
    }
    long long dfs(int u, int t, long long f) {
        if (!f || u == t) return f;
        for (int &i = it[u]; i < (int)g[u].size(); i++) {
            E &e = g[u][i];
            if (lvl[e.to] != lvl[u] + 1 || e.cap == 0) continue;
            long long got = dfs(e.to, t, min(f, e.cap));
            if (!got) continue;
            e.cap -= got;
            g[e.to][e.rev].cap += got;
            return got;
        }
        return 0;
    }
    long long maxflow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            it.assign(n, 0);
            while (long long pushed = dfs(s, t, (long long)4e18)) flow += pushed;
        }
        return flow;
    }
};
```

#### Note

- Use level graph BFS + blocking flow DFS.

---

### 9.5 Kuhn's Algorithm (Bipartite Matching)

```cpp
vector<vector<int>> adjL;
vector<int> matchR;
vector<bool> usedL;
bool tryKuhn(int u) {
    for (int v : adjL[u]) {
        if (matchR[v] == -1 ||
            (!usedL[matchR[v]] && (usedL[matchR[v]] = true, tryKuhn(matchR[v])))) {
            matchR[v] = u;
            return true;
        }
    }
    return false;
}
int maxMatching(int leftN, int rightN) {
    matchR.assign(rightN, -1);
    int result = 0;
    for (int u = 0; u < leftN; u++) {
        usedL.assign(leftN, false);
        if (tryKuhn(u)) result++;
    }
    return result;
}
```

##### Use

- Maximum bipartite matching without building a full flow network.
- Natural companion to Dinic: bipartite matching is max-flow on a source→left→right→sink network with unit capacities, but Kuhn's is simpler to code directly.

##### Complexity

```
O(V * E)
```

---

### 9.6 Hopcroft-Karp (Faster Bipartite Matching)

```cpp
// Same bipartite matching problem as Kuhn's, but finds multiple augmenting paths per BFS phase
// via alternating BFS (build layers) + DFS (augment along shortest augmenting paths),
// instead of one augmenting path per left vertex.
```

##### Use

- Same result as Kuhn's, but `O(E * sqrt(V))` instead of `O(V * E)` — worth it when `V` is large (`> ~2000`) and Kuhn's TLEs.

##### Complexity

```
O(E * sqrt(V))
```

---

### 9.7 Min-Cost Max-Flow

```cpp
// Extend Dinic's edge struct with a `cost` field.
// Replace the BFS level-graph step with Bellman-Ford/SPFA shortest-path-by-cost
// (since costs can be negative for residual edges), then push flow only along
// the cheapest augmenting path each phase (successive shortest paths / SPFA-Dinic hybrid).
```

##### Use

- Assignment problems / transportation problems where you need max flow at minimum total cost, not just max flow.
- Reuses the existing Dinic structure and the existing Bellman-Ford/SPFA code from the Graph Algorithms chapter.

##### Complexity

```
O(F * E)  where F is total flow (successive shortest augmenting paths)
```

---

### 9.8 Trie (Lowercase)

```cpp
struct Trie {
    struct Node {
        int nxt[26];
        bool end = false;
        Node() { memset(nxt, -1, sizeof(nxt)); }
    };
    vector<Node> t{Node()};
    void add(const string &s) {
        int u = 0;
        for (char c : s) {
            int x = c - 'a';
            if (t[u].nxt[x] == -1) {
                t[u].nxt[x] = t.size();
                t.push_back(Node());
            }
            u = t[u].nxt[x];
        }
        t[u].end = true;
    }
    bool has(const string &s) const {
        int u = 0;
        for (char c : s) {
            int x = c - 'a';
            if (t[u].nxt[x] == -1) return false;
            u = t[u].nxt[x];
        }
        return t[u].end;
    }
};
```

---

### 9.9 Aho-Corasick (Pattern Matching)

```cpp
struct Aho {
    struct Node {
        int nxt[26], link = 0, out = 0;
        Node() { memset(nxt, -1, sizeof(nxt)); }
    };
    vector<Node> t{Node()};
    void add(const string &s) {
        int u = 0;
        for (char c : s) {
            int x = c - 'a';
            if (t[u].nxt[x] == -1) {
                t[u].nxt[x] = t.size();
                t.push_back(Node());
            }
            u = t[u].nxt[x];
        }
        t[u].out++;
    }
    void build() {
        queue<int> q;
        for (int c = 0; c < 26; c++) {
            int v = t[0].nxt[c];
            if (v == -1)
                t[0].nxt[c] = 0;
            else
                q.push(v);
        }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            t[u].out += t[t[u].link].out;
            for (int c = 0; c < 26; c++) {
                int v = t[u].nxt[c];
                if (v == -1)
                    t[u].nxt[c] = t[t[u].link].nxt[c];
                else
                    t[v].link = t[t[u].link].nxt[c], q.push(v);
            }
        }
    }
    int countMatches(const string &s) {
        int u = 0, ans = 0;
        for (char c : s) {
            u = t[u].nxt[c - 'a'];
            ans += t[u].out;
        }
        return ans;
    }
};
```

---

### 9.10 Heavy-Light Decomposition (HLD)

```cpp
vector<vector<int>> g;
vector<int> parent, depth, heavy, head, pos, sz;
int timer = 0;
int dfs_sz(int u, int p) {
    parent[u] = p;
    sz[u] = 1;
    int mx = 0;
    for (int v : g[u])
        if (v != p) {
            depth[v] = depth[u] + 1;
            int s = dfs_sz(v, u);
            sz[u] += s;
            if (s > mx) mx = s, heavy[u] = v;
        }
    return sz[u];
}
void dfs_hld(int u, int h) {
    head[u] = h;
    pos[u] = ++timer;
    if (heavy[u] != -1) dfs_hld(heavy[u], h);
    for (int v : g[u])
        if (v != parent[u] && v != heavy[u]) dfs_hld(v, v);
}
vector<pair<int, int>> path_segments(int u, int v) {
    vector<pair<int, int>> segs;
    while (head[u] != head[v]) {
        if (depth[head[u]] < depth[head[v]]) swap(u, v);
        segs.push_back({pos[head[u]], pos[u]});
        u = parent[head[u]];
    }
    if (depth[u] > depth[v]) swap(u, v);
    segs.push_back({pos[u], pos[v]});
    return segs;
}
```

---

### 9.11 Mo's Algorithm

```cpp
struct Query {
    int l, r, idx;
};
int B;
bool operator<(const Query &a, const Query &b) {
    int A = a.l / B, C = b.l / B;
    if (A != C) return A < C;
    return (A & 1) ? a.r > b.r : a.r < b.r;
}
// Maintain current [L,R] with add(pos)/remove(pos), store answers by original idx.
```

---

### 9.12 Mo's Algorithm With Point Updates

```cpp
struct QueryU {
    int l, r, t, idx;  // t = number of updates applied before this query
};
int B;
bool operator<(const QueryU &a, const QueryU &b) {
    int al = a.l / B, bl = b.l / B;
    if (al != bl) return al < bl;
    int ar = a.r / B, br = b.r / B;
    if (ar != br) return ar < br;
    return a.t < b.t;
}
// Extra pointer `curT` walks through the update list forward/backward, applying or
// undoing updates whose position lies inside the current [L,R] window (and adjusting
// the answer), in addition to the usual add(pos)/remove(pos) moves on L and R.
```

##### Use

- Extends the static Mo's Algorithm above to arrays with point updates interleaved with range queries offline.
- Sort by `(l/B, r/B, t)` instead of just `(l/B, r/B)`; block size becomes `B ≈ n^(2/3)` instead of `sqrt(n)`.

##### Complexity

```
O((N + Q) * N^(2/3))
```

---

### 9.13 Mo's Algorithm With Hilbert Curve Order

```cpp
inline long long hilbertOrder(int x, int y, int pow, int rotate) {
    if (pow == 0) return 0;
    int hpow = 1 << (pow - 1);
    int seg = (x < hpow) ? ((y < hpow) ? 0 : 3) : ((y < hpow) ? 1 : 2);
    seg = (seg + rotate) & 3;
    const int rotateDelta[4] = {3, 0, 0, 1};
    int nx = x & (x ^ hpow), ny = y & (y ^ hpow);
    int nrot = (rotate + rotateDelta[seg]) & 3;
    long long subSquareSize = 1LL << (2 * pow - 2);
    long long ans = seg * subSquareSize;
    long long add = hilbertOrder(nx, ny, pow - 1, nrot);
    ans += (seg == 1 || seg == 2) ? add : (subSquareSize - add - 1);
    return ans;
}
struct QueryH {
    int l, r, idx;
    long long order;
};
// order = hilbertOrder(l, r, LOG, 0), then just sort queries by `order` ascending
bool cmpHilbert(const QueryH &a, const QueryH &b) { return a.order < b.order; }
```

##### Use

- Alternative sort key for Mo's Algorithm that walks queries along a Hilbert space-filling curve instead of block order.
- Guarantees `O((N + Q) * sqrt(N))` total pointer movement in the worst case (block-order Mo's has a known adversarial worst case that's slower in practice for certain query patterns); Hilbert order removes that weakness at the cost of a more complex comparator.
- Drop-in replacement: keep the same `add(pos)`/`remove(pos)` maintenance logic, only change how queries are sorted.

##### Complexity

```
O((N + Q) * sqrt(N)) guaranteed, same asymptotic as standard Mo's but better constant/worst-case behavior
```

---

### 9.14 Mo's Algorithm — Recommended Practice

```
CSES - Distinct Values Queries (can be solved offline with Mo's or a Fenwick sweep)
Codeforces - Powerful Array (classic Mo's Algorithm introduction)
Codeforces - Query on a Tree 8 / tree flattening + Mo's on Euler tour
Classic - Count distinct elements in range [l, r] offline
Classic - Range mode query (most frequent element) offline
```

---

### 9.15 Meet in the Middle

```cpp
long long bestSubsetSumLE(const vector<long long> &a, long long S) {
    int n = a.size(), m = n / 2;
    vector<long long> L, R;
    for (int mask = 0; mask < (1 << m); mask++) {
        long long s = 0;
        for (int i = 0; i < m; i++)
            if (mask >> i & 1) s += a[i];
        if (s <= S) L.push_back(s);
    }
    for (int mask = 0; mask < (1 << (n - m)); mask++) {
        long long s = 0;
        for (int i = 0; i < n - m; i++)
            if (mask >> i & 1) s += a[m + i];
        if (s <= S) R.push_back(s);
    }
    sort(R.begin(), R.end());
    long long ans = 0;
    for (long long x : L) {
        auto it = upper_bound(R.begin(), R.end(), S - x);
        if (it != R.begin()) ans = max(ans, x + *prev(it));
    }
    return ans;
}
```

## 10) Comprehensive Missing Tricks & Function Ideas

### 10.1 Foundations & Utilities: extra useful functions

```cpp
template <class T>
bool chmin(T &a, const T &b) {
    if (b < a) {
        a = b;
        return true;
    }
    return false;
}
template <class T>
bool chmax(T &a, const T &b) {
    if (b > a) {
        a = b;
        return true;
    }
    return false;
}
long long mod_pow(long long a, long long e, long long mod) {
    long long r = 1 % mod;
    a %= mod;
    while (e) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return r;
}
long long ceil_div(long long a, long long b) {
    if (b < 0) a = -a, b = -b;
    return a >= 0 ? (a + b - 1) / b : a / b;
}
long long floor_div(long long a, long long b) {
    if (b < 0) a = -a, b = -b;
    return a >= 0 ? a / b : -((-a + b - 1) / b);
}
```

#### Extra ideas

- Coordinate-compress pairs/tuples when a value alone is not enough.
- Prefer `long long` in weighted/DP transitions by default.
- Keep one reusable `restore_path(par, target)` helper for graph and DP reconstructions.

---

### 10.2 Graphs: missed patterns and tricks

```cpp
// Multi-test graph reset trick:
// vector<vector<int>> adj(n+1); vector<int> vis(n+1,0);
// Recreate per test instead of manual clear loops on huge static arrays.
// Edge index trick for undirected graph with parent edge:
// store edges as pairs (to, id), and skip only parent edge id in DFS.
```

```cpp
// Bridge / articulation skeleton (Tarjan low-link)
vector<vector<pair<int, int>>> g;
vector<int> tin, low, isCut;
vector<pair<int, int>> bridges;
int timerDFS = 0;
void dfsBridge(int u, int pe = -1) {
    tin[u] = low[u] = ++timerDFS;
    int children = 0;
    for (auto [v, id] : g[u])
        if (id != pe) {
            if (tin[v])
                low[u] = min(low[u], tin[v]);
            else {
                dfsBridge(v, id);
                low[u] = min(low[u], low[v]);
                children++;
                if (low[v] > tin[u]) bridges.push_back({u, v});
                if (pe != -1 && low[v] >= tin[u]) isCut[u] = 1;
            }
        }
    if (pe == -1 && children > 1) isCut[u] = 1;
}
```

#### Common graph problem recognition

- **Shortest path + 0/1 edges** → 0-1 BFS.
- **Topological order + DAG transitions** → DAG DP.
- **Connectivity under edge additions** → DSU.
- **Offline connectivity with removals** → reverse process + DSU.
- **Constraints of form `x - y <= c`** → Bellman-Ford / SPFA model.

---

### 10.3 Trees: missed ideas

```cpp
// Rerooting DP pattern:
// 1) dfs_down(u,p): compute contribution inside subtree.
// 2) dfs_up(u,p,fromParent): reroot transition to children.
// This solves sum of distances, max distance to any node, etc.
```

```cpp
// Binary lifting helper: kth node on path(u,v)
int kth_on_path(int u, int v, int k, function<int(int, int)> lca, function<int(int, int)> jump,
    const vector<int> &depth) {
    int w = lca(u, v);
    int left = depth[u] - depth[w] + 1;
    if (k <= left) return jump(u, k - 1);
    int right = depth[v] - depth[w];
    int need = left + right - k;
    return jump(v, need);
}
```

---

### 10.4 Strings: missed functions and patterns

```cpp
vector<int> z_function(const string &s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r) z[i] = min(r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) l = i, r = i + z[i] - 1;
    }
    return z;
}
```

```cpp
// Double-hash substring helper idea:
// pref[i], pw[i] for each mod; getHash(l,r) in O(1).
// Use for palindrome checks, repeated substring checks, lexicographic compare with LCP binary search.
```

#### String problem recognition

- Many pattern queries in one text → Aho-Corasick.
- Prefix/suffix border questions → prefix-function / Z-function.
- Need lexicographic cyclic operations → suffix-array / Booth-style ideas.

---

### 10.5 Data Structures (DS): missed important functions

```cpp
struct FenwickRange {
    int n;
    vector<long long> b1, b2;
    FenwickRange(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        b1.assign(n + 1, 0);
        b2.assign(n + 1, 0);
    }
    void add(vector<long long> &b, int i, long long v) {
        for (; i <= n; i += i & -i) b[i] += v;
    }
    long long sum(const vector<long long> &b, int i) const {
        long long r = 0;
        for (; i > 0; i -= i & -i) r += b[i];
        return r;
    }
    void range_add(int l, int r, long long v) {
        add(b1, l, v);
        add(b1, r + 1, -v);
        add(b2, l, v * (l - 1));
        add(b2, r + 1, -v * r);
    }
    long long pref(int i) const { return sum(b1, i) * i - sum(b2, i); }
    long long range_sum(int l, int r) const { return pref(r) - pref(l - 1); }
};
```

```cpp
// DSU rollback idea (for offline dynamic connectivity):
// keep stack of parent/size changes, no path compression, union by size only, rollback to checkpoint.
```

#### DS problem-type checklist

- Point update + prefix/range sum → Fenwick.
- Range update + range query → lazy segtree or two-BIT trick.
- Static idempotent range query (min/gcd/max) → sparse table.
- Order statistics with updates → PBDS / segtree over compressed values.

---

### 10.6 Number Theory (NS): missed functions and ideas

```cpp
long long ext_gcd(long long a, long long b, long long &x, long long &y) {
    if (!b) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1, g = ext_gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}
// Solve a*x + b*y = c
bool diophantine(long long a, long long b, long long c, long long &x, long long &y) {
    long long g = ext_gcd(abs(a), abs(b), x, y);
    if (c % g) return false;
    x *= c / g;
    y *= c / g;
    if (a < 0) x = -x;
    if (b < 0) y = -y;
    return true;
}
```

```cpp
// CRT merge (x ≡ a1 mod m1, x ≡ a2 mod m2) can be built using ext_gcd.
// Keep answer modulo lcm(m1, m2) and check consistency by gcd divisibility.
```

#### Number theory recognition

- Congruence system with multiple mods → CRT.
- Huge exponent with mod prime/composite → Euler/Fermat + fast power.
- Frequent factorization queries up to N → SPF sieve.

---

### 10.7 Dynamic Programming (DP): missed important patterns

```cpp
// Reconstruction helper (1D choice DP)
vector<int> restore_choice(int target, const vector<int> &from) {
    vector<int> pick;
    while (target != -1 && from[target] != -1) {
        pick.push_back(target - from[target]);
        target = from[target];
    }
    reverse(pick.begin(), pick.end());
    return pick;
}
```

```cpp
// Bitset knapsack idea:
// bitset<MAXS+1> bs; bs[0]=1;
// for(int w:weights) bs |= (bs<<w);
// reachable sum queries in O(N*MAXS/word_size).
```

```cpp
// Divide & Conquer DP optimization condition:
// dp[i][j] = min_{k<j}(dp[i-1][k] + cost(k+1, j))
// with monotone opt: opt[i][j] <= opt[i][j+1].
```

#### DP problem-type recognition (high-value)

- Sequence with local transitions → 1D DP.
- Partition into k groups with cost interval → D&C / Knuth candidates.
- State depends on subset of used elements → bitmask DP.
- Count strings/numbers with digit constraints → digit DP.
- Tree answer requiring include/exclude node states → tree DP with 2-state transitions.

---

### 10.8 Final quick ACPC checklist by topic

- **Graphs:** shortest path family, SCC/2-SAT, flow, bridges/articulation, DSU offline.
- **DS:** Fenwick variants, segtree lazy, sparse table, PBDS/compression workflow.
- **Strings:** KMP + Z + Aho, hashing for O(1) substring compare.
- **Number theory (NS):** gcd/ext-gcd, inverses, CRT, sieve/SPF, modular power.
- **DP:** state design, transition proof, memory compression, reconstruction, optimization conditions.
- **Bits:** masks, subset iteration, popcount/parity, bitset acceleration, XOR basis patterns.

## 11) Bit Manipulation & Bitset

### 11.1 Bit Operations Cheat Sheet

```cpp
// read/set/clear/toggle bit i (0-indexed)
bool getBit(long long x, int i) { return (x >> i) & 1LL; }
long long setBit(long long x, int i) { return x | (1LL << i); }
long long clearBit(long long x, int i) { return x & ~(1LL << i); }
long long toggleBit(long long x, int i) { return x ^ (1LL << i); }
// lowbit and common predicates
long long lowbit(long long x) { return x & -x; }
bool isPowerOfTwo(long long x) { return x > 0 && (x & (x - 1)) == 0; }
```

```cpp
// builtins (GCC/Clang)
int cnt1(unsigned int x) { return __builtin_popcount(x); }
int cnt1ll(unsigned long long x) { return __builtin_popcountll(x); }
int lsbIndex(unsigned int x) { return __builtin_ctz(x); }       // x != 0
int msbIndex(unsigned int x) { return 31 - __builtin_clz(x); }  // x != 0
int parity(unsigned int x) { return __builtin_parity(x); }      // 1 if odd count of bits
```

#### Notes

- Use unsigned shifts for bit-heavy logic to avoid sign issues.
- For 64-bit masks, always shift with `1LL << i`.
- `x & (x-1)` removes the lowest set bit.

---

### 11.2 Brian Kernighan's Trick (Named)

```cpp
int countBits(int x) {
    int cnt = 0;
    while (x) {
        x &= (x - 1);  // clears the lowest set bit each iteration
        cnt++;
    }
    return cnt;
}
```

##### Use

- Counting set bits, or iterating over each set bit's position, in `O(popcount(x))` instead of `O(bits)`.
- Prefer `__builtin_popcount` when only the count is needed; use this trick when you must also process each bit individually.

---

### 11.3 Gray Code

```cpp
int toGray(int n) { return n ^ (n >> 1); }
int fromGray(int g) {
    int n = 0;
    for (; g; g >>= 1) n ^= g;
    return n;
}
```

##### Use

- Enumerate all `2^n` subsets so that consecutive subsets differ by exactly one bit — useful for incremental subset DP/brute force where recomputing from scratch is too slow.
- `toGray(i)` gives the `i`-th subset in Gray-code order.

##### Complexity

```
O(1) per conversion, O(2^n) to enumerate all subsets
```

---

### 11.4 Submask / Supmask Iteration Tricks

```cpp
// iterate all submasks of mask
for (int sub = mask;; sub = (sub - 1) & mask) {
    // use sub
    if (sub == 0) break;
}
// iterate all masks of n bits
for (int mask = 0; mask < (1 << n); mask++) {
    // use mask
}
```

```cpp
// iterate set bits of mask in O(number_of_set_bits)
for (int m = mask; m; m &= (m - 1)) {
    int b = __builtin_ctz(m);
    // bit b is set
}
```

#### Use Cases

- Subset DP transitions.
- Meet-in-the-middle state filtering.
- Inclusion-exclusion over selected features.

---

### 11.5 Important Bit Tricks

```cpp
// next combination with same popcount (Gosper's hack), x > 0
unsigned int nextComb(unsigned int x) {
    unsigned int c = x & -x;
    unsigned int r = x + c;
    return (((r ^ x) >> 2) / c) | r;
}
```

```cpp
// compress coordinates into bit positions and store chosen values in a mask
// when n <= 20..24, brute force on masks can be feasible with pruning
```

```cpp
// XOR swap trick exists but DO NOT use in CP production; prefer std::swap.
```

#### Problem Recognition

- `n <= 20` and "choose subset" → bitmask brute force / DP.
- Need to count enabled features fast → popcount.
- Need nearest differing state by one element → toggle one bit.

---

### 11.6 Bitmask DP Starter Patterns

```cpp
// TSP-style DP: dp[mask][last]
const long long BIG = (long long)4e18;
vector<vector<long long>> dp(1 << n, vector<long long>(n, BIG));
for (int s = 0; s < n; s++) dp[1 << s][s] = 0;
for (int mask = 0; mask < (1 << n); mask++) {
    for (int u = 0; u < n; u++)
        if ((mask >> u) & 1) {
            if (dp[mask][u] == BIG) continue;
            for (int v = 0; v < n; v++)
                if (((mask >> v) & 1) == 0) {
                    int nmask = mask | (1 << v);
                    dp[nmask][v] = min(dp[nmask][v], dp[mask][u] + cost[u][v]);
                }
        }
}
```

```cpp
// SOS DP (sum over subsets) idea:
// for(int i=0;i<n;i++) for(int mask=0;mask<(1<<n);mask++)
//   if(mask&(1<<i)) f[mask]+=f[mask^(1<<i)];
```

#### Complexity

- Bitmask DP over subsets: usually `O(n * 2^n)` or `O(n^2 * 2^n)`.
- SOS DP: `O(n * 2^n)`.

---

### 11.7 std::bitset: How To Use

```cpp
const int MAXN = 200005;
bitset<MAXN> bs;
bs.set(5);    // set bit 5
bs.reset(5);  // clear bit 5
bs.flip(5);   // toggle bit 5
bs[10] = 1;   // direct access
int ones = (int)bs.count();
bool any = bs.any();
bool none = bs.none();
bitset<MAXN> a, b;
a |= b;
a &= b;
a ^= b;
a <<= 3;
a >>= 2;
```

```cpp
// subset sum acceleration with bitset
// reachable sums after processing each weight
bitset<200001> can;
can[0] = 1;
for (int w : weights) can |= (can << w);
// can[s] tells whether sum s is achievable
```

#### When bitset is strong

- Dense boolean DP states.
- Many OR/AND/XOR operations on big binary vectors.
- Fast subset-sum feasibility queries.

---

### 11.8 XOR Basis (Linear Basis) – important bit module

```cpp
struct XorBasis {
    static const int LOG = 60;
    long long b[LOG]{};
    void add(long long x) {
        for (int i = LOG - 1; i >= 0; i--) {
            if (((x >> i) & 1) == 0) continue;
            if (!b[i]) {
                b[i] = x;
                return;
            }
            x ^= b[i];
        }
    }
    bool canMake(long long x) const {
        for (int i = LOG - 1; i >= 0; i--)
            if ((x ^ b[i]) < x) x ^= b[i];
        return x == 0;
    }
    long long maxXor(long long x = 0) const {
        for (int i = LOG - 1; i >= 0; i--) x = max(x, x ^ b[i]);
        return x;
    }
};
```

#### XOR Basis Use Cases

- Maximum subset xor.
- Check if xor target is representable.
- Offline queries on xor-space (with prefix basis variants).

---

### 11.9 Common Bit Problems Checklist

- Subset count / subset optimization.
- Min operations using toggles.
- Pair xor max/min.
- Gaussian elimination over GF(2) / xor basis.
- Profile DP on grids (state per row/column mask).
