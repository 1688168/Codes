from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # events[x] = list of (height, flag) where flag=+1 start, flag=-1 end
        events = defaultdict(list)
        for L, R, H in buildings:
            events[L].append((H, 1))    # starting event
            events[R].append((H, -1))   # ending event

        # We need a "multiset with max" in Python.
        # Use a max-heap (store -height) + a frequency map for lazy deletions.
        heap = [0]                     # max height is -heap[0]; start with ground
        freq = defaultdict(int)
        freq[0] = 1

        res = []

        for x in sorted(events.keys()):
            # process all events at this x
            for h, flag in events[x]:
                if flag == 1:
                    freq[h] += 1
                    heappush(heap, -h)
                else:
                    freq[h] -= 1

            # clean up heap top if it refers to heights no longer active
            while heap and freq[-heap[0]] == 0:
                heappop(heap)

            curr_h = -heap[0] if heap else 0

            # record key point if height changes
            if not res or res[-1][1] != curr_h:
                res.append([x, curr_h])

        return res