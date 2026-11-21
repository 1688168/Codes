
############################
# 20261121
############################
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events=[]
        for (st, ed) in intervals:
            events.append((st, 1))
            events.append((ed, -1))
        
        events.sort(key=lambda x: (x[0], x[1]))
    
        max_acc = 0
        acc=0
        for event in events:
            acc += event[1]
            max_acc=max(max_acc, acc)
        
        return max_acc
        
############################
# 20231039
############################

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mxn = 0

        ts = []
        for a, b in intervals:
            ts.append((a, 1))
            ts.append((b, -1))

        ts.sort()

        cnt = 0
        for t, c in ts:
            cnt += c
            mxn = max(mxn, cnt)

        return mxn


############################
# sweep line Solution
############################
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for st, ed in intervals:
            times.append((st, 1))
            times.append((ed, -1))

        times.sort()

        mxm = 0
        curr = 0
        for ii in range(len(times)):
            curr += times[ii][1]
            mxm = max(mxm, curr)

        return mxm
