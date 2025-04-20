class Solution {
    public int maxSubArray(int[] nums) {
        int N = nums.length;
        int mxs=Integer.MIN_VALUE;
        int dp = 0;

        for(var x: nums){
            dp = Math.max(dp+x, x);
            mxs = Math.max(mxs, dp);
        }

        return mxs;
    }
}

/*
* optimize a value from a single array -> type I DP
* -> max(sum(subarray))
* N=10^5 -> NlogN
* dp[ii]: max subarray sum for array ending at ii from nums

*/