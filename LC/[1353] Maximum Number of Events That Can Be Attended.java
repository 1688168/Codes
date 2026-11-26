import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int maxEvents(int[][] events) {
        Arrays.sort(events, Comparator.comparingInt(event -> event[0]));

        int N = events.length;
        PriorityQueue<Integer> mnq = new PriorityQueue<>();
        int jj = 0;
        int cnt = 0;

        // int lastDay = 0;
        // for (int[] event : events) {
        //     lastDay = Math.max(lastDay, event[1]);
        // }

        int lastDay = Arrays.stream(events)
            .mapToInt(event -> event[1])
            .max()
            .orElse(0);

        for (int ii = 1; ii <= lastDay; ii++) {
            while (jj < N && events[jj][0] <= ii) {
                mnq.offer(events[jj][1]);
                jj++;
            }

            while (!mnq.isEmpty() && mnq.peek() < ii) {
                mnq.poll();
            }

            if (!mnq.isEmpty()) {
                mnq.poll();
                cnt++;
            }
        }

        return cnt;
    }
}