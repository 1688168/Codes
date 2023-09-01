# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_set = set([n.val for n in nodes])

        def lca(root):
            if root is None:
                return (0, None)

            lc, left = lca(root.left)
            if left is not None:
                return (lc, left)

            rc, right = lca(root.right)
            if right is not None:
                return (rc, right)

            cnt = (1 if root.val in node_set else 0) + lc + rc
            if cnt == len(node_set):
                return (cnt, root)

            return (cnt, None)

        return lca(root)[1]
