
#####################
# 20230114
#####################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        : carry a min sofar value
        : profit=max(p[ii]-minSoFar, profit)
        : minSoFar=min(minSoFar, p[ii])
        """
        profit=0
        minSoFar=prices[0]
        for p in prices:
            profit=max(profit, p-minSoFar)
            minSoFar=min(p, minSoFar)

        return max(0, profit)


#####################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=prices[0]
        mx_profit=0
        for p in prices:
            mx_profit=max(mx_profit, p-min_so_far)
            min_so_far=min(min_so_far, p)

        return mx_profit
