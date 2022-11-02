# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        * 1st node of preorder is the root
        * all nodes left to the root (from pre-order) in the in-order array is the left sub-tree
        * all nodes right to the root (from pre-order) in the in-order array is the right sub-tree
        ex:
        pre-order: 3 9 20 15 7
        in-order : 9 3 15 20 7
        """

        if len(preorder)== 0 or len(inorder)==0: return None

        rt=TreeNode(preorder[0])
        i0=inorder.index(preorder[0])

        # in preorder: we think of i0 as num of nodes on the left
        # in in-order: we think of i0 as the index of the current root.
        rt.left = self.buildTree(preorder[1:1+i0], inorder[:i0]) #i0 is also num of nodes on the left
        rt.right= self.buildTree(preorder[1+i0:], inorder[i0+1:])

        return rt
