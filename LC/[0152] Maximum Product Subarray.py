class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        : Kadane's algorithm -> max subarray sum
        : dp[ii] = max(dp[ii-1]+nums[ii], nums[ii])
        : x [x x x x ii] x
        : nii is postive, we want dp[ii-1] postive
        : nii is negative, we wnat dp[ii-1] min
        : keep both dp1 for max, dp2 for min
        """
        dp1=1
        dp2=1
        N=len(nums)
        res=float('-inf')
        for nn in nums:
            tmp1=dp1
            tmp2=dp2
            dp1=max(tmp1*nn, tmp2*nn, nn)
            dp2=min(tmp1*nn, tmp2*nn, nn)
            res=max(res, dp1)

        return res

            
