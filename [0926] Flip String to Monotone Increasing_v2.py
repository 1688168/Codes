class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        dp[ii][0]:= ans of s[:ii+1] and s[ii]=0
        dp[ii][1]:= ans of s[:ii+1] and s[ii]=1

        """
        N = len(s)
        dp = [[0] * N for _ in range(2)]

        dp[0][0] = 0 if s[0] == '0' else 1
        dp[1][0] = 1 if s[0] == '0' else 0

        for ii in range(1, N):
            if s[ii] == '0':
                dp[0][ii] = dp[0][ii - 1]
                dp[1][ii] = 1 + min(dp[1][ii - 1], dp[0][ii - 1])
            else:  # s[ii]==1
                dp[0][ii] = 1 + dp[0][ii - 1]
                dp[1][ii] = min(dp[0][ii - 1], dp[1][ii - 1])

        return min(dp[0][N - 1], dp[1][N - 1])

