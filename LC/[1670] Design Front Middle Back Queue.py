from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self.fq = deque()
        self.bq = deque()

    def rebalance(self):
        if not self.fq and not self.bq:
            return
        if len(self.fq) == len(self.bq):
            return
        while len(self.bq) > len(self.fq)+1:
            self.fq.append(self.bq.popleft())
            if not self.bq:
                return

        while len(self.fq) > len(self.bq):
            self.bq.appendleft(self.fq.pop())
            if not self.fq:
                return

    def pushFront(self, val: int) -> None:
        self.fq.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        self.fq.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.bq.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.fq and not self.bq:
            return -1
        if not self.fq:
            return self.bq.popleft()

        val = self.fq.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:

        if len(self.bq) > len(self.fq):
            val = self.bq.popleft()
        else:
            if not self.fq:
                return -1
            val = self.fq.pop()
        return val

    def popBack(self) -> int:
        if not self.fq and not self.bq:
            return -1
        if self.bq:
            val = self.bq.pop()
            self.rebalance()
            return val

        if self.fq:
            val = self.fq.pop()
            self.rebalance()
            return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
