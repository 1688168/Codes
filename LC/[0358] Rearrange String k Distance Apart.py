from collections import Counter
from heapq import heappush, heappop, heappushpop, heapify


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        """

        """
        res = ""
        c2f = Counter(s)
        mxq = [(-ff, cc) for cc, ff in c2f.items()]
        heapify(mxq)

        if k == 0:
            return s

        while mxq:
            kk = min(len(mxq), k)

            # if last round and the freq still greater than 1 (cannot honor required gap)
            if len(mxq) < k and mxq[0][0] < -1:
                return ""  # the condition of not making it

            tmp = []
            for _ in range(kk):
                ff, cc = heappop(mxq)
                ff += 1
                res += cc
                if ff < 0:
                    tmp.append((ff, cc))

            for ff, cc in tmp:
                heappush(mxq, (ff, cc))

        return res
