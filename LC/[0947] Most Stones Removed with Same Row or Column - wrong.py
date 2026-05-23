class DSU:
    def __init__(self, N=10000):
        self.parent={}
        self.size={}
        self.N=10000+1
        
    def union(self, a, b):
        pa=self.find(a)
        pb=self.find(b)
        if pa==pb: return

        # union by size: ensure pa > pb
        if self.size[pa] < self.size[pb]: pa, pb = pb, pa

        # make smaller tree (pb) be the child of larger tree (pa)
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]

    def find(self, x):
        if x not in self.parent: 
            self.parent[x]=x
            self.size[x]=1
            return self.parent[x]

        if x != self.parent[x]: self.parent[x] = self.find(self.parent[x])
    
        return self.parent[x]
    
    def get_gid(self, x, y):
        return self.N*x+y

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # use DSU to group all stones
        dsu=DSU()

        ## some inputs validation
        ### is stones all unique
        ### can stones be null

        ## union all stones in same row
        for xx, yy in stones:
            gid=xx
            dsu.union(dsu.get_gid(xx, yy), gid)

        ## union all stones in sam col
        for xx, yy in stones:
            gid=yy
            dsu.union(dsu.get_gid(xx, yy), gid)

        ## return numOfStone-numOfGroups
        return len(stones) - (len(set([dsu.find(dsu.get_gid(xx, yy)) for xx, yy in stones])))
        

# ## High level strategy
# * each connected group we only need to keep 1
# * total stone-numOfGroup -> max stones we can remove

# ## Cost Analysis 
# * Union/Find (path compression/Union by size) -> O(alpha(MN)). 10^4*Alph -> 10^6

