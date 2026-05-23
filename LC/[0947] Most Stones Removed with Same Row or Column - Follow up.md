### LeetCode 947 Follow-Up: Stone Removal Sequence

**The Problem**
Instead of returning the *maximum number* of stones that can be removed, return a **valid sequence** (the exact order) of stones to remove to achieve that maximum count.

**The Challenge**
The standard Disjoint Set Union (DSU) approach calculates the total number of components, but it destroys the structural hierarchy of the connections through path compression. DSU cannot easily tell you *which* stone to remove first. If you randomly remove a "bridge" stone that connects two halves of a component, the group splits into two, and you permanently lose the ability to remove one of the resulting roots. 

**The Solution**
To guarantee we do not sever connected components prematurely, we must treat the stones as a graph and remove them from the outside in.
1. **Graph Construction:** Treat each stone as a node. Edges exist between stones sharing a row or column.
2. **Spanning Tree:** For each isolated group of stones (connected component), pick any unvisited stone as the root and traverse the group to map all connections.
3. **Post-Order DFS Traversal:** Use Depth-First Search (DFS) and only add a stone to the removal sequence *after* its recursive calls finish. This mathematically guarantees we are only ever removing the "leaf" nodes of our spanning tree, keeping the core bridge structures intact until they are the only stones left.

---

### The Python Implementation

Yes, we can absolutely write code for this. To make it optimized for a senior-level interview, this version builds the graph in **$\mathcal{O}(N)$ time** using hash maps, rather than relying on an $\mathcal{O}(N^2)$ nested loop to find edges.

