class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
            int N1 = text1.size();
            int N2 = text2.size();
    
            string ss = "#" + text1;
            string tt = "#" + text2;
    
            auto dp = vector<vector<int>>(N1+1, vector<int>(N2+1, 0));
    
            for(int ii=1; ii<=N1; ++ii){
                for(int jj=1; jj<=N2; ++jj){
                    if(ss[ii]==tt[jj]){
                        dp[ii][jj] = max(dp[ii][jj], dp[ii-1][jj-1]+1);
                    }else{
                        dp[ii][jj] = max(dp[ii][jj], max(dp[ii-1][jj], dp[ii][jj-1]));
                    }
                }
            }
    
    
            return dp[N1][N2];
    
        }
    };