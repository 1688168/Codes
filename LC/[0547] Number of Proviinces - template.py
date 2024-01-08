###################
# 20240108
###################
class UnionFind:
    def __init__(self, n=None):
        self.c2f={}
        if n is None: return
        for ii in range(n):
            self.c2f[ii]=ii #initialize all node as its own parent
    
    def union(self, x, y):
        """
        merge ancestor of x and y
        """
        x=self.find(x)
        y=self.find(y)

        if x < y:
            self.c2f[y]=x
        else:
            self.c2f[x]=y
    def find(self, x):
        if self.c2f[x] != x:
            self.c2f[x]=self.find(self.c2f[x])
        
        return self.c2f[x]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        G=isConnected
        N=len(G)
        uf=UnionFind(N)
        for ii in range(N):
            for jj in range(N):
                if ii != jj and G[ii][jj]==1:
                    uf.union(ii, jj)
        
        groups=set()
        for child, parent in uf.c2f.items():
            ancestor=uf.find(child)            
            groups.add(ancestor)

        return len(groups)

###################
# 20240107
###################
class UnionFind:
    def __init__(self, n=None):
        self.child2father = {}
        if n is not None:
            for ii in range(n):
                self.child2father[ii] = ii

    def union(self, x, y):
        # x = self.child2father[x]
        # y = self.child2father[y]
        x = self.find(x)
        y = self.find(y)

        if x < y:
            self.child2father[y] = x
        else:
            self.child2father[x] = y

    def find(self, x):
        if self.child2father[x] != x:
            self.child2father[x] = self.find(self.child2father[x])

        return self.child2father[x]


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        for ii in range(N):
            for jj in range(N):
                if ii != jj and isConnected[ii][jj] == 1:
                    if uf.find(ii) != uf.find(jj):
                        uf.union(ii, jj)

        groups = set()
        for child, father in uf.child2father.items():
            groups.add(uf.find(father))

        return len(groups)

###############################


class UnionFind:
    def __init__(self, n=None):
        self.child2father = {}
        if n is not None:
            for ii in range(n):
                self.child2father[ii] = ii

    def union(self, x, y):
        x = self.child2father[x]
        y = self.child2father[y]
        if x < y:
            self.child2father[y] = x
        else:
            self.child2father[x] = y

    def find(self, x):
        if self.child2father[x] != x:
            self.child2father[x] = self.find(self.child2father[x])
        return self.child2father[x]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        for ii in range(N):
            for jj in range(N):
                if ii != jj and isConnected[ii][jj] == 1:
                    if uf.find(ii) != uf.find(jj):
                        uf.union(ii, jj)

        groups = set()
        for child, father in uf.child2father.items():
            groups.add(uf.find(father))

        return len(groups)
