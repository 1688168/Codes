from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        this solution only works when k=1
        """
        N = len(barcodes)
        n2f = Counter(barcodes)
        bc = []
        for nn in barcodes:
            bc.append((n2f[nn], nn))
        barcodes = bc
        barcodes.sort(key=lambda x: (-x[0], -x[1]))

        """
        since the problem is guaranteed to have answer.
        """
        ii = 0

        res = [0]*N
        # print(barcodes)
        for ff, nn in barcodes:
            res[ii] = nn
            ii += 2
            if ii >= N:
                ii = 1

        return res
