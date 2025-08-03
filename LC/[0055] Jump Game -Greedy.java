class Solution {
    public boolean canJump(int[] nums) {
        int N = nums.length;
        int max_reachable = 0;//we can always reach 1st step
        for(int ii=0; ii<N; ++ii){//check each ii if reachable
            if(ii > max_reachable) return false; //we cannot reach ii before reaching N-1. 
            if(max_reachable >= N-1) return true;//we can reach N-1 from here no need to check further
            max_reachable = Math.max(max_reachable, ii + nums[ii]);
        }

        return true;
    }
}

