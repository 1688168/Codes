# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if root is None: return None
            if (root.val-p.val)*(root.val-q.val) <= 0: 
                return root
    
            left = lca(root.left, p, q)  
            if left is not None: return left          
            right=lca(root.right, p, q)
            if right is not None: return right

            return None

        return lca(root, p, q)
        