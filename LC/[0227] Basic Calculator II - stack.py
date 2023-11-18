class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)
        res = 0
        op = "+"
        prev = 0
        stkPrev = []
        stkRes = []
        stkOp = []

        ii = 0

        def calc(num):
            nonlocal res, prev
            if op == "+":
                res += num
                prev = num
            elif op == "-":
                res -= num
                prev = -num
            elif op == "*":
                res = (res-prev) + prev*num
                prev = prev*num
            else:  # op=="/"
                res = (res-prev) + abs(prev)//abs(num) * \
                    (1 if prev > 0 else -1) * (1 if num > 0 else -1)
                prev = abs(prev)//abs(num) * (1 if prev >
                                              0 else -1) * (1 if num > 0 else -1)

        while ii < N:
            if s[ii].isdigit():
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                num = int(s[ii:jj])
                ii = jj
                calc(num)

            else:

                if s[ii] == "(":
                    stkPrev.append(prev)
                    stkOp.append(op)
                    stkRes.append(res)
                    res = 0
                    op = "+"
                    prev = 0
                elif s[ii] == ")":
                    num = res
                    res = stkRes.pop()
                    op = stkOp.pop()
                    prev = stkPrev.pop()
                    calc(num)
                elif s[ii] == ' ':
                    pass
                else:
                    op = s[ii]
                ii += 1
        return res
