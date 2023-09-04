# https://www.youtube.com/results?search_query=leetcode+2297
"""
monotonic stack
[1944]
[2282]
"""


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        N = len(nums)
        dp = [math.inf]*N  # dp[ii] min cost to reach ii from statt
        dp[0] = 0
        stk_desc = []
        stk_asc = []
        for ii, vv in enumerate(nums):
            # what's the prev valid jump?
            # Type I: prev ii which nums[ii] <= nums[jj] and all kk in between are < nums[ii]
            # Type II:
            # type I jump to higher or equal
            while stk_desc and vv >= nums[stk_desc[-1]]:
                dp[ii] = min(dp[ii], costs[ii]+dp[stk_desc.pop()])

            while stk_asc and vv < nums[stk_asc[-1]]:  # jump lower
                dp[ii] = min(dp[ii], costs[ii]+dp[stk_asc.pop()])

            stk_desc.append(ii)
            stk_asc.append(ii)

        return dp[-1]
