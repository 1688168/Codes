import java.util.OptionalInt;
import java.util.stream.IntStream;
class Solution {
    public int lengthOfLIS(int[] nums) {
        int N = nums.length;
        //declare DP
        //Define DP: dp[ii]: max increasing sub-seq @ ii
        //dp[ii] = max(dp[jj] + 1, dp[ii]) for jj< ii
        var dp= new int[N];

        //initialize dp
        for(int ii=0; ii<N; ++ii) dp[ii]=1; //at least one element.

        //populate DP
        for(int ii=0; ii<N; ++ii){
            for(int jj=ii-1; jj>=0; --jj){
                dp[ii] = Math.max(dp[ii], (nums[ii] > nums[jj])?dp[jj]+1:dp[ii]);
            }
        }

        // int ans=1;
        // for(int ii=0; ii<N; ++ii) ans = Math.max(ans, dp[ii]);

        OptionalInt max = IntStream.of(dp).max();//[java][stream][max][array]

        // if (max.isPresent()) {
        //     return max.getAsInt();
        // } else {
        //     System.out.println("Array is empty!");
        //     return 1;
        // }


        return IntStream.of(dp)
                        .max()
                        .orElse(Integer.MIN_VALUE);
    }
}

// * N=2500 -> 400N
// * given a single array.
// * max increasing.
// * current status can be derived from previous state. -> dp
// * option of each N -> always take (VS house robber: rob/no_rob)
// * Type II DP is about previous state (dp[jj]) is at some point that we need to search backward. VS type I DP, previous state is @ (ii-1)
    
    