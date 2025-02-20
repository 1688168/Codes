class Solution {
    public:
        string minWindow(string s1, string s2) {
            int m = s1.size();
            int n = s2.size();
    
            s1 = "#" + s1;
            s2 = "#" + s2;
    
            vector<vector<int>> dp(m+1, vector<int>(n+1, INT_MAX/2));
    
            for(int jj=1; jj<=n; ++jj) dp[0][jj] = INT_MAX/2;
            for(int ii=1; ii<=m; ++ii) dp[ii][0]=0;
    
            dp[0][0] = 0;
    
            for(int ii=1; ii<=m; ++ii){
                for(int jj=1; jj<=n; ++jj){
                    if(s1[ii]==s2[jj]){
                        dp[ii][jj]=dp[ii-1][jj-1]+1;
                    }else{
                        dp[ii][jj] = dp[ii-1][jj]+1;
                    }
                }
            }
            
            int len = INT_MAX/2;
            int pos;
            for(int ii=1; ii<=m; ++ii){
                if(dp[ii][n] < len){
                    len=dp[ii][n];
                    pos=ii;
                }
            }
    
            if(len == INT_MAX/2) return "";
    
            return s1.substr(pos-len+1, len);
        }
    };
    
    /*
    dp[ii][jj]: the minimum subsequence len k, s.t. s2[1:jj] is a subsequence of s1[ii-k+1:ii]
    
    if 
        s1[ii]==s2[jj]: dp[ii][jj] = dp[i-1][jj-1]
    else
        dp[ii][jj] = dp[ii-1][jj]+1
    
    s1 x x x x {x x x x x x ii}
    s2 [y y y] jj
    
    return min{dp[ii][N]} where ii=1, 2, ..., M
    */