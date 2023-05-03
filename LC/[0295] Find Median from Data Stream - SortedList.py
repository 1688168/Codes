"""
Time: O(N)
Space: O(N)
run time: 22.55%
"""

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sl=SortedList()
        

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
     
        if len(self.sl) %2 == 0:   
            mm=len(self.sl)//2-1        
            return (self.sl[mm]+self.sl[mm+1])/2
        else:
            mm=len(self.sl)//2
            return self.sl[mm]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()