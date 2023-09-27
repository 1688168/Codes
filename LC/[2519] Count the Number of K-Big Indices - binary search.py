###############
# 20230926
###############
from bisect import bisect_left


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        """
        left[ii]: True if nums[:ii] has more than k elements
        """
        N = len(nums)

        def helper(nums):
            inserts = []
            ans = [False]*N
            for ii in range(N):
                idx = bisect_left(inserts, nums[ii])
                if idx >= k:
                    ans[ii] = True
                inserts.insert(idx, nums[ii])
            return ans

        left = helper(nums)
        right = helper(nums[::-1])[::-1]

        return sum([int(a & b) for a, b in zip(left, right)])


########################################


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        def helper(nums):
            N = len(nums)
            res = [False]*N
            insert = []
            for ii, vv in enumerate(nums):
                idx = bisect_left(insert, vv)
                if idx >= k:
                    res[ii] = True

                insert.insert(idx, vv)

            return res

        left = helper(nums)
        right = helper(nums[::-1])[::-1]

        # return sum([int(left[ii] and right[ii]) for ii in range(len(nums))])
        return sum(a & b for a, b in zip(left, right))
