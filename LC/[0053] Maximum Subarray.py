class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadan's algorithm
        # dp[ii]: max subarray sum ending @ ii
        # dp[ii]=max(dp[ii-1]+dp[ii], dp[ii])

        mxs=float('-inf')
        dp=float('-inf')
        for ii in range(len(nums)):
            if ii==0:
                dp=nums[ii]
            else:
                dp=max(dp+nums[ii], nums[ii])

            mxs=max(mxs, dp)

        return mxs
