class Solution {
    public int rob(int[] nums) {
        //take metrics
        int N=nums.length; 
        if(N==0) return 0;
        if(N==1) return nums[0];

        //declare dp to maintain states
        /*
        * dp[ii][jj]: max profit for houses in [ii, jj]
        * dp[ii][jj] = max(nums[ii] +  dp[ii+2][jj], dp[ii+1][jj])
                           ^^^^^^^^^^^^^^^^^^^^^^^.  ^^^^^^^^^^^^
                           rob ii                    no rob ii
        */
        var dp = IntStream.range(0, N)
                          .mapToObj(ii -> IntStream.range(0, N)
                                          .map(jj -> 0)
                                          .toArray()
                          )
                          .toArray(int[][]::new);
        //initialize dp - base case -> a single house
        IntStream.range(0, N).forEach(ii->dp[ii][ii]=nums[ii]);
        //IntStream.range(0, N).forEach(ii->System.out.println(dp[ii][ii]));

        for(int ll=2; ll<=N; ++ll){//for each interval size
            for(int ii=0; ii+ll-1<N; ++ii){//for each starting point of interval
                int jj = ii+ll-1;
                dp[ii][jj] = Math.max(nums[ii]+((ii+2>jj)?0:dp[ii+2][jj]), dp[ii+1][jj]);
            }
        }

        return Math.max(nums[0]+((N-2<2)?0:dp[2][N-2]), dp[1][N-1]);
    }
}
/*
//Interval DP
* base case:
* 1. one house.
* 2. two house: max from the two
* 3. [xx]N or N[xx]
*/