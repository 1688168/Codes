"""
Each stone is a graph node.
Two stones are connected if they share a row or column.
For each connected component, keep one root stone and remove all others.
Use DFS postorder so children are removed before parents.

Key intuition:
A bridge stone does not need to be the final remaining stone.
It only needs to stay until all stones depending on it are removed.
After its DFS children are removed, it is no longer acting as a bridge.
"""

"""
## Implementation
1. Build the graph as an adjacency list.
   * To avoid O(n^2) pairwise stone comparison, first build row_map and col_map.
   * row_map[row] stores all stone indices in that row.
   * col_map[col] stores all stone indices in that column.
   * For each row/column group, connect all stones through one representative.

2. For each connected component, pick any unvisited node as the DFS root.
   * Keep that root stone.
   * Use postorder DFS to output the removal sequence.
   * Postorder removes children before parents, so every removed stone still has its parent available.
"""

from collections import defaultdict
from typing import List


class Solution:
    def removeStonesSequence(self, stones: List[List[int]]) -> List[List[int]]:
        n = len(stones)

        # row_map[row] stores all stone indices in that row.
        row_map = defaultdict(list)

        # col_map[col] stores all stone indices in that column.
        col_map = defaultdict(list)

        # Use each stone's index as its graph node id.
        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)

        # Graph representation as an adjacency list.
        graph = [[] for _ in range(n)]

        def connect_group(indices):
            # If this row/column has fewer than 2 stones, no edge is needed.
            if len(indices) <= 1:
                return

            # Use the first stone as the representative.
            first = indices[0]

            # Connect every other stone in this row/column to the representative.
            for j in range(1, len(indices)):
                other = indices[j]

                # Add undirected edge: first <-> other.
                graph[first].append(other)
                graph[other].append(first)

        # Connect stones sharing the same row.
        for indices in row_map.values():
            connect_group(indices)

        # Connect stones sharing the same column.
        for indices in col_map.values():
            connect_group(indices)

        visited = [False] * n
        removal_order = []

        def dfs(node, is_root):
            visited[node] = True

            # Visit children/neighbors first.
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, False)

            # Postorder: remove this stone only after its DFS children are processed.
            # Do not remove the root stone of this component.
            if not is_root:
                removal_order.append(node)

        # Run DFS for each connected component.
        for i in range(n):
            if not visited[i]:
                dfs(i, True)

        # Convert stone indices back to coordinates.
        return [stones[i] for i in removal_order]