# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            find the 1st node that splits the two nodes
        """

        itr=root
        while itr is not None:
            if p.val < itr.val and q.val < itr.val:
                itr=itr.left
            elif p.val > itr.val and q.val > itr.val:
                itr=itr.right
            else:
                return itr
