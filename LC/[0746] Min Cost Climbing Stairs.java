class Solution {
    private int hp(int st, int N, int[] cost){
        if(N-2==st || N-3==st){//pay nothing to reach starting point
            return 0;
        }
        
        if(N <= 0) return 0; //base case not likely to happen
        
        return Math.min(hp(st, N-1, cost)+cost[N-2], hp(st, N-2, cost)+cost[N-3]);

    }
    public int minCostClimbingStairs(int[] cost) {
        int N = cost.length;
        return Math.min(hp(0, N, cost), hp(1, N, cost));
    }
}
/*
* # Analysis
* N=1000 -> two loops
* given an array and optimize cost -> DP
*/