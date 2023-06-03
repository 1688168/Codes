##############
# 20230603
##############

from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)

        @lru_cache(None)
        def dfs(st, amt):
            if amt == 0: return 0
            if st >= N: return -1
            if amt < 0: return -1

            loc_cnt = float('inf')
            for ii in range(st, N):
                cnt = dfs(ii, amt - coins[ii])
                if cnt != -1:
                    loc_cnt = min(loc_cnt, 1+cnt)
            
            return loc_cnt if loc_cnt != float('inf') else -1
        

        return dfs(0, amount)
        

#####################


from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            return min_cost if min_cost != float('inf') else -1

        return dfs(amount)

==========================
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :param coins:
        :param amount:
        :return:
        """
        if amount < 1: return 0
        # coins.sort(reverse=True)
        # print("conis: ", coins)
        #@lru_cache(None)
        def hp(amt=amount):
            if amt == 0: return 0
            if amt < 0: return -1

            #coin_cnt = amt // coins[st]

            if dp[amt-1] != 0: return dp[amt-1]
            mn_cnt = float('inf')

            #for ii in range(coin_cnt, -1, -1):
            for c in coins:
                cnt = hp(amt - c)

                if cnt >= 0 and 1+cnt < mn_cnt:
                    # print(" st: ", st, " cnt: ", cnt, " ii: ", ii, " mn_cnt: ", mn_cnt)
                    mn_cnt = cnt + 1
                # print(" st: ", st, " cnt: ", cnt, " ii: ", ii, " mn_cnt: ", mn_cnt)

            dp[amt-1] = mn_cnt if mn_cnt != float('inf') else -1

            return dp[amt-1]
        dp=[0]*amount
        return hp()


# ===
# = not sure why this is TLE
# ===
from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :param coins:
        :param amount:
        :return:
        """

        if amount < 1: return 0
        coins.sort(reverse=True)
        #print("conis: ", coins)
        @lru_cache(None)
        def dp(st,amt):
            if amt == 0: return 0
            if amt < 0 or st >= len(coins): return -1

            mxc=amt//coins[st]
            min_cost=float('inf')
            for cc in reversed(range(mxc+1)):
                #print(" ==== cc: ", cc)

                resp=dp(st+1, amt-cc*coins[st])

                if resp != -1:
                    #print(" cc: ", cc, " resp: ", resp)
                    min_cost=min(min_cost, cc+resp)

            return min_cost

        res = dp(0, amount)

        return res if res != float('inf') else -1
