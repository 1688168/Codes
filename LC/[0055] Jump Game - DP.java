class Solution {
    public boolean canJump(int[] nums) {
        int N=nums.length;
        var dp = IntStream.range(0, N)//default false for all
                          .map(ii -> 0)
                          .toArray();
        //initial value
        dp[0] = 1; //first step is always reachable

        for(int ii=1; ii<N; ++ii){
            for(int jj = ii-1; jj>=0; --jj){
                if(dp[jj]==1 && jj+nums[jj]>= ii){//jj is reachable
                    dp[ii] = 1;
                    break;//prune 
                }
            }
        }   

        return dp[N-1]==1;
    }
}

// * N=10^4 -> nlogn
// * true/false -> reach the end
// * dp[ii] = can reach @ ii
//   dp[ii] = dp[jj] && jj+nums[jj] >= ii
// * type II dp N^2