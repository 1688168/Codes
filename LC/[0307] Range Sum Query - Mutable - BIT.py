class NumArray:
    """
    Problem Clarification:
        1. Can ask if update and sumRange function is distributed evenly. If not, we can use naive method.

    Problem Pormulation:
        We need to have two functionality of this class:
            1. update a val of array given index.
            2. compute range sum queries.

    Thought Proecess:
        There're two naive solution:
            method 1. update using array[i] = val but compute range sum query using loop from index i to index j to calculate the sum of the elements.
            method 2. to creae an extra array called prefix sum array, which stores cumulative sum of the first i element(including ith element) at index i of new array, we can get get range sume query from index i to index j by simply computing prefix sum(0,j) - sum(0, i-1) when i!= 0 but each time when we need update, we need to re construct the prfix sum array.

    Time Complexity Anaylsis:
        For method 1, update operation takes O(1) but computing range sume takes O(n)
        For method 2, update operation takes O(n) but computing range sum takes O(1)

    Note:
        For naive solution, it will get TLE.
    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.prefix_sums = [0 for _ in range(self.n)]
        if self.n != 0:
            self.prefix_sums[0] = self.nums[0]
        for i in range(1, self.n):
            self.prefix_sums[i] = self.prefix_sums[i-1] + self.nums[i]

    def update(self, i: int, val: int) -> None:
        # update
        self.nums[i] = val
        # reconstruct prefix sum array
        self.prefix_sums = [0 for _ in range(self.n)]
        self.prefix_sums[0] = self.nums[0]
        for i in range(1, self.n):
            self.prefix_sums[i] = self.prefix_sums[i-1] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix_sums[j]
        return self.prefix_sums[j] - self.prefix_sums[i-1]


class BinaryIndexTree:
    def __init__(self, n):
        # we stor partial sum in each node of the tree
        self._trees = [0 for _ in range(n+1)]

    def update(self, i, delta):
        while i < len(self._trees):
            self._trees[i] += delta
            i += self.lowbit(i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self._trees[i]
            i -= self.lowbit(i)
        return s

    def lowbit(self, x):
        return x & (-x)


class NumArray:
    """
    Problem Pormulation:
        We need to have two functionality of this class:
            1. update a val of array given index.
            2. compute range sum queries.

    Thought Proecess:
        1. We can use binary index tree data structure

    Time Complexity Anaylsis:
        1. Initially, we build binary index tree will take O(nlogn).
        2. But for following query and update operation, both takes O(logn).

    """

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = BinaryIndexTree(self.n)
        # inital
        for i in range(self.n):
            self.bit.update(i+1, self.nums[i])

    def update(self, i: int, val: int) -> None:
        # update tree
        self.bit.update(i+1, val - self.nums[i])
        # update array
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.bit.query(j+1) - self.bit.query(i)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
