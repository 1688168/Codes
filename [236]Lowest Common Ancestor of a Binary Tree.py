# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(rt):
            if not rt: return (0, None)

            left=lca(rt.left)
            if left[0] == 2: return left
            right=lca(rt.right)
            if right[0] == 2: return right

            cnt=left[0]+right[0] + int(rt==p) + int(rt==q)

            return (cnt, rt if cnt==2 else None)



        return lca(root)[1]
