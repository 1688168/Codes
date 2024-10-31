class Solution {
public:
    int getMoneyAmount(int n) {
        auto dp = vector<vector<int>>(n+2, vector<int>(n+2, 0));

        //edge case:?
        //for(int ii=1; ii<=n; ++ii) dp[ii][ii]=0;


        for(int len=2; len<=n; ++len){ //all length, len=1 -> no need to pay at all
            for(int ii=1; ii<=n-len+1; ++ii){//each starting value
                int jj = ii+len-1; //paired ending value
                dp[ii][jj]=INT_MAX;
                for(int kk=ii; kk<=jj; ++kk){//guess kk in range(ii, jj)

                    dp[ii][jj] = min(dp[ii][jj], kk+max(dp[ii][kk-1], dp[kk+1][jj]));
                }
            }
        }

        return dp[1][n];
        
    }
};