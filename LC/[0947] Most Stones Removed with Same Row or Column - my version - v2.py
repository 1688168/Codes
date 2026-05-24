class DSU:
    def __init__(self):
        self.parent={}
        self.size={}
    
    def union(self, a, b):
        pa=self.find(a)
        pb=self.find(b)

        if pa==pb: return #already unioned

        # union by size: ensure pa size > pb size
        if self.size[pa] < self.size[pb]: pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
    
    def find(self, x):

        # handle new node initialization
        if x not in self.parent:
            self.parent[x]=x
            self.size[x]=1


        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x]) # path compression

        return self.parent[x]
    

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()

        # process stone to union row/cols
        for x, y in stones:
            dsu.union((x, -1), (-1, y))

        
        # num of groups
        roots=set()
        for (x, y) in stones:
            roots.add(dsu.find((x, -1)))
        
        return len(stones) - len(roots)
        



