class Solution {
public:
    int numDistinct(string s, string t) {
        int N1 = s.size();
        int N2 = t.size();

        //if subsequence of s can compose t -> N1 >= N2
        if(N1 < N2) return false;
        if(N1==N2) return s==t; // there is only one way subsequent of s equal to t then they are same size

        /* analysis
        * - N1, N2 <= 1000 (looping s, t is 1MM)
        * - two series DP
        * if s[ii]==t[jj] -> dp[ii][jj] = dp[ii-1][jj-1] -> the problem can be reduced to a smaller problem -> DP
        * whenever you count -> dp[ii][jj] += previous answer
        */

        s = '#'+s;
        t = '#'+t;

        //declare dp
        auto dp = vector<vector<long long>>(N1+1, vector<long long>(N2+1, 0L));

        //initialize dp
        dp[0][0] = 1; //null can compose null
        //then t is null, there is one way to compose t for all ii in s
        for(int ii=1; ii<=N1; ++ii) dp[ii][0]=1;

        //populate dp
        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                //why this way overflows?
                // if(s[ii]==t[jj]) dp[ii][jj] += dp[ii-1][jj-1];
                // dp[ii][jj] += dp[ii-1][jj];
                if (s[ii]==t[jj])
                    //leverage this: The test cases are generated so that the answer fits on a 32-bit signed integer.
                    dp[ii][jj] = min(LLONG_MAX/2, dp[ii-1][jj] + dp[ii-1][jj-1]);
                else
                    dp[ii][jj] = dp[ii-1][jj];
            }
        }

        return dp[N1][N2];
        
    }
};

/*
1. two series counting/optimizing something -> DP III
2. dp[ii][jj] = dp[ii-1][jj-1], dp[ii][jj-1], dp[ii-1][jj]
3. S subsequence to compose T -> len(s) >= T
*/