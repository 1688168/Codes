class Solution:
    class DSU:
        def __init__(self):
            self.node2Parent = dict() # given a node, point to parent
            self.node2Size = dict()   # given a node, point to group size

        def union(self, a, b):
            pa = self.find(a)
            pb = self.find(b)

            if pa==pb: return # already same parent -> noop
            if self.node2Size[pa] < self.node2Size[pb]:
                pa, pb = pb, pa
            
            # union by size: please smaller tree under larger tree to reduce tree height and shorten search path
            self.node2Parent[pb] = pa
            self.node2Size[pa] += self.node2Size[pb]
        
        def find(self, x):
            if x not in self.node2Parent:
                self.node2Parent[x] = x
                self.node2Size[x] = 1
            
            if x != self.node2Parent[x]: # path compression. if x's parent is not itself, point x's parent to the ultiomate parent
                self.node2Parent[x] = self.find(self.node2Parent[x])
            
            return self.node2Parent[x]

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # we are given a matrix:M where M[ii][jj] indicate node ii connected to node jj
        # we will build union find data structure and count the num of parents

        N=len(isConnected)  # num of nodes
        M = isConnected     # the matrix
        dsu= self.DSU()
        for ii in range(N):
            for jj in range(ii+1, N):
                if M[ii][jj] == 1: dsu.union(ii, jj)
        
        return len({dsu.find(city) for city in range(N)}) # set comprehension
        # return len(set([dsu.find(x) for x in range(N)]))
        

# # Problem Statement
# * N cities.
# * connected: graph

# ## Given
# * NXN matrix
# * M[ii][jj] = 1 -> city ii and jj are connected otherwise not-connected

# ## Ask Total Num of Provinces

# # Constraints Aanlysis
# * N: 1~200
# * N^2=40,000 
# * N=1 -> return 1

# > DFS: -> N^2 -> okay
# > Union-Find -> N(AlphaXN) -> better
# ## Edge Cases

# # Stratedy and Complexity Analysis
# * DFS all cities and mark visited a long the way. increment count on each new DFS
# * build union/Find and count num of parents (all connected cities share one parent)

# # Lesson Learned
# * This is the classic UnionFind problem
# * Please notice the given grid is not a 2D plan represent nodes location.  The Given Grid is NXN matrix indicate which nodes are connected.