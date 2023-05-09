# 20230508
# Run time: 27.22%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Obj:
    def __init__(self, node):
        self.node=node
    def __lt__(self, other):
        return self.node.val <= other.node.val

from heapq import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None

        mnh = []
        for ll in lists:
            if ll is not None:
                heappush(mnh, Obj(ll))
        
        head=ListNode()
        itr=head

        while len(mnh) > 0:
            curr = heappop(mnh)
            itr.next=curr.node
            itr=itr.next
            if curr.node.next is not None:
                heappush(mnh, Obj(curr.node.next))
        
        return head.next if head.next is not None else None


        



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




######
# 20230508: do not need to create warpper obj
# Time: Nlogk on insert to heap
# space: O(N), the array to host the Node pointers
# runtime: 42.29
######
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        N = len(lists) 
        if N == 0: return None
        mnq=[]
        arr=[]

        for ii, LL in enumerate(lists):            
            if LL is not None:
                heappush(mnq, (LL.val, ii))
                arr.append(LL)
            else:
                arr.append(None)

        head=ListNode()
        itr=head
        while len(mnq) > 0:
            (vv, ii) = heappop(mnq)
            itr.next=(arr[ii])
            itr=itr.next
            if arr[ii].next is not None:
                v = arr[ii].next.val               
                heappush(mnq, (v,ii))
            arr[ii]=arr[ii].next
            
        return head.next if head.next is not None else None