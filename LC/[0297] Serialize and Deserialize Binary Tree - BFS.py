# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    """
    : serialize: into CSV string in level order (BFS):
    : 1. #: None
    : when you see BFS -> using deque
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        : BFS: 1,2,3,#,#,4,5
        :      i j
        :         i  j //i=i+1, j=j+2
        :          i     j
        :type root: TreeNode
        :rtype: str
        """
        if root is None: return "" # corner case

        dq=deque([root])
        res=""
        while len(dq) > 0:
            curr=dq.popleft()
            if curr is not None:
                res += (str(curr.val)+',')
                dq.append(curr.left)
                dq.append(curr.right)
            else:
                res += '#,'


        return res[:-1]  # remove the last unused comma


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0: return None
        arr=data.split(",")
        print(" arr: ", arr)
        ii, jj, N=0, 1, len(arr)
        nodes=[]
        for ii in range(len(arr)): #place all nodes into a list
            nodes.append(TreeNode(int(arr[ii])) if arr[ii] != '#' else None)

        ii, jj = 0, 1
        while jj < len(nodes): # link all nodes
            if nodes[ii] is not None:
                nodes[ii].left=nodes[jj]
                nodes[ii].right=nodes[jj+1]
                jj += 2

            ii += 1

        return nodes[0]




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
