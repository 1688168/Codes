# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dfs(dq, depth):
            if dq is None or len(dq) == 0:
                return None

            curr_depth = 0
            while dq[curr_depth] == '-':
                curr_depth += 1

            if curr_depth != depth+1:
                return None
            while dq[0] == '-':
                dq.popleft()
            if len(dq) == 0:
                return None
            val = ""
            while dq and dq[0].isdigit():
                val += dq.popleft()
            val = int(val)
            rt = TreeNode(val)
            rt.left = dfs(dq, curr_depth)
            rt.right = dfs(dq, curr_depth)
            return rt

        dq = collections.deque(list(traversal))
        return dfs(dq, -1)
