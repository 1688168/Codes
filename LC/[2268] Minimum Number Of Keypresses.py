
#############
# 20240115
#############
from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c2f = Counter(s)
        ffcc = [(ff, cc) for cc, ff in c2f.items()]
        ffcc.sort(reverse=True)

        lvl = 0
        c2n = {}
        jj = 0
        cnt = 0
        for ff, cc in ffcc:
            if jj % 9 == 0:
                lvl += 1
            jj += 1
            cnt += (lvl*ff)

        return cnt


#############
# 20231008
#############


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
