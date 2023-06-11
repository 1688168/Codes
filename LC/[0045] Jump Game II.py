
#####################
# 20230611: greedy solution
#####################

class Solution:
    def jump(self, nums: List[int]) -> int:
        N=len(nums)
        steps=0 #num of steps taken
        ll=rr=0 #range which can be achieved by jumpping nums of "steps"
     
        while rr < N-1: #because answer is guaranteed existing
            maxRange=0
            for ii in range(ll, rr+1):
                maxRange=max(maxRange, ii+nums[ii])
            ll=rr+1
            rr=maxRange
            steps+=1

        return steps
        



#####################
# 20230611: TLE
#####################

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        dp[i] = min jump to reach i
              = dp[j]+1            
        """

        N = len(nums)
        dp=[float('inf')]*N
        dp[0]=0
        for ii in range(N):
            for jj in reversed(range(ii)):
                if jj+nums[jj] >= ii: dp[ii]=min(dp[ii], dp[jj]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1