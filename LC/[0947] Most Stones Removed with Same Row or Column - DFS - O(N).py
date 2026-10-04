from collections import defaultdict
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = [[] for _ in range(n)]

        row_map = defaultdict(list) # collect nodes on this row
        col_map = defaultdict(list) # collect nodes on this col

        for i, (row, col) in enumerate(stones): # or original stone list index is the ID of each stone
            row_map[row].append(i)
            col_map[col].append(i)

        # Connect each group through its first stone.
        def connect_group(indices):
            first = indices[0]

            for other in indices[1:]:
                graph[first].append(other)
                graph[other].append(first)

        for indices in row_map.values():
            connect_group(indices)

        for indices in col_map.values():
            connect_group(indices)

        visited = set()

        # Iterative DFS avoids Python's recursion-depth limit.
        def dfs(start):
            stack = [start]
            visited.add(start)

            while stack:
                node = stack.pop()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        components = 0

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return n - components