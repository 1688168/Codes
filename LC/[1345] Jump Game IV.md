* array of integers
* N=5*10^4 * 10^2
-> min num to reach end

> DP
dp[ii]: min num to reach ii
dp[ii] = dp[jj]+1 if nums[jj]==nums[ii] or jj==ii--1
=====> why we cannot use DP: current state could be <=====
-> current state could be affected by future state due to rule 3: we can jump to anywhere when arr[ii]==arr[jj] where ii!= jj
shortest distance -> BFS


---
class Solution {
public:
    int minJumps(vector<int>& arr) 
    {
        int n = arr.size();
        if (n==1) return 0;
        unordered_map<int,vector<int>>Map;
        for (int i=0; i<n; i++)
            Map[arr[i]].push_back(i);
        
        vector<int>visited(n,0);
        queue<int>q;
        q.push(0);
        visited[0] = 1;
        
        int step = 0;
        while (!q.empty())
        {
            int len = q.size();
            while (len--)
            {
                int cur = q.front();
                q.pop();
                
                if (cur+1 < n && visited[cur+1]==0)
                {
                    q.push(cur+1);
                    visited[cur+1] = 1;
                }
                if (cur-1 >= 0 && visited[cur-1]==0)
                {
                    q.push(cur-1);
                    visited[cur-1] = 1;
                }
                for (int next: Map[arr[cur]])
                {
                    if (visited[next] == 0)
                    {
                        q.push(next);
                        visited[next] = 1;
                    }
                } 
                Map.erase(arr[cur]);
                
            }
            step += 1;
            if (visited[n-1] == 1)
                return step;
        }
        
        return -1;
    }
};