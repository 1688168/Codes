class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
       
        int m=s1.size();
        int n=s2.size();

        if(m+n != s3.size()) return false;

        //c++ initialize 2d vector
        auto dp = vector<vector<bool>>(m+1, vector<bool>(n+1, false));
        s1="#"+s1;
        s2="#"+s2;
        s3="#"+s3;
        dp[0][0]=1;//earlier we already checked if m+n=s3.size()
        //initialize DP (think about those that is not initialized in dp loop)

        for(int ii=1; ii<=m; ++ii){
            dp[ii][0] = dp[ii-1][0] && s1[ii]==s3[ii];
        }

        for(int jj=1; jj<=n; ++jj){
            dp[0][jj] = dp[0][jj-1] && s2[jj]==s3[jj];
        }

        for(int ii=1; ii<=m; ++ii){
            for(int jj=1; jj<=n; ++jj){
                if(s1[ii]==s3[ii+jj] && dp[ii-1][jj]){
                    dp[ii][jj]=true;
                }else if(s2[jj]==s3[ii+jj] && dp[ii][jj-1]){
                    dp[ii][jj]=true;
                }
            }
        }
        return dp[m][n];
    }
};