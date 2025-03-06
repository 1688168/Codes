class Solution {
    public:
        int minimumDeleteSum(string s1, string s2) {
            int N1=s1.size();
            int N2=s2.size();
            s1="#"+s1;
            s2="#"+s2;
    
            //declare DP
            auto dp = vector<vector<int>>(N1+1, vector<int>(N2+1, INT_MAX/2));
            //initialize DP
            dp[0][0]=0;
            for(int ii=1; ii<=N1; ++ii){
                dp[ii][0] = dp[ii-1][0]+s1[ii];
            }
    
    
            for(int jj=1; jj<=N2; ++jj){
                dp[0][jj] = dp[0][jj-1]+s2[jj];
            }
    
            //populate DP
            for(int ii=1; ii<=N1; ++ii){
                for(int jj=1; jj<=N2; ++jj){
                    if(s1[ii]==s2[jj]){
                        dp[ii][jj]=dp[ii-1][jj-1];
                    }else{
                        dp[ii][jj] = min(dp[ii-1][jj]+s1[ii], dp[ii][jj-1]+s2[jj]);
                    }
                }
            }
    
            return dp[N1][N2];
            
        }
    };