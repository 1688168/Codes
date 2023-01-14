import bisect

class MyCalendar:

    def __init__(self):
        self.calendar=[]
        

    def book(self, start: int, end: int) -> bool:
        if len(self.calendar) == 0:
            self.calendar.append((start, end))
            return True
        
        idx = bisect.bisect_right(self.calendar, start, key=lambda x: x[0])
        idx-=1

        if idx==-1:
            if end <= self.calendar[0][0]:
                self.calendar=[(start, end)]+self.calendar
                return True
            else:
                return False
        
        print(" got idx: ", idx)
        if idx >= 0 and start < self.calendar[idx][1]:
            return False
        
        # insert in the middle
        if idx + 1 < len(self.calendar) and end > self.calendar[idx+1][0]:           
            return False

        self.calendar=self.calendar[:idx+1] + [(start, end)] + self.calendar[idx+1:]

        # # insert in the end
        # if idx >= len(self.calendar)-1 and start >= self.calendar[-1][1]:
        #     self.calendar.append((start, end))
        #     return True

        return True
    
