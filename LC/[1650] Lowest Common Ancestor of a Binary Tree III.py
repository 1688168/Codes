#################
# 20230917
#################
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pdepth, qdepth = 0, 0
        pi, qi = p, q
        while pi is not None:
            pdepth += 1
            pi = pi.parent

        while qi is not None:
            qdepth += 1
            qi = qi.parent

        while pdepth > qdepth:
            p = p.parent
            pdepth -= 1

        while qdepth > pdepth:
            q = q.parent
            qdepth -= 1

        while p != q:
            p = p.parent
            q = q.parent

        return p


#######################################
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # find p depth
        # find q depth
        # walk back via parent link

        def depth(nn, d):
            if nn is None:
                return d
            return depth(nn.parent, d+1)

        p_depth = depth(p, 0)
        q_depth = depth(q, 0)

        if p_depth >= q_depth:
            longer = p
            shorter = q
        else:
            longer = q
            shorter = p

        diff = max(p_depth, q_depth) - min(p_depth, q_depth)

        while diff > 0:
            longer = longer.parent
            diff -= 1

        while longer is not None and shorter is not None and longer.val != shorter.val:
            longer = longer.parent
            shorter = shorter.parent

        return longer
