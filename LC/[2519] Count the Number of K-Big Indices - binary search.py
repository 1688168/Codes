from bisect import bisect_left


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

        return sum([int(left[ii] and right[ii]) for ii in range(len(nums))])
