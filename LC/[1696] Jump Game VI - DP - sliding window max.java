import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    static final class Pair {
        int val, idx;
        Pair(int v, int i) { val = v; idx = i; }
    }

    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        Deque<Pair> dq = new ArrayDeque<>();
        dq.addLast(new Pair(nums[0], 0));

        int dp = nums[0];

        for (int i = 1; i < n; i++) {
            // evict outside window
            while (!dq.isEmpty() && i - dq.peekFirst().idx > k) {
                dq.pollFirst();
            }

            dp = dq.peekFirst().val + nums[i];

            // maintain decreasing by dp value
            while (!dq.isEmpty() && dp >= dq.peekLast().val) {
                dq.pollLast();
            }

            dq.addLast(new Pair(dp, i));
        }

        return dp;
    }
}