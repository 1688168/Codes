# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:

        def isFlipEquivalent(rt1, rt2):
            if rt1 is None and rt2 is None:
                return True
            if rt1 is None or rt2 is None:
                return False
            if rt1.val != rt2.val:
                return False

            same_order = (
                isFlipEquivalent(rt1.left, rt2.left)
                and isFlipEquivalent(rt1.right, rt2.right)
            )

            return same_order or (
                isFlipEquivalent(rt1.left, rt2.right)
                and isFlipEquivalent(rt1.right, rt2.left)
            )

        return isFlipEquivalent(root1, root2)



        