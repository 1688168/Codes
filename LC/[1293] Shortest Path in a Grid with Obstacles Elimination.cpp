/*
* DP?: we can consider DP if we can only move down and right.  In this problem, user can go up and left (go back), this violates DP requirement (no afterward effects)
*/

class Solution {
     bool visited[41][41][1601];
public:
    int shortestPath(vector<vector<int>>& grid, int K) {
       int m=grid.size();
       int n=grid[0].size();
       if(m==1 && n==1) return 0;
       //Shortest distance -> BFS -> Queue
       queue<vector<int>>q;
       q.push({0,0,0});
       visited[0][0][0]=1;
       auto dir = vector<pair<int, int>>({{0,1},{0,-1},{1,0},{-1,0}});
       int step = 0;
       while(!q.empty()){
           int len = q.size();
           while(len--){
               int x = q.front()[0];
               int y = q.front()[1];
               int k = q.front()[2];
               q.pop();
               for(int t=0; t<4; ++t){
                   int i = x+dir[t].first;
                   int j = y+dir[t].second;
                   if(i<0||i>=m || j < 0 || j >= n) continue;
                   if(i==m-1 && j==n-1) return step+1;
                   if(grid[i][j]==1){
                       if(k==K)continue;
                       if(visited[i][j][k+1]==1)continue;
                       visited[i][j][k+1]=1;
                       q.push({i, j, k+1});
                   }else{
                       if(visited[i][j][k]==1)continue;
                       visited[i][j][k]=1;
                       q.push({i, j, k});
                   }
               }
           }//end of while
           ++step;
       }
        return -1;
    }
};