class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        """
        # I/O:
        + arr[ii]: int
        => max sum, non-empty subarray

        # Analysis:
        + N=10^5 -> nlogn

        > Bruteforce:
        + take-continue
        + take-start-new
        + no-take

        > DP:

        > Greedy:
        """
        N=len(arr)


        def dfs(st, deleted, ttl):
        
            if st >= N: return ttl

            if st==0 or ttl == -math.inf:                
                return max(dfs(st+1, False, arr[st]), dfs(st+1, True, -math.inf), ttl)            
           
            if deleted:
                return max(dfs(st+1, True, ttl+arr[st]), #take and continue
                           dfs(st+1, True, -math.inf), # skip current and start fresh
                           dfs(st+1, False, arr[st]), ttl)  # take current and start fresh
            else:
                return max(dfs(st+1, False, ttl+arr[st]), # take and continue
                           dfs(st+1, False, arr[st]), # take and start fresh
                           dfs(st+1, True, -math.inf),# skip current and start fresh
                           dfs(st+1, True, ttl), ttl) # skip current and continue

        mxs = dfs(0, False, -math.inf)    
        return mxs
