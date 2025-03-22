class Solution {
    public int maxSubArray(int[] nums) {
        int N = nums.length;
        int dp=Integer.MIN_VALUE/2;
        int mss= nums[0];

        for(int ii=0; ii<N; ++ii){
            dp = Math.max(nums[ii], nums[ii]+dp);
            mss=Math.max(mss, dp);
        }

        return mss;
        
    }
}