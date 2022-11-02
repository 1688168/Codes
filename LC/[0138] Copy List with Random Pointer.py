#############
# 20221102
#############
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        old2new={}

        def dfs(node):
            if node is None: return None
            if node in old2new: return old2new[node]
            old2new[node]=Node(node.val)
            old2new[node].next=dfs(node.next)
            old2new[node].random=dfs(node.random)


            return old2new[node]

        dfs(head)
        return old2new[head]
        

###########################################################
###########################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        mp={}

        itr=head
        #create copy of nodes
        while itr is not None:
            mp[itr]=Node(itr.val)
            itr=itr.next


        # link the nodes
        itr=head
        while itr is not None:
            mp[itr].next=mp[itr.next] if itr.next is not None else None
            mp[itr].random=mp[itr.random] if itr.random is not None else None
            itr=itr.next

        return mp[head]
