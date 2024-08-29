//20240829
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
        ListNode prev = null;

        //handle edge cases
        //nothing to remove
        if(n==0) return head;

        //n==1 and only one node
        if(n==1 && head.next==null) return null;
     
        //move fast go n 
        //since we initialize fast/slow @ head, we need to go up to (n-1)
        for(int ii=0; ii<n-1 && fast != null; ++ii){
            fast = fast.next;
        }

        //not enouth nodes from the end for n
        if(fast == null) return null;

        while(fast.next != null){
            //System.out.println("fast: "+ fast.val + " slow: " + slow.val);
            prev=slow;
            slow=slow.next;
            fast=fast.next;
        }
        
        //System.out.println("to be removed: " + slow.val);
        if(prev == null && slow.next==null) return null;//remove only one node
        if(prev==null && slow.next!=null) return head.next; //removing head
        if(prev != null)prev.next=slow.next; //normal case
    
        return head;
    }
}

/* ----------------------------- */
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