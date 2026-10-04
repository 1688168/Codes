# LeetCode 947 Follow-Up: Return Removal Sequence

## Follow-Up Question

Instead of returning the maximum number of removable stones, return an actual valid order of stones to remove that achieves the maximum.

---

## Key Difference From Original Problem

Original problem asks:

```text
How many stones can be removed?
```

Follow-up asks:

```text
Which stones should be removed, in what order?
```

DSU is excellent for counting connected components, but it does not naturally preserve a valid removal order.

---

## Core Insight

For a connected component of size `k`:

```text
maximum removable stones = k - 1
```

So the goal is:

```text
remove every stone except one
```

---

## Why Random Removal Fails

Suppose a stone acts as a bridge between two parts of the component.

If we remove that bridge too early:

```text
the component splits
```

Then we may end up with multiple isolated stones that can no longer be removed.

So:

```text
removal order matters
```

---

## Graph Mental Model

Treat each stone as a graph node.

Two stones are connected if they share:
- same row
- same column

Each connected component represents one removable group.

---

## Correct Strategy: DFS Postorder Traversal

For each connected component:

1. Pick any stone as the DFS root.
2. Traverse the component using DFS.
3. Add a stone to the removal sequence AFTER processing its children.
4. Keep the DFS root unremoved.

This is called:

```text
postorder DFS
```

Meaning:

```text
children first, parent later
```

---

## Why Postorder Works

In the DFS spanning tree:

- every non-root node has a parent
- the parent shares a row or column with the child

Therefore:

```text
when removing a child,
its parent still exists
```

So every removal operation remains valid.

This guarantees:

```text
all non-root stones can be safely removed
```

---

## Algorithm

### Step 1 — Build Graph

Each stone is a node.

Add edges between stones sharing:
- same row
- same column

---

### Step 2 — DFS Components

For every unvisited stone:

- run DFS
- collect nodes in postorder
- exclude the DFS root

---

### Step 3 — Return Removal Sequence

The collected postorder nodes form a valid maximum-removal sequence.

---

## Optimization

### Naive Graph Construction

```text
compare every pair of stones
```

Complexity:

```text
O(N²)
```

---

### Optimized Construction

Use hash maps:

```python
row_map[row] -> stones in that row
col_map[col] -> stones in that col
```

This avoids pairwise comparison.

---

## Complexity

With optimized graph construction:

```text
Time: O(N)
Space: O(N)
```

More precisely:

```text
O(V + E)
```

where:
- `V = stones`
- `E = constructed adjacency edges`

---

## Comparison: DSU vs DFS

### DSU

Great for:

```text
counting connected components
```

But DSU loses:
- traversal structure
- removal order
- spanning-tree relationships

---

### DFS

Great for:

```text
constructing a valid deletion order
```

because DFS preserves:
- parent/child structure
- traversal hierarchy
- postorder processing

---

## Main Takeaway

Original problem:

```text
How many groups exist?
```

Follow-up problem:

```text
What is a safe order to remove stones?
```

Therefore:

| Goal | Best Tool |
|---|---|
| Count components | DSU |
| Construct removal order | DFS postorder |

The deep insight:

```text
remove from the outside inward
```

using postorder DFS.


## Why We Can Pick Any Node as the DFS Root

We can choose any node in the connected component as the DFS root because the root is simply the one stone we decide to keep at the end.

The important property is not which node is the root, but rather:

```text
every non-root node has a DFS parent
```

Postorder DFS removes:

```text
children before parents
```

Therefore, when a node is removed, its DFS parent still exists, so the removal is always valid.

A bridge node does not need to be the final remaining node. It only needs to stay alive until all nodes depending on it have already been removed. After a bridge node's children are removed, that bridge node is no longer acting as a bridge, because there is no remaining subtree depending on it.

So regardless of which node is chosen as the root:

- all descendants are removed first
- bridge nodes are removed only after their dependent subtrees disappear
- after their children are gone, bridge nodes are no longer bridges
- exactly one node remains per connected component

Thus, any node can serve as the DFS root, leading to many possible valid removal sequences.