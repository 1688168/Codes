class MyCalendar:

    def __init__(self):
        self.calendar=[]


    def book(self, start: int, end: int) -> bool:
        #print(" calendar: ", self.calendar, " start: ", start, " end: ", end)
        if len(self.calendar)==0:
            self.calendar.append((start, end))
            return True

        # Binary searc upper bound
        idx = self.bsearch(start)
        #print(" idx: ", idx)
        # idx is the index of the next start time in self.calendar

        """
        1---3
           2----6
              4-----20
        """


        # return False if conflict
                # is prev(idx.end) > start
        if idx >=0 and self.calendar[idx][1] > start:
            return False


        # is idx.start < end
        if idx+1 < len(self.calendar) and self.calendar[idx+1][0] < end:
            return False

        # insert and return True
        self.calendar=self.calendar[:idx+1] + [(start, end)] + self.calendar[idx+1:]
        return True


    def bsearch(self, x):
        """
        : finding the index of the largest value that is smaller than x
        """
        ll, rr, ans = 0, len(self.calendar)-1, -1
        while ll <= rr:
            mm=ll+(rr-ll)//2

            if self.calendar[mm][0] <= x:
                ans=mm
                ll=mm+1
            else:
                rr=mm-1
        return ans


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
