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
        res=""
        if root is None: return '#'
        res = str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right) + ','

        return res[:-1]



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr=data.split(",")
        dq=deque(arr)
        print("arr: ", arr)
        def dfs(dq):
            curr = dq.popleft()
            if curr == '#': return None

            node = TreeNode(int(curr))
            left = dfs(dq)
            right = dfs(dq)

            node.left=left
            node.right=right

            return node

        return dfs(dq)





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
