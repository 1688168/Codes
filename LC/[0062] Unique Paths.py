class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp=[[0]*n for _ in range(m)]

        for ii in range(n):
            dp[0][ii]=1


        for ii in range(1,m):
            dp[ii][0]=1

        for ii in range(1, m):
            for jj in range(1, n):
                dp[ii][jj]=dp[ii-1][jj]+dp[ii][jj-1]

        return dp[-1][-1]
