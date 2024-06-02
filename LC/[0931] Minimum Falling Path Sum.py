class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N=len(matrix)

        # declare DP
        """
        dp[ii][jj]: min sum @ [ii, jj]
        """
        dp=[[math.inf]*N for _ in range(N)]
        
        # initialize DP
        for jj in range(N): dp[0][jj] = matrix[0][jj]

        for ii in range(1, N):
            for jj in range(N):
                left = dp[ii-1][jj-1] if jj-1 >=0 else math.inf
                center = dp[ii-1][jj]
                right = dp[ii-1][jj+1] if jj+1 < N else math.inf

                dp[ii][jj] = min(dp[ii][jj], matrix[ii][jj]+min(left, center, right))
        
        return min(dp[-1])
