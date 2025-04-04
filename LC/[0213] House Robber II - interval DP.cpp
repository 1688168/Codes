class Solution {
    public:
        int rob(vector<int>& nums) {
            int N = nums.size();
            if(N==0) return 0;
            if(N==1) return nums[0];
    
            auto dp =vector<vector<int>>(N, vector<int>(N, 0));
            for(int ii=0; ii<N; ++ii) dp[ii][ii] = nums[ii];
            for(int len = 2; len<=N; ++len){//interval size
                for(int ii=0; ii+len-1<N; ++ii){ //starting point
                    int jj = ii+len-1;
                    dp[ii][jj] = max(nums[ii] + ((ii+2 > jj)? 0:dp[ii+2][jj]), dp[ii+1][jj]);
                }
            }
    
            return max(dp[1][N-1], nums[0] + ((N-2< 2)?0:dp[2][N-2]));
    
        }
    };
    
    /*
    * follow up
    * a circle.
    * pick a num and the neighbors are eliminated
    * max profit to pick and eliminate
    */