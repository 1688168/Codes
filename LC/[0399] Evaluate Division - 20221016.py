from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]],
                                      values: List[float],
                                      queries: List[List[str]]) -> List[float]:
        g=defaultdict(set) #declare graph

        for ii, (aa, bb) in enumerate(equations): # populate the graph per equation
            g[aa].add((bb, values[ii]))
            g[bb].add((aa, 1.0/values[ii]))


        res=[]


        def dfs(aa, bb): #DFS from aa to bb


            if aa not in g or bb not in g:
                return -1.0
            if aa==bb: return 1.0
            visited.add(aa)

            for child, val in g[aa]:
                if child in visited: continue
                ans=dfs(child, bb)
                if ans !=-1.0:
                    return val*ans
            #visited.remove(aa)
            return -1.0

        for cc, dd in queries:
            visited=set()
            res.append(dfs(cc, dd))

        return res
