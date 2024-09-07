class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        0/1 knapsack solution (similar to 494)
        """
        ttl = sum(stones)
        dp = [False]*(ttl*2+2)
        offset = ttl

        # we will be looping from 1, so initialize stones[0]
        dp[stones[0]+offset] = 1
        dp[-stones[0]+offset] = 1

        N = len(stones)
        for ii in range(1, N):
            dp2 = [False]*(ttl*2+2)
            for s in range(-ttl, ttl+1):
                if -ttl <= s-stones[ii] <= ttl:
                    dp2[s+offset] = dp2[s+offset] or dp[s-stones[ii]+offset]
                if -ttl <= s+stones[ii] <= ttl:
                    dp2[s+offset] = dp2[s+offset] or dp[s+stones[ii]+offset]
            dp = dp2

        for s in range(ttl+1):
            if dp[s+offset]:
                return s

        return 0
