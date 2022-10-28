# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        dq=deque([root])

        if root is None: return res

        while (sz:=len(dq)) > 0:
            curr_lvl=[]
            for _ in range(sz):
                curr=dq.popleft()
                curr_lvl.append(curr.val)

                if curr.left is not None:
                    dq.append(curr.left)
                if curr.right is not None:
                    dq.append(curr.right)

            res.append(curr_lvl)

        return res
