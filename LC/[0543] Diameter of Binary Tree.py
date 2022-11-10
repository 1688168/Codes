# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mxl=0

        def dfs(rt):
            nonlocal mxl
            if rt is None: return 0

            left=dfs(rt.left)
            right=dfs(rt.right)

            curr = left + right  #num of edges
            mxl = max(curr, mxl)

            return 1 + max(left, right) # num of nodes



        dfs(root)

        return mxl


        
