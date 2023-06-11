class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        : feasibility
        : dp[N-1]
        : dp[ii]: feasible to jump to location ii
        : dp[ii] = if exists jj where dp[jj] is True and jj+nums[jj] >= ii
        """
        N = len(nums)
        dp = [False] * N

        dp[0] = True # can you reach location 0? yes

        for ii in range(1, N):
            for jj in reversed(range(ii)):
                if dp[jj] and jj + nums[jj] >= ii:
                    dp[ii] = True
                    break

        return dp[N - 1]

# leetcode submit region end(Prohibit modification and deletion)
