class Solution {
    public:
        int maxSumAfterPartitioning(vector<int>& arr, int k) {
            int N = arr.size();
            //declare/define DP
            vector<vector<int>> dp = vector(N, vector(k+1, INT_MIN/2));
            //initialize DP base cases
            //when ii=0
            dp[0][1] = arr[0];
    
            //when jj=0 //no partition
            for(int ii=1; ii<N; ++ii) dp[ii][0] = 0;
    
            //when jj=1 //one partition
    
            int mx = 0;
            for(int ii=1; ii<N; ++ii){
                mx=max(mx, arr[ii]);
                dp[ii][1] = mx*(ii+1);
            }
    
            //populate DP
            for(int ii=1; ii<N; ++ii){//for each element
                for(int jj=2; jj<=min(ii, k); ++jj){//for each partition
                    int mx=0;
                    int ttl=0;
                    for(int ss=ii; ss>=1; --ss){ //for each interval start
                        mx=max(mx, arr[ss]);
                        ttl += arr[ss];
                        dp[ii][jj] = max(dp[ii][jj], dp[ss-1][jj-1]+mx*(ii-ss+1));
                    }
                }
            }  
    
            return dp[N-1][k];
        }
    };