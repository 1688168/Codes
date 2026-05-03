class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        MM=isConnected 
        N=len(MM) # num of cities
        
        roots = {a: a for a in range(N)} #declare/initialize the roots (every nodes default to it's own parent root)

        def union(a, b):
            """
            * given two nodes, unify the parent of both nodes in the record
            """
            x = find(a) # find a's root parent
            y = find(b) # find b's root parent
            if x!= y:
                roots[x] = y # make a's root parent same as b's root parent (union the look up path)
        
        def find(x):
            """
            * given a node x: return the root of the node
            """
            if roots[x] != x: # x is not the root parent
                roots[x] = find(roots[x]) # compress the look up path. make parent of x be the root parent (compress)

            return roots[x]
        
        # need to traverse all nodes and identify it's root parent if connected
        for ii in range(N):     # for each row --- O(N^2)
            for jj in range(ii+1, N): # for each column, only traverse half of the matrix due to symmetry
                #if ii == jj: continue # self is already defaulted -- not required any more since we only traverse half of the matrix
                if MM[ii][jj] != 1: continue # ignore if not connected
                union(ii, jj) # if two nodes are connected, Merge the two groups

        # how many unique parents existing?
        return len(set(find(x) for x in range(N)))



"""
## Problem
* find num of connected groups

## Given
* a matrix indicating connectivity of two nodes (cities)
* asking number of connected groups

## Observation
* we need to repeatedly look up root node and identify groups -> compress the tree
* DSU (UnionFind)
"""