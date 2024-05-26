/*
* 20240526
*/

class Solution {

    vector<vector<int>> two_sum(int st, int target, vector<int> & nums){
        int ll=st, rr=nums.size()-1;
        vector<vector<int>> res;
        while(ll<rr){
            int a=nums[ll], b=nums[rr];
            if(a+b==target){       
                res.push_back({a, b});
                ++ll;
                --rr;
                while(ll>st && ll < rr && nums[ll]==nums[ll-1])++ll;
            }else if(a+b > target){
                --rr;
            }else{
                ++ll;
            }
        }
        return res;
    }

public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int N=nums.size();
        
        vector<vector<int>> res;
        for(int ii=0; ii<N-2; ++ii){
            if(ii>0 && nums[ii]==nums[ii-1]) continue;
            vector<vector<int>> twos = two_sum(ii+1, 0-nums[ii], nums);

            for(int jj=0; jj<twos.size(); ++jj){
                res.push_back({nums[ii], twos[jj][0], twos[jj][1]});
            }
        }

        return res;        
    }
};

/* --------------------------------------------------- */
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
