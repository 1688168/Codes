class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
       int N = intervals.length;
       
       if(N == 0) return true;

       Arrays.sort(intervals, Comparator.comparingInt((int[] pair) -> pair[0])
                                 .thenComparingInt(pair -> pair[1])); 
       
       //we actually do not need to sort by ed
       //Arrays.sort(intervals, Comparator.comparingInt((int[] pair) -> pair[0]));
       int st = intervals[0][0];
       int ed = intervals[0][1];

       for(int ii=1; ii<N; ++ii){
            int ns = intervals[ii][0];
            int ne = intervals[ii][1];
            if(ns < ed && ne >= st) return false;
            st = ns;
            ed = ne;
       }

       return true;
    }
}