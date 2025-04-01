class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        int prevRobbedMxp=0;
        int prevNoRobMxp=0;
        int curr=0;
        for(int ii=0; ii<N; ++ii){
            curr = Math.max(prevRobbedMxp, prevNoRobMxp+nums[ii]);
            int prevNoRobMxpTmp = prevNoRobMxp;
            prevNoRobMxp=Math.max(prevRobbedMxp, prevNoRobMxp);
            prevRobbedMxp=prevNoRobMxpTmp+nums[ii];
        }

        return Math.max(prevNoRobMxp, prevRobbedMxp);
    }
}
/*
* N=100
* dp[ii]: max profit @ house ii
* dp[ii] = dp[ii-1] + isPrevRobbed?0:nums[ii]
*/