# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_nodes = set()

        # BFS to find all deepest deepest_nodes
        dq = deque([root])

        while (sz := len(dq)) > 0:
            deepest_nodes = set()
            while sz > 0:

                curr = dq.popleft()
                deepest_nodes.add(curr.val)
                if curr.left is not None:
                    dq.append(curr.left)
                if curr.right is not None:
                    dq.append(curr.right)
                sz -= 1

        # the bottom deepest_nodes
        # print("deepest_nodes", deepest_nodes)

        def lca(root):
            if root is None:
                return (None, 0)
            p, lc = lca(root.left)
            if p is not None:
                return (p, lc)
            p, rc = lca(root.right)
            if p is not None:
                return (p, rc)

            curr = 1 if root.val in deepest_nodes else 0
            cnt = curr + lc + rc
            if cnt == len(deepest_nodes):
                return (root, cnt)
            return (None, cnt)

        return lca(root)[0]
