class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        : dp[ii] = max(num[ii] + dp[ii-2], dp[ii-1])
        """
        N=len(nums)
        dp=[0]* N
        
        dp[0]=nums[0]

        for ii in range(1, N):
            dp[ii] = max(nums[ii]+ (dp[ii-2] if ii-2 >= 0 else 0), dp[ii-1] if ii-1>=0 else 0)

        return dp[N-1]
