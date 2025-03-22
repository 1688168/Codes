###########
# 20240303
###########

import numpy as np
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        * max subarray sum - Kadane
        + dp[ii]: max subarray sum with index ending @ ii
        + dp[ii]=max(nums[ii], dp[ii-1]+nums[ii])
        """
        N=len(nums)
        dp=0
        
        ans=-int(1e9)
        ans=-float('inf')
        ans = -np.inf
        for ii, nn in enumerate(nums):
            dp=max(dp+nn, nn)
            ans=max(ans, dp)

        return ans


        

###########
# 20230920
###########
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = -math.inf
        """
        dp[ii]=max subarray sum ending @ ii
        """
        mx = -math.inf
        for ii in range(N):
            dp = max(nums[ii], nums[ii]+dp)
            mx = max(mx, dp)

        return mx
