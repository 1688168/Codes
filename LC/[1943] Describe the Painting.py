from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)   # position -> delta color sum

        for seg in segments:
            l, r, c = seg
            events[l] += c
            events[r] -= c

        rets: List[List[int]] = []
        cnt = 0
        start = -1
        end = -1

        for pos in sorted(events.keys()):
            diff = events[pos]

            if start == -1:
                start = pos
            else:
                end = pos              
                rets.append([start, end, cnt])
                start = end

            cnt += diff

            if cnt == 0:
                start = -1

        return rets