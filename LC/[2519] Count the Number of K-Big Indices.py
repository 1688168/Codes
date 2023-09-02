from heapq import heappushpop, heappush, heappop


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        """
        * How do we precalc if left and right has k elements < self?
        * consider left only (right is just reverse)
        => how to pre-calc for each index ii in nums, if k+ elements in the left < nums[ii]
        * for each ii
          maintain a max heap with k elements only
          if nums[ii] > heap[0] -> True
        * reverse above for right hand side
        """

        def helper(nums):
            N = len(nums)
            res = [False] * N
            mxh = []

            for ii, vv in enumerate(nums):
                if len(mxh) < k:
                    heappush(mxh, -vv)
                    continue

                if vv > -mxh[0]:
                    res[ii] = True
                heappushpop(mxh, -vv)

            return res

        left = helper(nums)
        right = helper(nums[::-1])[::-1]

        return sum([int(left[ii] and right[ii]) for ii in range(len(nums))])
