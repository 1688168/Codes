class Solution {
    public:
        int minSpaceWastedKResizing(vector<int>& nums, int k) {
            int N = nums.size();
            //declare/define DP
            int dp[N][k+1]; //for each number, each adjustment count
            int mx=0;
            int sum = 0;
            //initialize DP
            for(int ii=0; ii<N; ++ii){
                for(int jj=0; jj<=k; ++jj){ 
                    dp[ii][jj] = INT_MAX/2; //default to max cost
                }
            }
    
            for(int ii=0; ii<N; ++ii){//when no reset, the best solution is default to max in (0, ii)
                mx = max(mx, nums[ii]);
                sum += nums[ii];
                dp[ii][0] = mx*(ii+1) - sum;
    
            }
    
            //ii need to be greater than s as s is previous section not including ii
            for(int ii=1; ii<N; ++ii){//for each element in nums, ii starts from 1, : the array can have any size as count
                for(int jj=1; jj<=min(ii, k); ++jj){//for each adjustment
                //for(int jj=1; jj<=min(ii, kk); ++jj)
              
                    int mx = 0;
                    int intervalSum=0;
                    
                    //we do not know the best previous adjustment index, so we try all and keep the optimal one
                    for(int ss=ii; ss>=1; --ss){//find prev adjustment. ss from 1: since start can be any size
                        mx = max(mx, nums[ss]);
                        intervalSum += nums[ss];
    
                        dp[ii][jj] = min(dp[ii][jj], dp[ss-1][jj-1]+mx*(ii-ss+1) - intervalSum);
                    }
    
                }
            }
    
            int ret = INT_MAX/2;
            for(int jj=0; jj<=k; ++jj){
                ret = min(ret, dp[N-1][jj]);
            }
            return ret;
            
        }
    };