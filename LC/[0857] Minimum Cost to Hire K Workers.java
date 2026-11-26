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

// ------------------------------
// -------------- 20261124
// ------------------------------

class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        // zip the two array and sort by rate (wage/quality)
        List<int[]> qw_list = new ArrayList<>();
        int N = quality.length;

        for(int ii=0; ii<N; ++ii){
            qw_list.add(new int[]{quality[ii], wage[ii]});
        }

        //sort by rate and convert to array
        int [][] qw_sorted = qw_list.stream().sorted(Comparator.comparingDouble(qw_pair -> qw_pair[1]*1.0/qw_pair[0])).toArray(int[][]::new);//check syntax::java sort arrayList and convert to array

        PriorityQueue<Integer> mxq = new PriorityQueue<>(Comparator.reverseOrder());//check syntax max priorityQueue
        
        // for each rate, select k workers with min quality and maintain/record acc_quality and min_amount
        int acc_q = 0;
        double mnm = Double.POSITIVE_INFINITY; //check syntax: Java max double value
        for(int ii=0; ii<N; ++ii){
            int curr_q = qw_sorted[ii][0];
            int curr_w = qw_sorted[ii][1];
            double curr_rate = (double)curr_w/curr_q;

            if(mxq.size() < k-1){
                acc_q += curr_q;
                mxq.offer(curr_q);
            }else{
                acc_q += curr_q;
                mnm = Math.min(mnm, curr_rate*acc_q);
                mxq.offer(curr_q);
                int out_q = mxq.poll();
                acc_q -= out_q;
            }
        }
        return mnm;
    }
}