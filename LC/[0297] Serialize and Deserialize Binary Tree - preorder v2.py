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
        : preorder: left most node is the root
        """
        # preorder traversal
        if root is None: return '#'
        return str(root.val)+ ',' + self.serialize(root.left)+ ',' + self.serialize(root.right)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr=data.split(',')

        dq=deque(arr)

        def dfs(dq):
            if dq is None: return None
            curr = dq.popleft()
            if curr =='#': return None
            node = TreeNode(int(curr))
            node.left=dfs(dq)
            node.right=dfs(dq)

            return node

        return dfs(dq)



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
