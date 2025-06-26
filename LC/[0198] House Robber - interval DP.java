class Solution {
    public int rob(int[] nums) {
        //solving with interval dp
        int N = nums.length;
        //define dp
        //dp[ii][jj]: the max profit robbing house between [ii, jj] (inclusive)
        //dp[ii][jj] = max(nums[ii]+dp[ii+2, jj], dp[ii+1, jj])

        //edge case handling on user inputs
        if(N==0) return 0;
        if(N==1) return nums[0];

        //declare and initialize DP
        //[java][2d][stream][array]
        var dp = IntStream.range(0, N)
                          .mapToObj(ii -> IntStream.range(0, N)
                                                   .map(jj -> 0)
                                                   .toArray()
                          ).toArray(int[][]::new);
        
        //initialize dp
        for(int ii=0; ii<N; ++ii) dp[ii][ii] = nums[ii];//max profit for single house
        
        //populate dp
        for(int ll=2; ll<= N; ++ll){//for each length
            for(int ii=0; ii+ll-1 < N; ++ii){
                int jj = ii+ll-1;
                dp[ii][jj] = Math.max(nums[ii]+(((ii+2)<= jj)? dp[ii+2][jj]:0), dp[ii+1][jj]);

            }
        }

        return dp[0][N-1];
    }
    
}