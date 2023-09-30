# Memory Limit Exceeded

from functools import lru_cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        :20210925: adding cache
        :param nums:
        :return:
        : Time: O(N^2).  T(N)=T(n-1)+T(n-1)
        """

        @lru_cache(None)
        def hp(st=0, prev=-1):
            if st >= len(nums):
                return 0

            tke = 0
            if prev == -1 or nums[st] > nums[prev]:
                tke = 1 + hp(st + 1, st)

            ntk = hp(st + 1, prev)

            return max(tke, ntk)

        return hp()
