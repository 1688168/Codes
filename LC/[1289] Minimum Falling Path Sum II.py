##############
# 20240601
##############
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        # I/O:
        + Grid
        => min sum of a falling path with non-zero shifts
        
        # Analysis:
        + N=200 -> O(N^2)
        + choice of exactly 

        > Bruteforce:
        -> N^N

        > DP: 
        * when you walk the grid from top->bottom or top-left->bottom-right ---> dp
        let dp[ii][jj]: min sum of a falling path with non-zero shift ending @ (ii, jj)
            dp[ii][jj] = dp[ii-1][k] + min1/min2
        """
        from heapq import heappush, heappop, heappushpop
        M=len(grid)
        N=len(grid[0])

        dp=[[0]*N for _ in range(M)]

        # initialize dp[0]
        mxh=[]
        for ii in range(N): 
            dp[0][ii]=grid[0][ii]
            if len(mxh)<2 or dp[0][ii] < -mxh[0][0]:
                heappush(mxh, (-dp[0][ii], ii))#this is a topK pattern
            if len(mxh)> 2: heappop(mxh)
        
        for ii in range(1, M):
            # we need to find min1, min2 in prev row
            min1_jj = mxh[1][1]
            min2_jj = mxh[0][1]
            mxh=[]
              
            for jj in range(N):
                #print(mxh)
                dp[ii][jj] = (dp[ii-1][min1_jj] if min1_jj != jj else dp[ii-1][min2_jj]) + grid[ii][jj]
                if len(mxh)<2 or dp[ii][jj] < -mxh[0][0]:
                    heappush(mxh, (-dp[ii][jj], jj))#this is a topK pattern
                if len(mxh)> 2: heappop(mxh)

        return min(dp[-1])
    
####################
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        # I/O:
        + Grid
        => min sum of a falling path with non-zero shifts
        
        # Analysis:
        + N=200 -> O(N^2)
        + choice of exactly 

        > Bruteforce:
        -> N^N

        > DP: 
        * when you walk the grid from top->bottom or top-left->bottom-right ---> dp
        let dp[ii][jj]: min sum of a falling path with non-zero shift ending @ (ii, jj)
            dp[ii][jj] = dp[ii-1][k] + min1/min2
        """
        from heapq import heappush, heappop, heappushpop
        M=len(grid)
        N=len(grid[0])

        dp=[[0]*N for _ in range(M)]

        # initialize dp[0]
        for ii in range(N): dp[0][ii]=grid[0][ii]
        
        for ii in range(1, M):
            # we need to find min1, min2 in prev row
            mxh=[]
            for kk, nn in enumerate(dp[ii-1]):
                if len(mxh)<2 or nn < -mxh[0][0]:
                    heappush(mxh, (-nn, kk))#this is a topK pattern
                if len(mxh)> 2: heappop(mxh)
            for jj in range(N):
                #print(mxh)
                dp[ii][jj] = (dp[ii-1][mxh[1][1]] if mxh[1][1] != jj else dp[ii-1][mxh[0][1]]) + grid[ii][jj]

        ans=math.inf
        for jj in range(N): ans=min(ans, dp[M-1][jj])
        return ans