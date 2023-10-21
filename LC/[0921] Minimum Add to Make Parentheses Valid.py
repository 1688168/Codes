class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0
        cnt = 0
        N = len(s)
        for ii, cc in enumerate(s):
            if cc == "(":
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    ans += 1
                    cnt = 0
        ans += cnt
        return ans
