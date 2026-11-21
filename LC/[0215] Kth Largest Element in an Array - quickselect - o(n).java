class Solution {

    private void swap(int ii, int jj, int[] nums){
        int tmp=nums[jj];
        nums[jj]=nums[ii];
        nums[ii]=tmp;
    }

    private int quickSelect(int st, int ed, int[] nums, int kth){
        int pivot = nums[st+(ed-st)/2];
        int ii=st;//first idx equal to pivot
        int jj=st;//runner
        int kk=ed;//first idx from right 
        
        while(jj<=kk){
            if(nums[jj] > pivot){
                swap(jj, kk--, nums);
            }else if(nums[jj]==pivot){
                ++jj;
            }else{
                swap(ii++, jj++, nums);
            }
        }
        //S S S P P L L
        //      i k
        //0 1 2 3 4 5 6
        if(ed-kk >= kth){
            return quickSelect(kk+1, ed, nums, kth);
        }else if(ed-ii+1 >=kth){
            return pivot;
        }else{
            return quickSelect(st, ii-1, nums, kth-(ed-ii+1));
        }
    }
    public int findKthLargest(int[] nums, int k) {
        int N=nums.length;
        return quickSelect(0, N-1, nums, k);
    }
}

/*
# quick select
* exp time: o(N): N+n/2+... ---> N
* worst time: O(N^2): N+(N-1)+(N-2)+... ---> N^2
*/