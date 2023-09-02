# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        """
        * record depth of the visited nodes  # Space: O(N)
        * find the LCA # Time: O(N)
        * distance = sum(dist to LCA)
        """
        n2depth = {}

        def lca(root, p, q, depth):
            nonlocal n2depth
            if root is None:
                return (0, None)
            n2depth[root.val] = depth

            lc, llca = lca(root.left, p, q, depth+1)
            if lc == 2:
                return (lc, llca)
            rc, rlca = lca(root.right, p, q, depth+1)
            if rc == 2:
                return (rc, rlca)

            cnt = int(root.val == p or root.val == q) + lc + rc
            if cnt == 2:
                return (cnt, root)

            return (cnt, None)

        lca = lca(root, p, q, 0)[1]
        if lca is None:
            return 0
        left_dist = n2depth[p]-n2depth[lca.val]
        right_dist = n2depth[q]-n2depth[lca.val]

        return left_dist+right_dist
