class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int N = s.size();
        if(N==1) return 1;

        s = "#"+s;
        auto dp = vector<vector<int>>(N+1, vector<int>(N+1, 0));//single char is palindrom
        for(int ii=0; ii<=N; ++ii) dp[ii][ii]=1;
        for(int len=2; len <= N; ++len){//try each len
            for(int ii=1; ii+len-1<=N; ++ii){//try each jj as starting interval
                int jj=ii+len-1;//ending interval 
                if(s[ii]==s[jj]){
                    dp[ii][jj] = dp[ii+1][jj-1]+2;//when st > ed, we should be 0
                }else{
                    dp[ii][jj] = max(dp[ii][jj-1], dp[ii+1][jj]);
                }

            }
        }
        return dp[1][N];
    }
};