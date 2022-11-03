# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        itr1=list1
        itr2=list2
        nh=ListNode()
        itr0=nh
        while itr1 is not None and itr2 is not None:
            if itr1.val < itr2.val:
                itr0.next=itr1
                itr0=itr0.next
                itr1=itr1.next
            else:
                itr0.next=itr2
                itr0=itr0.next
                itr2=itr2.next


        while itr1 is not None:
            itr0.next=itr1
            itr0=itr0.next
            itr1=itr1.next


        while itr2 is not None:
            itr0.next=itr2
            itr0=itr0.next
            itr2=itr2.next



        return nh.next
