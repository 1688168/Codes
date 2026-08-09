# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        def getHeight(rt):
            hh=0
            while rt:
                rt=rt.left
                hh+=1
            return hh


        def hasK(rt, k): #O(h) where h is logN
            if rt is None: return False
            
            path = []
            kk = k
            while kk>0:
                path.append(kk)
                kk//=2
            path.reverse()

            for nn in path[1:]:
                if nn%2==0:
                    rt = rt.left
                else:
                    rt = rt.right
                if rt is None: return False
            
            return True


        hh = getHeight(root)
        ll = pow(2, hh-1)
        rr = pow(2, hh)-1

        # binary search
        cnt = ll
        while ll <= rr:
            mm = ll + (rr-ll)//2
            if hasK(root, mm):
                cnt=mm
                ll=mm+1
            else:
                rr=mm-1

        return cnt



"""
## Problem statement
* given a complete tree -> count num of nodes with less than O(N) solution
## Analysis
* N=5*10^4
* value of the node is red herring

## strategy
* create a method hasK

* binary search the max

"""
        