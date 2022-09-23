# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        : DFS - to reduce required space to build the graph for the Tree.
        : in-order traverse the tree
        : for each node:
        : A: curr is target
          -> DFS to output children with depth = k
        : B: curr is NOT target
          -> find target from left
             a. on the left
             -> curr depth==k => outout curr
             -> output right with depth = k-curr_depth
             b. on the right (mirror a)

        """
        
