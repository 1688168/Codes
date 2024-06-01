#############
# 20240601
#############
from  heapq import heappush, heappop, heappushpop
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N=len(costs)
        K=len(costs[0])

        dp=[[0]*K for _ in range(N)] #min cost ending @ color jj where 0<jj< kk

        # initialize dp
        mxq=[]
        for jj in range(K): 
            dp[0][jj]=costs[0][jj]
            if len(mxq) < 2 or dp[0][jj] < -mxq[0][0]:
                heappush(mxq, (-dp[0][jj], jj))
            if len(mxq) > 2: heappop(mxq)

        
        for ii in range(1, N):
            # find the top 2 min
            min1_jj=mxq[1][1]
            min2_jj=mxq[0][1]
            mxq=[]
            for jj in range(K):             
                dp[ii][jj] = costs[ii][jj] + (dp[ii-1][min1_jj] if min1_jj != jj else dp[ii-1][min2_jj]) 
                if len(mxq) < 2 or dp[ii][jj] < -mxq[0][0]:
                    heappush(mxq, (-dp[ii][jj], jj))
                if len(mxq) > 2: heappop(mxq)


        return min(dp[-1])
        

#########################
from  heapq import heappush, heappop, heappushpop
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        N=len(costs)
        K=len(costs[0])

        dp=[[0]*K for _ in range(N)] #min cost ending @ color jj where 0<jj< kk

        # initialize dp
        for jj in range(K): dp[0][jj]=costs[0][jj]

        
        for ii in range(1, N):
            # find the top 2 min
            mxq=[]
            for jj in range(K):
                if len(mxq) < 2 or dp[ii-1][jj] < -mxq[0][0]:
                    heappush(mxq, (-dp[ii-1][jj], jj))
                if len(mxq) > 2: heappop(mxq)
            for jj in range(K):
                min1_jj=mxq[1][1]
                min2_jj=mxq[0][1]

                dp[ii][jj] = costs[ii][jj] + (dp[ii-1][min1_jj] if min1_jj != jj else dp[ii-1][min2_jj]) 


        return min(dp[-1])
        