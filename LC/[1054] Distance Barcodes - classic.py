from collections import Counter
from heapq import heappush, heappop, heappushpop, heapify


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        k=1
        """
        n2f = Counter(barcodes)
        mxq = [(-ff, nn) for nn, ff in n2f.items()]
        heapify(mxq)
        k = 1+1  # no adjacence
        res = []
        while mxq:
            tmp = []

            kk = min(len(mxq), k)  # it is guaranteed that we have solution
            for _ in range(kk):
                ff, nn = heappop(mxq)
                ff += 1
                if ff < 0:
                    tmp.append((ff, nn))
                res.append(nn)

            for ff, nn in tmp:
                heappush(mxq, (ff, nn))

        return res
