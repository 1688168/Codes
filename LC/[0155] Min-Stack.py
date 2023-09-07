class MinStack:

    def __init__(self):
        self.mn = None
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.mn = val
            self.stack.append(0)
        else:
            if val >= self.mn:
                self.stack.append(val-self.mn)
            else:
                self.stack.append(val-self.mn)
                self.mn = val

    """

    1

    -1
    2
    1
    5  4
    """

    def pop(self) -> None:
        if len(self.stack) == 0:
            return

        if self.stack[-1] < 0:
            self.mn = self.mn-self.stack[-1]
        self.stack.pop()
        return

    def top(self) -> int:
        if len(self.stack) == 0:
            return None

        if self.stack[-1] >= 0:
            return self.stack[-1]+self.mn
        else:
            return self.mn

    def getMin(self) -> int:
        return self.mn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
