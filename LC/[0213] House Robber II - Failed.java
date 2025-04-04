class Solution {

    private int hp(int st, boolean isFirstRobbed, int prevRob, int curr, int[] nums){
        int N = nums.length;

        if(st >= N) return curr;
        if(prevRob == -1 || prevRob != st-1){//prevNoRob
            if(st==N-1){
                if(isFirstRobbed)
                    return hp(st+1, isFirstRobbed, prevRob, curr, nums);
                else  //last element, prevNoRob, firstNoRob  
                    return hp(st+1, isFirstRobbed, st, curr+nums[st], nums); 
            }else{//
                return Math.max(hp(st+1, isFirstRobbed, st, curr+nums[st], nums), hp(st+1, isFirstRobbed, prevRob, curr, nums));
            }
           
        }else{//prevRob
            return hp(st+1, isFirstRobbed, prevRob, curr, nums);
        }

    }

    public int rob(int[] nums) {
        return Math.max(hp(0, true, 0, nums[0], nums), hp(0, false, -1, 0, nums));
    }
}