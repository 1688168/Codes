#########################
# 20231210
#########################
from heapq import heappush, heappop
from heapq import heappush, heappop, heappushpop


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        mx = 0
        mnh = []
        for ns, ne in intervals:
            if mnh and ns < mnh[0]:
                heappush(mnh, ne)
            else:
                if mnh:
                    heappop(mnh)
                heappush(mnh, ne)
            mx = max(mx, len(mnh))

        return mx

#########################
# 20231203
#########################


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        mxs = 0
        mnq = []

        for st, ed in intervals:
            while mnq and st >= mnq[0]:
                heappop(mnq)
            heappush(mnq, ed)
            mxs = max(mxs, len(mnq))
        return mxs


#########################
# heap solution
#########################


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
