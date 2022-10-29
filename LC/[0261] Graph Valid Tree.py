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




        
