
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
