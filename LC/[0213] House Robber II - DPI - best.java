class Solution {
    private int houseRobberI(int [] nums){
        int N = nums.length;
        if(N==0) return 0;

        int rob = nums[0];
        int no_rob = 0;

        for(int ii=1; ii<N; ++ii){
            int tmp_rob = rob;
            int tmp_no_rob = no_rob;

            rob = nums[ii]+tmp_no_rob;
            no_rob = Math.max(tmp_rob, tmp_no_rob);
        }

        return Math.max(rob, no_rob);
    }

    public int rob(int[] nums) {
        /*
        //first rob
        r nr o o o nr -> max profit 1
        //first no rob
        0 o  o o o o  -> max profit 2
        => return max(mxP1, mxP2)
        */
        //first rob
        int N = nums.length;
        if(N==1) return nums[0];
        if(N==2) return Math.max(nums[0], nums[1]);
        int mxp_first_rob = nums[0] + houseRobberI(Arrays.copyOfRange(nums, 2, N-1));
        int mxp_first_no_rob = houseRobberI(Arrays.copyOfRange(nums, 1, N));//[java][slicing][array]
        return Math.max(mxp_first_rob, mxp_first_no_rob);
    }
}