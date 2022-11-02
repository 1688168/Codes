# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        : 1. find the mid-point
        : 2. reverse the 2nd part
        : 3. merge the two list
        : ---- slow, fast
        : 1 2 3 4 5 6
        :       s
        :            f
        : --- odd case
        : 1 2 3 4 5 6 7
                  s
                       f

        """
        if head is None: return None
        slow=fast=head

        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev is None:
            return head

        prev.next=None

        # reversing the 2nd part

        pp=None
        curr=slow
        while slow:
            nxt=slow.next
            slow.next=pp
            pp=slow
            slow=nxt

        returning_head=ListNode()
        itr=returning_head
        itr0=head
        itr1=pp

        print(" origHead ", itr0.val, " reversed head: ", itr1.val)

        while itr0 is not None and itr1 is not None:
            itr.next=itr0
            itr0=itr0.next
            itr=itr.next
            itr.next=itr1
            itr1=itr1.next
            itr=itr.next

        if itr0 is not None:
            itr.next=itr0

        return returning_head.next
