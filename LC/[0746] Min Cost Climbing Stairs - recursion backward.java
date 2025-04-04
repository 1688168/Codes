class Solution {
    private int hp(int st, int N, int[] cost){
        if(N<=st){//pay nothing to reach starting point
            return cost[st];
        }
 
        int cc = N == cost.length? 0: cost[N];
        return Math.min(hp(st, N-1, cost), hp(st, N-2, cost)) + cc;
    }
    public int minCostClimbingStairs(int[] cost) {
        int N = cost.length;//num of stairs
        return Math.min(hp(0, N, cost), hp(1, N, cost));
    }
}