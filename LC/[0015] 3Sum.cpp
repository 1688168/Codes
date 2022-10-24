class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int N=nums.size();
        vector<vector<int>> res;
        for(int ii=0; ii<N; ++ii){
            if(nums[ii] > 0) break;
            if(ii==0 || nums[ii] != nums[ii-1])//O(N) time
                two_sum_sorted(nums, ii, res);
        }
        
        return res;
    }

    void two_sum_sorted(vector<int> & nums, int idx, vector<vector<int>> & res){
        int ll=idx+1, rr=nums.size()-1;
        while(ll<rr){
            int sum=nums[idx]+nums[ll]+nums[rr];

            if(sum==0){
                res.push_back({nums[idx], nums[ll], nums[rr]});
                ++ll;
                while(ll<rr and nums[ll]==nums[ll-1])++ll;
                // rr-=1
            }else if(sum > 0){
                --rr;
            }else{
                ++ll;
            }
        }
    }
};
