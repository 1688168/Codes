import java.util.*;

class Solution {
    public int maxSumRangeQuery(int[] nums, int[][] requests) {
        int N = nums.length;
        long[] events = new long[N + 1]; // Use long to avoid overflow in intermediate sums

        // 1. Convert interval requests to events
        for (int[] req : requests) {
            int st = req[0], ed = req[1];
            events[st] += 1;
            if (ed + 1 < N) {
                events[ed + 1] -= 1;
            }
        }

        // 2. Build frequency array via prefix sum
        long[] freq = new long[N];
        freq[0] = events[0];
        for (int i = 1; i < N; i++) {
            freq[i] = freq[i - 1] + events[i];
        }

        // 3. Sort frequencies and nums so biggest freq gets biggest num
        Arrays.sort(freq);
        Arrays.sort(nums);

        // 4. Compute result
        long M = 1_000_000_007L;
        long ttl = 0;
        for (int i = 0; i < N; i++) {
            ttl = (ttl + (freq[i] * nums[i]) % M) % M;
        }

        return (int) ttl;
    }
}