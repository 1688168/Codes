import java.util.*;

class Solution {
    public int minMoves(int[] nums, int limit) {
        int n = nums.length;
        TreeMap<Integer, Integer> events = new TreeMap<>();//java treemap is c++ map (ordered)

        for (int i = 0; i < n / 2; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            if (a > b) {//java swap
                int tmp = a;
                a = b;
                b = tmp;
            }

            add(events, 2, +2);
            add(events, a + 1, -1);
            add(events, a + b, -1);
            add(events, a + b + 1, +1);
            add(events, b + limit + 1, +1);
        }

        int best = Integer.MAX_VALUE;
        int cur = 0;

        for (Map.Entry<Integer, Integer> e : events.entrySet()) {
            cur += e.getValue();
            best = Math.min(best, cur);
        }

        return best;
    }

    private void add(TreeMap<Integer, Integer> map, int key, int delta) {
        map.put(key, map.getOrDefault(key, 0) + delta);//java map operation
    }
}
