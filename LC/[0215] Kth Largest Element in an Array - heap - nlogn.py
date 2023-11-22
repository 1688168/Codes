from heapq import heappush, heappop, heappushpop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mnh = []
        for ii, vv in enumerate(nums):
            if ii < k:
                heappush(mnh, vv)
                continue

            heappushpop(mnh, vv)

        return mnh[0]
