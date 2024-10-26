    class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int N = nums.size();
         nums.insert(nums.begin(), 1);
         nums.push_back(1);

         auto dp = vector<vector<int>> (N+2, vector<int>(N+2, 0));

         for(int len=1; len<=N; ++len){//try length
            for(int ii=1; ii+len-1<= N; ++ii){//each ii starting balloon in the interval
                int jj=ii+len-1; //ending balloon in the interval
                for(int kk=ii; kk<=jj; ++kk){//each last balloon in range [ii, jj]
                    /*
                    > consider dp[ii][kk-1] could be dp[1][0].
                    this is not a valid range, but since we inserted dummy in the begin and end.   dp[1][0] is actually 0
                    */
                    dp[ii][jj] = max(dp[ii][jj], dp[ii][kk-1] + dp[kk+1][jj] + nums[ii-1]*nums[kk]*nums[jj+1]);
                }
            }
         }
         return dp[1][N];
    }
};