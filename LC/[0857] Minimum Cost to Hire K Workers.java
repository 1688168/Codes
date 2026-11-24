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


//-------------- 20261124
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        //we want to first sort by rate
        List<int[]> quality_wage = new ArrayList<>();
        int N = quality.length;
        for(int ii=0; ii<N; ++ii){
            quality_wage.add(new int[]{quality[ii], wage[ii]});
        }

        int[][] quality_wage_sorted = quality_wage.stream().sorted(Comparator.comparingDouble(worker -> (double) worker[1] / worker[0])).toArray(int[][]::new);

    //     int[][] quality_wage_sorted = quality_wage.toArray(new int[0][]);
    //     Arrays.sort(quality_wage_sorted,
    // Comparator.comparingDouble(worker -> (double) worker[1] / worker[0]));

        //using each rate as threshold
        PriorityQueue<Integer> mxq = new PriorityQueue<>(Comparator.reverseOrder());    
        int acc_q = 0;
        double min_money = Double.POSITIVE_INFINITY;//how to do max_double in java?

        for(int ii=0; ii<N; ++ii){
            int curr_q = quality_wage_sorted[ii][0];
            int curr_w = quality_wage_sorted[ii][1];
            double rate = curr_w*1.0/curr_q;
        
            if (mxq.size() < k - 1) {
                mxq.offer(curr_q);
                acc_q += curr_q;
            } else {
                min_money = Math.min(min_money, (acc_q + curr_q) * rate);

                mxq.offer(curr_q);
                acc_q += curr_q;
                acc_q -= mxq.poll();
            }
        }
        return min_money;
    }
}


/*
* this is using sort to see who qualifies given a threshold.
* this then uses heap to select the next best candidate
 */