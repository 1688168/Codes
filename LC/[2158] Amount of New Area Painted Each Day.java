import java.util.*;

/*
Overall strategy (DSU / "next-unpainted" jump pointers):
- Each day paints an interval [start, end).
- Naively, you might mark every unit position in that interval, but that can be too slow.
- Instead, we keep an array next[i] that points to the smallest position >= i that is NOT painted yet.
  * If i is unpainted, next[i] == i.
  * If i is painted, next[i] jumps forward (eventually to the next unpainted spot).
- We use a path-compressed find() to jump over already-painted positions quickly.
- For each day, we:
  1) Jump to the first unpainted position >= start.
  2) While that position is still < end, we paint it and "union" it to the next position.
  3) Count how many new unit positions were painted that day.
Time: ~O(total newly painted units * inverseAckermann), very fast in practice.
*/
class Solution {

    public int[] amountPainted(int[][] paint) {
        // paint.length is the number of days (each row is one day's interval).
        int days = paint.length;

        // We'll need an array sized by the maximum coordinate endpoint across all days.
        // Example: if a day paints [3, 10), we may touch positions up to 9 and link 9 -> 10.
        int maxCoord = 0;
        for (int[] seg : paint) {
            // seg[1] is the end coordinate (exclusive).
            maxCoord = Math.max(maxCoord, seg[1]);
        }

        // next[i] is our "jump pointer" structure:
        // - next[i] == i means i is currently unpainted.
        // - next[i] > i means i is painted, and next[i] tells you where to go next.
        // We allocate maxCoord + 1 because we may point to maxCoord itself as a sentinel.
        int[] next = new int[maxCoord + 1];

        // Initialize next pointers: every position is initially unpainted.
        // So the next unpainted position at i is i itself.
        for (int i = 0; i <= maxCoord; i++) {
            next[i] = i;
        }

        // ans[day] will store the amount of NEW area painted on that day.
        int[] ans = new int[days];

        // Process each day independently, while reusing the global "already painted" structure.
        for (int day = 0; day < days; day++) {
            int start = paint[day][0];
            int end = paint[day][1]; // interval is [start, end)

            int newlyPainted = 0;

            // Jump to the first unpainted position at or after start.
            int pos = find(next, start);

            // While pos is inside the current day's interval, it means pos is unpainted and should be painted now.
            while (pos < end) {
                newlyPainted++;      // We just painted one new unit (pos).

                // Mark pos as painted by linking it forward.
                // After painting pos, the "next unpainted position at pos" cannot be pos anymore,
                // so we set next[pos] to pos + 1 (i.e., skip over it).
                next[pos] = pos + 1;

                // Now jump again: find the next unpainted spot starting from pos (which now points to pos+1).
                pos = find(next, pos);
            }

            // Store the total newly painted units for this day.
            ans[day] = newlyPainted;
        }

        return ans;
    }

    // find(next, x) returns the smallest y >= x such that y is unpainted (i.e., next[y] == y),
    // or returns next.length (or x beyond bounds) when there's nothing left to paint.
    //
    // Path compression:
    // If next[x] points to some later position, we recursively find the true next unpainted position,
    // then rewrite next[x] to that result so future queries are faster.
    private int find(int[] next, int x) {
        // If x is already beyond our tracked coordinate range, just return x.
        // This avoids ArrayIndexOutOfBounds and acts as a natural "past the end" sentinel.
        if (x >= next.length) return x;

        // If next[x] == x, x is unpainted, so x is the answer.
        if (next[x] == x) return x;

        // Otherwise, x is painted. Jump to next[x], and compress the path.
        next[x] = find(next, next[x]);
        return next[x];
    }
}