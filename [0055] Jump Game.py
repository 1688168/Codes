
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        : feasibility
        : dp[N-1]
        """
        N = len(nums)
        dp = [False] * N

        dp[0] = True

        for ii in range(1, N):
            # dp[ii]=any([True if dp[jj] and jj+nums[jj] >= ii else False for jj in reversed(range(ii))])
            for jj in reversed(range(ii)):
                if dp[jj] and jj + nums[jj] >= ii:
                    dp[ii] = True
                    break

        return dp[N - 1]

# leetcode submit region end(Prohibit modification and deletion)
