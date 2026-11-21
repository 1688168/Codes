import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heap[0]


##########
# 20261121
##########
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapify(mxq := [-nn for nn in nums])
        for _ in range(k-1): heappop(mxq)
        return -mxq[0]