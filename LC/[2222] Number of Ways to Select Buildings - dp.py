######################
# 20231008
######################
class Solution:
    def numberOfWays(self, s: str) -> int:

        s = '#'+s
        N = len(s)

        dp = [[[0]*2 for _ in range(4)] for _ in range(N)]

        dp[0][0][0] = 1
        dp[0][0][1] = 1

        for ii in range(1, N):
            for jj in range(4):
                for kk in range(2):
                    if jj == 0:
                        dp[ii][jj][kk] = dp[ii-1][jj][kk]
                    else:
                        dp[ii][jj][kk] = dp[ii-1][jj][kk]
                        if int(s[ii]) == kk:
                            dp[ii][jj][kk] += dp[ii-1][jj-1][1-int(s[ii])]

        return dp[-1][-1][0]+dp[-1][-1][1]


###############################################

class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        Number of ways: -> number of ways to climb stair
        at each index II -> make decision
        we can derive current state via finished sub-problems -> DP
        dp[ii][jj][kk]:  number of valid ways @ ii to select jjth buildings which is type kk 
        """
        s = '#' + s
        N = len(s)
        building_num = 3
        dp = [[[0]*2 for _ in range(building_num+1)] for _ in range(N)]

        # define initial state
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        for ii in range(1, N):  # for each building select or not select
            for jj in range(building_num+1):  # select 0, 1, 2, 3 buildings
                for kk in range(2):  # building type 0 or 1
                    if jj == 0:
                        dp[ii][jj][kk] = dp[ii-1][jj][kk]
                    else:  # jj >= 1
                        # not select
                        dp[ii][jj][kk] = dp[ii-1][jj][kk]

                        # select
                        if ord(s[ii]) - ord('0') == kk:
                            dp[ii][jj][kk] += dp[ii-1][jj-1][1-kk]

        return dp[-1][-1][1] + dp[-1][-1][0]


###############################################
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
