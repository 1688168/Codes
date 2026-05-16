# DSU — Disjoint Set Union (Union-Find)

---

## 🔑 Core Purpose

> Efficiently **maintain connectivity** among elements under repeated merges.

---

## ⚡ Core Operations (the “superpowers”)

- **Union(a, b)** → merge the groups of `a` and `b`  
- **Find(x)** → return the representative (root) of `x`’s group  
  → used to check: `find(a) == find(b)`

---

## 🧠 Mental Model (When to Use DSU)

Ask yourself:

- **Am I grouping things into components?**
- **Do I care about connectivity, not paths?**
  - Need path → DFS/BFS  
  - Need only “connected or not” → DSU
- **Are unions happening repeatedly (possibly over time)?**
  - You want to update connectivity **without recomputing from scratch**

---

## 🔍 Key Intuition

> DSU = **lazy graph traversal + cached connectivity**

- DFS/BFS → recompute structure every time  
- DSU → **incrementally builds and remembers structure**

---

## 🚩 Common Use Cases

### 1. Grouping / Connected Components
- Number of connected components  
- Friend circles / provinces  
- “Is everything connected?”

---

### 2. Repeated Connectivity Queries
- “Are x and y connected?”
- Many queries → DSU avoids repeated traversal

---

### 3. Dynamic / Incremental Edge Addition
- Edges added over time  
- Need fast updates + queries

---

### 4. Implicit Graphs
- Matrix input (like connectivity matrix)
- Edge list processed step-by-step

---

## ⚙️ Performance Optimization

### Path Compression (key idea)

> “Every time I look something up, I make it faster next time.”

- Flattens the tree during `find()`
- Turns long chains into near-direct links to root

---

### Time Complexity

- Without optimization → up to **O(N)** per operation  
- With path compression (+ union by rank/size) →  
  → **~O(1) amortized** (technically inverse Ackermann)

---

## 🧠 Clean Summary

> DSU is a data structure for:
- Maintaining **disjoint groups**
- Supporting fast **merge + connectivity queries**
- Avoiding repeated graph traversals

---

## ⚡ One-line Trigger (for interviews)

> “If I only care about connectivity and there are repeated unions/queries → use DSU.”