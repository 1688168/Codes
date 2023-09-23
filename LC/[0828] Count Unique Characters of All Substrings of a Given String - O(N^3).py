from collections import Counter


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        N = len(s)
        ttl = 0
        for ii in range(N):
            for jj in range(ii, N):
                ctr = Counter(list(s[ii:jj+1]))
                cnt = 0
                for idx, val in ctr.items():
                    if val == 1:
                        cnt += 1

                ttl += cnt
        return ttl
