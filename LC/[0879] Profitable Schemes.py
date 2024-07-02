class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        + n: max members alowed
        + minProfit: sum(subset) > minProfit to be profitable
        + group[ii]: num of members required
        + profit[ii]: profit @ crime[ii]
        
                         N
        x x x x x ii x x x
        j member
        k profit

        """
        M=int(1e9)+7

        N = len(profit)
        M = minProfit

        dp=[[[0]*N for _ in range(M+1)] for _ in range(profit+1)]