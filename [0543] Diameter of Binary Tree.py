class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        mxl=-1
        def dfs(rt):
            nonlocal mxl
            if rt is None: return 0
            left = dfs(rt.left)
            right = dfs(rt.right)

            mxl=max(mxl, left+right)
            return 1+max(left, right)


        dfs(root)

        return mxl
