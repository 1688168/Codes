# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Obj:
    def __init__(self, node):
        self.node=node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        -- check corner case
        """

        N=len(lists)
        mnq=[]
        for ii in range(N):
            if lists[ii] is not None:
                heappush(mnq, Obj(lists[ii]))

        head=ListNode()
        itr=head


        while len(mnq) > 0:
            curr=heappop(mnq)
            itr.next=curr.node
            itr=itr.next
            if curr.node.next is not None:
                heappush(mnq, Obj(curr.node.next))



        return head.next if head else None
