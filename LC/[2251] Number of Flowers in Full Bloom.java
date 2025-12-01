import java.util.*;

class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        // 1) Build difference map: time -> delta count
        //    +1 at start, -1 at end + 1 (since intervals are inclusive)
        TreeMap<Integer, Integer> events = new TreeMap<>();
        for (int[] interval : flowers) {
            int st = interval[0];
            int ed = interval[1];
            events.put(st, events.getOrDefault(st, 0) + 1);
            events.put(ed + 1, events.getOrDefault(ed + 1, 0) - 1);
        }

        int n = people.length;
        int[] rets = new int[n];

        // 2) Prepare people as (time, originalIndex) and sort by time
        int[][] ppl_ts_idx = new int[n][2];
        for (int i = 0; i < n; ++i) {
            ppl_ts_idx[i][0] = people[i]; // time
            ppl_ts_idx[i][1] = i;         // original index
        }
        Arrays.sort(ppl_ts_idx, (a, b) -> Integer.compare(a[0], b[0]));

        // 3) Sweep events and people together
        int cnt = 0;  // current number of flowers in bloom
        Iterator<Map.Entry<Integer, Integer>> it = events.entrySet().iterator();
        Map.Entry<Integer, Integer> curEvent = null;

        if (it.hasNext()) {
            curEvent = it.next();
        }

        for (int[] ts_idx : ppl_ts_idx) {
            int t = ts_idx[0];
            int idx = ts_idx[1];

            // Apply all events up to and including time t
            while (curEvent != null && curEvent.getKey() <= t) {
                cnt += curEvent.getValue();
                curEvent = it.hasNext() ? it.next() : null;
            }

            rets[idx] = cnt;
        }

        return rets;
    }
}

// class Solution {
//     public int[] fullBloomFlowers(int[][] flowers, int[] people) {
//         int N = flowers.length;//number of intervals

//         //convert intervals to sorted events
//         Map<Integer, Integer> events = new TreeMap<>();
//         for(var interval: flowers){
//             int st=interval[0];
//             int ed=interval[1];
//             events.put(st, events.getOrDefault(st, 0)+1);
//             events.put(ed+1, events.getOrDefault(ed+1, 0)-1);
//         }
//         //prepare output space
//         int[] rets = new int[people.length];

//         //sort the people, we want to know the original index
//         //convert people array to 2D (ts, idx) array
//         int[][] ppl_ts_idx = new int[people.length][2];
//         for(int ii=0; ii<people.length; ++ii){
//             ppl_ts_idx[ii][0] = people[ii];
//             ppl_ts_idx[ii][1] = ii;
//         }

//         //soprt ppl_ts_idx by ts
//         Arrays.sort(ppl_ts_idx, (a, b) -> Integer.compare(a[0], b[0]));

//         //we need to convert events to array so we can reference by index
//         int[][] events_arr = new int[2*N][2];
//         int ii=0;
//         for(Map.Entry<Integer, Integer> entry: events.entrySet()){
//             events_arr[ii][0] = entry.getKey();//ts
//             events_arr[ii++][1] = entry.getValue();//cnt
//         }

//         //now we have sorted people (with idx) and sorted events (by treeMap nature)
//         int jj=0; //starting point of events_arr
//         int cnt=0;
//         for(var ts_idx: ppl_ts_idx){ //for each ppl, we accumulate cnt from events upto ts
//             int ts=ts_idx[0];
//             int idx=ts_idx[1];

//             while(jj<2*N && events_arr[jj][0] <= ts){
//                 cnt += events_arr[jj][1];
//                 ++jj;
//             }
//             rets[idx]=cnt;   
//         }

//         return rets;
        
//     }
// }

