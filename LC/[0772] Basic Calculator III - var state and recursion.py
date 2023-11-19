######################
# 20231119
#######################
class Solution:
    def calculate(self, s: str) -> int:
        """
        commit (+,-)
        pending ()
        """
        N = len(s)

        def calc(pending, nn, op):
            if op == "+":
                return (pending+nn)

            elif op == "-":
                return (pending-nn)

            elif op == "*":
                pending *= nn
                return pending
            elif op == "/":
                sign = (1 if pending*nn >= 0 else -1)
                return abs(pending)//abs(nn)*sign
            else:
                msg = f"unexpected op=[{op}]"
                raise Exception(msg)

        def dfs(ii):
            op = "+"
            committed = 0
            pending = 0

            while ii < N:
                cc = s[ii]
                if cc.isdigit():  # parese num
                    jj = ii
                    while jj < N and s[jj].isdigit():
                        jj += 1
                    nn = int(s[ii:jj])
                    pending = calc(pending, nn, op)
                    ii = jj
                    continue
                else:
                    if cc == ' ':
                        pass
                    elif cc in ['+', '-', '*', '/']:
                        op = cc
                        if op in ["+", "-"]:
                            committed += pending
                            pending = 0
                    elif cc == "(":
                        ii, nn = dfs(ii+1)
                        pending = calc(pending, nn, op)
                        continue
                    elif cc == ")":
                        return ii+1, committed+pending
                    else:
                        msg = f"unexpected ch=[{c}]"
                        raise Exception(msg)
                    ii += 1
            return ii, committed+pending

        return dfs(0)[1]

##########################################################


class Solution:
    def calculate(self, s: str) -> int:
        """
        * The integer division should truncate toward zero.
        * no space
        * postive numbers
        ---
        * ('*', '/'): handle by varible state
        * parenthesis: leverage recursion
        """
        ii = 0
        N = len(s)

        def calculator():
            nonlocal ii

            committed = 0
            pending = 0
            op = '+'

            def calc(num):
                nonlocal pending
                if op == '+':
                    pending += num
                elif op == '-':
                    pending -= num
                elif op == '*':
                    pending *= num
                elif op == '/':
                    sign = 1 if pending*num >= 0 else -1
                    pending = abs(pending)//abs(num)*sign
                else:
                    raise Exception(f"Invalid operator {op}")

            while ii < N:
                c = s[ii]
                if c == ' ':
                    ii += 1
                    continue

                if c.isdigit():  # got a number
                    # pars out the num
                    jj = ii
                    while jj < N and s[jj].isdigit():
                        jj += 1
                    num = int(s[ii:jj])
                    calc(num)
                    ii = jj
                else:
                    ii += 1
                    if c in ('+', '-'):
                        op = c
                        committed += pending
                        pending = 0
                    elif c in ('*', '/'):
                        op = c
                    elif c == '(':
                        calc(calculator())
                    elif c == ')':
                        return committed+pending
                    else:
                        print("what's this?: ", c)
                        raise Exception(f"Unexpected token {c}")

            return committed+pending

        return calculator()
