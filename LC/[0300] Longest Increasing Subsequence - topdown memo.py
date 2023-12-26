#############
# 20231226
#############
from functools import lru_cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[-1]*N for _ in range(N)]

        def hp(prev, st):
            if st >= N:
                return 0

            if dp[st][prev] != -1:
                return dp[st][prev]

            tke = 0
            if prev == -1 or nums[st] > nums[prev]:
                tke = 1+hp(st, st+1)

            ntk = hp(prev, st+1)
            dp[st][prev] = max(tke, ntk)
            return dp[st][prev]

        return hp(-1, 0)


######################


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def hp(st=0, prev=-1):
            if st >= len(nums):
                return 0
            if dp[st][prev] != -1:
                return dp[st][prev]

            tke = 0
            if prev == -1 or nums[st] > nums[prev]:
                tke = 1 + hp(st + 1, st)

            ntk = hp(st + 1, prev)

            dp[st][prev] = max(tke, ntk)
            return dp[st][prev]

        dp = [[-1]*len(nums) for _ in range(len(nums))]

        return hp()
