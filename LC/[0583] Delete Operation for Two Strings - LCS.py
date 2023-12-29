class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        - two strings
        - N: 500
        => min delete to make word1==word2
        => ttl length - LCS
        """
        word1 = '#'+word1
        word2 = '%'+word2

        M = len(word1)
        N = len(word2)
        dp = [[0]*N for _ in range(M)]
        for ii in range(1, M):
            for jj in range(1, N):
                if word1[ii] == word2[jj]:
                    dp[ii][jj] = 1+dp[ii-1][jj-1]
                else:
                    dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])

        return M+N-(dp[-1][-1])*2-2  # the two '#' added are fake
