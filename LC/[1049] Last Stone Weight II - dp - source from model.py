class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        0/1 knapsack solution (similar to 494)
        """
        ttl = sum(stones)
        dp = [False]*(ttl*2+2)
        offset = ttl

        # we will be looping from 1, so initialize stones[0]
        dp[stones[0]+offset] = True
        dp[-stones[0]+offset] = True

        N = len(stones)
        for ii in range(1, N):
            dp_new = [False]*(ttl*2+2)
            for ss in range(-ttl, ttl+1):
                if -ttl <= ss-stones[ii]:
                    dp_new[ss+offset] = dp_new[ss+offset] or dp[ss-stones[ii]+offset]
                if ss+stones[ii] <= ttl:
                    dp_new[ss+offset] = dp_new[ss+offset] or dp[ss+stones[ii]+offset]
            dp = dp_new
        
        for ss in range(ttl+1):
            if dp[ss+offset]: return ss
 
        return 0
    