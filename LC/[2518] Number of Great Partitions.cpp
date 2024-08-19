using LL = long long;
class Solution {
    LL dp[10005][1005];
    LL M = 1e9+7;
public:
    int countPartitions(vector<int>& nums, int k) {
        if(accumulate(nums.begin(), nums.end(), 0LL) < 2*k) return 0;
        int n=nums.size();
        nums.insert(nums.begin(), 0);
        dp[0][0]=1;
        for(int ii=1; ii<=n; ++ii){//each proj
            for(int jj=0; jj<k; ++jj){//each group A sum value
                dp[ii][jj] = (dp[ii][jj] + dp[ii-1][jj])%M;
                if(jj >= nums[ii]) dp[ii][jj] =  (dp[ii][jj] + dp[ii-1][jj-nums[ii]])%M;
            }
        }
        LL invalid = 0;
        for(int jj=0; jj<k; ++jj ) invalid = (invalid + dp[n][jj])%M;

        LL total = 1;
        for(int ii=0; ii<n; ++ii) total = (total*2)%M;

        return (total - 2*invalid+M)%M;
    }
};