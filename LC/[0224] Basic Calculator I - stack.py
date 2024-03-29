############
# 20231118
############
class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)
        stk_n = []
        stk_op = []
        res = 0
        ii = 0
        op = "+"

        def calc(aa, op, bb):
            if op == "+":
                return aa+bb
            elif op == "-":
                return aa-bb
            else:
                msg = f"unexpected op {op}"
                raise Exception(msg)
            return 0

        while ii < N:
            cc = s[ii]
            if cc.isdigit():
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                nn = int(s[ii:jj])
                ii = jj
                res = calc(res, op, nn)
                continue
            else:
                if cc == " ":
                    pass
                elif cc == "(":
                    stk_n.append(res)
                    res = 0
                    stk_op.append(op)
                    op = "+"
                elif cc == ")":
                    prev = stk_n.pop()
                    op = stk_op.pop()
                    res = calc(prev, op, res)
                elif cc in ("+", "-"):
                    op = cc
                else:
                    msg = f"unexpected char = {cc}"
                    raise Exception(msg)
                ii += 1

        return res


############
# 20231112
############
class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)
        op = "+"
        stk_n = []
        stk_op = []
        ans = 0
        ii = 0

        def calc(a, b, o):
            if o == "+":
                return a+b
            elif o == "-":
                return a-b
            else:
                msg = f"unexpected operator {op}"
                raise Exception(f"{msg}")
        while ii < N:
            cc = s[ii]
            if cc.isdigit():  # parse out the num
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1
                nn = int(s[ii:jj])
                ans = calc(ans, nn, op)
                ii = jj
                continue
            else:
                if cc == ' ':  # ignore space
                    pass
                elif cc == "(":
                    stk_n.append(ans)
                    stk_op.append(op)
                    ans = 0
                    op = "+"
                elif cc == ")":
                    nn = stk_n.pop()
                    op = stk_op.pop()
                    ans = (calc(nn, ans, op))

                elif cc == "+":
                    op = cc
                elif cc == "-":
                    op = cc
                else:
                    msg = f"unexpected cc: {cc}"
                    print(mm)
                    raise Exception(f"{msg}")

            ii += 1

        return ans
#############################################


class Solution:
    def calculate(self, s: str) -> int:
        """
        * contents of parenthesis need to be processes and then degrade to numbers outside of the parenthesis
        => when we reach parenthesis -> push current state to stack.
        * manually code stack
        * recursive and leverage the system stack
        strategy:
        1. process char by char
        2. skip space
        3. if parenthesis, push current state to stack
        4. process contents inside parenthesis like a new string.
        5. when we reach ")", pop the stack and resume calc

        Time: O(N)
        Space: O(N) the max stack
        """
        N = len(s)

        # define the state
        op = '+'
        curr = 0
        ii = 0

        stack_num = []
        stack_op = []

        def calc(num):
            nonlocal curr
            if op == '+':
                curr += num
            elif op == '-':
                curr -= num
            # elif op=='*':
            #     curr *= num
            # elif op=='/':
            #     curr //=num
            else:
                print("invalid operator: ", op)
                raise Exception(f"invalid operator {op}")

            return curr

        while ii < N:
            c = s[ii]

            if c == ' ':
                ii += 1
                continue  # skip space

            if c.isdigit():
                # parse out the num
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1

                num = int(s[ii:jj])
                calc(num)
                ii = jj
                # each time we got a num, we update curr with curr_op

            else:  # c is operator or ()
                ii += 1
                if c == '(':
                    stack_num.append(curr)
                    stack_op.append(op)
                    curr = 0
                    op = '+'
                elif c == ')':
                    num = curr
                    curr = stack_num.pop()
                    op = stack_op.pop()
                    calc(num)
                elif c in ('+', '-'):
                    op = c
        return curr


###########
# 20221104
###########
class Solution:
    def calculate(self, s: str) -> int:
        """
        * to process parenthesis -> stack
        """
        stack = []
        N = len(s)
        op = '+'
        num = 0
        res = 0

        def calc(a, b, op):
            if op == '+':
                return a+b
            if op == '-':
                return a-b
        ii = 0
        while ii < N:
            cc = s[ii]
            if cc.isdigit():
                # parse out num
                jj = ii
                while jj < N and s[jj].isdigit():
                    jj += 1

                num = int(s[ii:jj])
                ii = jj
                res = calc(res, num, op)
                # print(" res: ", res, " jj: ", jj)
            else:  # operators or space

                if s[ii] == ' ':
                    ii += 1
                    continue  # ignore space

                if s[ii] == '(':
                    stack.append((res, op))
                    op = '+'
                    res = 0
                elif s[ii] == ')':
                    prev, pop = stack.pop()
                    res = calc(prev, res, pop)
                elif s[ii] == '+':
                    op = '+'
                elif s[ii] == '-':
                    op = '-'
                else:
                    print(" unexpected s[ii]: ", s[ii])
                ii += 1

        return res
