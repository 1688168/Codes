class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N=len(isConnected)

        MM = isConnected

        # defines the min idx of connected nodes
        ancestor = [ii for ii in range(N)] # all nodes initialized the ancestor as itself

        def union(a, b): 
            x = find(a) # find a's ultimate ancestor
            y = find(b) # find b's ultimate ancestor
            ancestor[x] = y # two connected nodes should have same ancestor
            
        def find(x):
            if ancestor[x] != x: #the ultimate ancestor is itself
                ancestor[x] = find(ancestor[x])
            
            return ancestor[x] # this is the ultimate ancestor
        
        # we need to process each node to identify num of groups
        for ii in range(N):
            for jj in range(N):
                if MM[ii][jj]==0: continue # ignore those not connected
            
                if ii==jj: continue # ignore self
                
                # ii, jj are connected and not self
                union(ii, jj)
        
        # identify num of groups
        ss = set()
        for x in ancestor:
            ss.add(find(x))
        
        return len(ss)


