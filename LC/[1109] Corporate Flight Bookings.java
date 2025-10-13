class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int N=n;
        List<int[]> events = new ArrayList<>();
        for(int ii=0; ii<bookings.length; ++ii){
            int st = bookings[ii][0];
            int ed = bookings[ii][1];
            int delta = bookings[ii][2];
            events.add(new int[]{st, delta});//[java][array][initialization]
            events.add(new int[]{ed+1, -delta});//ed is inclusive, we need to add 1 for the actual delta drop
        }

        int[][] events_arr = events.toArray(new int[events.size()][]);

        int[] ans = new int[N];
        for(var x: events_arr){
            int ts=x[0];
            int delta=x[1];
            if(ts-1<N) ans[ts-1] += delta;//convert to index 0
        }
        for(int ii=1; ii<N; ++ii){
             ans[ii] += ans[ii-1];
        }
        return ans;
    }
}

// * n flights (1, n)
// * bookins[first, last, seat] <-- range addition, first-last is inter
// * -> answer