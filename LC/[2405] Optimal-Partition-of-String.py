class Solution:
    def partitionString(self, s: str) -> int:
        gps = 1
        chars = set()
        N = len(s)
        for ii in range(N):
            c = s[ii]
            if c in chars:
                gps += 1
                chars = set()
                chars.add(c)
            else:
                chars.add(c)
        return gps


##################
class Solution:
    def partitionString(self, s: str) -> int:
        dic = {}
        c = 0
        for i in s:
            if (i in dic):
                c += 1
                dic = {}
                dic[i] = 1
            else:
                dic[i] = 1
        if len(dic) != 0:
            c += 1
        return c
