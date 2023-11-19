from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        numStack = deque()
        opsStack = deque()
        ans = 0
        opsSet = set(['/', '*', '+', '-'])

        ii = 0
        while ii < len(s):
            c = s[ii]
            if c in opsSet:

                opsStack.append(c)
                ii += 1
            else:
                start = ii
                while ii < len(s) and s[ii] not in opsSet:
                    ii += 1
                # print(" curr num: ", s[start:ii])
                currNum = int(s[start:ii])
                if opsStack and opsStack[-1] in ['/', '*']:
                    currOp = opsStack.pop()
                    prevNum = numStack.pop()
                    if currOp == '/':
                        numStack.append(prevNum//currNum)
                    else:
                        numStack.append(prevNum*currNum)
                else:
                    numStack.append(currNum)

        # print(" numStack: ", numStack)
        # print(" opsStack: ", opsStack)

        while opsStack:
            op = opsStack.popleft()
            n1 = numStack.popleft()
            n2 = numStack.popleft()
            if op == '-':
                numStack.appendleft(n1-n2)
            else:
                numStack.appendleft(n1+n2)
            # print("numStack: ", numStack)

        return numStack[0]
