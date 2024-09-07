class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        N=len(stones)
        dp=[math.inf]*(30*100+1) 
        """
        * dp[jj]: remaining weight using upto iith stone
        """
        
        for ii, ww in enumerate(stones): # each resource [0, N-1]
            dp_old=dp.copy()
            if ii==0:
                dp[ww]=ww
                continue
            for jj in range(3000): #contribution model
                if dp[jj]==math.inf: continue
                # adding
                if jj+ww <= 3000:
                    dp[jj+ww] = min(dp[jj+ww], dp_old[jj]+ww)
                # substracting
                if jj-ww >=0:
                    dp[jj-ww] = min(dp[jj-ww], dp_old[jj]-ww)

        for ii in range(3000):
            if dp[ii] != math.inf: return dp[ii]
        

        return -1
        