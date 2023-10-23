#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<int>next[1005]; //this is for graph
    //the matrix is to record distance btn any two nodes
    int matrix[1005][1005]; //this is for matrix
public:
    vector<int> closestNode(int n, vector<vector<int>>& edges, vector<vector<int>>& query) 
    {
        for (auto& edge: edges) //build the graph
        {
            int a = edge[0], b = edge[1];
            next[a].push_back(b);
            next[b].push_back(a);
        }
        
        for (int i=0; i<n; i++) //calc distance and populate the matrix
            dfs(i,i,0);
                
        vector<int>rets;
        for (auto& q: query) //start to process the queries
        {
            int start = q[0], end = q[1], node = q[2];
            int dist = INT_MAX;
            int ret;
            
            int cur = start;
            while (1)
            {
                if (matrix[cur][node] < dist)
                {
                    dist = matrix[cur][node];
                    ret = cur;
                }
                if (cur==end) break;
                
                for (int j: next[cur])
                {
                    //this is a genius way to determin if child is on the path to end
                    if (matrix[cur][end]==matrix[j][end]+1) //if j is on the path, it must satisfy this
                    {
                        cur = j;//since thi sis a tree (no cycle), we can only have one path
                        break; //once we identify which child in the path, we can break
                    }
                }                
            }
            rets.push_back(ret);                        
        }
        
        return rets;
             
    }
    
    void dfs(int root, int cur, int dist)
    {
        for (int j: next[cur])//for each child
        {
            if (j!=root && matrix[root][j]==0) //avoid visited and circle, should have put root in visited
            {
                matrix[root][j] = dist+1;
                dfs(root, j, dist+1);                
            }            
        }
    }
};