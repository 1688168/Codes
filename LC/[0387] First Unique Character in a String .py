class Solution:
    def firstUniqChar(self, s: str) -> int:
        c2f = collections.Counter(s)
        for ii, cc in enumerate(s):
            if c2f[cc] == 1:
                return ii
        return -1
