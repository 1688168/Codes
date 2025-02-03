class Solution {
public:
    int minDistance(string word1, string word2) {
        int N1=word1.size();
        int N2=word2.size();

        word1 = "#"+word1;
        word2 = "#"+word2;

        auto dp = vector<vector<int>>(N1+1, vector<int>(N2+1, 0));
        
        for(int ii=0; ii<=N1; ++ii) dp[ii][0]=ii;
        for(int jj=0; jj<=N2; ++jj) dp[0][jj] = jj;

        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(word1[ii]==word2[jj]){
                    dp[ii][jj]=dp[ii-1][jj-1];
                }else{
                    dp[ii][jj] = 1+min(dp[ii-1][jj-1], min(dp[ii][jj-1], dp[ii-1][jj]));
                }
              
            }
        }

        return dp[N1][N2];
        
    }
};