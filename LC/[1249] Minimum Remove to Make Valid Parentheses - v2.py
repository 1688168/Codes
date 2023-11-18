##############
# 20231118
##############
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        1. skip if left_count is <=0
        2. remove remainings 
        3. re-construct the paren string
        """
        N = len(s)
        left_cnt = 0
        res = ""
        for ii, cc in enumerate(s):
            if cc.isalpha():
                res += cc
            else:
                if cc == "(":
                    res += cc
                    left_cnt += 1
                elif cc == ")":
                    if left_cnt > 0:
                        left_cnt -= 1
                        res += cc
                else:
                    raise Exception(f"Unexpected char {cc}")

        # do we still have unmatched left_paren
        res_reversed = ""
        ii = len(res)-1

        # if left_cnt==0: return res

        while left_cnt > 0:
            left_cnt -= 1
            while ii >= 0 and (cc := res[ii]) != "(":
                res_reversed += cc
                ii -= 1
            ii -= 1

        while ii >= 0:
            res_reversed += res[ii]
            ii -= 1

        return res_reversed[::-1]


####################################
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
