class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int dp1=1;
        int dp2=1;
        int ans=INT_MIN;



        for(int ii=0; ii<nums.size();++ii){
            int tmp1=dp1;
            int tmp2=dp2;

            dp1=max(max(tmp1*nums[ii], tmp2*nums[ii]), nums[ii]);
            dp2=min(min(tmp1*nums[ii], tmp2*nums[ii]), nums[ii]);
            ans=max(ans, dp1);
        }

        return ans;

    }
};
