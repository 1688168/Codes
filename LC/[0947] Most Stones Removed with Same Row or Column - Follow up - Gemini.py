from collections import defaultdict
from typing import List

class Solution:
    def removeStonesSequence(self, stones: List[List[int]]) -> List[List[int]]:
        # 1. O(N) Graph Building
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        
        # Group stone indices by their row and column
        for i, (r, c) in enumerate(stones):
            row_map[r].append(i)
            col_map[c].append(i)
            
        # Build the adjacency list
        graph = defaultdict(list)
        for i, (r, c) in enumerate(stones):
            for neighbor in row_map[r]:
                if neighbor != i: graph[i].append(neighbor)
            for neighbor in col_map[c]:
                if neighbor != i: graph[i].append(neighbor)
                
        visited = set()
        removal_sequence = []
        
        # 2. Post-Order DFS Traversal
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
            # Post-Order: Add to sequence only after visiting all children.
            # This ensures we remove leaves first, never breaking a bridge.
            removal_sequence.append(stones[node])

        # 3. Process each connected component
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                # The root of the DFS tree is the final stone standing.
                # Since the problem asks for what to remove, we discard the root.
                removal_sequence.pop() 
                
        return removal_sequence
