class Solution {
    public int climbStairs(int n) {
        
        //define dp
        //dp[ii] = dp[ii-1]+dp[ii-2] (stair ii can only be reach from ii-1 and ii-2)
        if(n<=2) return n;
        int prev=2;
        int prevprev=1;
        int curr=0;
        for(int ii=3; ii<=n; ++ii){
            curr=prev+prevprev;
            prevprev=prev;
            prev=curr;
        }
        return curr;
    }
}
/* For type I DP: current state ii can be derived from (ii-1) state -> we only need one variable to remember state[ii-1]
*/