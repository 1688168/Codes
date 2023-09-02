# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        1. record path to startValue (space: logN)
        2. record path to destValue
        3. locate LCA (Time: logN)
        4. change start path to all U
        5. append destPath
        """
        start_path = []
        dest_path = []

        def find(root, val, path):
            if root is None:
                return False

            if root.val == val:
                return True
            path.append('L')
            left = find(root.left, val, path)
            if left:
                return left
            path.pop()
            path.append('R')
            right = find(root.right, val, path)
            if right:
                return right
            path.pop()
            return False

        find(root, startValue, start_path)
        find(root, destValue, dest_path)

        kk = 0
        while kk < min(len(start_path), len(dest_path)) and start_path[kk] == dest_path[kk]:
            kk += 1
        res = ""
        for ii in range(kk, len(start_path)):
            res += "U"

        res += "".join(dest_path[kk:])
        return res
