# LeetCode 947: Mental Model for the O(n) DFS Graph

## 1. Translate the removal rule into connectivity

Each stone is a graph node. Two stones are related when they share a row or column.

A connected component can be reduced to one remaining stone, so:

```text
Maximum removals = number of stones − number of connected components
```

DFS discovers those components.

## 2. Both graph versions use stone indices as nodes

```python
stones[i]  # Coordinates of stone i
graph[i]   # Neighbor indices of stone i
```

The row and column maps help find related stones. Their coordinates are not the graph’s node IDs.

## 3. Start with the obvious O(n²) construction

Compare every pair of stones. If they share a row or column, add an undirected edge:

```python
graph[i].append(j)
graph[j].append(i)
```

This takes O(n²) time because it checks every pair, even when few edges exist.

## 4. Ask what information DFS actually needs

DFS needs to know **which stones can reach each other**.

It does not need a direct edge between every related pair.

For three stones sharing a row, the pairwise graph contains:

```text
A–B, A–C, B–C
```

We can omit `B–C` because B can still reach C:

```text
B → A → C
```

That edge is **redundant for connectivity**: removing it does not change the connected components.

## 5. Connect each group through one representative

Group stone indices by row and column:

```python
row_map[row].append(i)
col_map[col].append(i)
```

For each group, choose its first stone and connect every other stone to it:

```python
def connect_group(indices):
    first = indices[0]

    for other in indices[1:]:
        graph[first].append(other)
        graph[other].append(first)
```

For `indices = [2, 5, 7, 9]`, this creates:

```text
    5
    |
7 — 2 — 9
```

We skip edges between 5, 7, and 9 because they can reach each other through 2.

**A group of k stones needs only k − 1 edges to stay connected.**

## 6. Why both directions matter

```python
graph[first].append(other)
graph[other].append(first)
```

These entries represent one undirected edge.

DFS might enter the group through any stone—for example, through a column connection. Every stone must be able to reach the representative, and the representative must be able to reach every stone.

## 7. Why the construction is O(n)

Each stone belongs to exactly:

- One row group.
- One column group.

Across all row groups, the total number of stones processed is n. The same holds for column groups. Connecting each group through a representative adds at most a linear number of edges.

Therefore, graph construction and DFS both take **O(n) average time**, with **O(n) space**.

The combined row and column graph may still contain cycles. That is fine: we need a linear number of edges, not a graph with absolutely no redundant edges. `visited` handles cycles.

## 8. Count versus removal sequence

For the original problem, DFS only counts components:

```python
return n - components
```

For the follow-up, choose any root per component and record non-root stones in DFS postorder. Children are removed before parents, so each removed stone still has its parent present.

## The idea to remember

**Preserve reachability, not every direct connection.**

When many nodes belong to the same group, connect them through one representative. Before adding all pairwise edges, ask:

> Does my answer require direct connections, or does it only require these nodes to remain reachable from one another?