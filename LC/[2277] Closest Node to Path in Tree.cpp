#include <iostream>
#include <vector>
using namespace std;

/* 
=> If we are being queried repeatedly on a dataset, can we precalc all the possible answers? 

*/

class Solution {
    vector<int>next[1005]; //this is for graph
    //the matrix is to record distance btn any two nodes
    int matrix[1005][1005]; //this is for matrix
public:
    vector<int> closestNode(int n, vector<vector<int>>& edges, vector<vector<int>>& query) 
    {
        //build the Graph
        for (auto& edge: edges) //build the graph
        {
            int a = edge[0], b = edge[1];
            next[a].push_back(b);
            next[b].push_back(a);
        }
        
        //build distance matrix
        for (int i=0; i<n; i++) //calc distance and populate the matrix
            dfs(i,i,0);
        
        // here we already built distance btn any two nodes
        // process queries
        vector<int>rets;
        for (auto& q: query) //start to process the queries
        {
            int start = q[0], end = q[1], node = q[2];
            int dist = INT_MAX; //default distance(node, path)
            int ret;
            
            int cur = start; //first node on the path
            while (1) //for a query
            {
                if (matrix[cur][node] < dist) //if curr dist(node, curr) < dist -> update candidate
                {
                    dist = matrix[cur][node]; //update new shortest distance (node, curr_on_the_path)
                    ret = cur; //update the node on the path with shortest distance (node, node_on_the_path)
                }
                //if curr==end, we are done
                if (cur==end) break; //if start == end. the distance is btn start to node 
                
                //identify next node on the path
                for (int j: next[cur]) 
                {
                    //this is a genius way to determin if child is on the path to end
                    if (matrix[cur][end]==matrix[j][end]+1) //if j is on the path, it must satisfy this
                    {
                        cur = j;//since this is a tree (no cycle), we can only have one path
                        break; //once we identify which child in the path, we can break
                    }
                    //here we found the next node on the path
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
                matrix[root][j] = dist+1; //since this is guaranteed as tree, no circle. there is only one path to reach this node
                dfs(root, j, dist+1);                
            }            
        }
    }
};