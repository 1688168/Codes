# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        def leftHeight(node):
            if node is None: return 0
            hh=0
            while node is not None:
                hh+=1
                node = node.left
            return hh
        
        def rightHeight(node):
            if node is None: return 0
            hh=0
            while node is not None:
                hh+=1
                node = node.right
            return hh

        ret = 1
        h1 = leftHeight(root.left)
        h2 = rightHeight(root.left)
        h3 = leftHeight(root.right)
        h4 = rightHeight(root.right)

        if h1==h2:
            ret += (1<<h1)-1
            return ret + self.countNodes(root.right)
        else:
            ret += (1<<h3)-1
            return ret + self.countNodes(root.left)

        return ret

## observations
# * for a full complete tree, num of nodes is 2^h-1
# * the tree is always has at least one side that is full complete
# * so if left side is not full complete, then right side definitely is full complete
# * based on which. we can apply a recursive solution
        