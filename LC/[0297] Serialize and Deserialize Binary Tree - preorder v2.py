#######################
# 20231208
#######################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#"

        return str(root.val)+","+str(self.serialize(root.left))+","+str(self.serialize(root.right))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tkns = data.split(",")
        nodes = collections.deque(
            [TreeNode(t) if t != '#' else None for t in tkns])

        def dfs(nodes):
            curr = nodes.popleft()
            if curr is None:
                return None
            left = dfs(nodes)
            right = dfs(nodes)
            curr.left = left
            curr.right = right
            return curr

        return dfs(nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
#######################
# 20231126
#######################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    """
    : preorder can uniquely re-construct the binary tree
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # preorder traversal
        if root is None:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tkn = data.split(",")
        dq = collections.deque(
            [TreeNode(t) if t != '#' else None for t in tkn])

        def dfs(dq):
            curr = dq.popleft()
            if curr is None:
                return None

            left = dfs(dq)
            right = dfs(dq)

            curr.left = left
            curr.right = right

            return curr

        return dfs(dq)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


#######################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        : preorder: left most node is the root
        """
        # preorder traversal
        if root is None:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')

        dq = deque(arr)

        def dfs(dq):
            if dq is None:
                return None
            curr = dq.popleft()
            if curr == '#':
                return None
            node = TreeNode(int(curr))
            node.left = dfs(dq)
            node.right = dfs(dq)

            return node

        return dfs(dq)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
