# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop, heappushpop


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        M = len(lists)
        mnq = []
        for ii in range(M):
            n = lists[ii]
            if n is not None:
                heappush(mnq, (n.val, ii, n))

        new_head = ListNode()
        itr = new_head

        while mnq:
            vv, ii, n = heappop(mnq)
            itr.next = ListNode(vv)
            itr = itr.next
            if n.next is not None:
                heappush(mnq, (n.next.val, ii, n.next))

        return new_head.next
