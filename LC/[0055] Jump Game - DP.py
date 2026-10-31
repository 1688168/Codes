class Solution:
    def canJump(self, nums: list[int]) -> bool:
        N=len(nums)
        dp = [False]*N
        dp[0]=True

        for ii in range(1, N):
            for jj in reversed(range(ii)):
                dp[ii] = dp[jj] and (nums[jj] + jj >=ii)
                if dp[ii]: break

        return dp[-1]