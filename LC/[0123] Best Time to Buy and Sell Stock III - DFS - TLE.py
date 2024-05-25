class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        + prices[ii]: price on day ii
        => Max(profit) - at most two transactions
        + N=10^5
        # bruteforce
        # DP - single array: Type I or Type II
        let state={0: zero transaction,
                   1: bought 1,
                   2: sold1,
                   3: bought 2,
                   4: sold2}
        """
        N=len(prices)
        def dfs(state, st, ttl):
            if st >= N: return ttl

            if state==0:
                return max(dfs(0, st+1, ttl), dfs(1, st+1, ttl-prices[st]))
            elif state==1:
                return max(dfs(1, st+1, ttl), dfs(2, st+1, ttl+prices[st]))
            elif state==2:
                return max(dfs(2, st+1, ttl), dfs(3, st+1, ttl-prices[st]))
            elif state==3:
                 return max(dfs(3, st+1, ttl), dfs(4, st+1, ttl+prices[st]))
            elif state==4:
                 return ttl


        
        return dfs(0, 0, 0)
        