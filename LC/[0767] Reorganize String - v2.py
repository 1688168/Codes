from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        c2f = Counter(s)

        ss = [(c2f[c], c) for c in s]
        ss.sort(key=lambda x: (-x[0], x[1]))

        so = [None]*N

        ii = 0
        for ff, cc in ss:
            so[ii] = cc
            if ii > 0 and so[ii] == so[ii-1]:
                return ""
            ii += 2
            if ii >= N:
                ii = 1
        return "".join(so)
