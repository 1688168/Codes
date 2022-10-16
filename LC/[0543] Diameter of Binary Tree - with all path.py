# Not successful
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mxl=0
        mxp_all=[]
        if root is None: return 0

        def dfs(rt):
            nonlocal mxl, mxp_all
            if rt is None: return (0, None)
            (left, lp) = dfs(rt.left)
            (right, rp) = dfs(rt.right)
            path=[rt.val]
            if lp is not None:
                path=lp+path
            if rp is not None:
                path=path+rp

            if left+right >= mxl:
                if left+right==mxl:
                    mxp_all.append(path[:])
                else:
                    mxp_all=path[:]


            mxl = max(mxl, left+right)
            if left >=right:
                path=(lp if lp is not None else [])+[rt.val]
            else:
                path=[curr.val]+(rp if rp is not None else [])
            return (1+max(left, right), path)

        dfs(root)
        print(" ==== > mxp_all: ", mxp_all)

        return mxl
