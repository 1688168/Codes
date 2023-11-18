#############
# 20231117
#############
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        N = len(s)
        left_cnt = 0
        cnt = 0
        for ii in range(N):
            if (cc := s[ii]) == "(":
                left_cnt += 1
            elif cc.isalpha():
                continue
            else:
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    cnt += 1
        return cnt+left_cnt


##########################
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
