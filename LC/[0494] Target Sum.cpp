class Solution {
    int dp[25][2005];
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        nums.insert(nums.begin(), 0);
        
        int offset = 1000;
        dp[0][0+offset]=1;
  
        for(int ii=1; ii<=n; ++ii){
            for(int jj=-1000; jj<=1000; ++jj){//no skip case (always take)
                if(jj-nums[ii]>=-1000 && jj-nums[ii]<=1000)
                    dp[ii][jj+offset] += dp[ii-1][jj-nums[ii]+offset];
                
                if(jj+nums[ii]>=-1000 && jj+nums[ii] <= 1000)
                    dp[ii][jj+offset] += dp[ii-1][jj+nums[ii]+offset];
            }
        }
        return dp[n][target+offset];       
    }
};