class Solution {
    private int minCost=Integer.MAX_VALUE;
    private int hp(int st, int ed, int curr, int[] cost){
        if(st >= ed){
            minCost = Math.min(minCost, curr);
            return minCost;
        }

        return Math.min(hp(st+1, ed, curr+cost[st], cost), hp(st+2, ed, curr+cost[st], cost));   
    }
    public int minCostClimbingStairs(int[] cost) {
        int N = cost.length;
        int mm = Math.min(hp(0, N, 0, cost), hp(1, N, 0, cost));

        return minCost;
    }
}