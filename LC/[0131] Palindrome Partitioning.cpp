class Solution {
    bool dp[16][16];
    vector<vector<string>> res;
public:
    vector<vector<string>> partition(string s) {
        //preprocessing is palindrome
        for(int ii=0; ii< s.size(); ++ii) dp[ii][ii] = true;//single char is palindrome

        for(int ii=0; ii< s.size()-1; ++ii){ //two neighboring equal chars is palindrome
            dp[ii][ii+1] = (s[ii]==s[ii+1]);
        }

        for( int len=3; len<=s.size(); ++len){//notice len start from 3. char 1 and 2 were initialized
            for(int ii=0; ii+len-1<s.size(); ++ii){
                int jj = ii+len-1;
    
                if(s[ii]==s[jj] && dp[ii+1][jj-1]){
                    dp[ii][jj]=true;
                }else{
                    dp[ii][jj]=false;
                }
            } 
        }

        vector<string> ans;
        dfs(0, s.size(), ans, s);

        return res;
    }

    void dfs(int cur, int n, vector<string> & ans, string & s){
        if(cur==n){
            res.push_back(ans);
            return;
        }

        for(int jj=cur; jj<n; ++jj){
            if(dp[cur][jj]){
                ans.push_back(s.substr(cur, jj-cur+1));
                dfs(jj+1, n, ans, s);
                ans.pop_back(); //back track
            }
        }
    }
};