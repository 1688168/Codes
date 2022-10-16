class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        : return max(not robbing 1st, not robbing last)
        : dp[ii] as max value with house ending @ ii
        : dp[ii] = max(nums[ii]+dp[ii-2], dp[ii-1])
        : not robbing 1st:
        """

        if len(nums)==1:
            return nums[0]

        dp=[0]*len(nums)
        # not robbing 1st
        for ii in range(1, len(nums)):
            dp[ii]=max(nums[ii]+ (dp[ii-2] if ii>=2 else 0), dp[ii-1])

        dp1=dp[-1]

        dp=[0]*len(nums)

        # not robbing last
        for ii in range(len(nums)-1):
            dp[ii] = max(nums[ii]+ (dp[ii-2] if ii-2 >= 0 else 0), dp[ii-1] if ii-1>=0 else 0)

        dp2=dp[-2]


        return max(dp1, dp2)






        
