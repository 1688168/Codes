
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
