from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = [[] for _ in range(n)]

        # Each stone is a node, identified by its index.
        # Connect two stones if they share a row or column.
        for i in range(n): # pair-wise compare stone (N^2)
            for j in range(i + 1, n):
                same_row = stones[i][0] == stones[j][0]
                same_col = stones[i][1] == stones[j][1]

                if same_row or same_col:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set() # required DFS data structure

        def dfs(node):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        components = 0

        for node in range(n):
            if node not in visited:
                # An unvisited stone starts a new component.
                components += 1 #any node can be a root and counts 1

                # Mark every stone in this component as visited.
                dfs(node)

        # Keep one stone per component.
        return n - components