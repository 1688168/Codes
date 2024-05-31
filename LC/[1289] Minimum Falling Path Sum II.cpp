class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        auto dp = vector<vector<int>>(m, vector<int>(n));
        for(int ii=0; ii<n;++ii){
            dp[0][ii]=grid[0][ii];
        }

        for(int ii=1; ii<m;++ii){
            vector<pair<int,int>> temp;
            for(int kk=0; kk<n; ++kk)
                temp.push_back({dp[ii-1][kk], kk});
            sort(temp.begin(), temp.end());
            for(int jj=0; jj<n; ++jj){
                if(jj!=temp[0].second){
                    dp[ii][jj]=temp[0].first+grid[ii][jj];
                }else
                    dp[ii][jj]=temp[1].first+grid[ii][jj];
            }
        }
        int ret = INT_MAX;
        for(int ii=0; ii<n; ++ii)
            ret=min(ret, dp[m-1][ii]);
        return ret;
        
    }
};