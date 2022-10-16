from functools import lru_cache
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        @lru_cache(None)
        def dp(st=0, mny=coins):
            if st >= len(costs): return 0

            buy=0
            if mny >= costs[st]:
                buy = 1+dp(st+1, mny-costs[st])
            no_buy=dp(st+1, mny)

            return max(buy, no_buy)


        return dp()	
