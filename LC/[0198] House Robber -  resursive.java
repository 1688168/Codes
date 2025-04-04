class Solution {
    int mxp = 0;
    private int hp(int st, int curr, boolean isPrevRobbed, int[] nums){
        int N = nums.length;
        if(st >=N) return curr;

        if(isPrevRobbed){
            return hp(st+1, curr, false, nums);
        }else{
            return Math.max(hp(st+1, curr, false, nums), hp(st+1, curr+nums[st], true, nums));
        }
    }
    public int rob(int[] nums) {
        return Math.max(hp(0, 0, false, nums), hp(0, 0, true, nums));
    }
}
/*
# Analysis:
* N=100
* single array
-> max profit
* constrain: cannot pick two consecutive house
*/
