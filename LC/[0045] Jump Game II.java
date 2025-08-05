class Solution {
    public int jump(int[] nums) {
        int N=nums.length;

        //declare and initialize dp
        var dp = IntStream.range(0, N)
                          .map(ii -> Integer.MAX_VALUE/2)
                          .toArray();

        //ii=0
        dp[0]=0;
        for(int ii=0; ii<N; ++ii) {
             for(int jj=ii-1; jj>=0; --jj) {
                 dp[ii] = (jj+nums[jj]) >= ii? Math.min(dp[ii], dp[jj]+1):dp[ii];
             }  
        }

        return dp[N-1];
    }
}

// * N=10^4 -> btn nlogn, N^2
// * greedy: yes/no (can you reach ii question)
// * DP II: dp[ii]: min num of jump to get ii
//     s.t. dp[ii] = min(dp[ii], dp[jj]+1) where 0<= jj < ii
// -> return dp[N-1]