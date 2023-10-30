#########################
# heap solution
#########################
from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort()
        mnq = []

        for ns, ne in intervals:
            if len(mnq) > 0 and ns >= mnq[0]:

                heappop(mnq)
            heappush(mnq, ne)

        return len(mnq)


#
