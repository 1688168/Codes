"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.orig2new={}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None

        if node in self.orig2new: return self.orig2new[node]
        self.orig2new[node]=Node(node.val)

        for child in node.neighbors:
            self.orig2new[node].neighbors.append(self.cloneGraph(child))

        return self.orig2new[node]
