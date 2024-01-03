class UnionFind:
    def __init__(self, n=None):
        self.child2father={}
        if n is not None:
            for ii in range(n):
                self.child2father[ii]=ii
    def union(self, x, y):
        x=self.child2father[x]
        y=self.child2father[y]
        if x < y:
            self.child2father[y]=x
        else:
            self.child2father[x]=y
        
    def find(self, x):
        if self.child2father[x] != x:
            self.child2father[x]=self.find(self.child2father[x])
        return self.child2father[x]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N=len(isConnected)
        uf=UnionFind(N)
        for ii in range(N):
            for jj in range(N):
                if ii!= jj and isConnected[ii][jj]==1:
                    if uf.find(ii) != uf.find(jj):
                        uf.union(ii, jj)
        
        groups=set()
        for child, father in uf.child2father.items():
            groups.add(uf.find(father))
        
        return len(groups)