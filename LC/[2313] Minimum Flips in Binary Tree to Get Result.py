###########
# 20231104
###########
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    memo is the best friend of dfs
    """

    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:

        memo = {}

        # @cache
        def dfs(root, res):
            if root.left is None and root.right is None:  # a leaf node
                return int((int(res) != root.val))

            if root is None:  # sanity check
                return 0

            if (root, res) in memo:
                return memo[(root, res)]

            if root.val == 2:  # or
                if res:  # true
                    ans = min(dfs(root.left, True), dfs(root.right, True))
                else:
                    ans = dfs(root.left, False)+dfs(root.right, False)
            elif root.val == 3:  # and
                if res:
                    ans = dfs(root.left, True)+dfs(root.right, True)
                else:
                    ans = min(dfs(root.left, False), dfs(root.right, False))

            elif root.val == 4:  # xor
                if res:
                    a1 = dfs(root.left, True) + dfs(root.right, False)
                    a2 = dfs(root.left, False) + dfs(root.right, True)
                    ans = min(a1, a2)
                else:
                    a1 = dfs(root.left, True)+dfs(root.right, True)
                    a2 = dfs(root.left, False)+dfs(root.right, False)
                    ans = min(a1, a2)

            elif root.val == 5:  # not
                child = root.left if root.left else root.right
                ans = dfs(child, not res)
            else:
                raise Exception(f"what the fuck? {root.val}")

            memo[(root, res)] = ans
            return ans

        return dfs(root, result)

####################################
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
