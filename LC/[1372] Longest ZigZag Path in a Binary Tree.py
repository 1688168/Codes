# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        mxl = 0

        def dfs(root, left_or_right):  # (0 or 1)
            nonlocal mxl
            if root is None:
                return 0

            left = right = 0
            if root.right:
                right = 1+dfs(root.right, 0)

            if root.left:
                left = 1+dfs(root.left, 1)

            mxl = max(mxl, left, right)

            return right if left_or_right == 1 else left

        dfs(root, 1)  # 1 is right
        dfs(root, 0)  # 0 is left

        return mxl
