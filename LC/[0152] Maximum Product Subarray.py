class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        : nums - ints
        : -> subarray with largest product
        : -> return the product
        : ----
        : Kadane's Algorithm
        : -> max subarray sum: dp[ii]=max(dp[ii-1]+num[ii], num[ii])
        : -> max subarray product:
        : dp1=1 #hold max ending @ ii
        : dp2=1 #hold min ending @ ii
        : dp1=max(dp1[ii-1]*nums[ii], dp2[ii-1]*nums[ii], nums[ii])
        : dp2=min(dp2[ii-1]*nums[ii], dp2[ii-1]*nums[ii], nums[ii])
        : res=max(dp1, res)
        """

        dp1=1
        dp2=1
        res=float('-inf')

        for nn in nums:
            tmp1=dp1
            tmp2=dp2
            dp1=max(nn, tmp1*nn, tmp2*nn)
            dp2=min(nn, tmp1*nn, tmp2*nn)
            res=max(res, dp1)
        
        return res