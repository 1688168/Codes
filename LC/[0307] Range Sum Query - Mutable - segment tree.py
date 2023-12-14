class SegTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0  # range sum
        self.left = None
        self.right = None


class SegTree:
    def __init__(self, a, b, nums):
        self.nums = nums
        self.root = SegTreeNode(a, b)
        self.init(self.root, a, b)

    def init(self, node, a, b):
        if a == b:
            node.sum = self.nums[a]
            return
        mm = (a+b)//2

        node.left = SegTreeNode(a, mm)
        node.right = SegTreeNode(mm+1, b)
        self.init(node.left, a, mm)
        self.init(node.right, mm+1, b)
        node.sum = node.left.sum+node.right.sum

    def update_single(self, node, idx, val):
        if idx < node.start or idx > node.end:
            return
        if node.start == node.end:
            node.sum = val
            return
        self.update_single(node.left, idx, val)
        self.update_single(node.right, idx, val)
        node.sum = node.left.sum+node.right.sum

    def query_range(self, node, a, b):
        if b < node.start or a > node.end:
            return 0
        if a <= node.start and b >= node.end:
            return node.sum
        return self.query_range(node.left, a, b)+self.query_range(node.right, a, b)


class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)

        self.st = SegTree(0, N-1, nums)

    def update(self, index: int, val: int) -> None:
        self.st.update_single(self.st.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query_range(self.st.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
