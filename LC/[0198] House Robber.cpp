class Solution {
public:
    int rob(vector<int>& nums) {
        int N = nums.size();
        vector<int> dp(N+1, 0); //where dp[i] is the max amount the robber could accumulate @ house i

        for(int ii=1; ii<=N; ++ii){
            dp[ii]=max(dp[ii-1], nums[ii-1]+ (ii>=2? dp[ii-2]:0));
        }

        return dp[N];
        
    }
};