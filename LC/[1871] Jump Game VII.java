class Solution {
    public boolean canReach(String s, int minJump, int maxJump) {
        int N=s.length();
        
        //rule out base cases
        if(s.charAt(N-1)=='1') return false;

        //do we have enough space?: N=10^5 -> okay
        int[] events = new int[N+1];//ending event is recorded after maxJump

        //special handle ii=0
        int canReach = 0;
        if(minJump <= N) events[minJump] = 1;
        if(maxJump+1 <= N) events[maxJump+1] = -1;

        for(int ii=1; ii<N; ++ii){
            canReach += events[ii];
            if(canReach == 0) continue;//not reachable, cannot contribute to the future
            if(s.charAt(ii) == '1') continue; //cannot jump to '1'

            if(ii+minJump <= N) events[ii+minJump] +=1;
            if(ii+maxJump+1 <=N) events[ii+maxJump+1] -= 1;
            
        }
        return canReach > 0;
    }
}

