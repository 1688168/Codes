class Solution {
    public:
        int minInsertions(string s) {
            int N = s.size();
    
            auto dp = vector<vector<int>>(N, vector<int>(N, 0));//no dummy, so len is N
            for(int ii=0; ii<N; ++ii) dp[ii][ii]=0;
            //for(int ii=0; ii<N-1; ++ii) if(s[ii]==s[ii+1]) dp[ii][ii+1]=0;
            
            for(int ll = 2; ll<=N; ++ll){//single char was already initialized.
                for(int ii=0; ii+ll-1 <N; ++ii){//max jj is N-1
                    int jj = ii+ll-1;
                    if(s[ii]==s[jj]){
                        dp[ii][jj]=dp[ii+1][jj-1];
                    }else{
                        dp[ii][jj]=1+min(dp[ii+1][jj], dp[ii][jj-1]);
                    }
                }
            }
    
            return dp[0][N-1];
            
        }
    };
    
    /*
    * to make a string palindrome.
    * a single char -> 0
    * two chars and equal -> 0 otherwise 1
    * 3 chars: if both ends equal, otherwise min(dp[ii+1][jj], dp[ii][jj-1])+1
    */