class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        => min num of ops to convert w1 to w2
        N=500 -> O(N^2)
        """
        w1 = word1
        w1 = '#'+w1
        w2 = word2
        w2 = '#'+w2
        N1 = len(w1)
        N2 = len(w2)

        # setup initial state
        dp = [[N1+N2]*N2 for _ in range(N1)]
        for ii in range(N1):
            dp[ii][0] = ii
        for ii in range(N2):
            dp[0][ii] = ii

        for ii in range(1, N1):
            for jj in range(1, N2):
                if w1[ii] == w2[jj]:  # no operation required
                    dp[ii][jj] = dp[ii-1][jj-1]
                else:

                    """
                    x x x x i x
                    y y y y y j
                    """

                    # insert: so w1[ii+1] is a new char equal to w2[jj]
                    #        ie. w1[:ii+1]==w2[:jj]
                    insert = 1+dp[ii][jj-1]
                    # replace
                    replace = 1+dp[ii-1][jj-1]
                    # delete: after removing w1[ii] -> w1[:ii]==w2[:jj+1]
                    delete = 1+dp[ii-1][jj]
                    dp[ii][jj] = min(insert, replace, delete)

        return dp[-1][-1]
