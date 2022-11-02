# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(p, q, itr):
            if itr is None: return (0, None)

            lc, lp = helper(p, q, itr.left)
            if lc==2: return (lc, lp)

            rc, rp = helper(p, q, itr.right)
            if rc==2: return (rc, rp)

            numOfMatches=lc+rc+ (1 if itr.val in (p.val, q.val) else 0)

            if numOfMatches==2:
                return (2, itr)
            else:
                return (numOfMatches, None)

        (cnt, pp) = helper(p, q, root)

        return pp
