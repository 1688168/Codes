/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        var fast = head;
        var slow = head;

        //move fast n steps
        for(int ii=0; ii<n && fast != null; ++ii) fast = fast.next;
        if(fast==null) return head.next;//nothing to remove

        while(fast.next !=null) {
            fast=fast.next;
            slow=slow.next;
        }

        slow.next = slow.next.next;

        return head;
    }
}