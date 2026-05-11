class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []

        for s, e in intervals:
            events.append((s, 1))      # interval starts
            events.append((e, -1))     # interval ends

        # Important: process starts before ends at the same point
        events.sort(key=lambda x: (x[0], -x[1]))

        res = []
        active = 0
        start = None

        for x, delta in events:
            if active == 0:
                start = x

            active += delta

            if active == 0:
                res.append([start, x])

        return res