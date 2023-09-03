"""
https://youtu.be/xi4QVECpmxQ

"""
from heapq import heappush, heappop, heappushpop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mxh=[]
        for (x, y) in points:
            if len(mxh) < k:
                heappush(mxh, (-(pow(x, 2)+pow(y, 2)), (x, y)))
                continue
            
            heappushpop(mxh, (-(pow(x, 2)+pow(y, 2)), (x, y)))
        
        return [point for dist, point in mxh]
    


# customize point obj
from heapq import heappush, heappop


class point:
    def distSq(self, x, y): return pow(x,2)+pow(y, 2)
    def __init__(self, x, y):
        self.dist=self.distSq(x, y)
        self.x=x
        self.y=y
    
    def __lt__(self, other):
        return self.dist > other.dist
        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:        
        mnq=[]
        
        for p in points:
            heappush(mnq, point(p[0], p[1]))
            if len(mnq) > k:
                heappop(mnq)
        
        
        res=[]
        for p in mnq:
            res.append([p.x, p.y])
        
        return res
        
        