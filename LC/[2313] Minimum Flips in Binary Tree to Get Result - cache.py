# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        if root is None:
            # node nums 1~ shouldn't hit this
            raise Exception(f"invalid node num")
        if root.val in (0, 1):  # a single node situation
            return int(result != root.val)

        @cache
        def dfs(node, result):
            # if leaf-node
            if node.left is None and node.right is None:
                return int(result != node.val)

            val = node.val  # current value
            if val == 2:  # or
                if result == 1:  # looking for True
                    left = dfs(node.left, 1)
                    right = dfs(node.right, 1)
                    return min(left, right)
                else:  # False
                    left = dfs(node.left, 0)
                    right = dfs(node.right, 0)
                    return left+right
            elif val == 3:  # AND
                if result == 1:
                    left = dfs(node.left, 1)
                    right = dfs(node.right, 1)
                    return left+right
                else:
                    left = dfs(node.left, 0)
                    right = dfs(node.right, 0)
                    return min(left, right)
            elif val == 4:  # XOR
                if result == 1:
                    left = dfs(node.left, 0)
                    right = dfs(node.right, 1)
                    a1 = left+right
                    left = dfs(node.left, 1)
                    right = dfs(node.right, 0)
                    a2 = left+right
                    return min(a1, a2)
                else:
                    left = dfs(node.left, 0)
                    right = dfs(node.right, 0)
                    a1 = left+right
                    left = dfs(node.left, 1)
                    right = dfs(node.right, 1)
                    a2 = left+right
                    return min(a1, a2)

            elif val == 5:  # NOT
                child = node.left if node.left else node.right

                ans = dfs(child, not result)
                return ans
            else:
                msg = f"Invalid val=[{val}]"
                raise Exception(msg)

        return dfs(root, 1 if result else 0)
