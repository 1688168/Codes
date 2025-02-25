class Solution {
    public:
        string shortestCommonSupersequence(string str1, string str2) {
            int m = str1.size();
            int n = str2.size();
    
            str1 = "#" + str1;
            str2 = "#" + str2;
    
            //declare dp
            auto dp = vector<vector<int>>(m+1, vector<int>(n+1, 0));
    
            //initialize dp
            for(int ii=1; ii<=m; ++ii) dp[ii][0]=ii;
            for(int jj=1; jj<=n; ++jj) dp[0][jj]=jj;
            dp[0][0]=0;
    
            //populate dp
            for(int ii=1; ii<=m; ++ii){
                for(int jj=1; jj<=n; ++jj){
                    if(str1[ii]==str2[jj]){
                        dp[ii][jj] = dp[ii-1][jj-1]+1;
                    }else{
                        dp[ii][jj] = min(dp[ii-1][jj], dp[ii][jj-1]) +1;
                    }
                }
            }
    
            //dp[m][n] => min super sequence
    
            int ii=m, jj=n;
            string ret;
            while(ii>0 && jj>0){
                if(str1[ii]==str2[jj]){
                    ret.push_back(str1[ii]);
                    --ii;
                    --jj;
                }else if (dp[ii][jj] == dp[ii-1][jj]+1){
                    ret.push_back(str1[ii]);
                    --ii;
                }else{
                    ret.push_back(str2[jj]);
                    --jj;
                }
            }
    
            while(ii > 0) ret.push_back(str1[ii--]);
            while(jj > 0) ret.push_back(str2[jj--]);
    
            reverse(ret.begin(), ret.end());
            return ret;
    
         }
    };