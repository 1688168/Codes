################
# 20231007
################

from functools import lru_cache


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


#######################################


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        @lru_cache(None)
        def dp(st=0, mny=coins):
            if st >= len(costs):
                return 0

            buy = 0
            if mny >= costs[st]:
                buy = 1+dp(st+1, mny-costs[st])
            no_buy = dp(st+1, mny)

            return max(buy, no_buy)

        return dp()
