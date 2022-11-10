from heapq import heappush, heappop
class MyCalendarThree:

    def __init__(self):
        self.map={}

    def book(self, startTime: int, endTime: int) -> int:
        self.map[startTime]=self.map.get(startTime, 0) + 1
        self.map[endTime]=self.map.get(endTime, 0) - 1
        ttl=0
        arr=[(kk, vv) for kk, vv in self.map.items()]
        arr.sort()
        mxt=0
        for tt, vv in arr:
            ttl+=vv
            mxt=max(ttl, mxt)

        return mxt




# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
