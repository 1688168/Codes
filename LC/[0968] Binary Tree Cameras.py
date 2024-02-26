# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Tree -> recursion
current state is determined by neighboring state -> house robber -> DP
Order matters: considering top down or bottom up
Leaf-nodes are uncovered -> greedy
"""


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def solve(rt):
            if not rt:  # base case if node is None
                return 0, 0, float('inf')

            L = solve(rt.left)
            R = solve(rt.right)

            dp0 = L[1]+R[1]  # uncovered
            dp1 = min(L[2]+min(R[1:]), R[2]+min(L[1:]))  # with Camera
            dp2 = 1+min(L)+min(R)  # without camera
            return dp0, dp1, dp2

        return min(solve(root)[1:])
