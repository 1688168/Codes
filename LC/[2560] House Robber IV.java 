class Solution {
    private boolean isFeasible(int[] nums, int capability, int k){
        int N = nums.length;
        int CC = capability;
        int rob=1;
        int no_rob=0;

        rob=nums[0] <= CC?1:0;

        for(int ii=1; ii<N; ++ii){
            int tmp_rob=rob;
            int tmp_no_rob=no_rob;
            if(nums[ii] <= CC){//can rob
                rob = 1 + tmp_no_rob;
            }
            no_rob = Math.max(tmp_rob, tmp_no_rob);
            if(Math.max(rob, no_rob) >= k) return Math.max(rob, no_rob) >= k;
        }
        int cnt = Math.max(rob, no_rob);
        return cnt >= k;
    }

    public int minCapability(int[] nums, int k) {
        int N = nums.length;
        int ll=0;
        int rr=1_000_000_000;
        int ans=Integer.MAX_VALUE;
        while(ll<=rr){
            int mm=ll+(rr-ll)/2;
            if(isFeasible(nums, mm, k)){
                ans=mm;
                rr=mm-1;
            }else{
                ll=mm+1;
            }
        }
        return ans;
    }
}

// > min capability to rob k houses
// * N=10^5
// * no adjacent
// * max capability on a house: cc
// -> we don't know cc -> guess -> binary search
// -> given a cc -> num of houses can rob -> isFeasible -> DP