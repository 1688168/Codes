###########
# 20230611
###########
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit=0
        prevLow=float('inf')

        for p in prices:
            if p > prevLow:
                totalProfit += p-prevLow
                prevLow = p
            else:
                prevLow=min(p, prevLow)


        return totalProfit


###########
# 20221106
###########
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        capture all profit opportunities
        """
        min_so_far=float('inf')
        ttl_profit=0
        for p in prices:
            min_so_far=min(p, min_so_far)

            if p > min_so_far:
                ttl_profit += (p-min_so_far)
                min_so_far=p

        return ttl_profit
        
##################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo=prices[0]
        hi=prices[0]
        ttp=0
        ii=0
        while ii < len(prices):
            while ii+1 < len(prices) and prices[ii+1] <= prices[ii]: ii += 1

            lo=prices[ii]
            while ii+1 < len(prices) and prices[ii+1] >= prices[ii]: ii += 1
            hi=prices[ii]

            ttp += (hi - lo)
            ii += 1

        return ttp
