################
# 20240403
################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        children = set([v.val for v in nodes])

        def helper(rt):
            if rt is None:
                return 0, None
            lc, la = helper(rt.left)
            if la is not None:
                return 0, la
            rc, ra = helper(rt.right)
            if ra is not None:
                return 0, ra

            curr_cnt = lc + rc + (1 if rt.val in children else 0)

            if curr_cnt == len(children):
                return curr_cnt, rt
            else:
                return curr_cnt, None

        cnt, ancestor = helper(root)

        return ancestor


###############################
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
