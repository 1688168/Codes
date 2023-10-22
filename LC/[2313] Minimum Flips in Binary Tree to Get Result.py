# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        memo = collections.defaultdict(dict)  # memo is DFS's best friend

        def dfs(node, expected):
            if node.left is None and node.right is None:
                return node.val != expected

            if node in memo and expected in memo[node]:
                return memo[node][expected]

            ans = int(1e5)+1
            if node.val == 2:
                if expected == 1:
                    ans = min(ans, dfs(node.left, 1))
                    ans = min(ans, dfs(node.right, 1))
                else:
                    ans = min(ans, dfs(node.left, 0)+dfs(node.right, 0))
            elif node.val == 3:
                if expected == 1:
                    ans = min(ans, dfs(node.left, 1) + dfs(node.right, 1))
                else:
                    ans = min(ans, dfs(node.left, 0))
                    ans = min(ans, dfs(node.right, 0))
            elif node.val == 4:
                if expected == 1:
                    ans = min(ans, dfs(node.left, 0)+dfs(node.right, 1))
                    ans = min(ans, dfs(node.left, 1)+dfs(node.right, 0))
                else:
                    ans = min(ans, dfs(node.left, 0)+dfs(node.right, 0))
                    ans = min(ans, dfs(node.left, 1)+dfs(node.right, 1))
            elif node.val == 5:
                child = (node.left if node.left is not None else node.right)
                if expected == 1:
                    ans = min(ans, dfs(child, 0))
                else:
                    ans = min(ans, dfs(child, 1))

            memo[node][expected] = ans
            return ans
        return int(dfs(root, result))
