from collections import defaultdict
from heapq import heappush, heappop
from typing import List, DefaultDict, Tuple

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        N=len(paint)
        ## declare/build events [loc, [[dd, flag]]]
        events: DefaultDict[List[Tuple[int, int]]] = defaultdict(list)
        for dd, (st, ed) in enumerate(paint):
            events[st].append((dd, 1))
            events[ed].append((dd, -1))
        
        ret=[0]*N
        mnh: List[int]=[]
        day2freq=defaultdict(int)
        # for each location, find the effective paint day and update contribution
        sorted_loc = sorted(events.keys()) # sorted location
        for ii, loc in enumerate(sorted_loc):
            for [dd, flag] in events[loc]:
                if flag > 0:
                    heappush(mnh, dd)
                    day2freq[dd] += 1
                else:
                    day2freq[dd] -= 1
            
            while mnh and day2freq[mnh[0]] == 0:
                heappop(mnh)
            
            if mnh and ii+1 < len(sorted_loc):
                 ret[mnh[0]] += sorted_loc[ii+1] - loc

        return ret