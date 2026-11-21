
class Obj:
    def __init__(self, st, ed):
        self.st=st
        self.ed=ed
    def __lt__(self, other):
        if self.ed==other.ed:
            return self.st < other.st
        else:
            return self.ed < other.ed


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        mnh=[]
        mx=0
        intervals.sort()
        
        for (st, ed) in intervals:
            if mnh and st < mnh[0].ed:
                heappush(mnh, Obj(st, ed))
            else:
                if mnh:
                    heappop(mnh)
                
                heappush(mnh, Obj(st, ed))
            mx=max(mx, len(mnh))
        return mx