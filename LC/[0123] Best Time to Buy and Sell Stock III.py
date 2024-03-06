"""
# DP Type 1: current state is relating to only previous date state
- template: 
    Kadane: dp[ii]=max(nums[ii], dp[ii-1]+nums[ii])
         -> one previous state
  house robber: dp[ii] = dp_rob/dp_no_rob
         -> two previous state
  buy/sell stock III: bought1, sold1, bought2, sold2 
         -> 4 previous state
         
- only need one state variable for DP type I
- use tmp vars for state transition
"""

###############
# 20231225
###############


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought1 = -prices[0]
        sold1 = 0
        bought2 = -prices[0]
        sold2 = 0

        for ii, pp in enumerate(prices):
            bought1_tmp = bought1
            sold1_tmp = sold1
            bought2_tmp = bought2
            sold2_tmp = sold2

            bought1 = max(bought1_tmp, -pp)
            sold1 = max(sold1_tmp, bought1_tmp+pp)
            bought2 = max(bought2_tmp, sold1_tmp-pp)
            sold2 = max(sold2_tmp, bought2_tmp+pp)

        return max(sold1, sold2)


##############################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        * 4 states
        hold1[k]: max( -price[k], hold1[k-1],) # the profit carried from earlier purchase or purchased today (-p profit)
        sold1[k]: max(hold[k-1]+p, sold1[k-1]) # selling stock1 today or already sold before today
        hold2: max(sold1[k-1]-p, hold2[k-1]) # first stock must be sold before purchasing next, or stock 2 already
               purchased before today
        sold2: max(hold2[k-1]+p, sold2[k-1])

        return max(sold1[n-1], sold2[n-2]), if youc an sell on last day, just sell it to capture any profit
        """

        hold1 = float('-inf')
        sold1 = 0
        hold2 = float('-inf')
        sold2 = 0

        for p in prices:
            hold1_tmp = hold1
            sold1_tmp = sold1
            hold2_tmp = hold2
            sold2_tmp = sold2

            hold1 = max(-p, hold1_tmp)
            sold1 = max(p+hold1_tmp, sold1_tmp)
            hold2 = max(-p+sold1_tmp, hold2_tmp)
            sold2 = max(p+hold2_tmp, sold2_tmp)

        return max(sold1, sold2)
