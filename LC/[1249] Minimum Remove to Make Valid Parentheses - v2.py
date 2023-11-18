class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
         1. scan through the string
         2. if left-paren, push
         3. if char, ignore
         4. if right-paren pop, but if stack.top is not left-paren or null -> add count
        """
        N = len(s)
        ii = 0
        stk = []

        res = ""
        while ii < N:
            cc = s[ii]
            if cc.isalpha():
                res += cc
                ii += 1
                continue
            else:
                if cc == "(":
                    stk.append(cc)
                elif cc == ")":
                    if stk:
                        stk.pop()
                    else:
                        ii += 1
                        continue
                else:
                    raise Exception(f"invalid input char {cc}")
            res += cc
            ii += 1

        res_tmp = ""
        jj = len(res)-1
        # print("stk: ", stk, " res: ", res)
        while stk:
            stk.pop()
            while jj >= 0 and res[jj] != "(":
                res_tmp += res[jj]
                jj -= 1
            jj -= 1
        while jj >= 0:
            res_tmp += res[jj]
            jj -= 1

        return res_tmp[::-1]
