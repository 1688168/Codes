import java.util.PriorityQueue;

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap =
            new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));

        for (ListNode node : lists) {
            if (node != null) {
                minHeap.offer(node);
            }
        }

        ListNode head = new ListNode(0);
        ListNode itr = head;

        while (!minHeap.isEmpty()) {
            ListNode node = minHeap.poll();

            itr.next = node;
            itr = itr.next;

            if (node.next != null) {
                minHeap.offer(node.next);
            }
        }

        return head.next;
    }
}