from collections import Counter, deque
from heapq import heappush, heappop, heappushpop


class Solution:
    def reorganizeString(self, s: str) -> str:
        c2f = Counter(s)
        dq = deque()
        mxq = []

        for cc, ff in c2f.items():
            heappush(mxq, (-ff, cc))

        res = ""
        while mxq:
            """
            mxq: a, b
            dq: None

            mxq: b1
            dq: a2

            mxq: a2
            dq: None

            mxq: None
            dq: a1
            """
            ff, cc = heappop(mxq)
            res += cc
            ff += 1

            if dq:
                f, c = dq.popleft()
                heappush(mxq, (f, c))

            if ff < 0:
                dq.append((ff, cc))

        if dq:
            return ""

        return res
