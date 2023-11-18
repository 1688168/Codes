class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # from left to right, remove extra ")"
        # remove right to left, remove extra "("

        ii = 0
        leftCnt = 0
        N = len(s)
        res = ""

        # remove extra ")"
        while ii < N:
            if s[ii].isalpha():
                res += s[ii]
            else:  # got a parentheses
                if s[ii] == "(":
                    leftCnt += 1
                    res += s[ii]
                else:  # ")"
                    if leftCnt > 0:
                        res += ")"
                        leftCnt -= 1
            ii += 1

        # remove extra "("
        ii = 0
        N = len(res)
        s = res[::-1]
        res = ""
        rightCnt = 0
        while ii < N:
            if s[ii].isalpha():
                res += s[ii]
            else:
                if s[ii] == ")":
                    rightCnt += 1
                    res += s[ii]
                else:  # "("
                    if rightCnt > 0:
                        res += "("
                        rightCnt -= 1

            ii += 1

        return res[::-1]
