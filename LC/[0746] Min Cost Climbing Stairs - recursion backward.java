class Solution {
    private int hp(int st, int ed, int[] cost){
         if(st==ed) return 0;//at the end
         if(ed-st==1) return cost[st];//only 1 step

         //starting two steps
         int prev = cost[st];//one step
         int prevprev=0;//no steps
         int curr=0;
         for(int ii=st+2; ii<=ed; ++ii){//starting from two stesp
            curr = Math.min(prev+cost[ii-1], prevprev+cost[ii-2]);
            prevprev=prev;
            prev=curr;
         }
         return curr;

    }
    public int minCostClimbingStairs(int[] cost) {
        /*
         * dp[ii]: min cost reaching ii
         * dp[ii] = dp[ii-1] + dp[ii-2]
         -> we need the state of prev 2 states
         */
        int N = cost.length;
        return Math.min(hp(0, N, cost), hp(1, N, cost));//reducing the problem to always start from 0
    }
}