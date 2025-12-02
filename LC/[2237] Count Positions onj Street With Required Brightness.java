class Solution {
    public int meetRequirement(int n, int[][] lights, int[] requirement) {
        int N=n;//take size of inputs
        // convert intervals to events
        int[] events = new int[N+1];
        for(var pp_range: lights){
            int pp = pp_range[0];
            int rr = pp_range[1];
            int st=Math.max(pp-rr, 0);
            int ed=Math.min(N, pp+rr+1);    
            events[st] += 1;
            events[ed] -= 1;
        }
        // ensure order of events (done)
        // accumulate count
        int ans=0;
        int cnt=0;
        for(int ii=0; ii<requirement.length; ++ii){
            cnt += events[ii];
            if(cnt >= requirement[ii]) ans+=1;
        }

        return ans;
    }
}


// ### Given
// * n: 
// * lights[ii] = ii, range. --> interval --> sweepline
// * requirement[ii]: required brightness @ ii

// ### Analysis
// * N=10^5 -> NlogN