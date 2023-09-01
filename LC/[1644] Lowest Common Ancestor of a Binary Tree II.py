
"""
same as 236, generic solution does not require P, Q existing
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if root is None:
                return 0, None

            lc, left = lca(root.left, p, q)
            if left is not None:
                return lc, left
            rc, right = lca(root.right, p, q)
            if right is not None:
                return rc, right

            cnt = (root.val == p.val or root.val == q.val)+lc+rc
            if cnt == 2:
                return cnt, root
            return cnt, None

        return lca(root, p, q)[1]
