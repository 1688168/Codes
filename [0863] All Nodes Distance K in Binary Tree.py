# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque
from pprint import pprint as pp
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        : build a graph and BFS for all k distant children
        : 1. traverse the tree and build the graph
        : 2. BFS
        : Time - O(N) for all nodes
        : space - O(N+V)
        """

        g=defaultdict(set)

        def dfs(tree, parent=None):
            if tree is None: return

            if parent is not None:
                g[tree.val].add(parent.val)
                g[parent.val].add(tree.val)

            dfs(tree.left, tree)
            dfs(tree.right, tree)

        def findNode(rt, val):
            if rt is None: return None

            if rt.val==val:
                return rt
            return findNode(rt.left, val) or findNode(rt.right, val)

        #build graph
        dfs(root)

        #pp(g)



        # BFS find k-distance children
        res=[]
        dq=deque([target.val])

        lvl=0
        visited=set()
        while len(dq)>0:
            sz=len(dq)
            for _ in range(sz):
                curr=dq.popleft()
                #print(" curr: ", curr, " lvl: ", lvl)
                if lvl==k:
                    res.append(curr)
                if curr in visited: continue
                visited.add(curr)

                for child in g[curr]:
                    if child in visited: continue
                    dq.append(child)


            lvl += 1
        return res
