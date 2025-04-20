class Solution {
    public int uniquePaths(int m, int n) {
        //current state can be derived from previous state.
        //for type I DP, we only need to keep previous state (no need to maintain the whole status) to preserve space
        //declare spaces for previous states
        //row zero are all 1s
        int[] prevY = IntStream.range(0, n+1).map(ii -> 1).toArray();
        int prevX=1;
        int currState = 0;
        if(m==1 || n==1) return 1;
        
        //consider edge cases
        //[0, jj] = 1
        for(int ii=1; ii<m; ++ii){
            prevX=1;
            for(int jj=1; jj<n; ++jj){
                currState = prevX+prevY[jj];
                prevX=currState;
                prevY[jj]=currState; 
            }
        }
        return currState;
    }
}