#############
# 20231008
#############
from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        char2Cnt = collections.Counter(s)
        sorted_usage = [(cc, ff) for (cc, ff) in char2Cnt.items()]
        sorted_usage.sort(key=lambda x: -x[1])

        N = len(sorted_usage)
        multiplier = 0
        cnt = 0
        for ii in range(N):
            if ii % 9 == 0:
                multiplier += 1
            cnt += sorted_usage[ii][1]*multiplier

        return cnt

############################


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c2cnt = Counter(list(s))

        letter_cnt = [(cnt, c) for (c, cnt) in c2cnt.items()]
        letter_cnt.sort(reverse=True)

        press = 0
        cnt = 0
        ii = 0
        # print(" sorted list: ", letter_cnt)
        for nn, char in letter_cnt:
            if ii % 9 == 0:
                press += 1
            cnt += (nn*press)
            ii += 1

        return cnt
