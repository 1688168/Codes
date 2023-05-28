##################
# 20230528
##################

from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0: return True

        g=defaultdict(set) 

        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        visited=set()
        def hasCycle(parent, nn, visited):
            if nn in visited: return True
            visited.add(nn)


            for child in g[nn]:
                if child == parent: continue
                if hasCycle(nn, child, visited): return True            

            return False

        
        return (not hasCycle(-1, 0, visited)) and len(visited)==n

############################
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==0: return True
        g=defaultdict(set)

        for aa, bb in edges:
            g[aa].add(bb)
            g[bb].add(aa)

        visited=set()
        def dfs(nn, prev):
            if  nn in visited: return False

            visited.add(nn)

            for child in g[nn]:
                if child == prev: continue
                if not dfs(child, nn): return False

            return True
        #print(" visited: ", visited)
        return dfs(0, -1) and len(visited)==n




        
