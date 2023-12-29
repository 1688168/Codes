##############
# 20231229
##############
class OO:
    def __init__(self, val, freq, seq):
        self.val = val
        self.freq = freq
        self.seq = seq

    def __lt__(self, o):
        if self.freq == o.freq:
            return self.seq > o.seq
        return self.freq > o.freq


class FreqStack:

    def __init__(self):
        self.val2freq = {}
        self.mxh = []
        self.seq = 0

    def push(self, val: int) -> None:
        freq = self.val2freq.get(val, 0)+1
        self.val2freq[val] = freq
        self.seq += 1
        heappush(self.mxh, OO(val, freq, self.seq))

    def pop(self) -> int:
        o = heappop(self.mxh)
        self.val2freq[o.val] -= 1
        return o.val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

####################
class oo:
    def __init__(self, freq, val, seq):
        self.freq = freq
        self.val = val
        self.seq = seq

    def __lt__(self, o):
        if self.freq == o.freq:
            return self.seq > o.seq
        else:
            return self.freq > o.freq


class FreqStack:

    def __init__(self):
        self.mm = {}
        self.mxq = []
        self.seq = 0

    def push(self, val: int) -> None:
        freq = self.mm.get(val, 0)+1
        self.seq += 1
        self.mm[val] = freq
        heappush(self.mxq, oo(freq, val, self.seq))

    def pop(self) -> int:
        self.mm[self.mxq[0].val] -= 1
        curr = heappop(self.mxq).val

        return curr


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
