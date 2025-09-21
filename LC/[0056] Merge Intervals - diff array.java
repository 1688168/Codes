class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals==null || intervals.length==0) return new int[0][0];
        int N = intervals.length;
        int ii=0;
        int[][] events = new int[2*N][2]; //each interval has start/end two timestamps
        //break interval into individual timeStamp (time, +/-1)
        for(var interval: intervals){//for each interval
            //start pair
            events[ii][0] = interval[0];//start of interval
            events[ii][1] = 1;//increment start
            //end pair

            events[++ii][0] = interval[1];//end of interval
            events[ii++][1] = -1;
        }

        //sort timeStamp. be careful when we have overlapping start and end
        Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]);//need to update start first before end
        });
      
        //apply sweeping line algorithm to determin merged interval start/end
        int sum=0;
        List<int[]> ret = new ArrayList<>();
        //int[] new_interval = new int[]{0, 0};//[java][declare and initialize array]
        int start=0;
        for(var event: events){
            int ts=event[0];
            int delta=event[1];
            if(sum==0 && delta==1){//opening interval
                start=ts;
            }
            else if(sum>0 && sum+delta==0){ //closing interval 
                ret.add(new int[]{start, ts});
            }
            sum += delta;
        }
        return ret.toArray(new int[ret.size()][]);
    }
}

 
