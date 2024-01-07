M = int(1e9+7)


def quick_pow(x, y):
    ret = 1
    cur = x
    while y:
        if y & 1:
            ret = ret * cur % M
        cur = cur * cur % M
        y >>= 1
    return ret


class Fancy:

    def __init__(self):
        self.mul = 1
        self.add = 0
        self.nums = []

    def inv(self, x):
        return quick_pow(x, M-2)

    def append(self, val: int) -> None:
        """
        self.nums.append((val-self.add)/self.mul) #it's floating here
        append: val = nums[ii]-add/mul
        what if we find val' s.t. val' % M == val % M

        inverse element:
        x/a===x*b (mod M)

        b = inv(a)
        a = inv(b)

        <=> a and M (互质)
        """
        # self.nums.append((val-self.add)/self.mul) #it's floating here
        # self.nums.append((val-self.add+M)%M*self.inv(self.mul)%M)
        val = (val-self.add+M) % M
        val = (val * self.inv(self.mul)) % M
        self.nums.append(val)

    def addAll(self, inc: int) -> None:
        self.add += inc
        self.add %= M

    def multAll(self, m: int) -> None:
        self.mul = self.mul*m % M
        self.add = self.add*m % M

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        return (self.nums[idx]*self.mul % M+self.add) % M


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
