class Solution {
    private int hr1(int[] nums, int rob, int noRob, boolean isFirstRob){//house robber I
        int N = nums.length;

        for(int ii=1; ii<N; ++ii){
            if(isFirstRob && ii==1) {
                noRob=rob;//update noRob
                continue; //since first rob, we cannot rob the 2nd
            }

            if(isFirstRob && ii==N-1) break;  //sint first rob, we cannot rob the last
            int noRobTmp = noRob;
            noRob = Math.max(rob, noRobTmp);
            rob =  noRobTmp + nums[ii];
        }

        return Math.max(noRob, rob);

    }
    public int rob(int[] nums) {
        //first rob
        int firstRob = hr1(nums, nums[0], 0, true);

        //first noRob
        int firstNoRob = hr1(nums, 0, 0, false);

        return Math.max(firstRob, firstNoRob);

    }
}