from heapq import heappush, heappop, heappushpop
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
            
            #print("ii: ", ii, " ------------ ")
            if houses[ii] != 0: #house is painted
                kk = houses[ii] #current color
                for jj in range(1, target+1): #for each target   
                     
                    for k in range(1, n+1): # previous color
                        if kk==k: #same color as prev house, same block
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj][k]) # no new cost added to same block
                        else: #diff color as prev house, new block
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj-1][k]) #no cost added to new block                                              
                       
            else: # house is NOT painted
                for jj in range(1, target+1):  # for each block
                    tmp=[]
                    for kk in range(1, n+1):
                        tmp.append((dp[ii-1][jj-1][kk], kk)) #assuming diff color so block-1              
                    tmp.sort()
                    mn1=tmp[0][0]
                    mn2=tmp[1][0]
                    mnk1=tmp[0][1]
                    for kk in range(1, n+1):    # for each curr color                                             
                        # when color is the same
                        dp[ii][jj][kk] = dp[ii-1][jj][kk] + cost[ii][kk-1]

                        # when color is diff
                        if kk != mnk1:
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], mn1+cost[ii][kk-1])
                        else:
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], mn2+cost[ii][kk-1])
                    

        

        #print(dp)
        ans = math.inf

        for kk in range(1, n+1):
            ans = min(ans, dp[-1][-1][kk])        

        return ans if ans!=math.inf else -1
