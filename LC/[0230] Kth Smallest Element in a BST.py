# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt=0
        self.val=None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def kth(rt):
            if self.cnt==k:
                return

            if rt is None: return


            kth(rt.left)

            self.cnt += 1
            if self.cnt == k:
                self.val=rt.val
                return
            kth(rt.right)

        kth(root)

        return self.val 



################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cnt=0
        self.val=None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if self.cnt==k:
            return self.val

        if root is None: return None


        self.kthSmallest(root.left, k)

        self.cnt += 1
        if self.cnt == k:
            self.val=root.val
            return self.val
        self.kthSmallest(root.right, k)

        return self.val
