from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build the graph
        gg=defaultdict(list) # model the nodes as graph for search
        for (aa, bb), vv in zip(equations, values):
            gg[aa].append((bb, vv))
            gg[bb].append((aa, 1.0/vv))

        res=[]

        def dfs(xx, zz):
            nonlocal visited
            if xx==zz: return 1.0

            for yy, vv in gg[xx]: # (yy, vv)
                if yy in visited: continue
                visited.add(yy)
                ans = dfs(yy, zz)
                if ans != -1: return vv*ans

            return -1.0

        # DFS on each query
        for xx, zz in queries:

            # check existance of node
            if xx not in gg or zz not in gg: 
                res.append(-1)
                continue
            
            visited={xx}
            res.append(dfs(xx, zz))

        return res

# “”“
# ## Analysis
# * if there is a path from A->B, we tag it with value x
# * if there is a path from B->C with value y
# * we can derive path A->C=x*y
# * if A->B with value x => B-> is with value 1/x
# * so this is a DFS, given connections, asking existance of path and deriving the associated value
# * DFS, we use cache to avoid repeated search, we will visited each node and each edge exactly once -> O(V+E)
# * V=40
# * E=20
# ”“”