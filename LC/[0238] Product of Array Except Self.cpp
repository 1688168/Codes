
//O(1) space solution
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int N=nums.size();
        vector<int> ans(N, 0);
        for(int ii=0; ii<nums.size(); ++ii){
            if(ii==0){
                ans[ii]=1;
            }else{
                ans[ii]=nums[ii-1]*ans[ii-1];
            }
        }

        int nn = 1;

        for(int ii=N-1; ii>=0; --ii){

             ans[ii] *= nn;
             nn *= nums[ii];
        }

        return ans;
    }
};
