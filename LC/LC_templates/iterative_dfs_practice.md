# Learning Iterative DFS

Practice in three stages: **visiting nodes**, **tracking paths**, and **simulating recursive calls**. GridMaster belongs to the third stage: a basic “push neighbors onto a stack” template does not capture physical backtracking.

## Practice sequence

Solve each problem iteratively, using the exercise below rather than simply choosing any accepted solution.

| Order | Problem | Difficulty | Practice instruction |
|---|---|---|---|
| 1 | [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Easy | Pop a node, process it, and push its children. Push right before left to visit left first. |
| 2 | [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | Medium | Add a global visited set. Mark rooms visited when pushing them. |
| 3 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Apply the stack to coordinates and four directions. Start a new traversal for each unvisited island. |
| 4 | [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Easy, but a useful jump | Use `(node, exiting)` entries to perform work after children finish. Avoid the reverse-preorder shortcut for this exercise. |
| 5 | [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium | First store `(node, path)` with separate path copies. Then redo it using one shared path and explicit backtracking. |
| 6 | [79. Word Search](https://leetcode.com/problems/word-search/) | Medium | Track cells used by the current path and undo those marks when returning. |
| 7 | [1778. Shortest Path in a Hidden Grid](https://leetcode.com/problems/shortest-path-in-a-hidden-grid/) | Medium · Premium | Store the next direction to try and the move needed to return to the parent. Map with DFS, then find the shortest distance with BFS. |
| 8 | [489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) | Hard · Premium | Maintain physical position and orientation while simulating recursive backtracking. |

The order reflects the learning progression, not strictly LeetCode's difficulty labels.

## Mental model 1: A stack of pending visits

For basic traversal, an entry means:

> Visit this node later.

```python
# Template: neighbors(node) supplies the graph's adjacent nodes.
stack = [start]
visited = {start}

while stack:
    node = stack.pop()
    # Process node here.

    for neighbor in neighbors(node):
        if neighbor in visited:
            continue

        visited.add(neighbor)
        stack.append(neighbor)
```

This is enough for reachability. You do not need to remember where a parent's loop paused. Marking nodes visited when pushing prevents duplicate pending entries.

In a tree, push children in reverse of the desired processing order because a stack is last-in, first-out. In a graph, this basic approach need not reproduce the exact recursive DFS tree; use explicit frames when that matters.

## Mental model 2: Remember work that happens after a child

For postorder traversal, visiting a node and finishing a node are different events.

```python
stack = [(root, False)]
result = []

while stack:
    node, exiting = stack.pop()
    if node is None:
        continue

    if exiting:
        result.append(node.val)
        continue

    # Schedule the parent to finish after both children.
    stack.append((node, True))
    stack.append((node.right, False))
    stack.append((node.left, False))
```

The second entry for the parent represents the work that recursion would perform after its child calls return.

## Mental model 3: A stack of paused function calls

For backtracking, an entry means:

> This function call is paused here. Remember how to continue it.

Consider the GridMaster code:

```python
master.move(direction)
dfs(nx, ny)
master.move(reverse)
```

While the child call runs, Python remembers:

- The parent's coordinates.
- Which direction the parent was exploring.
- That the reverse move must execute after the child returns.
- Which direction the parent should try next.

An iterative version must store this information explicitly. A useful frame is:

```python
(x, y, next_direction_index, return_direction)
```

Conceptual algorithm:

```text
Look at the top frame.
    If it has another direction to try:
        Advance its direction index.
        If the neighbor is valid and unvisited:
            Move to the neighbor.
            Push a child frame.
    Otherwise:
        Pop the finished frame.
        Move back to its parent, unless this was the root.
```

The top frame corresponds to the robot's current location. Keep the parent on the stack while exploring its child. Advance the parent's direction index before descending so it resumes at the next direction when the child finishes.

For GridMaster, each completed frame must restore the robot to its parent. For Robot Room Cleaner, also restore the orientation required by the parent's continuation.

## Global visited versus current-path membership

| Purpose | When to mark | When to unmark |
|---|---|---|
| Reachability, islands, hidden-grid mapping | When discovering/pushing a node | Never during that traversal |
| Word Search with a shared path | When entering a cell on the current path | When backtracking out of that cell |
| All paths in a DAG | Track the current path; global visited would suppress valid alternative paths | Pop from a shared path when returning, or use independent path copies |

Do not automatically add a global visited set to every DFS problem. Decide whether you are finding reachable nodes or enumerating possible paths.

## Practice routine

For each problem:

1. Write a recursive solution first.
2. Identify what each call must remember.
3. Identify what happens before visiting a child.
4. Identify what happens after the child returns.
5. Choose a stack entry that preserves the needed information.
6. Trace a tiny example using the table below.
7. Implement the iterative version without looking at a solution.
8. Explain every push, peek, and pop before moving on.

| Step | Stack (bottom → top) | Visited / current path | Action |
|---|---|---|---|
| 0 | | | |
| 1 | | | |
| 2 | | | |

Useful trace cases:

- A tree with a root and two children: check stack ordering.
- A graph with a cycle: check duplicate prevention.
- A diamond-shaped DAG: check that both paths to the shared destination survive.
- A grid with a dead end: check path cleanup and physical backtracking.

## Milestones

- [ ] I can solve 144, 841, and 200 using a stack without copying a template.
- [ ] I can explain why postorder needs deferred work.
- [ ] I can distinguish global visited from current-path membership.
- [ ] I can explain what a paused recursive call remembers.
- [ ] I can implement a frame that resumes at the next neighbor.
- [ ] I can keep the robot's physical position consistent with the top frame.
- [ ] I can map the hidden grid iteratively, then run BFS for the shortest path.

Start with **144 → 841 → 200**. Once those feel routine, postorder traversal is the bridge to explicit backtracking.
