class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        mxl=-1
        mxp=[]
        def dfs(rt):
            nonlocal mxl, mxp
            if rt is None: return (0, None)
            (left, lp) = dfs(rt.left)
            (right, rp) = dfs(rt.right)
            #print(" rt: ", rt.val, " lp: ", lp, " rp: ", rp)


            path=[rt.val]
            if lp is not None:
                path= lp + path
            if rp is not None:
                path= path + rp

            if left+right > mxl:
                mxp=path[:]
            mxl=max(mxl, left+right)

            path=[rt.val]
            if left > right:
                path=(lp if lp else []) + path

            if right >= left:
                path=path+(rp if rp else [])
            #print(" rt: ", rt.val, " path: ", path, " mxp: ", mxp, " lp: ", lp, " rp: ", rp)
            return (1+max(left, right), path[:])

        l, p = dfs(root)
        print("max path: ====> ", mxp)
        return mxl
