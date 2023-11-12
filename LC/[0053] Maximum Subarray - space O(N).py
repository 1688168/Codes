###########
# 20230919
###########
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        """
        dp[ii]=max subarray sum ending @ ii
        """
        mx = -math.inf
        for ii in range(N):
            dp[ii] = max(nums[ii], nums[ii]+(dp[ii-1] if ii >= 1 else 0))
            mx = max(mx, dp[ii])

        return mx


#####################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadan's algorithm
        # dp[ii]: max subarray sum ending @ ii
        # dp[ii]=max(dp[ii-1]+dp[ii], dp[ii])

        mxs = float('-inf')
        dp = float('-inf')
        for ii in range(len(nums)):
            if ii == 0:
                dp = nums[ii]
            else:
                dp = max(dp+nums[ii], nums[ii])

            mxs = max(mxs, dp)

        return mxs
