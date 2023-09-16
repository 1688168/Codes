
#########
# 20230916: TLE
#########
from collections import Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def dfs(st, status):

            if st >= N:
                return 1

            has_prior_diff_k = False
            for ii in range(st):
                if (status[ii] and 1) and (abs(nums[ii]-nums[st]) == k):
                    has_prior_diff_k = True
                    break

            if has_prior_diff_k:
                return dfs(st+1, status)
            else:
                status2 = status[:]
                status2[st] = 1
                return dfs(st+1, status2) + dfs(st+1, status)

        status = [0] * 1001
        return dfs(0, status)-1
