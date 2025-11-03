class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int N=s.length();
        boolean[] reachable = new boolean[N]; //default to be all false.

        //edge case check
        if(s.charAt(0) == '1' || s.charAt(N-1)=='1') return false;

        reachable[0]=true; //initial step is always true

        int next_start=0;
        for(int ii=0; ii<N; ++ii){
            if(s.charAt(ii) == '1') continue; //not reachable per definition
            if(!reachable[ii]) continue;
            int min_reach=Math.max(next_start, ii+minJump);
            int max_reach=Math.min(N-1, ii+maxJump);
            for(int jj=min_reach; jj<= max_reach; ++jj){
                if(s.charAt(jj)=='1') continue;
                reachable[jj]=true;
            }
            if(reachable[N-1]) return true;
            next_start = Math.max(next_start, max_reach);
        }
        
        return false;
    }
}