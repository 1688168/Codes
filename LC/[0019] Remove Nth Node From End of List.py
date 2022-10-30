# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
        ii=0
        while ii < n and fast is not None:
            fast=fast.next
            ii+=1

        """

       p
        x x x x x
          f
        s

        """

        prev=None
        while fast is not None:
            prev=slow
            slow=slow.next
            fast=fast.next

        if prev is None: #we are removing head
            head=head.next
        else:
            prev.next=slow.next

        return head
