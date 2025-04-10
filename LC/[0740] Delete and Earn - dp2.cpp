class Solution {
    public:
        int deleteAndEarn(vector<int>& nums) {
            if(nums.size()==0) return 0;
            sort(nums.begin(), nums.end());
            int M = nums.back();
            vector<int> gain(M+1, 0);
            for(auto x: nums) gain[x] += x;
    
            vector<int> dp(M+1, 0);//dp[ii]: max gain by ending with ii
            dp[1]=gain[1];
            for(int ii=2; ii<=M; ++ii){
                dp[ii]=max(dp[ii-2]+gain[ii], dp[ii-1]);
            }
    
            return dp[M];
            
        }
    };
    /*
    * we want to delete a value and remove v+1, v+2
    * so this array actually is sortable as the result is the same after the sort
    */