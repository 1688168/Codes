class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        # I/O:
        + M houses
        + N colors
        ++ painted or unpainted
        + Target Blocks
        
        # Analysis:
        + current state only dependes on previous state -> Type I DP

        """
        # insert dummy
        houses=[math.inf]+houses   #for prev house
        cost = [[math.inf]] + cost #cost also start from 1 as 0 is dummy

        m=len(houses)

        # declare dp
        dp=[[[math.inf]*(n+1) for _ in range(target+1)] for _ in range(m)]
        
        # initialize DP 
        if houses[1] != 0: #first house is colored? (remember 0 is dummy)
            dp[1][1][houses[1]] = 0 # house 1 already painted, cost=0, all other color on house1 are invalid
        else:
            for kk in range(1, n+1):
                dp[1][1][kk]=cost[1][kk-1]
        

        # populate DP
        for ii in range(2, m): # for each house, 0 is dummy, 1 is initialized
            if houses[ii] != 0: #house is painted
                k = houses[ii] #current color
                for jj in range(1, target+1): #for each target                  
                    for kk in range(1, n+1): # previous color
                        if k==kk: #same color as prev house, same block
                            dp[ii][jj][k] = min(dp[ii][jj][k], dp[ii-1][jj][kk]) # no new cost added to same block
                        else: #diff color as prev house, new block
                            dp[ii][jj][k] = min(dp[ii][jj][k], dp[ii-1][jj-1][kk]) #no cost added to new block
            else: # house is NOT painted
                for jj in range(1, target+1):   # for each block
                    for k in range(1, n+1):    # for each prev color
                        for kk in range(1, n+1): # for each curr color
                            if k==kk: #curr color same as prev color
                                dp[ii][jj][k] = min(dp[ii][jj][k], dp[ii-1][jj][kk] + cost[ii][k-1])
                            else: # curr color diff than prev color
                                dp[ii][jj][k] = min(dp[ii][jj][k], dp[ii-1][jj-1][kk] + cost[ii][k-1])
        
        ans = math.inf

        for kk in range(1, n+1):
            ans = min(ans, dp[-1][-1][kk])
        
        #print(dp)

        return ans if ans!=math.inf else -1
