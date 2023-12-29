class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[ii][jj]: the min number of deletes required to make word1[:ii+1] and word2[:jj+1] the same
        => return dp[-1][-1]
        dp[ii-1][ii-1]
        dp[ii][jj-1]
        dp[ii-1][jj]
        """
        word1 = '#'+word1
        word2 = '#'+word2
        M = len(word1)
        N = len(word2)
        dp = [[M+N]*N for _ in range(M)]  # setup initial state
        for ii in range(N):
            dp[0][ii] = ii  # setup initial state when ii=0
        for ii in range(M):
            dp[ii][0] = ii  # setup initial state when jj=0

        for ii in range(1, M):
            for jj in range(1, N):
                if word1[ii] == word2[jj]:
                    dp[ii][jj] = dp[ii-1][jj-1]
                else:
                    dp[ii][jj] = 1+min(dp[ii-1][jj], dp[ii][jj-1])

        return dp[-1][-1]
