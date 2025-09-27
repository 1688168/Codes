class MyCalendarThree:
    
    def __init__(self):
        self.map=defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.map[startTime] = self.map.get(startTime,0)+1
        self.map[endTime] = self.map.get(endTime,0)-1
        sum=0
        mx=0
        for kk, vv in sorted(self.map.items()):
            sum += vv
            mx=max(mx, sum)
        
        return mx

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)