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
        int ii=0;
        ListNode fast = head;
        ListNode slow = head;
        while(ii<n && fast != null){
            ++ii;
            fast=fast.next;
        }

        ListNode prev = null;
        while(fast != null){
            fast=fast.next;
            prev=slow;
            slow=slow.next;
        }

        if(prev != null){
            prev.next=slow.next;
        }else{
            head=head.next;
        }
        return head;        
    }
}