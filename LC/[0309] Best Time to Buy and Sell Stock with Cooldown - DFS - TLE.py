class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        # I/O:
        + prices[ii]:
        => max profit

        # Analysis:
        + N= 5000
        ** Bruteforce by dfs: 2^5000
        ** DP: cool down is same as house robber that cannot rob two house in a row
        """

        N=len(prices)
        def dfs(st, prev, ttl):
            if st>=N:
                return ttl
            
            if prev is None: # can only buy
                return max(dfs(st+1, st, ttl-prices[st]), dfs(st+1, prev, ttl))
            else: #can sell
                return max(dfs(st+2, None, ttl+prices[st]), dfs(st+1, prev, ttl))

        return dfs(0, None, 0)

        