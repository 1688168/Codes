# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq=deque([root])

        
        lvl=0
        while len(dq)>0:
            sz=len(dq)
            curr_lvl=[]
            for _ in range(sz):
                curr=dq.popleft()
                curr_lvl.append(curr)
                if curr.left is not None: dq.append(curr.left)
                if curr.right is not None: dq.append(curr.right)


            if lvl %2 ==1:
                ll, rr = 0, len(curr_lvl)-1
                while ll < rr:
                    curr_lvl[ll].val, curr_lvl[rr].val=curr_lvl[rr].val, curr_lvl[ll].val
                    ll+=1
                    rr-=1
            lvl += 1

        return root
