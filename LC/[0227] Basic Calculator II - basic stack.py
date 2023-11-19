class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)
        ii = 0
        stk = []
        op = "+"
        while ii < N:
            cc = s[ii]
            # print("ii: ", ii, " cc: ", cc, " op: ", op, " stk: ", stk)

            if cc.isdigit():  # is getting a digit
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                nn = int(s[ii:jj])
                ii = jj
                if op in ["*", "/"]:
                    if stk and op == "*":
                        stk[-1] *= nn
                        op = "+"
                    elif stk and op == "/":
                        sign = (1 if stk[-1] > 0 else -1)
                        # notice the special handle for the negative number division
                        stk[-1] = sign * (abs(stk[-1])//nn)
                        op = "+"
                    else:
                        msg = f"""Unexpected op=[{op}], nn=[{nn}], s=[{s}]"""
                        raise Exception(msg)

                elif op in ["+", "-"]:
                    sign = 1 if op == "+" else -1
                    # let number carry the sign in the stack
                    stk.append(sign*nn)
                else:
                    msg = f"""Unexpected op=[{op}], nn=[{nn}], s=[{s}]"""
                    raise Exception(msg)
                continue
            else:  # not digit cases
                if cc == ' ':
                    pass
                else:
                    op = cc
            ii += 1

        # print(" ending stk: ", stk)

        return sum(stk)
