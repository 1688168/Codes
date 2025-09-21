import java.util.*;

class Solution {
    // Event: (time, delta) where +1 = open, -1 = close
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return new int[0][0];

        int n = intervals.length;
        int[][] events = new int[n * 2][2]; // [time, delta]
        int k = 0;
        for (int[] it : intervals) {
            events[k][0] = it[0]; events[k++][1] = +1; // open
            events[k][0] = it[1]; events[k++][1] = -1; // close
        }

        // Sort by time asc; at same time, process OPEN (+1) before CLOSE (-1)
        Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            // tie: +1 first → descending by delta
            return Integer.compare(b[1], a[1]);
        });

        List<int[]> res = new ArrayList<>();
        int sum = 0;
        int start = 0;

        for (int[] e : events) {
            int t = e[0], delta = e[1];

            // starting a new merged interval
            if (sum == 0 && delta == +1) {
                start = t;
            }
            // closing the current merged interval
            else if (sum > 0 && sum + delta == 0) {
                res.add(new int[] { start, t });
            }

            sum += delta;
        }

        return res.toArray(new int[res.size()][]);
    }
}