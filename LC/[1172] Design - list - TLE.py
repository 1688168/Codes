from collections import defaultdict


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stks = defaultdict(list)
        self.leftNotFull = 0
        self.rightNotEmpty = -1

    def push(self, val: int) -> None:
        # push the val
        self.stks[self.leftNotFull].append(val)

        # update leftNotFull
        while len(self.stks[self.leftNotFull]) >= self.capacity:
            self.leftNotFull += 1

        # update rightNotEmpty
        self.rightNotEmpty = max(self.rightNotEmpty,
                                 (self.leftNotFull - 1) if (len(self.stks[self.leftNotFull]) == 0) else self.leftNotFull)

        # print(" ----- push -----: ", val)
        # print(" rightNotEmpty: ", self.rightNotEmpty)

    def pop(self) -> int:

        return self.popAtStack(self.rightNotEmpty)

    def popAtStack(self, index: int) -> int:
        # print(" popATStack index: ", index)
        if self.rightNotEmpty == -1:
            return -1    # nothing to pop
        if index > self.rightNotEmpty:
            return -1  # index out-of-bound
        if len(self.stks[index]) == 0:
            return -1  # stk is empty

        # print(" ----- push -----")
        # print(" rightNotEmpty: ", self.rightNotEmpty)

        val = self.stks[index].pop()              # get the value

        # update rightNotEmpty
        if index == self.rightNotEmpty and len(self.stks[index]) == 0:
            while self.rightNotEmpty >= 0 and len(self.stks[self.rightNotEmpty]) == 0:
                self.rightNotEmpty -= 1

        # update leftNotFull
        self.leftNotFull = min(self.leftNotFull, index)

        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
