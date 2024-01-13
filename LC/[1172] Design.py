from heapq import heappush, heappop, heappushpop
from pprint import pprint as pp


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # list to maintian the unlimited stacks
        self.stks = []

        # mnq to maintian leftNotFull
        self.leftNotFull = []

        # who is in the heap?
        self.idxInHeap = set()

    def push(self, val: int) -> None:
        # if self.leftNotFull and self.leftNotFull[0] > len(self.stks) -1: self.leftNotFull=[]

        # no stk at all or no leftNotFull -> need new stack
        if not self.stks or not self.leftNotFull:
            new_stk = [val]
            self.stks.append(new_stk)

            if len(new_stk) < self.capacity:
                idx = len(self.stks)-1
                heappush(self.leftNotFull, idx)
                self.idxInHeap.add(idx)
        else:  # fill left not full
            idx = self.leftNotFull[0]
            self.stks[idx].append(val)

            if len(self.stks[idx]) == self.capacity:
                self.idxInHeap.remove(heappop(self.leftNotFull))

        # print(" ---- push ----: ", val)
        # print("stks: ", end="")
        # pp(self.stks)
        # print("leftNotFull: ", end="")
        # pp(self.leftNotFull)

    def pop(self) -> int:
        # stks is empty -> nothing to pop
        if not self.stks:
            return -1

        val = self.stks[-1].pop()  # pop last element

        removed_idx = []
        while self.stks and not self.stks[-1]:  # remove all empty stacks
            # here we might be removing idx that is still in leftNotFull
            idx = len(self.stks)-1
            self.stks.pop()  # remove empty stks
            removed_idx.append(idx)

        is_any_removed = False
        # print(" removed idx: ", removed_idx)
        for idx in removed_idx:
            if idx in self.idxInHeap:
                is_any_removed = True
                self.idxInHeap.remove(idx)
                self.leftNotFull.remove(idx)

        if is_any_removed:
            heapify(self.leftNotFull)

        if self.stks and len(self.stks[-1]) < self.capacity:
            idx = len(self.stks)-1
            if idx not in self.idxInHeap:
                self.idxInHeap.add(idx)
                heappush(self.leftNotFull, idx)

        # print(" ----- pop ---- ", val)
        # pp(self.stks)
        # pp(self.leftNotFull)

        return val

    def popAtStack(self, index: int) -> int:
        # print(" entering popAtStack: ", index)
        if index >= len(self.stks):
            return -1
        if not self.stks[index]:
            return -1

        val = self.stks[index].pop()

        removed_idx = []
        while self.stks and not self.stks[-1]:
            idx = len(self.stks)-1
            removed_idx.append(idx)
            self.stks.pop()  # remove trailing empty stacks

        is_any_removed = False
        for idx in removed_idx:
            if idx in self.idxInHeap:
                is_any_removed = True
                self.idxInHeap.remove(idx)
                self.leftNotFull.remove(idx)

        if is_any_removed:
            heapify(self.leftNotFull)

        if index not in self.leftNotFull and index < len(self.stks):
            heappush(self.leftNotFull, index)
            self.idxInHeap.add(index)

        # print(" ----- popAtIdx: ", index)
        # pp(self.stks)
        # pp(self.leftNotFull)

        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
