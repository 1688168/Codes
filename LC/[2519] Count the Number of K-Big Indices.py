#############
# 20230026
#############

from heapq import heappush, heappop, heappushpop


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        """
        * left, right of ii both has k elements smaller
        * consider left only (right is just the reverse and X2 on Time)
        * for each ii, has > k prev smaller elements
        x x x x x

        max_heap[ii] maintain the bottom k elements upto ii
        max_heap[0] the largest bottom k element upto ii
        if max_heap[-1] <= current => count += 1

        * heap insert: logN
        * N inert -> NlogN
        * Time = O(2NlogN)
        * space (O(K))
        """
        N = len(nums)

        def helper(nums):
            mxh = []
            arr = [False]*N
            for ii, vv in enumerate(nums):
                if ii < k:
                    heappush(mxh, -vv)
                    continue

                if nums[ii] > -mxh[0]:
                    arr[ii] = True

                heappushpop(mxh, -vv)

            return arr

        left = helper(nums)
        right = helper(nums[::-1])[::-1]

        return sum([int(a & b) for a, b in zip(left, right)])


###########################################################


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
