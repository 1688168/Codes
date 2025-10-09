class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        //take measurement
        int N=trips.length;
        //declare events array
        int[][] events = new int[2*N][3];

        //convert intervals to events
        for(int ii=0;ii<N;++ii){
            int delta=trips[ii][0];
            int st=trips[ii][1];
            int ed=trips[ii][2];

            events[ii*2][0]=st;
            events[ii*2][1]=delta;
            events[ii*2+1][0]=ed;
            events[ii*2+1][1]=-delta;
        }

        //sort events
        Arrays.sort(events, (a,b)->a[0]==b[0]?Integer.compare(a[1], b[1]):Integer.compare(a[0], b[0]));

        //sweeping line to find out required max capacity
        int sum=0;
        for(int ii=0; ii<2*N; ++ii){//traverse all events
            int ts=events[ii][0];
            int delta=events[ii][1];
            sum+=delta;
            if(sum > capacity) return false;
        }

        return true;
    }
}

// * capacity
// * trips: (nn, start, end)
// * sweeping line regular form delta is +/-1.  here num of passengers changed delta to nn
// * can pick up/drop off all passengers
// * is capacity >= max overlap?