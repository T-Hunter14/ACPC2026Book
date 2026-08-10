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
    int t = 1; cin >> t;
    while (t--) solve();
    return 0;
}
```

---

### Custom Sort

```cpp\nstruct node{ int x, y; };\nsort(all(v), [](const node& a, const node& b){ return a.x!=b.x ? a.x<b.x : a.y>b.y; });\n```

##### Use

- Sort struct.
- Multi-key sorting.

##### Complexity

- `O(n log n)`

---

### Coordinate Compression (Restore Values)

```cpp
struct compressor{
    vector<int> vals;
    void build(vector<int> v){ vals=move(v); sort(all(vals)); vals.erase(unique(all(vals)), vals.end()); }
    int  get(int x) const { return lower_bound(all(vals), x) - vals.begin(); }
    int  rev(int id) const { return vals[id]; }
};
```

##### Use

```cpp\ncompressor cp;\n\ncp.build(a);\n\nint id = cp.get(x);\n\nint val = cp.rev(id);\n```

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

```cpp\nauto vals=a; sort(all(vals)); vals.erase(unique(all(vals)), vals.end());\nfor(auto &x:a) x = lower_bound(all(vals), x) - vals.begin();\n```

##### Complexity

- `O(n log n)`

##### Notes

- Cannot restore original values.
- Faster to write during contests.

---

### Debug

```cpp
#ifndef ONLINE_JUDGE
template<class T> void dbg(const vector<T>& v){ cerr<<"[ "; for(const auto& x:v) cerr<<x<<' '; cerr<<"]\n"; }
#define debug(x) cerr<<#x<<" = "<<(x)<<'\n'
#else
#define debug(x) ((void)0)
#define dbg(v)   ((void)0)
#endif
```

##### Use

```cpp\ndebug(n);\ndebug(ans);\n\ndbg(v);\n```

##### Notes

- Disabled automatically on Online Judge.

---

### Random (RNG helper)

```cpp\nmt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());\nlong long rnd(long long l, long long r){ return uniform_int_distribution<long long>(l, r)(rng); }\n```

##### Use

```cpp\nlong long x = rnd(1, 100);\n```

##### Complexity

- `O(1)`

##### Notes

- Stress testing
- Randomized algorithms

---

### Shuffle

```cpp\nshuffle(all(v), rng);\n```

##### Complexity

- `O(n)`

##### Notes

- Generate random permutation.
- Useful for anti-hack.

---

### ckmin / ckmax

```cpp\ntemplate<class T> bool ckmin(T& a, const T& b){ return b<a ? (a=b, true) : false; }\ntemplate<class T> bool ckmax(T& a, const T& b){ return a<b ? (a=b, true) : false; }\n```

##### Use

```cpp\nckmin(ans, cur);\n\nckmax(ans, cur);\n```

##### Complexity

- `O(1)`

##### Notes

- Very common in DP and Graphs.

---

### Next / Previous Permutation

```cpp\nnext_permutation(all(v));\n\nprev_permutation(all(v));\n```

##### Complexity

- `O(n)`

##### Notes

- Generate permutations.
- Useful in brute force.

---

### Useful STL Tricks

```cpp\n*max_element(all(v));\n\n*min_element(all(v));\n\naccumulate(all(v), 0LL);\n\nreverse(all(v));\n\nrotate(v.begin(), v.begin() + k, v.end());\n\niota(all(v), 0);\n```

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

```cpp\nlong long l=0, r=(long long)1e18, ans=-1;\nwhile(l<=r){\n    long long mid=(l+r)>>1;\n    if(check(mid)) ans=mid, r=mid-1;\n    else l=mid+1;\n}\n```

##### Complexity

- `O(log Range)`

##### Notes

- Finds first valid value.

---

### Binary Search Template (Last True)

```cpp\nlong long l=0, r=(long long)1e18, ans=-1;\nwhile(l<=r){\n    long long mid=(l+r)>>1;\n    if(check(mid)) ans=mid, l=mid+1;\n    else r=mid-1;\n}\n```

##### Complexity

- `O(log Range)`

##### Notes

- Finds last valid value.

---

### Ternary Search

```cpp\nwhile(r-l>3){\n    long long m1=l+(r-l)/3, m2=r-(r-l)/3;\n    if(f(m1)<f(m2)) r=m2; else l=m1;\n}\n```

##### Complexity

- `O(log Range)`

##### Notes

- Convex / Concave functions only.
- Usually for optimization problems.

---


## 2) Graph Algorithms

### DSU (Standard)

```cpp
struct dsu {
    vector<int> p, sz;
    int cc;

    dsu() {}

    dsu(int n) {
        init(n);
    }

    void init(int n) {
        cc = n;

        p.resize(n + 1);
        sz.assign(n + 1, 1);

        iota(all(p), 0);
    }

