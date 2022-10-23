class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=prices[0]
        mx_profit=0
        for p in prices:
            mx_profit=max(mx_profit, p-min_so_far)
            min_so_far=min(min_so_far, p)

        return mx_profit
