class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ttl = sum(stones) #if all take in as postive (solution space)
        dp = [False]*(ttl*2+2)
        offset = ttl

        N = len(stones)
        for ii, ww in enumerate(stones) : #contributing model
            if ii==0:
                dp[ww+offset]=True
                dp[-ww+offset]=True
                continue

            dp_new = [False]*(ttl*2+2)
            for ss in range(-ttl, ttl+1):#current wight is ss
                # adding current
                if ss+ww<=ttl: #current with new stone
                    dp_new[ss+ww+offset] = dp_new[ss+ww+offset] or dp[ss+offset]

                # substracting
                if -ttl <= ss-ww:
                    dp_new[ss-ww+offset] = dp_new[ss-ww+offset] or dp[ss+offset]
            dp = dp_new.copy()

        for ss in range(ttl+1):
            if dp[ss+offset]:
                return ss

        return 0
