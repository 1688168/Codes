#########################
# heap solution
#########################
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0: return 0
        intervals.sort()
        mnq=[]

        for ns, ne in intervals:
            if len(mnq) > 0 and ns >= mnq[0]:

                heappop(mnq)
            heappush(mnq, ne)


        return len(mnq)

    
############################
### sweep line Solution
############################
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times=[]
        for st, ed in intervals:
            times.append((st, 1))
            times.append((ed, -1))

        times.sort()

        mxm=0
        curr=0
        for ii in range(len(times)):
            curr += times[ii][1]
            mxm=max(mxm, curr)

        return mxm
