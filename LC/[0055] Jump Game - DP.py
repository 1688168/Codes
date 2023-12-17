class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        dp[ii] = True if dp[jj]+ nums[jj] >= N=-1
        """
        N = len(nums)
        dp = [False]*N
        dp[0] = True
        for ii in range(N):
            for jj in reversed(range(ii)):
                if dp[jj] and jj+nums[jj] >= ii:
                    dp[ii] = True
                    break

        return dp[-1]
