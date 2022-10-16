class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)

        dp = [0] * (N)

        for ii in reversed(range(N)):
            dp[ii] = 1
            miPlusOneJMinusOne = 0
            for jj in range(ii + 1, N):
                mij = 0
                if s[ii] == s[jj]:
                    mij = 2 + miPlusOneJMinusOne
                else:
                    mij = max(dp[jj - 1], dp[jj])
                miPlusOneJMinusOne = dp[jj]
                dp[jj] = mij
                # print(dp)
        # print(dp)
        return dp[N - 1]
