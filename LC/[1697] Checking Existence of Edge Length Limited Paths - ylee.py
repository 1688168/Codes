class DSU:
    def __init__(self, n):
        self.n2parents = dict()
        self.n2size = dict()

        # initialize all
        for ii in range(n): self.find(ii) # see if we need this
    
    def union(self, aa, bb):
        pa = self.find(aa)
        pb = self.find(bb)

        if pa==pb: return
        if self.n2size[pa] < self.n2size[pb]:
            pa, pb = pb, pa
        
        self.n2parents[pb] = pa #union by size
        self.n2size[pa] += self.n2size[pb] #update size

    def find(self, xx):
        # lazy initialization
        if xx not in self.n2parents:
            self.n2parents[xx] = xx
            self.n2size[xx] = 1

        if xx != self.n2parents[xx]:
            self.n2parents[xx] = self.find(self.n2parents[xx]) # path compression
        
        return self.n2parents[xx]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # initialize DSU
        dsu = DSU(n)

        # initialize outputs
        ans = [False] * len(queries)

        # sort edges by weight - in place sort
        edgeList.sort(key=lambda x: x[2])

        # sort query indexes
        queryOrder = sorted(range(len(queries)), key=lambda ii: queries[ii][2])

        # run query one by one and union
        edge_idx = 0
        for ii in queryOrder:
            p, q, l = queries[ii]
            for jj in range(edge_idx, len(edgeList)):
                if edgeList[jj][2] < l:
                    dsu.union(edgeList[jj][0], edgeList[jj][1])
                    edge_idx += 1
                else:
                    break
            
            ans[ii] = dsu.find(p)==dsu.find(q)

        return ans
54