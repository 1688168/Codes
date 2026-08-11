class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            height = 0

            while node is not None:
                height += 1
                node = node.left

            return height

        def count(node):
            if node is None:
                return 0

            left_subtree_height = left_height(node.left)
            right_subtree_height = left_height(node.right)

            if left_subtree_height == right_subtree_height:
                # The left subtree is perfect.
                #
                # Current node + left subtree:
                # 1 + (2^height - 1) = 2^height
                return (
                    (1 << left_subtree_height)
                    + count(node.right)
                )

            # The right subtree is perfect.
            return (
                (1 << right_subtree_height)
                + count(node.left)
            )

        return count(root)