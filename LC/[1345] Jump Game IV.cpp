
class Solution {
public:
    int minJumps(vector<int>& arr) 
    {
        int n = arr.size();
        if (n==1) return 0;
        unordered_map<int,vector<int>>Map;//value2idx
        for (int i=0; i<n; i++)
            Map[arr[i]].push_back(i);
        
        vector<int>visited(n,0);
        queue<int>q;
        q.push(0);
        visited[0] = 1;
        
        int step = 0;//BFS
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
                for (int next: Map[arr[cur]])//for each index you can visit from this current value
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
