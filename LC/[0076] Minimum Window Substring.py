from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""

        ll, rr = 0, 0
        matched = 0
        char2cnt = Counter(t)

        mnl = float('inf')
        mns = ""

        """
        ADOBECODEBANC
        ^^^^^^
        l    r
        ABC

        """

        for rr in range(m):
            c = s[rr]

            char2cnt[c] = char2cnt.get(c, 0) - 1

            if char2cnt[c] >= 0:
                matched += 1
            # print("mnl: ", mnl, " mns: ", mns)
            while ll <= rr and matched == n:
                if rr-ll+1 < mnl:
                    mnl = rr-ll+1
                    mns = s[ll:rr+1]
                prev = s[ll]

                char2cnt[prev] += 1
                if char2cnt[prev] > 0:
                    matched -= 1

                ll += 1

        return mns


###############
# 20230702 TLE
###############
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        res = ""

        ll = 0
        char2cnt = {}
        for c in t:
            char2cnt[c] = char2cnt.get(c, 0)+1

        def is_substring(s):
            char2cnt_copy = char2cnt.copy()
            cnt = 0
            for c in s:
                if c not in char2cnt_copy:
                    continue
                cnt += 1
                char2cnt_copy[c] -= 1
                if char2cnt_copy[c] == 0:
                    del char2cnt_copy[c]
            return True if cnt == n else False

        for rr in range(m):
            while ll <= rr and is_substring(s[ll:rr+1]):
                if res == "" or (res != "" and rr-ll+1 < len(res)):
                    res = s[ll:rr+1]

                ll += 1
            # print("res: ", res)

        return res
