"""
Each stone is a graph node.
Two stones are connected if they share a row or column.
For each connected component, keep one root stone and remove all others.
Use DFS postorder so children are removed before parents.
"""

from collections import defaultdict
from typing import List


class Solution:
    def removeStonesSequence(self, stones: List[List[int]]) -> List[List[int]]:
        # n is the total number of stones.
        n = len(stones)

        # row_map maps each row number to the list of stone indices in that row.
        row_map = defaultdict(list) # row index to stones index

        # col_map maps each column number to the list of stone indices in that column.
        col_map = defaultdict(list) # col index to stones index

        # Build row_map and col_map.
        # We use stone index i as the graph node id.
        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)

        # graph[i] stores all stones connected to stone i.
        graph = [[] for _ in range(n)] # Graph representation as a matrix (adjacency matrix)

        # Helper function:
        # Given all stones in the same row/column,
        # connect them through the first stone as a representative.
        def connect_group(indices):
            # If the group has 0 or 1 stone, no edges are needed.
            if len(indices) <= 1:
                return

            # Use the first stone as the representative.
            first = indices[0]

            # Connect every other stone in this group to the representative.
            # This is enough to make the entire group connected.
            for j in range(1, len(indices)):
                other = indices[j]

                # Add undirected edge: first <-> other.
                graph[first].append(other)
                graph[other].append(first)

        # Connect stones that share the same row.
        for indices in row_map.values(): # for the stone indexes in the list sharing same row
            connect_group(indices) # connect all stones (index) that sharing same row

        # Connect stones that share the same column.
        for indices in col_map.values():
            connect_group(indices)

        # visited[i] tells whether stone i has already been visited by DFS.
        visited = [False] * n

        # removal_order stores stone indices in the order we remove them.
        removal_order = []

        def dfs(node, is_root):
            # Mark current stone as visited.
            visited[node] = True

            # Visit all connected neighboring stones first.
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, False)

            # Postorder logic:
            # Add this stone to removal order only AFTER children are processed.
            # But do NOT remove the component root.
            if not is_root:
                removal_order.append(node)

        # Run DFS from every unvisited stone.
        # Each DFS call handles one connected component.
        for i in range(n):
            if not visited[i]:
                # Treat i as the root of this component.
                # We keep this root stone, so is_root=True.
                dfs(i, True)

        # Convert stone indices back to actual [x, y] coordinates.
        return [stones[i] for i in removal_order]