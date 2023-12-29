class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        N=
        => shortest string such that both str1, str2 are its subsequence
        """
        s1 = '#'+str1
        s2 = '#'+str2
        N1 = len(s1)
        N2 = len(s2)
        dp = [[math.inf]*N2 for _ in range(N1)]

        # initial states
        for ii in range(N1):
            dp[ii][0] = ii
        for ii in range(N2):
            dp[0][ii] = ii

        for ii in range(1, N1):
            for jj in range(1, N2):
                if s1[ii] == s2[jj]:
                    dp[ii][jj] = dp[ii-1][jj-1]+1
                else:
                    """
                    x x x x ii 
                    y y y y y y jj x
                    """
                    add_s1 = dp[ii-1][jj]
                    add_s2 = dp[ii][jj-1]

                    dp[ii][jj] = 1+min(add_s1, add_s2)

        # reconstruct the path
        res = []
        ii, jj = N1-1, N2-1
        while ii > 0 and jj > 0:
            """
            x x x x x a
            y y y b
            """
            # if dp[ii][jj]==(dp[ii-1][jj-1]+1): << why this is not working?
            # s1[ii]==s2[jj] means dp[ii][jj]==dp[ii-1][jj-1], but not the other way around
            if s1[ii] == s2[jj]:
                res.append(s1[ii])
                ii -= 1
                jj -= 1
            elif dp[ii][jj] == (dp[ii-1][jj]+1):
                res.append(s1[ii])
                ii -= 1
            else:
                res.append(s2[jj])
                jj -= 1

        while ii > 0:
            res.append(s1[ii])
            ii -= 1
        while jj > 0:
            res.append(s2[jj])
            jj -= 1

        # print("res: ", "".join(res))
        return "".join(res[::-1])
