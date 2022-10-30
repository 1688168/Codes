# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lb, rb = float('-inf'), float('inf')

        def helper(rt, lb, rb):
            if rt is None: return True
            if rt.val >= rb or rt.val <= lb: return False

            left = helper(rt.left, lb, rt.val)
            right = helper(rt.right, rt.val, rb)
            if not left or not right: return False

            return True

        return helper(root, lb, rb)
