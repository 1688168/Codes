from heapq import heappush, heappop, heappushpop


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mnq = []
        for n in nums:
            if len(self.mnq) < k:
                heappush(self.mnq, n)
            else:
                heappushpop(self.mnq, n)

        self.k = k

    def add(self, val: int) -> int:
        if len(self.mnq) < self.k:
            heappush(self.mnq, val)
        else:
            heappushpop(self.mnq, val)
        return self.mnq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
