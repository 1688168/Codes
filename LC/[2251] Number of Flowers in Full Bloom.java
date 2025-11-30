import java.util.*;

class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        // events: time -> delta count (+1 at start, -1 at end+1)
        TreeMap<Integer, Integer> events = new TreeMap<>();//sorted map

        // build events from interval
        for (int[] flower : flowers) {
            int st = flower[0];
            int ed = flower[1];
            events.put(st, events.getOrDefault(st, 0) + 1);
            events.put(ed + 1, events.getOrDefault(ed + 1, 0) - 1); // inclusive interval
        }

        // flatten events into arrays (sorted by time because TreeMap)
        // map is already sorted, do we need to flatten it?
        int m = events.size();
        int[] times = new int[m];//we can use 2D array to in place of C++ pairs
        int[] deltas = new int[m];
        int k = 0;
        for (Map.Entry<Integer, Integer> e : events.entrySet()) {
            times[k] = e.getKey();
            deltas[k] = e.getValue();
            k++;
        }

        int n = people.length;
        int[] ans = new int[n];

        // peopleSorted: [time, originalIndex]
        int[][] peopleSorted = new int[n][2];
        for (int i = 0; i < n; i++) {
            peopleSorted[i][0] = people[i];
            peopleSorted[i][1] = i;
        }
        //java sort 2d array
        Arrays.sort(peopleSorted, (a, b) -> Integer.compare(a[0], b[0]));

        int cnt = 0;   // current number of blooming flowers
        int j = 0;     // pointer into events

        // sweep people in time order, consuming events as we go
        for (int[] p : peopleSorted) { //for each sorted ppl pair
            int t = p[0];
            int originalIdx = p[1];

            while (j < m && times[j] <= t) {//accumulate the cnts up to arrival time
                cnt += deltas[j];
                j++;
            }

            ans[originalIdx] = cnt;
        }

        return ans;
    }
}