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