class Solution {
public:
    void sortColors(vector<int>& nums) {
        int N=nums.size();
        int ii=0, jj=0, kk=N-1;
        while(jj<=kk){
            if(nums[jj]< 1){
                swap(nums[ii++], nums[jj++]);
                // ++ii;
                // ++jj;
            }else if (nums[jj]==1){
                ++jj;
            }else{
                swap(nums[jj], nums[kk--]);
                //--kk;
            }

        }
        
    }
};