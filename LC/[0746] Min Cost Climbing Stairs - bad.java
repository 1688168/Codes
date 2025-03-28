class Solution {
    private int hp(int st, int ed, int[] cost){
        if(ed<=st){//pay nothing to reach starting point
            return cost[st];
        }
 
        return Math.min(hp(st, ed-1, cost), hp(st, ed-2, cost)) + cost[ed];

    }
    public int minCostClimbingStairs(int[] cost) {
        int N = cost.length;//num of stairs
        return Math.min(hp(0, N-1, cost), hp(1, N-1, cost));
    }
}
/*
* # Analysis
* N=1000 -> two loops
* given an array and optimize cost -> DP
*/