class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        # I/O:
        + arr[ii]:
        + k: at most k partitions
        => 
        # Analysis:
        + N=500

        # DP:
        + let dp[ii][jj]: max sum ending @ ii with jj as last partition length
        """
        N=len(arr)
        dp=[0]*N
    
        """
        x x x x x
        """
        dp[0]=arr[0]

        for ii in range(1, N):
            mx=-math.inf          
            for jj in reversed(range(max(ii-k+1, 0), ii+1)):               
                mx=max(mx, arr[jj])
                dp[ii] = max(dp[ii], (dp[jj-1] if jj-1 >=0 else 0)+mx*(ii-jj+1))
        
        return dp[-1]