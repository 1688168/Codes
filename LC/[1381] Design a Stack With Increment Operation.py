class CustomStack:

    def __init__(self, maxSize: int):
        self.nums = [0] * maxSize
        self.mx = maxSize
        self.offset = [0] * maxSize
        self.cnt = 0
        self.diff = 0

    def push(self, x: int) -> None:
        if self.cnt == self.mx:
            return
        if self.cnt > 0:
            self.offset[self.cnt-1] += self.diff
        self.diff = 0
        self.nums.append(x)
        self.offset[self.cnt] = 0
        self.cnt += 1

    def pop(self) -> int:
        if self.cnt == 0:
            return -1
        self.diff += self.offset[self.cnt-1]
        val = self.nums.pop()+self.diff
        self.cnt -= 1

        return val

    def increment(self, k: int, val: int) -> None:
        if self.cnt == 0:
            return
        self.offset[min(k-1, self.cnt-1)] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
