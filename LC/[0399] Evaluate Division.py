from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        : each time you see a question => what is the data structure or algorithm it is asking?
        : trying to find if a can get to b
        : DFS (path existance)
        : given pairs (relationship)
            1. build a graph
            2. do DFS search if path exists
            3. return -1 if not existing
        """
        g=defaultdict(set)
        value_map={}  #given a pair, what's the value

        visited=set()
        for ii, (a, b) in enumerate(equations):
            value_map[(a,a)]=1
            value_map[(b,b)]=1
            value_map[(a,b)]=values[ii]
            value_map[b,a]=1/values[ii]
            g[a].add(b)
            g[b].add(a)


        res=[]
        def dfs(x,y):
            if (x,y) in value_map:
                return value_map[(x,y)]
            else:
                visited.add(x)
                for child in g[x]:
                    if (child) in visited: continue
                    ans=dfs(child, y)
                    if ans!= -1:
                        value_map[(child, y)]=ans
                        return value_map[(x, child)] * ans

            return -1


        for x, y in queries:
            visited=set()
            if x not in g or y not in g:
                res.append(-1)
                continue
            res.append(dfs(x,y))

        return res
