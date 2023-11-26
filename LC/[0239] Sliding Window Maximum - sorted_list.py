from sortedcontainers import SortedList


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sl = SortedList()

        res = []
        for ii, nn in enumerate(nums):
            sl.add((nn, ii))
            if len(sl) >= k:
                idx = sl.bisect_left((nums[ii-k+1], ii-k+1))
                res.append(sl[-1][0])
                del sl[idx]

        return res
