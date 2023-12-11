from heapq import heappush, heappop, heappushpop
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = 0
        """
        consume max freq first and fill idle later
        """
        c2f = Counter(tasks)
        mxf = [-f for f in c2f.values()]  # we only need freq
        heapq.heapify(mxf)

        while mxf:
            tmp = []
            k = min(n+1, len(mxf))

            for _ in range(k):
                curr = heappop(mxf)
                curr += 1
                if curr < 0:
                    tmp.append(curr)

            if len(tmp) > 0:
                cnt += (n+1)
            else:
                cnt += k

            for t in tmp:
                heappush(mxf, t)

        return cnt
