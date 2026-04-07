class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N=len(isConnected) # take size 
        MM=isConnected     # assign alias
        ancestor={ii:ii for ii in range(N)} #initialize ancestor as self

        def union(a, b):
            """
            if a and b are connected, a and b should share same ancestor
            """
            x = find(a)
            y = find(b)
            ancestor[x] = y # making b's ancestor be the ultimate boss
        
        def find(x):
            if ancestor[x] != x:
                ancestor[x] = find(ancestor[x])

            return ancestor[x]

        # we need to process each node so we can group them
        for ii in range(N):
            for jj in range(N):
                if ii==jj: continue # no need to process self
                if MM[ii][jj] ==0: continue # ignore those not connected
                union(ii, jj) #we need to union connected nodes
        

        # how many unique ancestors?
        return len(set(find(ii) for ii in ancestor.keys()))

