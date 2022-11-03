class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1=len(text1)
        N2=len(text2)

        dp=[[None]*N2 for _ in range(N1)]

        def lcs(ii, jj):
            if ii < 0 or jj < 0: return 0

            if dp[ii][jj] is not None: return dp[ii][jj]

            if text1[ii]==text2[jj]:
                dp[ii][jj] = 1 + lcs(ii-1, jj-1)
            else:
                dp[ii][jj] = max(lcs(ii-1, jj), lcs(ii, jj-1))

            return dp[ii][jj]

        lcs(N1-1, N2-1)

        return dp[-1][-1]
        
