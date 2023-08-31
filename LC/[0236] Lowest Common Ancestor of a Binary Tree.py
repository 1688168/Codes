###########
# 20230831
###########
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if root is None: return 0, None
            
            lc, left = lca(root.left, p, q)
            if left is not None: return lc, left
            rc, right = lca(root.right, p, q)
            if right is not None: return rc, right

            cnt = (root.val==p.val or root.val==q.val)+lc+rc
            if cnt == 2: return cnt, root
            return cnt, None
        
        return lca(root, p, q)[1]


#####################
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
