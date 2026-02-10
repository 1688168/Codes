# from __future__ import annotations

from collections import Counter, defaultdict
from heapq import heappop, heappush
from typing import DefaultDict, List, Tuple

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Sweep line over x-coordinates.
        Use a max-heap of active heights (stored as negative values) and a Counter
        for lazy deletions of heights that have ended.
        """
        # Build events: at x, add list of starting heights and ending heights.
        # We'll encode starts as negative heights so they sort before ends at the same x.
        
        # python type annotation, and declaration events: events: DefaultDict[int, List[int]] = defaultdict(list)
        events: DefaultDict[int, List[int]] = defaultdict(list)
        for left, right, height in buildings:# process each building and construct all events (turning points)
            events[left].append(-height)  # start event
            events[right].append(height)  # end event

        # Active heights: max-heap via negative values
        heap: List[int] = [0]  # 0 means ground level (height 0) --- given a height, sort
        active = Counter({0: 1}) # count numf of heights at each ii

        result: List[List[int]] = [] # define return var
        prev_max = 0

        for x in sorted(events): #sort events and process each (for each ii --- building start/end point)
            # Apply all events at x.
            # Sort so starts (negative) are processed before ends (positive)
            # to avoid generating extra points at the same x.
            for h in sorted(events[x]): # for each height at this point
                if h < 0:  # start
                    height = -h
                    active[height] += 1
                    heappush(heap, -height) # maintain the max h
                else:      # end
                    height = h
                    active[height] -= 1 # count number of hight at this building point

            # Pop heap while the top height is no longer active (lazy deletion).
            while heap and active[-heap[0]] == 0:
                heappop(heap)

            curr_max = -heap[0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result


"""
# Problem Statements
* building[i]=[left, right, height]
       
         ----- height
         -----
0 ---left-----right

* no equal line

# Analysis
* N=10^4 -> nlogn
* building is already sorted
* we are given ranges -> we need to do range aggregation -> sweepline
1. collect events for a turning points: x:[+/-h]
2. for each turning points: could be 0 (start or end), could be H
"""