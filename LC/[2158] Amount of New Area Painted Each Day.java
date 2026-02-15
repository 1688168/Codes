import java.util.*;

class Solution {
    public int[] amountPainted(int[][] paint) {
        int n = paint.length;

        // Find the max coordinate to size arrays safely
        int max = 0;
        for (int[] seg : paint) {
            max = Math.max(max, seg[1]);
        }

        // next[i] points to the next candidate position to paint (like DSU parent)
        int[] next = new int[max + 1];
        for (int i = 0; i <= max; i++) {
            next[i] = i;
        }

        int[] ans = new int[n];

        for (int day = 0; day < n; day++) {
            int start = paint[day][0];
            int end = paint[day][1];

            int painted = 0;
            int pos = find(next, start);

            while (pos < end) {
                painted++;
                // Mark pos as painted by linking it to the next position
                next[pos] = pos + 1;
                pos = find(next, pos); // jump to next unpainted
            }

            ans[day] = painted;
        }

        return ans;
    }

    // Path-compressed "find": returns smallest index >= x that is not yet painted
    private int find(int[] next, int x) {
        if (x >= next.length) return x; // defensive (end boundary)
        if (next[x] == x) return x;
        next[x] = find(next, next[x]);
        return next[x];
    }
}