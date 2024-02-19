################
# 20240218
################
from heapq import heappush, heappop, heappushpop
class MedianFinder:

    def __init__(self):
        self.mxh=[]
        self.mnh=[]


    def rebalance(self):
        while len(self.mxh) > len(self.mnh)+1:
            heappush(self.mnh, -heappop(self.mxh))
        
        while len(self.mnh) > len(self.mxh):
            heappush(self.mxh, -heappop(self.mnh))


    def addNum(self, num: int) -> None:
        if not self.mxh or num < -self.mxh[0]:
            heappush(self.mxh, -num)
        else:
            heappush(self.mnh, num)
        
        self.rebalance()

    def findMedian(self) -> float:
        if len(self.mxh) > len(self.mnh):
            return -self.mxh[0]
        
        else:
            return (-self.mxh[0]+self.mnh[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
################
# 20231126: 67.49%
################
from heapq import *
from heapq import heappush, heappop, heappushpop


class MedianFinder:

    def __init__(self):
        self.mxq = []  # 0~mid
        self.mnq = []  # mid~max

    def addNum(self, num: int) -> None:

        if self.mxq and num > self.mxq[0]*-1:
            heappush(self.mnq, num)
        else:
            heappush(self.mxq, -num)

        while self.mxq and len(self.mxq) - len(self.mnq) > 1:
            heappush(self.mnq, -heappop(self.mxq))

        while self.mnq and len(self.mnq) - len(self.mxq) > 1:
            heappush(self.mxq, -heappop(self.mnq))

    def findMedian(self) -> float:
        if self.mxq and len(self.mxq) == len(self.mnq):
            return (self.mxq[0]*-1 + self.mnq[0])/2
        else:
            if len(self.mxq) > len(self.mnq):
                return -1*self.mxq[0]
            else:
                return self.mnq[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


#############
20230430 redo, T: 55.66
#############


class MedianFinder:

    def __init__(self):
        self.mxh = []
        self.mnh = []

    def rebalance(self, mxh, mnh):
        lx, ls = len(mxh), len(mnh)
        if lx <= (ls+1):
            if len(self.mnh) > 0 and len(self.mxh) > 0 and (-self.mxh[0]) > self.mnh[0]:
                topx = -self.mxh[0]
                topn = self.mnh[0]

                heappop(self.mxh)
                heappop(self.mnh)
                heappush(self.mxh, -topn)
                heappush(self.mnh, topx)
        else:
            heappush(self.mnh, -self.mxh[0])
            heappop(self.mxh)

    def addNum(self, num: int) -> None:
        if len(self.mxh) <= len(self.mnh):
            heappush(self.mxh, -num)
        else:
            heappush(self.mnh, num)
        self.rebalance(self.mxh, self.mnh)

    def findMedian(self) -> float:
        if (len(self.mxh)+len(self.mnh)) % 2 == 0:
            return (-self.mxh[0]+self.mnh[0])/2
        else:
            return -self.mxh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


###################
class MedianFinder:

    def __init__(self):
        """
        : keep mnq size 1 > or equal do mxq .size
        : start from push to mnq.
        : anything greater than mnq[0], push to mnq and rebalance

        """
        self.mnq = []
        self.mxq = []

    def addNum(self, num: int) -> None:
        def rebalance():
            if len(self.mnq) > len(self.mxq)+1:
                heappush(self.mxq, heappop(self.mnq)*-1)
            elif len(self.mxq) > len(self.mnq):
                heappush(self.mnq, heappop(self.mxq)*-1)

        if not self.mnq or num > self.mnq[0]:
            heappush(self.mnq, num)
        else:
            heappush(self.mxq, -num)

        rebalance()

    def findMedian(self) -> float:
        if len(self.mnq) > len(self.mxq):
            return self.mnq[0]
        else:
            return (self.mnq[0]+(-self.mxq[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
