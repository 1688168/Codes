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
        events: DefaultDict[int, List[int]] = defaultdict(list)
        for left, right, height in buildings:
            events[left].append(-height)  # start event
            events[right].append(height)  # end event

        # Active heights: max-heap via negative values
        heap: List[int] = [0]  # 0 means ground level (height 0)
        active = Counter({0: 1})

        result: List[List[int]] = []
        prev_max = 0

        for x in sorted(events):
            # Apply all events at x.
            # Sort so starts (negative) are processed before ends (positive)
            # to avoid generating extra points at the same x.
            for h in sorted(events[x]):
                if h < 0:  # start
                    height = -h
                    active[height] += 1
                    heappush(heap, -height)
                else:      # end
                    height = h
                    active[height] -= 1

            # Pop heap while the top height is no longer active (lazy deletion).
            while heap and active[-heap[0]] == 0:
                heappop(heap)

            curr_max = -heap[0]
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max

        return result