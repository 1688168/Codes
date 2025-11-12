class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {
        int N = ranges.length;
        int[][] events = new int[N*2][2];

        //convert interval to events
        for(int ii=0; ii<N; ++ii){
            events[ii*2][0] = ranges[ii][0];
            events[ii*2][1] = 1;
            events[ii*2+1][0] = ranges[ii][1]+1;
            events[ii*2+1][1] = -1;
        }

        //sort events
        Arrays.sort(events, (a , b)->a[0]==b[0]?Integer.compare(b[1], a[1]):Integer.compare(a[0],b[0]));

        for (int[] iv : events) {
            System.out.print("[" + iv[0] + "," + iv[1] + "] ");
        }
        
        List<int[]> intervals = new ArrayList<>();
        
        int sum=0;
        int start=0;
        for(var ee: events){
            int ts=ee[0];
            int delta=ee[1];
            // System.out.println("ts: " + ts + ": delta=" + delta);
            if(sum==0 && delta==1){
                start=ts;
                sum+=delta;
                // System.out.println("Start set: " + start);
                continue;
            }

            if(sum>0 && sum+delta==0){
                // System.out.println("Setting End");
                intervals.add(new int[]{start, ts-1});
            }
            sum+=delta;
        }

        // var merged = intervals.toArray(new int[intervals.size()][]);
        System.out.println();
        // for (int[] iv : intervals) {
        //     System.out.print("[" + iv[0] + "," + iv[1] + "] ");
        // }

        for(var x:  intervals){
            if(left >= x[0] && right <= x[1]) return true;
        }
        return false;
    }
}

// * if we merge all intervals
// * how many intervals in [left, right]?