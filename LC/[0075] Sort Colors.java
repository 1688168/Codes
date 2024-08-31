//20240830
class Solution {
    public void sortColors(int[] nums) {
        int N=nums.length;
        int ii=0, jj=0, kk=N-1;
        int tmp=0;
        while(jj<=kk){
            if(nums[jj]==0){
                tmp=nums[jj];
                nums[jj]=nums[ii];
                nums[ii]=tmp;
                ++ii;
                ++jj;
            }else if(nums[jj]==1){
                ++jj;
            }else{
                tmp=nums[kk];
                nums[kk]=nums[jj];
                nums[jj]=tmp;
                --kk;
            }
        }
    }
}

//---------------
class Solution {
    private void swap(int ii, int jj, int[] nums){//java swap
        int tmp = nums[ii];
        nums[ii]=nums[jj];
        nums[jj]=tmp;
    }
    public void sortColors(int[] nums) {
        int N = nums.length;
        int ii=0, jj=0, kk=N-1;
        while(jj<=kk){
            if(nums[jj]<1){
                swap(ii++, jj++, nums);
            }else if(nums[jj]==1){
                ++jj;
            }else{
                swap(jj, kk--, nums);
            }
        }
    }
}
