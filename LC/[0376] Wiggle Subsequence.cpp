class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if(nums.size()==0) return 0;
        int p=1, q=1;
        for(int ii=1; ii<nums.size(); ++ii){
            if(nums[ii] > nums[ii-1]){
                q=p+1;
            }else if(nums[ii] < nums[ii-1]){
                p=q+1;
            }
        }

        return max(p, q);
    }
};