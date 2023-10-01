###########
# 20231001
###########
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        dp = [[0]*N2 for _ in range(N1)]

        for ii in range(N1):
            for jj in range(N2):
                if text1[ii] == text2[jj]:
                    dp[ii][jj] = 1 + (dp[ii-1][jj-1] if ii >=
                                      1 and jj >= 1 else 0)
                else:
                    dp[ii][jj] = max(dp[ii-1][jj] if ii >=
                                     1 else 0, dp[ii][jj-1] if jj >= 1 else 0)

        return dp[-1][-1]


###########
# 20230903
###########
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        text1 = '#'+text1
        text2 = '#'+text2
        N1 = len(text1)
        N2 = len(text2)

        dp = [[0]*N2 for _ in range(N1)]
        # dp[ii][jj] is the LCS for text1 ending on ii, text2 ending on jj

        for ii in range(1, N1):
            for jj in range(1, N2):
                if text1[ii] == text2[jj]:
                    dp[ii][jj] = dp[ii-1][jj-1]+1
                else:
                    # dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1], dp[ii-1][jj-1])
                    dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
        return dp[-1][-1]


###########
# 20230604
###########
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for ii in range(m-1, -1, -1):
            for jj in range(n-1, -1, -1):
                if text1[ii] == text2[jj]:
                    dp[ii][jj] = 1+dp[ii+1][jj+1]
                else:
                    dp[ii][jj] = max(dp[ii+1][jj], dp[ii][jj+1])

        return dp[0][0]


#######################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        dp = [[None]*N2 for _ in range(N1)]

        def lcs(ii, jj):
            if ii < 0 or jj < 0:
                return 0

            if dp[ii][jj] is not None:
                return dp[ii][jj]

            if text1[ii] == text2[jj]:
                dp[ii][jj] = 1 + lcs(ii-1, jj-1)
            else:
                dp[ii][jj] = max(lcs(ii-1, jj), lcs(ii, jj-1))

            return dp[ii][jj]

        lcs(N1-1, N2-1)

        return dp[-1][-1]
