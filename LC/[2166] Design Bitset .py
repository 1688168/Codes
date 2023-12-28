class Bitset:

    def __init__(self, size: int):
        self.N = size
        self.cnt = 0
        self.ttl_flip = 0
        # each bit is represented by how many flips on the index
        self.flips = [0]*size

    def fix(self, idx: int) -> None:
        if (self.ttl_flip+self.flips[idx]) % 2 == 0:  # if current is zero
            self.flips[idx] += 1
            self.cnt += 1

    def unfix(self, idx: int) -> None:
        if (self.ttl_flip+self.flips[idx]) % 2 == 1:  # if current is 1
            self.flips[idx] += 1
            self.cnt -= 1

    def flip(self) -> None:
        self.ttl_flip += 1
        self.cnt = self.N-self.cnt

    def all(self) -> bool:
        return self.cnt == self.N

    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        res = ""
        for ii in range(self.N):
            if (self.flips[ii]+self.ttl_flip) % 2 == 1:
                res += "1"
            else:
                res += "0"
        return res


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
