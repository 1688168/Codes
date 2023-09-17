class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        * decision criteria:
        - how many building have been selected
        - what is the type of the last selected building

        * dp[ii][jj][kk]
        the total number of plans: 
        after looking at the ii-th building, 
        given there have been jj buildings selected, 
        and the last selected building type is kk


        dp[ii][jj]][kk]=dp[i-1][jj][kk] if not select ii-th + dp[ii-1][jj-1][1-k] if select ith & ith building must be type k

        return dp[n][3][0] + dp[n][3][1]
        """
        N = len(s)

        s = '#'+s

        dp = [[[0]*2 for _ in range(4)] for _ in range(N+1)]

        dp[0][0][0] = 1
        dp[0][0][1] = 1

        for ii in range(1, N+1):
            for jj in range(4):
                for kk in range(2):
                    dp[ii][jj][kk] = dp[ii-1][jj][kk]

                    if jj >= 1 and ord(s[ii])-ord('0') == kk:
                        dp[ii][jj][kk] += dp[ii-1][jj-1][1-kk]

        return dp[N][3][0] + dp[N][3][1]
