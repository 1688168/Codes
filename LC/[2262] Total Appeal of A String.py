from collections import defaultdict


class Solution:
    def appealSum(self, s: str) -> int:
        char2prevPos = {}
        N = len(s)
        ttl = 0
        for ii, cc in enumerate(s):
            a = ii-char2prevPos.get(cc, -1)
            b = N-ii
            ttl += a*b
            char2prevPos[cc] = ii

        return ttl


########################
########################


class Solution:
    def appealSum(self, s: str) -> int:
        char2idx = defaultdict(list)
        for ii, cc in enumerate(s):
            char2idx[cc].append(ii)

        ttl = 0
        N = len(s)
        for cc, lst in char2idx.items():
            lst = [-1]+lst+[N]

            for jj in range(1, len(lst)-1):
                a = lst[jj]-lst[jj-1]
                b = N-lst[jj]
                ttl += a*b

        return ttl
