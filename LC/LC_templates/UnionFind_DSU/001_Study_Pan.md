# Union Find (DSU) Study Plan

The goal is to learn these ideas in order:

1. Basic DSU implementation  
2. Connected components  
3. Grid modeling  
4. Cycle detection  
5. Component grouping  
6. Dynamic connectivity  
7. Weighted/offline union  
8. Reverse union tricks  
9. DSU + sorting  
10. Advanced DSU intuition

---
# Union Find (DSU) Study Plan

The goal is to learn these ideas in order:

1. Basic DSU implementation  
2. Connected components  
3. Grid modeling  
4. Cycle detection  
5. Component grouping  
6. Dynamic connectivity  
7. Weighted/offline union  
8. Reverse union tricks  
9. DSU + sorting  
10. Advanced DSU intuition

---

# Phase 1 — Learn the Core DSU Pattern

## 1. 547. Number of Provinces
Difficulty: Easy-Medium

### Learn
- Basic DSU template
- `find()`
- `union()`
- Path compression
- Connected components

### Why first
This is the cleanest “people in groups” DSU problem.

You should memorize:
- `parent[]`
- `rank/size[]`
- component counting

---

## 2. 684. Redundant Connection
Difficulty: Medium

### Learn
- DSU for cycle detection
- If two nodes already have same root → adding edge creates cycle

### Core insight

```python
if find(u) == find(v):
    return [u, v]

union(u, v)
```

This is one of the most important DSU patterns.

---

# Phase 2 — Grid Connectivity

## 3. 200. Number of Islands
Difficulty: Medium

### Learn
- Convert 2D grid → graph
- Mapping:

```python
id = r * cols + c
```

### Important
Even though DFS is easier here, solving it with DSU teaches:
- grid unions
- neighbor unions
- component counting

---

## 4. 947. Most Stones Removed with Same Row or Column
Difficulty: Medium+

### Learn
- Bipartite-style DSU modeling
- Rows and columns as nodes

### Big insight
Instead of connecting stones directly:
- connect row node ↔ column node

This is where Union Find starts becoming “creative modeling.”

---

# Phase 3 — DSU as Grouping Engine

## 5. 721. Accounts Merge
Difficulty: Medium+

### Learn
- DSU on strings/emails
- HashMap + DSU
- Group reconstruction after unions

### Important pattern
Union first, reconstruct later:

```python
groups[root].append(email)
```

Very common in interviews.

---

## 6. 1202. Smallest String With Swaps
Difficulty: Medium+

### Learn
- DSU + connected component processing
- Sorting within components

### Key insight
Indices in same component can permute freely.

This teaches:
> “Union Find identifies freedom of movement.”

That idea appears everywhere later.

---

# Phase 4 — Dynamic Connectivity

## 7. 305. Number of Islands II
Difficulty: Hard-

### Learn
- Online DSU
- Dynamically adding nodes
- Incremental connectivity

### Important
This is the first “real DSU hard problem.”

You learn:
- activate cells
- merge neighbors
- maintain island count dynamically

Huge interview value.

---

# Phase 5 — Offline / Reverse Union Tricks

## 8. 803. Bricks Falling When Hit
Difficulty: Hard

### Learn
- Reverse processing
- DSU with “virtual roof”
- Component sizes

### Major concept
Instead of deleting bricks:
- process hits backwards
- add bricks back

This is one of the most famous DSU tricks.

If you understand this deeply, your DSU level jumps.

---

# Phase 6 — Union by Sorted Order

## 9. 1697. Checking Existence of Edge Length Limited Paths
Difficulty: Hard-

### Learn
- Offline queries
- Sort edges by weight
- Process queries in order

### Huge pattern
This teaches:
> “Union edges gradually while answering queries.”

This idea appears in:
- MST
- Kruskal
- threshold connectivity
- many hard graph problems

Extremely important.

---

# Phase 7 — Advanced DSU Intuition

## 10. 2421. Number of Good Paths
Difficulty: Hard

### Learn
- DSU + value ordering
- Component aggregation
- Advanced counting

### Why final
This problem forces you to truly understand:
- why unions happen in an order
- what information components store
- how DSU combines with sorting

This is “advanced interview DSU.”

---

# Recommended Study Order

| Stage | Problem | Main Idea |
|---|---|---|
| 1 | 547 | Basic DSU |
| 2 | 684 | Cycle detection |
| 3 | 200 | Grid unions |
| 4 | 947 | Creative node modeling |
| 5 | 721 | Group reconstruction |
| 6 | 1202 | Component processing |
| 7 | 305 | Dynamic connectivity |
| 8 | 803 | Reverse union |
| 9 | 1697 | Offline sorted union |
| 10 | 2421 | Advanced DSU |

---

# What You Should Master

By the end, you should instantly recognize:

| Pattern | Example |
|---|---|
| Connected components | 547 |
| Cycle detection | 684 |
| Grid DSU | 200 |
| Row/column modeling | 947 |
| String grouping | 721 |
| Permutation freedom | 1202 |
| Dynamic union | 305 |
| Reverse processing | 803 |
| Offline sorted queries | 1697 |
| Ordered unions + counting | 2421 |

---

# DSU Template You Should Memorize

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

        return True
```

You should become completely fluent with:
- why path compression works
- why union by size/rank matters
- amortized near-O(1) complexity

The core complexity is essentially:

```text
O(α(n))
```

where α(n) is the inverse Ackermann function.

---

# After These 10

## MST / Kruskal
- 1584. Min Cost to Connect All Points
- 1489. Find Critical and Pseudo-Critical Edges in MST

## Prime-factor DSU
- 952. Largest Component Size by Common Factor
- 2709. Greatest Common Divisor Traversal

## Really hard DSU
- 2157. Groups of Strings
- 1632. Rank Transform of a Matrix

These are where DSU becomes genuinely difficult/creative.