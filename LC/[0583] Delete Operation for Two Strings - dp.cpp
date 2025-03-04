class Solution {
    public:
        int minDistance(string word1, string word2) {
            int N1=word1.size();
            int N2=word2.size();
    
            string ss = "#"+word1;
            string tt = "#"+word2;
    
            //declare and define dp
            /*
            dp[ii][jj]: min delete required to make ss[:ii+1],  t[:j+1] the same
            */
            auto dp = vector<vector<int>>(N1+1, vector<int>(N2+1, INT_MAX/2));
            
            //initialize dp
            for(int ii=1; ii<=N1; ++ii)dp[ii][0]=ii;
            for(int jj=1; jj<=N2; ++jj)dp[0][jj]=jj;
            dp[0][0]=0;
    
            for(int ii=1; ii<=N1; ++ii){
                for(int jj=1; jj<=N2; ++jj){
                    if(ss[ii]==tt[jj]){
                        dp[ii][jj]=dp[ii-1][jj-1];
                    }else{
                        dp[ii][jj] = min(dp[ii-1][jj], dp[ii][jj-1])+1;
                    }
                }
            }
    
    
            return dp[N1][N2];
        }
    };