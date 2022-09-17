using LL=long long;
class Solution {
public:
        long long numberOfWays(string s) {
        /* dp[ii][jj][kk] being number of ways to visite iith building, selected jj num of buildings and s[ii]=kk (0 or 1)
        *
        */

        LL N = s.size();
        LL dp[100005][4][2];//this is way faster than vector

        s = "#"+s;
        // vector<LL> K(2, 0);
        // vector<vector<LL>> KK(4, K);
        // vector<vector<vector<LL>>> dp(N+1, KK);

        dp[0][0][1]=1;
        dp[0][0][0]=1;

        for(int ii=1; ii<=N; ++ii){
            for(int jj=0; jj<4; ++jj){
                for(int kk=0; kk<2; ++kk){
                    //case I iith building is not selected
                    dp[ii][jj][kk]=dp[ii-1][jj][kk];

                    if(jj >= 1 && kk==(s[ii]-'0')){
                        dp[ii][jj][kk] += dp[ii-1][jj-1][1-kk];
                    }
                }
            }
        }



        return dp[N][3][1]+dp[N][3][0];

    }
};
