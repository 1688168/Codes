class Solution {
    public int rob(int[] nums) {
        int N=nums.length;
        int rob=0;
        int no_rob=0;
        
        //ii=0
        rob=nums[0];
      
        for(int ii=1; ii<N; ++ii){
            int tmp_rob=rob;
            int tmp_no_rob=no_rob;
            rob = tmp_no_rob+nums[ii];
            no_rob = Math.max(tmp_rob, tmp_no_rob);
        }

        return Math.max(rob, no_rob);
        
    }
}