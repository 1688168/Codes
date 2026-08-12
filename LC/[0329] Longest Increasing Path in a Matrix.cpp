class Solution {
public:
    int m;
    int n;
    int memo[200][200];
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();
        int ret = 0;
        for(int ii=0; ii<m; ++ii){
            for(int jj=0; jj<n; ++jj){
                ret = max(ret, dfs(matrix, ii, jj));
            }
        }
        return ret;    
    }

    int dfs(vector<vector<int>> & matrix, int ii, int jj){
        if(memo[ii][jj] != 0) return memo[ii][jj];
        vector<pair<int, int>> dir{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int ret = 1;
        for(int kk=0; kk<4; ++kk){
            int x = ii+dir[kk].first;
            int y = jj+dir[kk].second;
            if(x < 0 || y < 0 || x >= m || y >= n) continue;
            if(matrix[x][y] <= matrix[ii][jj]) continue;
            ret = max(ret, 1+dfs(matrix, x, y));
        }
        memo[ii][jj] = ret;
        return ret;
    }
};