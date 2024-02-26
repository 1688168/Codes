# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
* current state is relating to neighbor states -> house robber
   -------------------------------
   house robber     Tree Camera
   -------------------------------
   profit           count
   rob/no rob       not coverred/has cam/no cam but coverred
   array prev       post order traversal

   * DP type I variation: house robber
   * Greedy: heuristic on how to assign camera
   * post-order recursion

   # states
     not covered         0
     has camera          1
     covered by neighbor 2


   # considering leaf-nodes. 
   -> Greedy: let leaf-node's parents has camera 
   -> None nodes should return 2 to force leaf-nodes with state=0
"""
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cnt=0
        def dfs(node):
            nonlocal cnt
            if node is None: return 2 # see comments above

            left=dfs(node.left)
            right=dfs(node.right)

            if left==0 or right==0: #either child is not covered -> need add camera to cover
                cnt += 1
                return 1 # current must has camera in order to cover both children
            
            if left==2 and right==2: # both children are covered,  
                return 0 # greedy, let parent camera to cover
            
            return 2 # either child has camera (1), ie, current is covered without a camera
        root_state = dfs(root)
        if root_state==0: # root is uncovered
            cnt += 1
        return cnt