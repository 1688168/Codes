class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int ii = nums.size()-1;
        while(ii-1 >= 0 &&nums[ii-1] >= nums[ii]){
            --ii;
        }
        if(ii==0){
            sort(nums.begin(), nums.end());
            return;
        }

        --ii;
        int jj=nums.size()-1;
        while(nums[jj] <= nums[ii]){
            --jj;
        }
        swap(nums[ii], nums[jj]);
        sort(nums.begin()+ii+1, nums.end());
        return;
    }
};