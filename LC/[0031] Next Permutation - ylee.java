class Solution {
    public void nextPermutation(int[] nums) {
        int N=nums.length;
        //find the pivot
        int ii = N-1;
        while(ii>=0){
            if(ii==N-1 || nums[ii] >= nums[ii+1]){
                --ii;
                continue;
            }
            break;
        }

        if(ii>=0){//we have pivot
            int jj=N-1;
            while(jj>ii && nums[jj] <= nums[ii]) --jj;
            
            int tmp = nums[ii];
            nums[ii] = nums[jj];
            nums[jj] = tmp;
        }

        //reverse the order
        int ll=ii+1;
        int rr=N-1;
        while(ll<rr){
            int tmp = nums[ll];
            nums[ll] = nums[rr];
            nums[rr]=tmp;
            ++ll;
            --rr;
        }
    }
}