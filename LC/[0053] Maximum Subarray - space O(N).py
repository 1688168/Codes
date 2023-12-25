###########
# 20231225
###########
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        - N: 10^5 -> NlogN
        - presum
        - all subarray: N(N^2)
        - max subarray sum
        dp[ii]: max subarray sum ending @ ii
        -> max(dp)

        Timeseries I: curren state @ ii depends on prev state @ (ii-1)
        dp[ii] = nums[ii] + dp[ii-1] where ii > 0 
        """
        N = len(nums)
        dp = [-math.inf]*N
        for ii in range(N):
            if ii == 0:
                dp[ii] = nums[ii]
                continue

            dp[ii] = nums[ii] + (dp[ii-1] if dp[ii-1] > 0 else 0)

        return max(dp)


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