    int find(int x) {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    bool same(int a, int b) {
        return find(a) == find(b);
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (sz[a] < sz[b])
            swap(a, b);

        p[b] = a;
        sz[a] += sz[b];

        cc--;

        return true;
    }

    int size(int x) {
        return sz[find(x)];
    }
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

```cpp\nif (d.same(u, v))\n```

#### Merge Components

```cpp\nd.unite(u, v);\n```

#### Component Size

```cpp\ncout << d.size(u);\n```

#### Number of Components

```cpp\ncout << d.cc;\n```

#### Cycle Detection

```cpp\nif (!d.unite(u, v)) {\n    // cycle found\n}\n```

#### Kruskal MST

```cpp\nif (d.unite(u, v))\n    mst += w;\n```

---

### DSU (Component Tracking)

```cpp
struct dsu {
    int cc;
    vector<int> p, sz;
    vector<vector<int>> comp;

    dsu() {}

    dsu(int n) {
        init(n);
    }

    void init(int n) {
        cc = n;

        p.resize(n + 1);
        sz.assign(n + 1, 1);

        iota(all(p), 0);

        comp.assign(n + 1, {});

        for (int i = 1; i <= n; i++)
            comp[i].push_back(i);
    }

    int find(int x) {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    bool same(int a, int b) {
        return find(a) == find(b);
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (sz[a] < sz[b])
            swap(a, b);

        p[b] = a;
        sz[a] += sz[b];

        if (comp[b].size() > comp[a].size())
            swap(comp[a], comp[b]);

        comp[a].insert(comp[a].end(), comp[b].begin(), comp[b].end());

        comp[b].clear();

        cc--;

        return true;
    }

    int size(int x) {
        return sz[find(x)];
    }

    vector<int>& members(int x) {
        return comp[find(x)];
    }

    vector<vector<int>> get_all_components() {
        vector<vector<int>> res;

        for (int i = 1; i < (int)comp.size(); i++) {
            if (!comp[i].empty())
                res.push_back(comp[i]);
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

```cpp\nfor (auto u : d.members(x))\n    cout << u << ' ';\n```

#### Print All Components

```cpp\nauto comps = d.get_all_components();\n\nfor (auto &c : comps) {\n    for (auto x : c)\n        cout << x << ' ';\n    cout << endl;\n}\n```

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

```cpp
vector<int> bfs(int src, const vector<vector<int>>& adj) {
    int n = (int)adj.size() - 1;
    vector<int> dist(n + 1, -1);
    queue<int> q;
    q.push(src); dist[src] = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) if (dist[v] == -1) {
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

```cpp\nauto dist = bfs(1, adj);\n```

---

### BFS With Parent (Restore Path)

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
        if (dist[v] != -1)
            continue;

        dist[v] = dist[u] + 1;
        par[v] = u;

        q.push(v);
    }
}
```

##### Restore Path

```cpp\nvector<int> path;\n\nfor (int cur = dest; cur != -1; cur = par[cur])\n    path.push_back(cur);\n\nreverse(all(path));\n```

##### Use

```
Print shortest path
Find route
```

---

### Multi Source BFS

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
        if (dist[v] != -1)
            continue;

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

### Grid BFS

```cpp
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

queue<pair<int,int>> q;

q.push({sx, sy});

dist[sx][sy] = 0;

while (!q.empty()) {
    auto [x, y] = q.front();
    q.pop();

    for (int k = 0; k < 4; k++) {

        int nx = x + dx[k];
        int ny = y + dy[k];

        if (nx < 0 || ny < 0 ||
            nx >= n || ny >= m)
            continue;

        if (grid[nx][ny] == '#')
            continue;

        if (dist[nx][ny] != -1)
            continue;

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

### BFS On State Graph

#### Example

```
(node , mask)
(node , parity)
(node , coins)
(node , fuel)
```

---

```cpp
queue<pair<int,int>> q;

vector<vector<int>> dist(
    n + 1,
    vector<int>(1 << k, -1)
);

q.push({src, 0});

dist[src][0] = 0;

while (!q.empty()) {

    auto [u, mask] = q.front();
    q.pop();

    for (auto v : adj[u]) {

        int nmask = mask;

        if (special[v])
            nmask |= (1 << id[v]);

        if (dist[v][nmask] != -1)
            continue;

        dist[v][nmask] =
            dist[u][mask] + 1;

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

### 0-1 BFS

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

### Useful Snippets

#### Count Connected Components

```cpp
int cc = 0;

for (int i = 1; i <= n; i++) {

    if (dist[i] != -1)
        continue;

    cc++;

    queue<int> q;

    q.push(i);

    dist[i] = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (auto v : adj[u]) {

            if (dist[v] != -1)
                continue;

            dist[v] = 0;
            q.push(v);
        }
    }
}
```

---

#### Find Farthest Node

```cpp\nint mx = 0;\nint node = src;\n\nfor (int i = 1; i <= n; i++) {\n    if (dist[i] > mx) {\n        mx = dist[i];\n        node = i;\n    }\n}\n```

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

```cpp\nvector<vector<int>> adj;\nvector<int> vis;\n\nvoid dfs(int u) {\n    vis[u] = 1;\n    for (int v : adj[u]) if (!vis[v]) dfs(v);\n}\n```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

##### Use

```cpp\ndfs(1);\n```

---

### Connected Components

```cpp\nvector<int> vis;\n\nvoid dfs(int u) {\n\n    vis[u] = 1;\n\n    for (auto v : adj[u]) {\n\n        if (!vis[v])\n            dfs(v);\n    }\n}\n```

##### Count Components

```cpp\nint cc = 0;\n\nfor (int i = 1; i <= n; i++) {\n\n    if (vis[i])\n        continue;\n\n    cc++;\n\n    dfs(i);\n}\n```

##### Complexity

```
O(V + E)
```

---

### DFS With Parent

```cpp\nvoid dfs(int u, int p) {\n\n    for (auto v : adj[u]) {\n\n        if (v == p)\n            continue;\n\n        dfs(v, u);\n    }\n}\n```

##### Use

```
Tree DFS
Avoid Going Back To Parent
```

---

### Subtree Size

```cpp
vector<int> sz;

void dfs(int u, int p) {

    sz[u] = 1;

    for (auto v : adj[u]) {

        if (v == p)
            continue;

        dfs(v, u);

        sz[u] += sz[v];
    }
}
```

##### Use

```cpp\ncout << sz[u];\n```

##### Meaning

```
Number Of Nodes In Subtree(u)
```

---

### Entry / Exit Time

```cpp
int timer = 0;

vector<int> tin, tout;

void dfs(int u, int p) {

    tin[u] = ++timer;

    for (auto v : adj[u]) {

        if (v == p)
            continue;

        dfs(v, u);
    }

    tout[u] = timer;
}
```

##### Check Ancestor

```cpp\nbool is_ancestor(int u, int v) {\n\n    return tin[u] <= tin[v]\n        && tout[v] <= tout[u];\n}\n```

##### Use

```
Ancestor Queries
Euler Tour
Subtree Queries
LCA
```

---

### Euler Tour (Flatten Tree)

```cpp
vector<int> tin;
vector<int> tout;
vector<int> flat;

int timer = 0;

void dfs(int u, int p) {

    tin[u] = timer++;

    flat.push_back(u);

    for (auto v : adj[u]) {

        if (v == p)
            continue;

        dfs(v, u);
    }

    tout[u] = timer - 1;
}
```

##### Subtree Range

```cpp\n[tin[u], tout[u]]\n```

##### Use

```
Segment Tree On Tree
Fenwick On Tree
Subtree Queries
```

---

### Cycle Detection (Undirected)

```cpp
bool dfs(int u, int p) {

    vis[u] = 1;

    for (auto v : adj[u]) {

        if (v == p)
            continue;

        if (vis[v])
            return true;

        if (dfs(v, u))
            return true;
    }

    return false;
}
```

##### Complexity

```
O(V + E)
```

---

### Cycle Detection (Directed)

```cpp
vector<int> vis;

bool dfs(int u) {

    vis[u] = 1;

    for (auto v : adj[u]) {

        if (vis[v] == 1)
            return true;

        if (vis[v] == 0 && dfs(v))
            return true;
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

### Topological Sort (DFS)

```cpp\nvector<int> vis;\nvector<int> topo;\n\nvoid dfs(int u) {\n\n    vis[u] = 1;\n\n    for (auto v : adj[u]) {\n\n        if (!vis[v])\n            dfs(v);\n    }\n\n    topo.push_back(u);\n}\n```

##### Build Topological Order

```cpp\nfor (int i = 1; i <= n; i++) {\n\n    if (!vis[i])\n        dfs(i);\n}\n\nreverse(all(topo));\n```

##### Complexity

```
O(V + E)
```

---

### Tree Diameter

#### First DFS

```cpp\ndfs(1);\n```

Find farthest node:

```cpp\nint a = max_element(\n    all(dist)\n) - dist.begin();\n```

---

#### Second DFS

```cpp\ndfs(a);\n```

Find farthest node:

```cpp\nint b = max_element(\n    all(dist)\n) - dist.begin();\n```

---

#### Diameter Length

```cpp\ndist[b]\n```

##### Complexity

```
O(N)
```

---

### DFS Order

```cpp\nvector<int> ord;\n\nvoid dfs(int u, int p) {\n\n    ord.push_back(u);\n\n    for (auto v : adj[u]) {\n\n        if (v == p)\n            continue;\n\n        dfs(v, u);\n    }\n}\n```

##### Use

```
Tree Traversal
Euler Variants
Offline Queries
```

---

### Bipartite Check (DFS)

```cpp
vector<int> color(n + 1, -1);

bool dfs(int u, int c) {

    color[u] = c;

    for (auto v : adj[u]) {

        if (color[v] == -1) {

            if (!dfs(v, c ^ 1))
                return false;
        }
        else {

            if (color[v] == color[u])
                return false;
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

### Useful Snippets

#### Collect Nodes Of Component

```cpp\nvector<int> comp;\n\nvoid dfs(int u) {\n\n    vis[u] = 1;\n\n    comp.push_back(u);\n\n    for (auto v : adj[u]) {\n\n        if (!vis[v])\n            dfs(v);\n    }\n}\n```

---

#### Leaf Detection

```cpp\nif (adj[u].size() == 1 && u != root)\n{\n    // leaf\n}\n```

---

#### Count Leaves

```cpp\nint leaves = 0;\n\nfor (int i = 2; i <= n; i++) {\n\n    if (adj[i].size() == 1)\n        leaves++;\n}\n```

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

```cpp
vector<int> topo;

vector<int> indeg(n + 1);

for (int u = 1; u <= n; u++) {
    for (auto v : adj[u]) {
        indeg[v]++;
    }
}

queue<int> q;

for (int i = 1; i <= n; i++) {
    if (indeg[i] == 0)
        q.push(i);
}

while (!q.empty()) {

    int u = q.front();
    q.pop();

    topo.push_back(u);

    for (auto v : adj[u]) {

        indeg[v]--;

        if (indeg[v] == 0)
            q.push(v);
    }
}
```

##### Complexity

```
Time  : O(V + E)
Memory: O(V)
```

---

### Check If DAG

```cpp\nif ((int)topo.size() != n)\n{\n    // cycle exists\n}\n```

##### Idea

```
A graph has a topological order
iff it is a DAG.
```

---

### Lexicographically Smallest Topological Order

```cpp
priority_queue<
    int,
    vector<int>,
    greater<int>
> pq;

for (int i = 1; i <= n; i++) {
    if (indeg[i] == 0)
        pq.push(i);
}

while (!pq.empty()) {

    int u = pq.top();
    pq.pop();

    topo.push_back(u);

    for (auto v : adj[u]) {

        indeg[v]--;

        if (indeg[v] == 0)
            pq.push(v);
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

### DFS Topological Sort

```cpp\nvector<int> vis;\nvector<int> topo;\n\nvoid dfs(int u) {\n\n    vis[u] = 1;\n\n    for (auto v : adj[u]) {\n\n        if (!vis[v])\n            dfs(v);\n    }\n\n    topo.push_back(u);\n}\n```

##### Build Order

```cpp\nfor (int i = 1; i <= n; i++) {\n\n    if (!vis[i])\n        dfs(i);\n}\n\nreverse(all(topo));\n```

##### Complexity

```
O(V + E)
```

---

### Cycle Detection In DAG

```cpp
vector<int> vis;

bool dfs(int u) {

    vis[u] = 1;

    for (auto v : adj[u]) {

        if (vis[v] == 1)
            return true;

        if (vis[v] == 0 && dfs(v))
            return true;
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

### Longest Path In DAG

```cpp\nvector<int> dp(n + 1, 0);\n\nfor (auto u : topo) {\n\n    for (auto v : adj[u]) {\n\n        dp[v] =\n            max(dp[v], \n                dp[u] + 1);\n    }\n}\n```

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

```cpp
vector<int> dist(n + 1, INF);

dist[src] = 0;

for (auto u : topo) {

    if (dist[u] == INF)
        continue;

    for (auto [v, w] : adj[u]) {

        dist[v] =
            min(dist[v],
                dist[u] + w);
    }
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

### Count Number Of Paths In DAG

```cpp\nvector<int> dp(n + 1);\n\ndp[src] = 1;\n\nfor (auto u : topo) {\n\n    for (auto v : adj[u]) {\n\n        dp[v] += dp[u];\n        dp[v] %= MOD;\n    }\n}\n```

##### Use

```
Count Paths
DP On DAG
```

---

### Path Restoration In DAG

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

```cpp\nvector<int> path;\n\nfor (int cur = dest;\n     cur != -1;\n     cur = par[cur])\n{\n    path.push_back(cur);\n}\n\nreverse(all(path));\n```

---

### Useful Snippets

#### Sources (Indegree = 0)

```cpp\nvector<int> srcs;\n\nfor (int i = 1; i <= n; i++) {\n\n    if (indeg[i] == 0)\n        srcs.push_back(i);\n}\n```

---

#### Sinks (Outdegree = 0)

```cpp\nvector<int> sinks;\n\nfor (int i = 1; i <= n; i++) {\n\n    if (adj[i].empty())\n        sinks.push_back(i);\n}\n```

---

#### Check Unique Topological Order

```cpp\nbool unique_order = true;\n\nwhile (!q.empty()) {\n\n    if ((int)q.size() > 1)\n        unique_order = false;\n\n    int u = q.front();\n    q.pop();\n\n    ...\n}\n```

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

```cpp
vector<long long> dijkstra(int src, const vector<vector<pair<int,int>>>& adj) {
    int n = (int)adj.size() - 1;
    vector<long long> dist(n + 1, INF);
    priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
    dist[src] = 0; pq.push({0, src});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d != dist[u]) continue;
        for (auto [v, w] : adj[u]) if (dist[v] > d + w) {
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

### Path Restore

```cpp
vector<int> dist(n + 1, INF);
vector<int> par(n + 1, -1);

priority_queue<
    pair<int,int>,
    vector<pair<int,int>>,
    greater<pair<int,int>>
> pq;

dist[src] = 0;

pq.push({0, src});

while (!pq.empty()) {

    auto [d, u] = pq.top();
    pq.pop();

    if (d != dist[u])
        continue;

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

```cpp\nvector<int> path;\n\nfor (int cur = dest;\n     cur != -1;\n     cur = par[cur])\n{\n    path.push_back(cur);\n}\n\nreverse(all(path));\n```

---

### Multi Source Dijkstra

```cpp
vector<int> dist(n + 1, INF);

priority_queue<
    pair<int,int>,
    vector<pair<int,int>>,
    greater<pair<int,int>>
> pq;

for (auto src : sources) {

    dist[src] = 0;
    pq.push({0, src});
}

while (!pq.empty()) {

    auto [d, u] = pq.top();
    pq.pop();

    if (d != dist[u])
        continue;

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

### State Graph Dijkstra

#### Example States

```
(node , fuel)

(node , mask)

(node , coupons)

(node , parity)
```

---

```cpp
priority_queue<
    array<int,3>,
    vector<array<int,3>>,
    greater<array<int,3>>
> pq;

vector<vector<int>> dist(
    n + 1,
    vector<int>(K, INF)
);

dist[src][0] = 0;

pq.push({0, src, 0});

while (!pq.empty()) {

    auto [d, u, state] = pq.top();
    pq.pop();

    if (d != dist[u][state])
        continue;

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

### Dense Graph Dijkstra

```cpp
vector<int> dist(n + 1, INF);
vector<int> vis(n + 1);

dist[src] = 0;

for (int it = 1; it <= n; it++) {

    int u = -1;

    for (int i = 1; i <= n; i++) {

        if (vis[i])
            continue;

        if (u == -1 ||
            dist[i] < dist[u])
        {
            u = i;
        }
    }

    vis[u] = 1;

    for (auto [v, w] : adj[u]) {

        dist[v] =
            min(dist[v],
                dist[u] + w);
    }
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

### Count Number Of Shortest Paths

```cpp
vector<int> dist(n + 1, INF);
vector<int> ways(n + 1, 0);

dist[src] = 0;
ways[src] = 1;

while (!pq.empty()) {

    auto [d, u] = pq.top();
    pq.pop();

    if (d != dist[u])
        continue;

    for (auto [v, w] : adj[u]) {

        if (dist[v] > dist[u] + w) {

            dist[v] = dist[u] + w;

            ways[v] = ways[u];
            pq.push({dist[v], v});
        }

        else if (dist[v] == dist[u] + w) {
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

### Shortest Path DAG After Dijkstra

```cpp\nif (\n    dist[v] ==\n    dist[u] + w\n)\n{\n    dag[u].push_back(v);\n}\n```

##### Use

```
All Shortest Paths
DP On Shortest Paths
```

---

### Dijkstra On Grid

```cpp\npriority_queue<\n    array<int, 3>, \n    vector<array<int, 3>>, \n    greater<array<int, 3>>\n> pq;\n\ndist[sx][sy] = 0;\npq.push({0, sx, sy});\n```

##### Use

```
Weighted Grid
Minimum Cost Path
```

---

### K Shortest Paths (Intro)

```cpp
vector<int> cnt(n + 1);

priority_queue<
    pair<int,int>,
    vector<pair<int,int>>,
    greater<pair<int,int>>
> pq;

pq.push({0, src});

while (!pq.empty()) {

    auto [d, u] = pq.top();
    pq.pop();

    cnt[u]++;

    if (cnt[u] > k)
        continue;

    for (auto [v, w] : adj[u]) {

        pq.push({d + w, v});
    }
}
```

##### Use

```
CSES Flight Routes
K Shortest Paths
```

---

### Useful Snippets

#### Unreachable Nodes

```cpp\nif (dist[u] == INF)\n{\n    // unreachable\n}\n```

---

#### Farthest Reachable Node

```cpp\nint mx = -1;\nint node = -1;\n\nfor (int i = 1; i <= n; i++) {\n\n    if (dist[i] == INF)\n        continue;\n\n    if (dist[i] > mx) {\n\n        mx = dist[i];\n        node = i;\n    }\n}\n```

---

#### Shortest Path Length

```cpp\ncout << dist[dest];\n```

---

#### Check Negative Edge

```cpp\nif (w < 0)\n{\n    // DON'T use Dijkstra\n}\n```

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

```cpp
struct dsu {
    vector<int> p, sz;

    dsu(int n) {
        p.resize(n + 1);
        sz.assign(n + 1, 1);

        iota(all(p), 0);
    }

    int find(int x) {
        return p[x] == x ? x : p[x] = find(p[x]);
    }

    bool unite(int a, int b) {

        a = find(a);
        b = find(b);

        if (a == b)
            return false;

        if (sz[a] < sz[b])
            swap(a, b);

        p[b] = a;
        sz[a] += sz[b];

        return true;
    }
};
```

---

### Standard Kruskal

```cpp
struct edge {
    int u, v, w;

    bool operator < (const edge &other) const {
        return w < other.w;
    }
};

vector<edge> edges;

sort(all(edges));

dsu d(n);

int mst = 0;

for (auto [u, v, w] : edges) {

    if (d.unite(u, v)) {
        mst += w;
    }
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

### Check If MST Exists

```cpp\nint used = 0;\n\nfor (auto [u, v, w] : edges) {\n\n    if (d.unite(u, v)) {\n\n        mst += w;\n        used++;\n    }\n}\n\nif (used != n - 1)\n{\n    cout << "IMPOSSIBLE";\n}\n```

##### Meaning

```
Graph is disconnected
No spanning tree exists
```

---

### Store MST Edges

```cpp\nvector<edge> mst_edges;\n\nfor (auto [u, v, w] : edges) {\n\n    if (d.unite(u, v)) {\n\n        mst += w;\n\n        mst_edges.push_back({\n            u, v, w\n        });\n    }\n}\n```

##### Use

```
Need actual MST
Need MST graph
Second MST
LCA on MST
```

---

### Build MST Graph

```cpp
vector<vector<pair<int,int>>> mst_adj(n + 1);

for (auto [u, v, w] : edges) {

    if (d.unite(u, v)) {

        mst_adj[u].push_back({
            v, w
        });

        mst_adj[v].push_back({
            u, w
        });
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

### Maximum Spanning Tree

```cpp\nsort(all(edges), [&](auto a, auto b) {\n    return a.w > b.w;\n});\n```

Everything else remains the same.

##### Use

```
Maximum total weight tree
```

---

### Number Of Connected Components

```cpp\ndsu d(n);\n\nfor (auto [u, v, w] : edges)\n    d.unite(u, v);\n\nint cc = 0;\n\nfor (int i = 1; i <= n; i++) {\n\n    if (d.find(i) == i)\n        cc++;\n}\n```

---

### Forest Cost

```cpp\nint cost = 0;\n\nfor (auto [u, v, w] : edges) {\n\n    if (d.unite(u, v))\n        cost += w;\n}\n```

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

```cpp\nsort(all(edges));\n```

---

#### MST Cost

```cpp\ncout << mst;\n```

---

#### Number Of MST Edges

```cpp\ncout << mst_edges.size();\n```

Should be:

```
n - 1
```

for connected graph.

---

#### Check Same Component

```cpp\nif (d.find(u) == d.find(v))\n{\n}\n```

---

#### Detect Cycle

```cpp\nif (!d.unite(u, v))\n{\n    // cycle edge\n}\n```

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

```cpp\nstruct edge {\n    int u, v, w;\n};\n```

---

### Standard Bellman Ford

```cpp
vector<int> dist(n + 1, INF);

dist[src] = 0;

for (int i = 1; i <= n - 1; i++) {

    bool changed = false;

    for (auto [u, v, w] : edges) {

        if (dist[u] == INF)
            continue;

        if (dist[v] > dist[u] + w) {

            dist[v] = dist[u] + w;

            changed = true;
        }
    }

    if (!changed)
        break;
}
```

##### Complexity

```
Time  : O(V * E)

Memory: O(V)
```

---

### Negative Cycle Detection

```cpp\nbool neg_cycle = false;\n\nfor (auto [u, v, w] : edges) {\n\n    if (dist[u] == INF)\n        continue;\n\n    if (dist[v] > dist[u] + w) {\n\n        neg_cycle = true;\n    }\n}\n```

##### Meaning

```
There exists a reachable negative cycle.
```

---

### Path Restore

```cpp
vector<int> dist(n + 1, INF);
vector<int> par(n + 1, -1);

dist[src] = 0;

for (int i = 1; i <= n - 1; i++) {

    for (auto [u, v, w] : edges) {

        if (dist[u] == INF)
            continue;

        if (dist[v] > dist[u] + w) {

            dist[v] = dist[u] + w;

            par[v] = u;
        }
    }
}
```

##### Restore Path

```cpp\nvector<int> path;\n\nfor (int cur = dest;\n     cur != -1;\n     cur = par[cur])\n{\n    path.push_back(cur);\n}\n\nreverse(all(path));\n```

---

### Restore Negative Cycle

```cpp
int x = -1;

for (int i = 1; i <= n; i++) {

    x = -1;

    for (auto [u, v, w] : edges) {

        if (dist[u] == INF)
            continue;

        if (dist[v] > dist[u] + w) {

            dist[v] = dist[u] + w;

            par[v] = u;

            x = v;
        }
    }
}
```

##### No Cycle

```cpp\nif (x == -1)\n{\n    // no negative cycle\n}\n```

---

##### Move Inside Cycle

```cpp\nfor (int i = 1; i <= n; i++)\n    x = par[x];\n```

---

##### Extract Cycle

```cpp\nvector<int> cyc;\n\nint cur = x;\n\ndo {\n\n    cyc.push_back(cur);\n\n    cur = par[cur];\n\n} while (cur != x);\n\ncyc.push_back(x);\n\nreverse(all(cyc));\n```

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

```cpp\nBellman Ford\n```

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

```cpp\nfor (int i = 1; i <= n; i++)\n    edges.push_back({0, i, 0});\n```

Then:

```cpp\nBellman Ford(0)\n```

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

```cpp\nw = -w;\n```

Then:

```cpp\nBellman Ford\n```

##### Warning

```
Need cycle handling
```

---

### Reachability From Negative Cycle

After detecting cycle nodes:

```cpp\nBFS / DFS\n```

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

```cpp\nif (dist[u] == INF)\n{\n}\n```

---

#### Reachable Node

```cpp\nif (dist[u] != INF)\n{\n}\n```

---

#### Early Stop Optimization

```cpp\nbool changed = false;\n\n...\n\nif (!changed)\n    break;\n```

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

```cpp
vector<vector<int>> dist(
    n + 1,
    vector<int>(n + 1, INF)
);

for (int i = 1; i <= n; i++)
    dist[i][i] = 0;

for (auto [u, v, w] : edges) {

    dist[u][v] =
        min(dist[u][v], w);
}
```

---

##### Main Floyd

```cpp
for (int k = 1; k <= n; k++) {

    for (int i = 1; i <= n; i++) {

        for (int j = 1; j <= n; j++) {

            dist[i][j] =
                min(
                    dist[i][j],
                    dist[i][k] +
                    dist[k][j]
                );
        }
    }
}
```

##### Complexity

```
Time  : O(N³)

Memory: O(N²)
```

---

### Undirected Graph

```cpp\ndist[u][v] =\ndist[v][u] = w;\n```

---

### Multiple Edges

```cpp\ndist[u][v] =\nmin(dist[u][v], w);\n```

---

### Query Distance

```cpp\ncout << dist[u][v];\n```

---

### Unreachable Nodes

```cpp\nif (dist[u][v] == INF)\n{\n}\n```

---

### Negative Cycle Detection

After Floyd:

```cpp\nfor (int i = 1; i <= n; i++) {\n\n    if (dist[i][i] < 0)\n    {\n        // negative cycle\n    }\n}\n```

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

```cpp\nvector<vector<int>> nxt(\n    n + 1, \n    vector<int>(n + 1, -1)\n);\n```

---

##### Initialization

```cpp\nfor (auto [u, v, w] : edges) {\n\n    dist[u][v] = w;\n\n    nxt[u][v] = v;\n}\n```

---

##### Floyd Update

```cpp\nif (\n    dist[i][j] >\n    dist[i][k] +\n    dist[k][j]\n)\n{\n    dist[i][j] =\n        dist[i][k] +\n        dist[k][j];\n\n    nxt[i][j] =\n        nxt[i][k];\n}\n```

---

##### Restore Path

```cpp\nvector<int> path;\n\nint cur = u;\n\nwhile (cur != v) {\n\n    path.push_back(cur);\n\n    cur = nxt[cur][v];\n}\n\npath.push_back(v);\n```

##### No Path

```cpp\nif (nxt[u][v] == -1)\n{\n}\n```

---

### Transitive Closure

Instead of shortest path:

```cpp\nvector<vector<int>> reach(\n    n + 1, \n    vector<int>(n + 1)\n);\n```

---

##### Initialization

```cpp\nreach[u][v] = 1;\n```

---

##### Floyd

```cpp
for (int k = 1; k <= n; k++) {

    for (int i = 1; i <= n; i++) {

        for (int j = 1; j <= n; j++) {

            reach[i][j] |=
                reach[i][k] &&
                reach[k][j];
        }
    }
}
```

##### Meaning

```
Can i reach j from i ?
```

---

### Minimum Directed Cycle

After Floyd:

```cpp\nint ans = INF;\n\nfor (int i = 1; i <= n; i++) {\n\n    ans =\n        min(ans, dist[i][i]);\n}\n```

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

```cpp\ndist[a][b] = cost;\n```

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

```cpp\nrun Floyd once\n```

Then:

```cpp\nanswer Q queries\n\nO(1)\n```

##### Total

```
Preprocess : O(N³)

Query      : O(1)
```

---

### Useful Snippets

#### Check Reachability

```cpp\nif (dist[u][v] != INF)\n{\n}\n```

---

#### Check Same SCC (small graph)

```cpp\nif (\n    dist[u][v] != INF &&\n    dist[v][u] != INF\n)\n{\n}\n```

##### Meaning

```
Mutually reachable
```

---

#### Count Reachable Nodes

```cpp\nint cnt = 0;\n\nfor (int v = 1; v <= n; v++) {\n\n    if (dist[u][v] != INF)\n        cnt++;\n}\n```

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

```cpp
const int LG = 20;

vector<vector<int>> up;
vector<int> dep;
vector<vector<int>> adj;

void dfs(int u, int p) {

    up[u][0] = p;

    for (int j = 1; j < LG; j++) {

        up[u][j] =
            up[
                up[u][j - 1]
            ][j - 1];
    }

    for (auto v : adj[u]) {

        if (v == p)
            continue;

        dep[v] = dep[u] + 1;

        dfs(v, u);
    }
}

void build(int n, int root = 1) {

    up.assign(
        n + 1,
        vector<int>(LG)
    );

    dep.assign(n + 1, 0);

    dfs(root, root);
}
```

---

### Jump K Levels

```cpp\nint jump(int u, int k) {\n\n    for (int j = 0; j < LG; j++) {\n\n        if (k & (1LL << j))\n            u = up[u][j];\n    }\n\n    return u;\n}\n```

##### Complexity

```
O(log N)
```

---

### Kth Ancestor

```cpp\nint kth_ancestor(int u, int k) {\n\n    return jump(u, k);\n}\n```

##### Example

```cpp\ncout << kth_ancestor(10, 3);\n```

Meaning:

```
3rd ancestor of node 10
```

---

### Check Ancestor

Needs Euler Tour.

```cpp\nbool is_ancestor(int u, int v) {\n\n    return tin[u] <= tin[v]\n        && tout[v] <= tout[u];\n}\n```

##### Complexity

```
O(1)
```

---

### Lift To Same Depth

```cpp\nif (dep[u] < dep[v])\n    swap(u, v);\n\nu = jump(\n    u, \n    dep[u] - dep[v]\n);\n```

##### Use

```
LCA
Path Queries
```

---

### Distance To Root

```cpp\ndep[u]\n```

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

```cpp\nup[u][0]\n```

---

#### Grand Parent

```cpp\nup[u][1]\n```

---

#### 4th Ancestor

```cpp\nup[u][2]\n```

because:

```
2² = 4
```

---

#### Move Up One Level

```cpp\nu = up[u][0];\n```

---

#### Move Up 13 Levels

```cpp\nu = jump(u, 13);\n```

---

#### Root Check

```cpp\nif (u == root)\n{\n}\n```

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

```cpp\nconst int LG = 20;\n```

for:

```
N <= 1e6
```

---

### Common Mistakes

#### Wrong

```cpp\ndfs(root, 0);\n```

Then:

```cpp\nup[0][j]\n```

may be accessed.

---

#### Safer

```cpp\ndfs(root, root);\n```

---

#### Wrong LG

```cpp\nconst int LG = 17;\n```

while:

```
N = 2e5
```

---

#### Safe

```cpp\nconst int LG = 20;\n```

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

```cpp
const int LG = 20;

vector<vector<int>> adj;
vector<vector<int>> up;

vector<int> dep;

void dfs(int u, int p) {

    up[u][0] = p;

    for (int j = 1; j < LG; j++) {

        up[u][j] =
            up[
                up[u][j - 1]
            ][j - 1];
    }

    for (auto v : adj[u]) {

        if (v == p)
            continue;

        dep[v] = dep[u] + 1;

        dfs(v, u);
    }
}

void build(int n, int root = 1) {

    up.assign(
        n + 1,
        vector<int>(LG)
    );

    dep.assign(n + 1, 0);

    dfs(root, root);
}
```

---

### LCA Query

```cpp
int lca(int u, int v) {

    if (dep[u] < dep[v])
        swap(u, v);

    int diff =
        dep[u] - dep[v];

    for (int j = 0; j < LG; j++) {

        if (diff & (1LL << j))
            u = up[u][j];
    }

    if (u == v)
        return u;

    for (int j = LG - 1; j >= 0; j--) {

        if (
            up[u][j] !=
            up[v][j]
        )
        {
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

### Distance Between Two Nodes

```cpp\nint dist(int u, int v) {\n\n    int p = lca(u, v);\n\n    return\n        dep[u]\n        +\n        dep[v]\n        -\n        2 * dep[p];\n}\n```

##### Complexity

```
O(log N)
```

---

### Kth Ancestor

```cpp\nint jump(int u, int k) {\n\n    for (int j = 0; j < LG; j++) {\n\n        if (k & (1LL << j))\n            u = up[u][j];\n    }\n\n    return u;\n}\n```

---

### Check Ancestor

Needs Euler Tour.

```cpp\nbool is_ancestor(int u, int v) {\n\n    return\n        tin[u] <= tin[v]\n        &&\n        tout[v] <= tout[u];\n}\n```

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

```cpp\nint p = lca(u, v);\n```

---

##### Lengths

```cpp\nint left =\n    dep[u] - dep[p];\n\nint right =\n    dep[v] - dep[p];\n```

---

##### Query

```cpp
int kth(int u,
        int v,
        int k)
{
    int p = lca(u, v);

    int left =
        dep[u] - dep[p];

    if (k <= left)
        return jump(u, k);

    k -= left;

    int right =
        dep[v] - dep[p];

    return jump(
        v,
        right - k
    );
}
```

##### Use

```
SPOJ QTREE2
```

---

### Length Of Path

```cpp\ndist(u, v)\n```

returns:

```
number of edges
```

---

### Number Of Nodes On Path

```cpp\ndist(u, v) + 1\n```

---

### Check If Node Lies On Path

```cpp\ndist(u, x)\n+\ndist(x, v)\n==\ndist(u, v)\n```

##### Complexity

```
O(log N)
```

---

### Find Parent

```cpp\nup[u][0]\n```

---

### Find Root Distance

```cpp\ndep[u]\n```

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

```cpp\nint p = lca(u, v);\n```

---

#### Distance

```cpp\ncout << dist(u, v);\n```

---

#### Parent

```cpp\ncout << up[u][0];\n```

---

#### Grand Parent

```cpp\ncout << up[u][1];\n```

---

#### Jump 10 Levels

```cpp\ncout << jump(u, 10);\n```

---

#### Same Depth

```cpp\nu = jump(\n    u, \n    dep[u] - dep[v]\n);\n```

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

```cpp\ndep[u]\n+\ndep[v]\n-\n2 * dep[lca(u, v)]\n```

---

#### Number Of Nodes

```cpp\ndist(u, v)+1\n```

---

#### Node On Path

```cpp\ndist(u, x)\n+\ndist(x, v)\n==\ndist(u, v)\n```

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

```cpp
vector<int> prefix_function(string s) {

    int n = s.size();

    vector<int> pi(n);

    for (int i = 1; i < n; i++) {

        int j = pi[i - 1];

        while (
            j > 0 &&
            s[i] != s[j]
        )
        {
            j = pi[j - 1];
        }

        if (s[i] == s[j])
            j++;

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

### Pattern Matching

Find all occurrences of:

```
pattern p

inside

text t
```

---

##### Build String

```cpp\nstring s =\n    p + "#" + t;\n```

---

##### Compute Prefix

```cpp\nauto pi =\n    prefix_function(s);\n```

---

##### Occurrences

```cpp\nvector<int> pos;\n\nint m = p.size();\n\nfor (int i = m + 1;\n     i < s.size();\n     i++)\n{\n    if (pi[i] == m)\n    {\n        pos.push_back(\n            i - 2 * m\n        );\n    }\n}\n```

##### Complexity

```
O(N + M)
```

---

### KMP Search Template

```cpp
vector<int> kmp(
    string t,
    string p
) {

    string s =
        p + "#" + t;

    auto pi =
        prefix_function(s);

    vector<int> pos;

    int m = p.size();

    for (int i = m + 1;
         i < s.size();
         i++)
    {
        if (pi[i] == m)
        {
            pos.push_back(
                i - 2 * m
            );
        }
    }

    return pos;
}
```

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

```cpp\nauto pi =\n    prefix_function(s);\n\ncout << pi.back();\n```

##### Complexity

```
O(N)
```

---

### All Borders

```cpp\nauto pi =\n    prefix_function(s);\n\nvector<int> borders;\n\nint cur = pi.back();\n\nwhile (cur > 0) {\n\n    borders.push_back(cur);\n\n    cur = pi[cur - 1];\n}\n```

##### Complexity

```
O(N)
```

---

### Count Occurrences Of Every Prefix

```cpp
auto pi =
    prefix_function(s);

vector<int> cnt(
    s.size() + 1
);

for (auto x : pi)
    cnt[x]++;

for (int i = s.size();
     i > 0;
     i--)
{
    cnt[
        pi[i - 1]
    ] += cnt[i];
}

for (int i = 0;
     i <= s.size();
     i++)
{
    cnt[i]++;
}
```

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

```cpp\nint n = s.size();\n\nauto pi =\n    prefix_function(s);\n\nint len =\n    n - pi.back();\n```

---

##### Check

```cpp\nif (n % len == 0)\n{\n    // periodic\n}\n```

---

### Smallest Period

```cpp\nint n = s.size();\n\nauto pi =\n    prefix_function(s);\n\nint len =\n    n - pi.back();\n\nif (n % len == 0)\n    cout << len;\nelse\n    cout << n;\n```

---

### Prefix Automaton Jump

```cpp\nj = pi[j - 1];\n```

##### Meaning

```
Go to next valid border
```

This is the whole magic of KMP.

---

### Distinct Prefix-Suffix Chain

```cpp\nint cur = pi.back();\n\nwhile (cur > 0) {\n\n    cout << cur << endl;\n\n    cur = pi[cur - 1];\n}\n```

##### Use

```
Borders Problems
```

---

### Useful Snippets

#### Prefix Array

```cpp\nauto pi =\n    prefix_function(s);\n```

---

#### Longest Border

```cpp\ncout << pi.back();\n```

---

#### Check Border Length K

```cpp\nif (pi.back() >= k)\n{\n}\n```

---

#### Number Of Occurrences

```cpp\nauto pos =\n    kmp(text, pattern);\n\ncout << pos.size();\n```

---

#### First Occurrence

```cpp\nif (!pos.empty())\n{\n    cout << pos[0];\n}\n```

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

```cpp\npi.back()\n```

---

#### Smallest Period

```cpp\nn - pi.back()\n```

---

#### Pattern Matching

```cpp\npattern + "#" + text\n```

---

#### Border Chain

```cpp\ncur = pi[cur - 1]\n```

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

```cpp
#define LNode(n) (2 * (n) + 1)
#define RNode(n) (2 * (n) + 2)
#define md(lx, rx) ((lx) + ((rx) - (lx)) / 2)

struct Node {

    int val;

    Node() {
        val = INF;
    }

    Node(int x) {
        val = x;
    }
};

struct SegTree {

    int tree_size;

    vector<Node> seg_data;

    SegTree(int n) {

        tree_size = 1;

        while (tree_size < n)
            tree_size *= 2;

        seg_data.resize(
            2 * tree_size
        );
    }

    Node merge(
        Node &a,
        Node &b
    ) {

        Node res;

        res.val =
            min(a.val, b.val);

        return res;
    }

    void init(
        vector<int> &nums,
        int ni,
        int lx,
        int rx
    ) {

        if (rx - lx == 1) {

            if (lx < nums.size())
                seg_data[ni] =
                    Node(nums[lx]);

            return;
        }

        init(
            nums,
            LNode(ni),
            lx,
            md(lx, rx)
        );

        init(
            nums,
            RNode(ni),
            md(lx, rx),
            rx
        );

        seg_data[ni] =
            merge(
                seg_data[LNode(ni)],
                seg_data[RNode(ni)]
            );
    }

    void init(
        vector<int> &nums
    ) {
        init(
            nums,
            0,
            0,
            tree_size
        );
    }

    void update(
        int idx,
        int val,
        int ni,
        int lx,
        int rx
    ) {

        if (rx - lx == 1) {

            seg_data[ni] =
                Node(val);

            return;
        }

        if (
            idx <
            md(lx, rx)
        )
        {
            update(
                idx,
                val,
                LNode(ni),
                lx,
                md(lx, rx)
            );
        }
        else {

            update(
                idx,
                val,
                RNode(ni),
                md(lx, rx),
                rx
            );
        }

        seg_data[ni] =
            merge(
                seg_data[LNode(ni)],
                seg_data[RNode(ni)]
            );
    }

    void update(
        int idx,
        int val
    ) {

        update(
            idx,
            val,
            0,
            0,
            tree_size
        );
    }

    Node query(
        int l,
        int r,
        int ni,
        int lx,
        int rx
    ) {

        if (
            lx >= r ||
            rx <= l
        )
        {
            return Node();
        }

        if (
            lx >= l &&
            rx <= r
        )
        {
            return seg_data[ni];
        }

        Node lf =
            query(
                l,
                r,
                LNode(ni),
                lx,
                md(lx, rx)
            );

        Node ri =
            query(
                l,
                r,
                RNode(ni),
                md(lx, rx),
                rx
            );

        return merge(
            lf,
            ri
        );
    }

    int query(
        int l,
        int r
    ) {

        return query(
            l,
            r,
            0,
            0,
            tree_size
        ).val;
    }
};
```

---

#### Common Modifications

##### Range Sum

```cpp\nres.val =\n    a.val + b.val;\n```

Identity:

```cpp\nval = 0;\n```

---

##### Range Maximum

```cpp\nres.val =\n    max(a.val, b.val);\n```

Identity:

```cpp\nval = -INF;\n```

---

##### Range GCD

```cpp\nres.val =\n    gcd(a.val, b.val);\n```

Identity:

```cpp\nval = 0;\n```

---

##### Range XOR

```cpp\nres.val =\n    a.val ^ b.val;\n```

Identity:

```cpp\nval = 0;\n```

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

        while (tree_size < n)
            tree_size *= 2;

        seg_data.resize(
            2 * tree_size
        );
    }

    Node merge(
        Node &a,
        Node &b
    ) {

        Node res;

        res.val =
            min(a.val, b.val);

        return res;
    }

    void init(
        vector<int> &nums,
        int ni,
        int lx,
        int rx
    ) {

        if (rx - lx == 1) {

            if (lx < nums.size())
                seg_data[ni] =
                    Node(nums[lx]);

            return;
        }

        init(
            nums,
            LNode(ni),
            lx,
            md(lx, rx)
        );

        init(
            nums,
            RNode(ni),
            md(lx, rx),
            rx
        );

        seg_data[ni] =
            merge(
                seg_data[LNode(ni)],
                seg_data[RNode(ni)]
            );
    }

    void init(
        vector<int> &nums
    ) {

        init(
            nums,
            0,
            0,
            tree_size
        );
    }

    void propagate(
        int ni,
        int lx,
        int rx
    ) {

        if (
            rx - lx == 1 ||
            !seg_data[ni].is_lazy
        )
            return;

        seg_data[
            LNode(ni)
        ].assign(
            seg_data[ni].lazy
        );

        seg_data[
            RNode(ni)
        ].assign(
            seg_data[ni].lazy
        );

        seg_data[ni].is_lazy = false;
    }

    void update(
        int l,
        int r,
        int val,
        int ni,
        int lx,
        int rx
    ) {

        propagate(
            ni,
            lx,
            rx
        );

        if (
            lx >= l &&
            rx <= r
        )
        {
            seg_data[ni]
                .assign(val);

            return;
        }

        if (
            lx >= r ||
            rx <= l
        )
        {
            return;
        }

        update(
            l,
            r,
            val,
            LNode(ni),
            lx,
            md(lx, rx)
        );

        update(
            l,
            r,
            val,
            RNode(ni),
            md(lx, rx),
            rx
        );

        seg_data[ni] =
            merge(
                seg_data[LNode(ni)],
                seg_data[RNode(ni)]
            );
    }

    void update(
        int l,
        int r,
        int val
    ) {

        update(
            l,
            r,
            val,
            0,
            0,
            tree_size
        );
    }

    Node query(
        int l,
        int r,
        int ni,
        int lx,
        int rx
    ) {

        propagate(
            ni,
            lx,
            rx
        );

        if (
            lx >= r ||
            rx <= l
        )
        {
            return Node();
        }

        if (
            lx >= l &&
            rx <= r
        )
        {
            return seg_data[ni];
        }

        Node lf =
            query(
                l,
                r,
                LNode(ni),
                lx,
                md(lx, rx)
            );

        Node ri =
            query(
                l,
                r,
                RNode(ni),
                md(lx, rx),
                rx
            );

        return merge(
            lf,
            ri
        );
    }

    int query(
        int l,
        int r
    ) {

        return query(
            l,
            r,
            0,
            0,
            tree_size
        ).val;
    }
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

```cpp
struct SparseTable {

    int n;

    vector<vector<int>> st;

    vector<int> lg;

    SparseTable() {}

    SparseTable(vector<int> &a) {

        build(a);
    }

    int merge(int a, int b) {

        return min(a, b);
    }

    void build(vector<int> &a) {

        n = a.size();

        lg.assign(n + 1, 0);

        for (int i = 2; i <= n; i++)
            lg[i] = lg[i / 2] + 1;

        int k = lg[n] + 1;

        st.assign(
            k,
            vector<int>(n)
        );

        st[0] = a;

        for (int j = 1; j < k; j++) {

            for (
                int i = 0;
                i + (1 << j) <= n;
                i++
            ) {

                st[j][i] =
                    merge(
                        st[j - 1][i],
                        st[j - 1]
                          [i + (1 << (j - 1))]
                    );
            }
        }
    }

    int query(int l, int r) {

        int k =
            lg[r - l + 1];

        return merge(
            st[k][l],
            st[k]
              [r - (1 << k) + 1]
        );
    }
};
```

---

#### Query

```cpp\nSparseTable sp(a);\n\ncout << sp.query(l, r);\n```

##### Complexity

```
O(1)
```

---

### Range Maximum Query

Change only:

```cpp\nint merge(int a, int b){\n\n    return max(a, b);\n}\n```

---

### Range GCD Query

Change only:

```cpp\nint merge(int a, int b){\n\n    return gcd(a, b);\n}\n```

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

```cpp\n#include <ext/pb_ds/assoc_container.hpp>\n#include <ext/pb_ds/tree_policy.hpp>\n\nusing namespace __gnu_pbds;\n```

---

#### Template

```cpp\ntemplate<typename T>\nusing ordered_set =\ntree<\n    T, \n    null_type, \n    less<T>, \n    rb_tree_tag, \n    tree_order_statistics_node_update\n>;\n```

---

#### Create

```cpp\nordered_set<int> st;\n```

---

#### Insert

```cpp\nst.insert(x);\n```

##### Complexity

```
O(log n)
```

---

#### Erase

```cpp\nst.erase(x);\n```

##### Complexity

```
O(log n)
```

---

#### Count Elements Smaller Than x

```cpp\nst.order_of_key(x);\n```

Example:

```cpp\nst.order_of_key(10);\n```

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

```cpp\n*st.find_by_order(k)\n```

Example:

```cpp\n*st.find_by_order(0)\n```

Returns:

```
smallest element
```

---

```cpp\n*st.find_by_order(1)\n```

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

```cpp\nst.size()\n```

---

#### Exists

```cpp\nst.find(x) != st.end()\n```

---

### Common Tricks

#### Count <= x

```cpp\nst.order_of_key(x + 1)\n```

---

#### Count > x

```cpp\nst.size()\n-\nst.order_of_key(x + 1)\n```

---

#### Count >= x

```cpp\nst.size()\n-\nst.order_of_key(x)\n```

---

### Ordered Multiset

Duplicates Allowed

```cpp\ntemplate<typename T>\nusing ordered_multiset =\ntree<\n    pair<T, int>, \n    null_type, \n    less<pair<T, int>>, \n    rb_tree_tag, \n    tree_order_statistics_node_update\n>;\n```

---

#### Insert Duplicate

```cpp\nms.insert({x, id});\n```

---

#### Erase One Occurrence

```cpp\nms.erase(\n    ms.lower_bound({x, 0})\n);\n```

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

```cpp\nset<int> st;\n```

---

#### Remove Segment

```cpp\nauto it = st.lower_bound(l);\n\nwhile(\n    it != st.end()\n    &&\n    *it <= r\n){\n    it = st.erase(it);\n}\n```

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

```cpp\nset<int> mex;\n```

---

#### Answer

```cpp\n*mex.begin()\n```

---

#### Update

Insert number:

```cpp\nfreq[x]++;\n\nif(freq[x] == 1)\n    mex.erase(x);\n```

Remove number:

```cpp\nfreq[x]--;\n\nif(freq[x] == 0)\n    mex.insert(x);\n```

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

```cpp\nmap<int, int> diff;\n```

instead of:

```cpp\nvector<int>\n```

---

#### Pattern

```cpp\ndiff[l]++;\n\ndiff[r+1]--;\n```

---

#### Sweep

```cpp\nint cur = 0;\n\nfor(auto [x, val] : diff){\n\n    cur += val;\n}\n```

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

```cpp\nfreq[x]\n```

and

```cpp\ncnt[f]\n```

where:

```
cnt[f]
=
how many numbers appear exactly f times
```

---

#### Update

```cpp\ncnt[freq[x]]--;\n\nfreq[x]++;\n\ncnt[freq[x]]++;\n```

---

#### Query

Check if frequency exists:

```cpp\ncnt[k] > 0\n```

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

```cpp\nerase(x)\n```

---

#### Solution

```cpp\npriority_queue<int> pq;\n\nmap<int, int> bad;\n```

Delete:

```cpp\nbad[x]++;\n```

---

#### Clean Top

```cpp\nwhile(\n !pq.empty()\n &&\n bad[pq.top()]\n){\n    bad[pq.top()]--;\n\n    pq.pop();\n}\n```

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

```cpp\nvector<int> comp;\n\nfor(auto x : a)\n    comp.push_back(x);\n\nfor(auto q : queries)\n    comp.push_back(q);\n```

---

```cpp\nsort(all(comp));\n\ncomp.erase(\n    unique(all(comp)), \n    comp.end()\n);\n```

---

#### Compress

```cpp\nid =\nlower_bound(\n    all(comp), \n    x\n)\n-\ncomp.begin();\n```

---

#### Recover

```cpp\ncomp[id]\n```

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

```cpp\nif(\n    a.size()\n    >\n    b.size()\n)\nswap(a, b);\n```

---

```cpp\nfor(auto x : a)\n    b.insert(x);\n```

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

```cpp
struct custom_hash {

    static uint64_t splitmix64(
        uint64_t x
    ) {

        x +=
        0x9e3779b97f4a7c15;

        x =
        (x ^ (x >> 30))
        * 0xbf58476d1ce4e5b9;

        x =
        (x ^ (x >> 27))
        * 0x94d049bb133111eb;

        return x ^ (x >> 31);
    }

    size_t operator()(
        uint64_t x
    ) const {

        static const uint64_t FIXED_RANDOM =
        chrono::steady_clock::
        now()
        .time_since_epoch()
        .count();

        return splitmix64(
            x + FIXED_RANDOM
        );
    }
};
```

---

#### Usage

```cpp\nunordered_map<\n    int, \n    int, \n    custom_hash\n> mp;\n```

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

```cpp\n*left.rbegin()\n```

---

#### Uses

```
Sliding Window Median

Running Median
```

---

### Order Statistics Trick

#### Count Inside Range

```cpp\nos.order_of_key(r + 1)\n-\nos.order_of_key(l)\n```

---

#### K-th Element

```cpp\n*os.find_by_order(k)\n```

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

```cpp\n*ms.rbegin()\n```

---

#### Minimum

```cpp\n*ms.begin()\n```

---

#### Window Difference

```cpp\n*ms.rbegin()\n-\n*ms.begin()\n```

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

```cpp\nauto it =\nst.lower_bound(x);\n```

Check:

```cpp\nit\n```

and

```cpp\nprev(it)\n```

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

```cpp\nint l = 0;\n\nfor(int r=0;r<n;r++){\n\n    add(a[r]);\n\n    while(!valid){\n\n        remove(a[l]);\n\n        l++;\n    }\n\n    ans =\n    max(\n        ans, \n        r-l+1\n    );\n}\n```

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

```cpp
int l = 0;

for(int r=0;r<n;r++){

    add(a[r]);

    while(valid){

        ans =
        min(
            ans,
            r-l+1
        );

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

```cpp\nans += r-l+1;\n```

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

```cpp\nmap<int, int> freq;\n\nint distinct;\n```

---

#### Add

```cpp\nif(++freq[x] == 1)\n    distinct++;\n```

---

#### Remove

```cpp\nif(--freq[x] == 0)\n    distinct--;\n```

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

```cpp\ncnt0\n\ncnt1\n```

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

```cpp\nvector<int> b = a;\n\nfor(auto x : a)\n    b.push_back(x);\n```

---

Then run:

```
Two Pointers
```

on:

```cpp\nb\n```

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

```cpp\nint l = 0;\n\nint r = n-1;\n```

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

```cpp\nwhile(l < r){\n\n    if(\n        a[l]+a[r]\n        == x\n    )\n    {\n        ...\n    }\n    else if (a[l]+a[r] < x) {\n        l++;\n    }\n    else{\n        r--;\n    }\n}\n```

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

```cpp\ni = 0;\n\nj = 0;\n```

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

```cpp\nint sum = 0;\n\nfor(int i=0;i<k;i++)\n    sum += a[i];\n\nfor(int r=k;r<n;r++){\n\n    sum += a[r];\n\n    sum -= a[r-k];\n\n}\n```

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

```cpp\nint l = 0;\n\nfor(int r=0;r<n;r++){\n\n    add(a[r]);\n\n    while(!valid){\n\n        remove(a[l]);\n\n        l++;\n    }\n}\n```

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

```cpp\nmap<int, int> freq;\n```

or

```cpp\nvector<int> freq;\n```

---

#### Add

```cpp\nfreq[x]++;\n```

---

#### Remove

```cpp\nfreq[x]--;\n```

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

```cpp\nint distinct;\n```

---

#### Add

```cpp\nif(++freq[x] == 1)\n    distinct++;\n```

---

#### Remove

```cpp\nif(--freq[x] == 0)\n    distinct--;\n```

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

```cpp\nans += r-l+1;\n```

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

```cpp\ndeque<int>\n```

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

```cpp\nmultiset\n```

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

```cpp\nfreq[x]\n```

and:

```cpp\nset<int> missing;\n```

---

Answer:

```cpp\n*missing.begin()\n```

---

#### Complexity

```
O(log n)
```

---

### Binary Array Window

#### State

```cpp\ncnt0\n\ncnt1\n```

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

```cpp\nvector<int> b = a;\n\nfor(auto x : a)\n    b.push_back(x);\n```

---

Run window on:

```cpp\nb\n```

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

```cpp\nwhile(...)\n```

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

```cpp\nvector<int> ans(n, -1); stack<int> st;\nfor(int i=n-1;i>=0;i--){\n    while(!st.empty() && a[st.top()]<=a[i]) st.pop();\n    if(!st.empty()) ans[i]=st.top();\n    st.push(i);\n}\n```

---

#### Complexity

```
O(n)
```

---

### Previous Greater Element

#### Pattern

```cpp\nfor(int i=0;i<n;i++){\n    while(!st.empty() && a[st.top()]<=a[i]) st.pop();\n    if(!st.empty()) ans[i]=st.top();\n    st.push(i);\n}\n```

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

```cpp\nr[i]-l[i]-1\n```

---

Area

```cpp\na[i] *\n(\n    r[i]-l[i]-1\n)\n```

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

```cpp\na[i]\n*\nleft\n*\nright\n```

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

```cpp\nans +=\na[i]\n*\nleft[i]\n*\nright[i];\n```

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

```cpp\nst.top() >= current\n```

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

```cpp\nst.top() <= current\n```

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

```cpp\nwhile(k && !st.empty() && st.back()>x){ st.pop_back(); k--; }\n```

---

Uses

```
Greedy + Stack
```

---

### Valid Parentheses

#### Pattern

```cpp\nstack<char> st;\n```

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

```cpp\nfor(int i=2*n-1;i>=0;i--)\n```

Use:

```cpp\na[i%n]\n```

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

```cpp\nmultiset\n```

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

```cpp
deque<int> dq;
for(int i=0;i<n;i++){
    while(!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
    dq.push_back(i);
    while(!dq.empty() && dq.front() <= i-k) dq.pop_front();
    if(i >= k-1) ans.push_back(a[dq.front()]);
}
```

---

#### Complexity

```
O(n)
```

---

### Sliding Window Minimum

#### Pattern

Replace:

```cpp\n<=\n```

with:

```cpp\n>=\n```

---

Answer:

```cpp\na[dq.front()]\n```

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

```cpp\na[dq.front()]\n```

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

```cpp\nmx - mn\n```

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

```cpp\ndp[i]\n=\nmax(\n    dp[j]\n)\n```

inside window.

---

Example

```cpp\ndp[i]\n=\nmax(\n    dp[j]\n)\n+\ncost\n```

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

```cpp\nwhile(!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();\n```

---

Answer

```cpp\na[dq.front()]\n```

---

### Minimum Queue

Pop:

```cpp\nwhile(!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();\n```

---

Answer

```cpp\na[dq.front()]\n```

---

### Circular Array Trick

Duplicate:

```cpp\nb = a;\n\nfor(auto x:a)\n    b.push_back(x);\n```

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

```cpp\ndq.front()\n```

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

```cpp\nint gcd(int a, int b){\n    return b?gcd(b, a%b):a;\n}\n```

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

```cpp\ngcd(a, b)=gcd(b, a%b)\n```

```cpp\ngcd(a, b)=gcd(a-b, b)\n```

```cpp\ngcd(a, b, c)=gcd(gcd(a, b), c)\n```

```cpp\ngcd(n, n+1)=1\n```

---

#### LCM

##### Function

```cpp\nint lcm(int a, int b){\n    return a/gcd(a, b)*b;\n}\n```

##### Complexity

```
O(log(min(a,b)))
```

##### Facts

```cpp\ngcd(a, b)*lcm(a, b)=a*b\n```

##### Warning

Bad

```cpp\na*b/gcd(a, b)\n```

Good

```cpp\na/gcd(a, b)*b\n```

---

#### Binary Power

##### Function

```cpp\nint power(int a, int b){\n\n    int res=1;\n\n    while(b){\n\n        if(b&1)\n            res*=a;\n\n        a*=a;\n        b>>=1;\n    }\n\n    return res;\n}\n```

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

```cpp\nint power(int a, int b, int mod){\n\n    int res=1;\n\n    while(b){\n\n        if(b&1)\n            res=1LL*res*a%mod;\n\n        a=1LL*a*a%mod;\n\n        b>>=1;\n    }\n\n    return res;\n}\n```

##### Complexity

```
O(log b)
```

---

### Extended Euclid

#### Function

```cpp
int exgcd(int a,int b,int &x,int &y){

    if(!b){

        x=1;
        y=0;

        return a;
    }

    int x1,y1;

    int g=exgcd(b,a%b,x1,y1);

    x=y1;
    y=x1-y1*(a/b);

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

### Modular Arithmetic

#### Normalize Mod

```cpp\nx%=mod;\n\nif(x<0)\n    x+=mod;\n```

---

#### Addition

```cpp\n(a+b)%mod\n```

---

#### Subtraction

```cpp\n((a-b)%mod+mod)%mod\n```

---

#### Multiplication

```cpp\n1LL*a*b%mod\n```

---

#### Division

```cpp\na*inv(b)%mod\n```

Never:

```cpp\na/b%mod\n```

---

### Modular Inverse

#### Fermat

##### Condition

```
mod must be prime
```

##### Function

```cpp\nint inv(int x){\n    return power(x, mod-2, mod);\n}\n```

##### Complexity

```
O(log mod)
```

---

#### Recursive Inverse

```cpp\nint inv(int x){\n    return x==1?1:\n    mod-1LL*(mod/x)*inv(mod%x)%mod;\n}\n```

##### Complexity

```
O(log mod)
```

---

#### Extended Euclid Inverse

##### Condition

```cpp\ngcd(a, m)==1\n```

##### Function

```cpp\nint inv(int a){\n\n    int x, y;\n\n    exgcd(a, mod, x, y);\n\n    return (x%mod+mod)%mod;\n}\n```

##### Works For

```
Non-prime mod
```

---

#### Generate All Inverses

```cpp\ninv[1]=1;\n\nfor(int i=2;i<=n;i++)\n    inv[i]=mod-(mod/i)*inv[mod%i]%mod;\n```

##### Complexity

```
O(n)
```

---

#### Facts

##### Inverse Exists iff

```cpp\ngcd(a, m)==1\n```

##### Product

```cpp\n(a*b)^-1\n=\na^-1*b^-1\n```

---

### Factorials

#### Build Factorial

```cpp\nfac[0]=1;\n\nfor(int i=1;i<=n;i++)\n    fac[i]=1LL*fac[i-1]*i%mod;\n```

##### Complexity

```
O(n)
```

---

#### Inverse Factorials

```cpp\ninvfac[n]=power(fac[n], mod-2);\n\nfor(int i=n;i>=1;i--)\n    invfac[i-1]=1LL*invfac[i]*i%mod;\n```

##### Complexity

```
O(n)
```

---

#### nCr

```cpp\nint C(int n, int r){\n\n    if(r<0||r>n)\n        return 0;\n\n    return 1LL*fac[n]*\n           invfac[r]%mod*\n           invfac[n-r]%mod;\n}\n```

##### Complexity

```
O(1)
```

---

### Legendre Formula

#### Power Of Prime Inside n!

```cpp\nint cnt(int n, int p){\n\n    int res=0;\n\n    while(n){\n\n        n/=p;\n        res+=n;\n    }\n\n    return res;\n}\n```

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

```cpp\ncnt(n, 5)\n```

##### Why?

```
2s are always more than 5s
```

---

#### Prime Exponent In nCr

```cpp\ncnt(n, p)\n-cnt(r, p)\n-cnt(n-r, p)\n```

---

#### Check m | n!

Factorize:

```cpp\nm=p1^a1*p2^a2...\n```

Check

```cpp\ncnt(n, pi)>=ai\n```

for every prime.

---

### Diophantine Equations

#### Equation

```
ax+by=c
```

---

#### Solution Exists iff

```cpp\nc%gcd(a, b)==0\n```

---

#### One Solution

From

```cpp\nax+by=g\n```

Multiply by

```cpp\nc/g\n```

---

#### General Solution

Let

```cpp\ng=gcd(a, b)\n```

Then

```cpp\nx=x0+k*(b/g)\n\ny=y0-k*(a/g)\n```

---

#### Positive Solutions

Move

```cpp\nk\n```

until

```cpp\nx>0\n\ny>0\n```

---

### Euler Phi

#### Function

```cpp
int phi(int n){

    int res=n;

    for(int i=2;i*i<=n;i++){

        if(n%i==0){

            while(n%i==0)
                n/=i;

            res-=res/i;
        }
    }

    if(n>1)
        res-=res/n;

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

```cpp\ngcd(x, n)==1\n```

---

#### Facts

##### Prime

```cpp\nphi(p)=p-1\n```

##### Prime Power

```cpp\nphi(p^k)=p^k-p^(k-1)\n```

##### Multiplicative

If

```cpp\ngcd(a, b)==1\n```

Then

```cpp\nphi(ab)=phi(a)*phi(b)\n```

##### Divisor Identity

```cpp\nΣ phi(d)=n\n```

over all divisors d of n.

---

#### Euler Theorem

If

```cpp\ngcd(a, m)==1\n```

Then

```cpp\na^phi(m)=1 mod m\n```

---

### Prime Testing

#### Trial Division

```cpp\nbool prime(int n){\n\n    if(n<2)\n        return false;\n\n    for(int i=2;i*i<=n;i++)\n        if(n%i==0)\n            return false;\n\n    return true;\n}\n```

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

```cpp
vector<int> lp(n+1);
vector<int> primes;

for(int i=2;i<=n;i++){

    if(!lp[i]){

        lp[i]=i;
        primes.push_back(i);
    }

    for(auto p:primes){

        if(p>lp[i]||i*p>n)
            break;

        lp[i*p]=p;
    }
}
```

##### Complexity

```
O(n)
```

##### Gives

```cpp\nlp[x]\n```

smallest prime factor.

---

### Prime Factorization

#### Using SPF

```cpp
vector<pair<int,int>> factor(int x){

    vector<pair<int,int>> res;

    while(x>1){

        int p=lp[x];

        int cnt=0;

        while(x%p==0){

            x/=p;
            cnt++;
        }

        res.push_back({p,cnt});
    }

    return res;
}
```

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

```cpp\nΠ(ai+1)\n```

---

#### Sum Of Divisors

```cpp\nΠ((p^(a+1)-1)/(p-1))\n```

---

#### Product Of Divisors

If

```cpp\nd=d(n)\n```

Then

```cpp\nn^(d/2)\n```

---

### Harmonic Lemma

#### Fact

Distinct values of

```cpp\nn/i\n```

are only

```
O(sqrt(n))
```

---

#### Loop

```cpp\nfor(int l=1, r;l<=n;l=r+1){\n\n    int k=n/l;\n\n    r=n/k;\n}\n```

##### Complexity

```
O(sqrt(n))
```

---

### Important Facts

#### Coprime

```cpp\ngcd(a, b)==1\n```

---

#### Consecutive Numbers

```cpp\ngcd(n, n+1)=1\n```

---

#### Count Multiples In [1,n]

```cpp\nn/x\n```

---

#### Count Multiples In [l,r]

```cpp\nr/x-(l-1)/x\n```

---

#### Distinct Prime Factors

Maximum for

```cpp\nn<=1e18\n```

is

```
15
```

---

#### Maximum Number Of Divisors

For

```cpp\nn<=1e18\n```

maximum is approximately

```
103680
```

---

#### Factorization Limits

```cpp\nsqrt(1e12)=1e6\n```

usually acceptable.

```cpp\nsqrt(1e18)=1e9\n```

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

```cpp
int solve(state){

    if(base_case)
        return answer;

    int &ret = dp[state];

    if(ret != -1)
        return ret;

    ret = initial_value;

    for(all_possible_choices){

        ret = combine(
            ret,
            solve(next_state)
        );
    }

    return ret;
}
```

---

### Complexity Formula

Always calculate:

```
Time = States × Transitions
```

Example:

```cpp\ndp[i][sum]\n```

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

```cpp\ndp[n]\n```

Transition:

```cpp\nf(n)=f(n-1)+f(n-2)\n```

```cpp
int solve(int n){

    if(n <= 1)
        return n;

    int &ret = dp[n];

    if(ret != -1)
        return ret;

    return ret =
           solve(n-1)
           +
           solve(n-2);
}
```

Complexity:

```
O(N)
```

---

### Tricks

##### Rolling Memory

Instead of:

```cpp\ndp[n]\n```

Use:

```cpp\na, b, c\n```

Memory:

```
O(1)
```

---

### Stair DP

State:

```cpp\ndp[i]\n```

Transition:

```cpp\ndp[i]=dp[i-1]+dp[i-2]\n```

Used in:

```
Ways
Counting
Paths
```

---

### Prefix DP

State:

```cpp\ndp[i]\n```

Meaning:

```
Answer for first i elements
```

Common form:

```cpp\ndp[i]=best(\n    dp[j]\n)\n```

where

```cpp\nj < i\n```

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

```cpp\n(i, rem)\n```

Meaning:

```
Current item
Remaining capacity
```

---

### Recursive

```cpp
int solve(
    int i,
    int rem
){

    if(i == n)
        return 0;

    int &ret =
    dp[i][rem];

    if(ret != -1)
        return ret;

    ret =
    solve(i+1,rem);

    if(rem >= w[i])
        ret = max(
            ret,
            val[i] +
            solve(
                i+1,
                rem-w[i]
            )
        );

    return ret;
}
```

---

### Iterative

```cpp\nfor(int i=0;i<n;i++){\n\n    for(int w=W;\n        w>=cost[i];\n        w--){\n\n        dp[w]=max(\n            dp[w], \n            dp[w-cost[i]]\n            + val[i]\n        );\n    }\n}\n```

---

### Important Tricks

##### Trick 1

Backward loop:

```cpp\nfor(w=W;w>=cost;w--)\n```

means

```
Take Once
```

---

##### Trick 2

Forward loop:

```cpp\nfor(w=cost;w<=W;w++)\n```

means

```
Take Infinite Times
```

---

##### Trick 3

Recover Solution

Store:

```cpp\npar[i][w]\n```

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

```cpp\ndp[value]\n=\nminimum weight\n```

---

Complexity:

```
O(NW)
```

---

### Subset Sum

State:

```cpp\n(i, sum)\n```

---

### Recursive

```cpp
bool solve(
    int i,
    int sum
){

    if(sum == target)
        return true;

    if(i == n)
        return false;

    int &ret =
    dp[i][sum];

    if(ret != -1)
        return ret;

    return ret =
           solve(i+1,sum)
           ||
           solve(
               i+1,
               sum+a[i]
           );
}
```

---

### Iterative

```cpp\ndp[0]=1;\n\nfor(auto x:a){\n\n    for(int s=S;\n        s>=x;\n        s--){\n\n        dp[s] |=\n        dp[s-x];\n    }\n}\n```

---

### Tricks

##### Count Solutions

Replace:

```cpp\nbool\n```

with

```cpp\nlong long\n```

---

##### Find One Solution

Store:

```cpp\ntake[i][sum]\n```

---

##### Bitset Optimization

```cpp\nbitset<MAX> bs;\n\nbs[0]=1;\n\nfor(auto x:a)\n    bs |= (bs<<x);\n```

Complexity:

```
O(N*S/64)
```

Huge optimization.

---

### Coin Change

---

### Count Ways

```cpp
ll solve(
    int i,
    int rem
){

    if(rem==0)
        return 1;

    if(i==n)
        return 0;

    ll &ret=
    dp[i][rem];

    if(ret!=-1)
        return ret;

    ret=
    solve(i+1,rem);

    if(rem>=coin[i])
        ret+=solve(
            i,
            rem-coin[i]
        );

    return ret;
}
```

---

### Tricks

##### Combination

```cpp\nsolve(i, ...)\n```

---

##### Permutation

```cpp\nsolve(0, ...)\n```

after choosing.

Very common trap.

---

### LCS

State:

```cpp\n(i, j)\n```

---

### Recursive

```cpp
int solve(
    int i,
    int j
){

    if(i==n || j==m)
        return 0;

    int &ret=
    dp[i][j];

    if(ret!=-1)
        return ret;

    if(a[i]==b[j])
        return ret=
               1+
               solve(i+1,j+1);

    return ret=
           max(
               solve(i+1,j),
               solve(i,j+1)
           );
}
```

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

```cpp\nn+m-LCS\n```

---

##### Edit Distance Relation

```
Insert/Delete only
```

Answer:

```cpp\nn+m-2*LCS\n```

---

Complexity:

```
O(NM)
```

---

### LIS

---

### O(N²)

```cpp\nfor(int i=0;i<n;i++){\n\n    dp[i]=1;\n\n    for(int j=0;j<i;j++){\n\n        if(a[j]<a[i])\n            dp[i]=max(\n                dp[i], \n                dp[j]+1\n            );\n    }\n}\n```

---

### O(N log N)

```cpp
vector<int> lis;

for(auto x:a){

    auto it=
    lower_bound(
        lis.begin(),
        lis.end(),
        x
    );

    if(it==lis.end())
        lis.push_back(x);

    else
        *it=x;
}
```

---

### Tricks

##### Strict LIS

```cpp\nlower_bound\n```

---

##### Non-Decreasing LIS

```cpp\nupper_bound\n```

---

##### Recover LIS

Store:

```cpp\nparent[]\n```

---

##### Count LIS

Need another DP.

---

### Grid DP

State:

```cpp\n(i, j)\n```

---

### Recursive

```cpp
ll solve(
    int i,
    int j
){

    if(i==n-1 &&
       j==m-1)
        return 1;

    if(i>=n ||
       j>=m)
        return 0;

    ll &ret=
    dp[i][j];

    if(ret!=-1)
        return ret;

    return ret=
           solve(i+1,j)
           +
           solve(i,j+1);
}
```

---

### Tricks

##### Obstacles

```cpp\nif(blocked)\n    return 0;\n```

---

##### Minimum Cost

Replace:

```cpp\n+\n```

with

```cpp\nmin(...)\n```

---

##### Maximum Cost

Use:

```cpp\nmax(...)\n```

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

```cpp\nu\n```

---

### Longest Path

```cpp
int solve(int u){

    int &ret=
    dp[u];

    if(ret!=-1)
        return ret;

    ret=0;

    for(auto v:adj[u]){

        ret=max(
            ret,
            1+solve(v)
        );
    }

    return ret;
}
```

---

### Tricks

##### Count Paths

```cpp\nret += solve(v);\n```

---

##### Longest Path

```cpp\nret=max(...)\n```

---

##### Shortest Path

```cpp\nret=min(...)\n```

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

```cpp\n(node, take)\n```

---

```cpp
int solve(
    int u,
    int take,
    int p
){

    int &ret=
    dp[u][take];

    if(ret!=-1)
        return ret;

    ret=take;

    for(auto v:adj[u]){

        if(v==p)
            continue;

        if(take)
            ret+=solve(
                v,0,u
            );

        else
            ret+=max(
                solve(v,0,u),
                solve(v,1,u)
            );
    }

    return ret;
}
```

---

### Tree DP Tricks

##### Subtree DP

```cpp\ndp[u]\n```

---

##### Rerooting

Need:

```cpp\ndp_down\ndp_up\n```

---

##### Diameter DP

Keep:

```cpp\nmx1\nmx2\n```

largest depths.

---

##### Tree Matching

State:

```cpp\n(u, take)\n```

common.

---

Complexity:

```
O(N)
```

---

### Range DP

State:

```cpp\n(l, r)\n```

---

### Recursive

```cpp
int solve(
    int l,
    int r
){

    if(l==r)
        return 0;

    int &ret=
    dp[l][r];

    if(ret!=-1)
        return ret;

    ret=INF;

    for(int k=l;k<r;k++){

        ret=min(
            ret,
            solve(l,k)
            +
            solve(k+1,r)
        );
    }

    return ret;
}
```

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

```cpp\nlen=1..n\n```

---

##### Partition Point

Usually:

```cpp\nfor(k=l;k<r;k++)\n```

---

##### Palindrome DP

State:

```cpp\ndp[l][r]\n```

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

```cpp
int solve(int mask){

    if(mask==
       (1<<n)-1)
        return 0;

    int &ret=
    dp[mask];

    if(ret!=-1)
        return ret;

    ret=INF;

    int pos=
    __builtin_popcount(mask);

    for(int i=0;i<n;i++){

        if(mask&(1<<i))
            continue;

        ret=min(
            ret,
            cost[pos][i]
            +
            solve(
                mask|(1<<i)
            )
        );
    }

    return ret;
}
```

---

### Bit Tricks

Check:

```cpp\nmask&(1<<i)\n```

Set:

```cpp\nmask|(1<<i)\n```

Remove:

```cpp\nmask^(1<<i)\n```

Count:

```cpp\n__builtin_popcount(mask)\n```

---

### Submask Enumeration

```cpp\nfor(\n    int sub=mask;\n    sub;\n    sub=(sub-1)&mask\n){\n}\n```

---

### Tricks

##### TSP

State:

```cpp\n(mask, last)\n```

---

##### Assignment

State:

```cpp\n(mask)\n```

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

```cpp\n(pos, tight, sum)\n```

---

### Template

```cpp
ll solve(
    int pos,
    int tight,
    int sum
){

    if(pos==
       num.size())
        return condition;

    ll &ret=
    dp[pos]
      [tight]
      [sum];

    if(!tight &&
       ret!=-1)
        return ret;

    ll ans=0;

    int mx=
    tight
    ? num[pos]-'0'
    : 9;

    for(int d=0;
        d<=mx;
        d++){

        ans+=solve(
            pos+1,
            tight &&
            d==mx,
            sum+d
        );
    }

    if(!tight)
        ret=ans;

    return ret;
}
```

---

### Most Important Digit DP Tricks

##### Count [L,R]

```cpp\nf(R)-f(L-1)\n```

Always.

---

##### Leading Zeros

Add state:

```cpp\nstarted\n```

```cpp\ndp[pos][tight][started]\n```

---

##### Divisibility

Add:

```cpp\nmod\n```

```cpp\ndp[pos][tight][mod]\n```

---

##### Digit Sum

Add:

```cpp\nsum\n```

---

##### Used Digits

Add:

```cpp\nmask\n```

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

```cpp\ndp[n][m]\n```

After:

```cpp\ndp[2][m]\n```

Memory:

```
O(M)
```

---

### State Compression

Before:

```cpp\ndp[i][j][k]\n```

After:

```cpp\ndp[j][k]\n```

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

```cpp
struct Fenwick {
    int n; vector<long long> bit;
    Fenwick(int n=0){ init(n); }
    void init(int n_){ n=n_; bit.assign(n+1,0); }
    void add(int idx,long long val){ for(;idx<=n;idx+=idx&-idx) bit[idx]+=val; }
    long long sumPrefix(int idx) const { long long r=0; for(;idx>0;idx-=idx&-idx) r+=bit[idx]; return r; }
    long long rangeSum(int l,int r) const { return sumPrefix(r)-sumPrefix(l-1); }
};
```

#### Complexity

- `add / prefix / range`: `O(log n)`

---

### SCC (Kosaraju)

```cpp
vector<vector<int>> g, rg;
vector<int> vis, order, comp;

void dfs1(int u){ vis[u]=1; for(int v:g[u]) if(!vis[v]) dfs1(v); order.push_back(u); }
void dfs2(int u,int c){ comp[u]=c; for(int v:rg[u]) if(comp[v]==-1) dfs2(v,c); }

int kosaraju(int n){
    vis.assign(n+1,0); order.clear();
    for(int i=1;i<=n;i++) if(!vis[i]) dfs1(i);
    comp.assign(n+1,-1);
    int scc=0;
    for(int i=n-1;i>=0;i--){
        int u=order[i];
        if(comp[u]==-1) dfs2(u, scc++);
    }
    return scc;
}
```

---

### 2-SAT (Implication Graph)

```cpp
struct TwoSAT {
    int n; vector<vector<int>> g, rg; vector<int> comp, order, vis, ans;
    TwoSAT(int n=0){ init(n); }
    void init(int n_){ n=n_; g.assign(2*n,{}); rg.assign(2*n,{}); }
    int id(int x,bool t){ return 2*x + (t?1:0); }
    void addImp(int u,int v){ g[u].push_back(v); rg[v].push_back(u); }
    void imply(int a,bool av,int b,bool bv){ addImp(id(a,av), id(b,bv)); }
    void either(int a,bool av,int b,bool bv){ imply(a,!av,b,bv); imply(b,!bv,a,av); }
    void forceVar(int a,bool av){ imply(a,!av,a,av); }
    void dfs1(int u){ vis[u]=1; for(int v:g[u]) if(!vis[v]) dfs1(v); order.push_back(u); }
    void dfs2(int u,int c){ comp[u]=c; for(int v:rg[u]) if(comp[v]==-1) dfs2(v,c); }
    bool satisfiable(){
        vis.assign(2*n,0); order.clear();
        for(int i=0;i<2*n;i++) if(!vis[i]) dfs1(i);
        comp.assign(2*n,-1); int c=0;
        for(int i=2*n-1;i>=0;i--) if(comp[order[i]]==-1) dfs2(order[i],c++);
        ans.assign(n,0);
        for(int i=0;i<n;i++){
            if(comp[id(i,false)]==comp[id(i,true)]) return false;
            ans[i] = comp[id(i,false)] < comp[id(i,true)];
        }
        return true;
    }
};
```

#### Note

- Build SCC on implication graph; variable `x` is true if `comp[id(x,true)] > comp[id(x,false)]`.

---

### Dinic (Max Flow)

```cpp
struct Dinic {
    struct E{ int to, rev; long long cap; };
    int n; vector<vector<E>> g; vector<int> lvl, it;
    Dinic(int n=0){ init(n); }
    void init(int n_){ n=n_; g.assign(n,{}); }
    void addEdge(int u,int v,long long c){
        E a{v,(int)g[v].size(),c}, b{u,(int)g[u].size(),0};
        g[u].push_back(a); g[v].push_back(b);
    }
    bool bfs(int s,int t){
        lvl.assign(n,-1); queue<int> q; q.push(s); lvl[s]=0;
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(auto &e:g[u]) if(e.cap>0 && lvl[e.to]==-1) lvl[e.to]=lvl[u]+1, q.push(e.to);
        }
        return lvl[t]!=-1;
    }
    long long dfs(int u,int t,long long f){
        if(!f || u==t) return f;
        for(int &i=it[u]; i<(int)g[u].size(); i++){
            E &e=g[u][i];
            if(lvl[e.to]!=lvl[u]+1 || e.cap==0) continue;
            long long got=dfs(e.to,t,min(f,e.cap));
            if(!got) continue;
            e.cap-=got; g[e.to][e.rev].cap+=got;
            return got;
        }
        return 0;
    }
    long long maxflow(int s,int t){
        long long flow=0;
        while(bfs(s,t)){
            it.assign(n,0);
            while(long long pushed=dfs(s,t,(long long)4e18)) flow+=pushed;
        }
        return flow;
    }
};
```

#### Note

- Use level graph BFS + blocking flow DFS.

---

### Trie (Lowercase)

```cpp
struct Trie {
    struct Node { int nxt[26]; bool end=false; Node(){ memset(nxt,-1,sizeof(nxt)); } };
    vector<Node> t{Node()};
    void add(const string& s){ int u=0; for(char c:s){ int x=c-'a'; if(t[u].nxt[x]==-1){ t[u].nxt[x]=t.size(); t.push_back(Node()); } u=t[u].nxt[x]; } t[u].end=true; }
    bool has(const string& s) const { int u=0; for(char c:s){ int x=c-'a'; if(t[u].nxt[x]==-1) return false; u=t[u].nxt[x]; } return t[u].end; }
};
```

---

### Aho-Corasick (Pattern Matching)

```cpp
struct Aho {
    struct Node { int nxt[26], link=0, out=0; Node(){ memset(nxt,-1,sizeof(nxt)); } };
    vector<Node> t{Node()};
    void add(const string& s){ int u=0; for(char c:s){ int x=c-'a'; if(t[u].nxt[x]==-1){ t[u].nxt[x]=t.size(); t.push_back(Node()); } u=t[u].nxt[x]; } t[u].out++; }
    void build(){
        queue<int> q;
        for(int c=0;c<26;c++){
            int v=t[0].nxt[c];
            if(v==-1) t[0].nxt[c]=0;
            else q.push(v);
        }
        while(!q.empty()){
            int u=q.front(); q.pop();
            t[u].out += t[t[u].link].out;
            for(int c=0;c<26;c++){
                int v=t[u].nxt[c];
                if(v==-1) t[u].nxt[c]=t[t[u].link].nxt[c];
                else t[v].link=t[t[u].link].nxt[c], q.push(v);
            }
        }
    }
    int countMatches(const string& s){ int u=0, ans=0; for(char c:s){ u=t[u].nxt[c-'a']; ans+=t[u].out; } return ans; }
};
```

---

### Heavy-Light Decomposition (HLD)

```cpp
vector<vector<int>> g;
vector<int> parent, depth, heavy, head, pos, sz;
int timer=0;

int dfs_sz(int u,int p){
    parent[u]=p; sz[u]=1; int mx=0;
    for(int v:g[u]) if(v!=p){
        depth[v]=depth[u]+1;
        int s=dfs_sz(v,u); sz[u]+=s;
        if(s>mx) mx=s, heavy[u]=v;
    }
    return sz[u];
}

void dfs_hld(int u,int h){
    head[u]=h; pos[u]=++timer;
    if(heavy[u]!=-1) dfs_hld(heavy[u],h);
    for(int v:g[u]) if(v!=parent[u] && v!=heavy[u]) dfs_hld(v,v);
}

vector<pair<int,int>> path_segments(int u,int v){
    vector<pair<int,int>> segs;
    while(head[u]!=head[v]){
        if(depth[head[u]]<depth[head[v]]) swap(u,v);
        segs.push_back({pos[head[u]], pos[u]});
        u=parent[head[u]];
    }
    if(depth[u]>depth[v]) swap(u,v);
    segs.push_back({pos[u], pos[v]});
    return segs;
}
```

---

### Mo's Algorithm

```cpp
struct Query { int l, r, idx; };
int B;
bool operator<(const Query& a, const Query& b){
    int A=a.l/B, C=b.l/B;
    if(A!=C) return A<C;
    return (A&1)? a.r>b.r : a.r<b.r;
}
// Maintain current [L,R] with add(pos)/remove(pos), store answers by original idx.
```

---

### Meet in the Middle

```cpp
long long bestSubsetSumLE(const vector<long long>& a, long long S){
    int n=a.size(), m=n/2;
    vector<long long> L, R;
    for(int mask=0; mask<(1<<m); mask++){
        long long s=0; for(int i=0;i<m;i++) if(mask>>i&1) s+=a[i];
        if(s<=S) L.push_back(s);
    }
    for(int mask=0; mask<(1<<(n-m)); mask++){
        long long s=0; for(int i=0;i<n-m;i++) if(mask>>i&1) s+=a[m+i];
        if(s<=S) R.push_back(s);
    }
    sort(R.begin(), R.end());
    long long ans=0;
    for(long long x:L){
        auto it=upper_bound(R.begin(), R.end(), S-x);
        if(it!=R.begin()) ans=max(ans, x+*prev(it));
    }
    return ans;
}
```

## 10) Comprehensive Missing Tricks & Function Ideas

### Foundations & Utilities: extra useful functions

```cpp
template<class T> bool chmin(T& a,const T& b){ if(b<a){ a=b; return true; } return false; }
template<class T> bool chmax(T& a,const T& b){ if(b>a){ a=b; return true; } return false; }
long long mod_pow(long long a,long long e,long long mod){ long long r=1%mod; a%=mod; while(e){ if(e&1) r=r*a%mod; a=a*a%mod; e>>=1; } return r; }
long long ceil_div(long long a,long long b){ if(b<0) a=-a,b=-b; return a>=0 ? (a+b-1)/b : a/b; }
long long floor_div(long long a,long long b){ if(b<0) a=-a,b=-b; return a>=0 ? a/b : -(( -a + b - 1)/b); }
```

#### Extra ideas

- Coordinate-compress pairs/tuples when a value alone is not enough.
- Prefer `long long` in weighted/DP transitions by default.
- Keep one reusable `restore_path(par, target)` helper for graph and DP reconstructions.

---

### Graphs: missed patterns and tricks

```cpp
// Multi-test graph reset trick:
// vector<vector<int>> adj(n+1); vector<int> vis(n+1,0);
// Recreate per test instead of manual clear loops on huge static arrays.

// Edge index trick for undirected graph with parent edge:
// store edges as pairs (to, id), and skip only parent edge id in DFS.
```

```cpp
// Bridge / articulation skeleton (Tarjan low-link)
vector<vector<pair<int,int>>> g;
vector<int> tin, low, isCut; vector<pair<int,int>> bridges; int timerDFS=0;
void dfsBridge(int u,int pe=-1){
    tin[u]=low[u]=++timerDFS; int children=0;
    for(auto [v,id]:g[u]) if(id!=pe){
        if(tin[v]) low[u]=min(low[u],tin[v]);
        else {
            dfsBridge(v,id); low[u]=min(low[u],low[v]); children++;
            if(low[v]>tin[u]) bridges.push_back({u,v});
            if(pe!=-1 && low[v]>=tin[u]) isCut[u]=1;
        }
    }
    if(pe==-1 && children>1) isCut[u]=1;
}
```

#### Common graph problem recognition

- **Shortest path + 0/1 edges** → 0-1 BFS.
- **Topological order + DAG transitions** → DAG DP.
- **Connectivity under edge additions** → DSU.
- **Offline connectivity with removals** → reverse process + DSU.
- **Constraints of form `x - y <= c`** → Bellman-Ford / SPFA model.

---

### Trees: missed ideas

```cpp
// Rerooting DP pattern:
// 1) dfs_down(u,p): compute contribution inside subtree.
// 2) dfs_up(u,p,fromParent): reroot transition to children.
// This solves sum of distances, max distance to any node, etc.
```

```cpp
// Binary lifting helper: kth node on path(u,v)
int kth_on_path(int u,int v,int k,
                function<int(int,int)> lca,
                function<int(int,int)> jump,
                const vector<int>& depth){
    int w=lca(u,v);
    int left=depth[u]-depth[w]+1;
    if(k<=left) return jump(u,k-1);
    int right=depth[v]-depth[w];
    int need=left+right-k;
    return jump(v,need);
}
```

---

### Strings: missed functions and patterns

```cpp
vector<int> z_function(const string& s){
    int n=s.size(); vector<int> z(n); int l=0,r=0;
    for(int i=1;i<n;i++){
        if(i<=r) z[i]=min(r-i+1,z[i-l]);
        while(i+z[i]<n && s[z[i]]==s[i+z[i]]) z[i]++;
        if(i+z[i]-1>r) l=i,r=i+z[i]-1;
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

### Data Structures (DS): missed important functions

```cpp
struct FenwickRange {
    int n; vector<long long> b1,b2;
    FenwickRange(int n=0){ init(n); }
    void init(int n_){ n=n_; b1.assign(n+1,0); b2.assign(n+1,0); }
    void add(vector<long long>& b,int i,long long v){ for(;i<=n;i+=i&-i) b[i]+=v; }
    long long sum(const vector<long long>& b,int i) const { long long r=0; for(;i>0;i-=i&-i) r+=b[i]; return r; }
    void range_add(int l,int r,long long v){ add(b1,l,v); add(b1,r+1,-v); add(b2,l,v*(l-1)); add(b2,r+1,-v*r); }
    long long pref(int i) const { return sum(b1,i)*i - sum(b2,i); }
    long long range_sum(int l,int r) const { return pref(r)-pref(l-1); }
};
```

```cpp\n// DSU rollback idea (for offline dynamic connectivity):\n// keep stack of parent/size changes, no path compression, union by size only, rollback to checkpoint.\n```

#### DS problem-type checklist

- Point update + prefix/range sum → Fenwick.
- Range update + range query → lazy segtree or two-BIT trick.
- Static idempotent range query (min/gcd/max) → sparse table.
- Order statistics with updates → PBDS / segtree over compressed values.

---

### Number Theory (NS): missed functions and ideas

```cpp
long long ext_gcd(long long a,long long b,long long& x,long long& y){
    if(!b){ x=1; y=0; return a; }
    long long x1,y1,g=ext_gcd(b,a%b,x1,y1);
    x=y1; y=x1-(a/b)*y1; return g;
}

// Solve a*x + b*y = c
bool diophantine(long long a,long long b,long long c,long long& x,long long& y){
    long long g=ext_gcd(abs(a),abs(b),x,y);
    if(c%g) return false;
    x*=c/g; y*=c/g;
    if(a<0) x=-x; if(b<0) y=-y;
    return true;
}
```

```cpp\n// CRT merge (x ≡ a1 mod m1, x ≡ a2 mod m2) can be built using ext_gcd.\n// Keep answer modulo lcm(m1, m2) and check consistency by gcd divisibility.\n```

#### Number theory recognition

- Congruence system with multiple mods → CRT.
- Huge exponent with mod prime/composite → Euler/Fermat + fast power.
- Frequent factorization queries up to N → SPF sieve.

---

### Dynamic Programming (DP): missed important patterns

```cpp
// Reconstruction helper (1D choice DP)
vector<int> restore_choice(int target,const vector<int>& from){
    vector<int> pick;
    while(target!=-1 && from[target]!=-1){
        pick.push_back(target-from[target]);
        target=from[target];
    }
    reverse(pick.begin(),pick.end());
    return pick;
}
```

```cpp\n// Bitset knapsack idea:\n// bitset<MAXS+1> bs; bs[0]=1;\n// for(int w:weights) bs |= (bs<<w);\n// reachable sum queries in O(N*MAXS/word_size).\n```

```cpp\n// Divide & Conquer DP optimization condition:\n// dp[i][j] = min_{k<j}(dp[i-1][k] + cost(k+1, j))\n// with monotone opt: opt[i][j] <= opt[i][j+1].\n```

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

```cpp
// read/set/clear/toggle bit i (0-indexed)
bool getBit(long long x,int i){ return (x>>i)&1LL; }
long long setBit(long long x,int i){ return x | (1LL<<i); }
long long clearBit(long long x,int i){ return x & ~(1LL<<i); }
long long toggleBit(long long x,int i){ return x ^ (1LL<<i); }

// lowbit and common predicates
long long lowbit(long long x){ return x & -x; }
bool isPowerOfTwo(long long x){ return x>0 && (x&(x-1))==0; }
```

```cpp
// builtins (GCC/Clang)
int cnt1(unsigned int x){ return __builtin_popcount(x); }
int cnt1ll(unsigned long long x){ return __builtin_popcountll(x); }
int lsbIndex(unsigned int x){ return __builtin_ctz(x); }      // x != 0
int msbIndex(unsigned int x){ return 31 - __builtin_clz(x); } // x != 0
int parity(unsigned int x){ return __builtin_parity(x); }     // 1 if odd count of bits
```

#### Notes

- Use unsigned shifts for bit-heavy logic to avoid sign issues.
- For 64-bit masks, always shift with `1LL << i`.
- `x & (x-1)` removes the lowest set bit.

---

### Submask / Supmask Iteration Tricks

```cpp
// iterate all submasks of mask
for (int sub = mask; ; sub = (sub - 1) & mask) {
    // use sub
    if (sub == 0) break;
}

// iterate all masks of n bits
for (int mask = 0; mask < (1 << n); mask++) {
    // use mask
}
```

```cpp\n// iterate set bits of mask in O(number_of_set_bits)\nfor (int m = mask; m; m &= (m - 1)) {\n    int b = __builtin_ctz(m);\n    // bit b is set\n}\n```

#### Use Cases

- Subset DP transitions.
- Meet-in-the-middle state filtering.
- Inclusion-exclusion over selected features.

---

### Important Bit Tricks

```cpp
// next combination with same popcount (Gosper's hack), x > 0
unsigned int nextComb(unsigned int x){
    unsigned int c = x & -x;
    unsigned int r = x + c;
    return (((r ^ x) >> 2) / c) | r;
}
```

```cpp\n// compress coordinates into bit positions and store chosen values in a mask\n// when n <= 20..24, brute force on masks can be feasible with pruning\n```

```cpp\n// XOR swap trick exists but DO NOT use in CP production; prefer std::swap.\n```

#### Problem Recognition

- `n <= 20` and "choose subset" → bitmask brute force / DP.
- Need to count enabled features fast → popcount.
- Need nearest differing state by one element → toggle one bit.

---

### Bitmask DP Starter Patterns

```cpp
// TSP-style DP: dp[mask][last]
const long long BIG = (long long)4e18;
vector<vector<long long>> dp(1<<n, vector<long long>(n, BIG));
for(int s=0;s<n;s++) dp[1<<s][s]=0;
for(int mask=0; mask<(1<<n); mask++){
    for(int u=0; u<n; u++) if((mask>>u)&1){
        if(dp[mask][u]==BIG) continue;
        for(int v=0; v<n; v++) if(((mask>>v)&1)==0){
            int nmask = mask | (1<<v);
            dp[nmask][v] = min(dp[nmask][v], dp[mask][u] + cost[u][v]);
        }
    }
}
```

```cpp\n// SOS DP (sum over subsets) idea:\n// for(int i=0;i<n;i++) for(int mask=0;mask<(1<<n);mask++)\n//   if(mask&(1<<i)) f[mask]+=f[mask^(1<<i)];\n```

#### Complexity

- Bitmask DP over subsets: usually `O(n * 2^n)` or `O(n^2 * 2^n)`.
- SOS DP: `O(n * 2^n)`.

---

### std::bitset: How To Use

```cpp
const int MAXN = 200005;
bitset<MAXN> bs;

bs.set(5);         // set bit 5
bs.reset(5);       // clear bit 5
bs.flip(5);        // toggle bit 5
bs[10] = 1;        // direct access

int ones = (int)bs.count();
bool any = bs.any();
bool none = bs.none();

bitset<MAXN> a, b;
a |= b; a &= b; a ^= b;
a <<= 3; a >>= 2;
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

### XOR Basis (Linear Basis) – important bit module

```cpp
struct XorBasis {
    static const int LOG = 60;
    long long b[LOG]{};

    void add(long long x){
        for(int i=LOG-1;i>=0;i--){
            if(((x>>i)&1)==0) continue;
            if(!b[i]){ b[i]=x; return; }
            x ^= b[i];
        }
    }

    bool canMake(long long x) const {
        for(int i=LOG-1;i>=0;i--) if((x^b[i])<x) x^=b[i];
        return x==0;
    }

    long long maxXor(long long x=0) const {
        for(int i=LOG-1;i>=0;i--) x=max(x, x^b[i]);
        return x;
    }
};
```

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




