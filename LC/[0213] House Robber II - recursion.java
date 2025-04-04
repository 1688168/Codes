class Solution {

    private int hp(int st, boolean isFirstRobbed, int prevRob, int curr, int[] nums){
        int N = nums.length;
        if(isFirstRobbed && st==N-1) return curr; //first robbed, we cannot rob the last
        if(st >= N) return curr;


        if(prevRob == -1 || prevRob != st-1){//prevNoRob
            return Math.max(hp(st+1, isFirstRobbed, st, curr+nums[st], nums), hp(st+1, isFirstRobbed, prevRob, curr, nums));
        }else{//prevRob
            return hp(st+1, isFirstRobbed, prevRob, curr, nums);
        }
    }
    public int rob(int[] nums) {
        return Math.max(hp(1, true, 0, nums[0], nums), hp(1, false, -1, 0, nums));
    }
}