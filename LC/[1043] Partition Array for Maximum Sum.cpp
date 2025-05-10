class Solution {
    public:
        int maxSumAfterPartitioning(vector<int>& arr, int k) {
            int N = arr.size();

            //make 1 indexed array
            arr.insert(arr.begin(), 0);

            //declare/define DP
            vector<int> dp(N+1, 0);
    
            //populate DP
            for(int ii=1; ii<=N; ++ii){//for each element
                int mx=0;
                for(int ss=ii; ss>=max(ii-k+1, 1); --ss){ //for each potential last interval
                    mx=max(mx, arr[ss]);          
                    dp[ii] = max(dp[ii], dp[ss-1]+mx*(ii-ss+1));
                }
            }  
            return dp[N];
        }
    };