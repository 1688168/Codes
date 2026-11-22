import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        int[][] workers = new int[quality.length][2];
        for (int i = 0; i < quality.length; i++) {
            workers[i][0] = quality[i];
            workers[i][1] = wage[i];
        }

        Arrays.sort(workers, Comparator.comparingDouble(
                (int[] worker) -> (double) worker[1] / worker[0]));

        PriorityQueue<Integer> maxHeap =
                new PriorityQueue<>(Comparator.reverseOrder());

        long totalQuality = 0;
        double minCost = Double.POSITIVE_INFINITY;

        for (int[] worker : workers) {
            int q = worker[0];
            double rate = (double) worker[1] / q;

            if (maxHeap.size() == k) {
                totalQuality -= maxHeap.poll();
            }

            maxHeap.offer(q);
            totalQuality += q;

            if (maxHeap.size() == k) {
                minCost = Math.min(minCost, totalQuality * rate);
            }
        }

        return minCost;
    }
}