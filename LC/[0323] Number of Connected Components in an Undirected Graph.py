from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build graph
        g=defaultdict(set)
        for aa, bb in edges:
            g[aa].add(bb)
            g[bb].add(aa)

        visited=set()
        def dfs(nn):
            visited.add(nn)

            for child in g[nn]:
                if child in visited: continue
                dfs(child)

        cnt=0

        for ii in range(n):
            if ii in visited: continue
            cnt += 1
            dfs(ii)

        return cnt
