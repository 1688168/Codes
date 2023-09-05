from collections import Counter


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
