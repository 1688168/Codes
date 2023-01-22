using LL = long long;
class Solution {
    vector<int> next[100005]; //adjacency list to represent the graph
    LL sum1[100005];          // sum1[node]: the maximum path from node to its non-leaf child
    LL sum2[100005];          // sum2[node]: the maximum path from node to its leaf child 
    LL ret = 0;
public:
    long long maxOutput(int n, vector<vector<int>>& edges, vector<int>& price) 
    {
        if (n==1) return 0; //if single node

        for (auto& edge: edges) //build the graph
        {
            int a = edge[0], b = edge[1];
            next[a].push_back(b);
            next[b].push_back(a);
        }

        dfs(0, -1, price); //traverse the tree from Node-zero, populate sum1 and sum2, 
        dfs2(0, -1, price);//traverse the tree from Node-zero, and add the top 2 children sum

        return ret;        
    }

    void dfs(int cur, int parent, vector<int>& price)//populate sum1, sum2
    {
        if (next[cur].size()==1 && //a leaf node
        next[cur][0] == parent)    //to avoid exit on node_root
        {
            sum1[cur] = 0; //non-leaf node max is zero
            sum2[cur] = price[cur];  //leaf node max is price
            return;
        }

        LL maxSum1 = 0, maxSum2 = 0;
        for (int nxt: next[cur])
        {
            if (nxt == parent) continue;
            dfs(nxt, cur, price);
            maxSum1 = max(maxSum1, sum1[nxt]);
            maxSum2 = max(maxSum2, sum2[nxt]);
        }
        sum1[cur] = maxSum1 + price[cur];
        sum2[cur] = maxSum2 + price[cur];
    }

    void dfs2(int cur, int parent, vector<int>& price)
    {
        /*
        * for each node as root, we find all the neighboring nodes with max_sum1+max_sum2
        */
        vector<pair<LL,int>>arr1; // {SumVal, childNodeId}
        vector<pair<LL,int>>arr2; 

        LL ans = sum1[cur];
        if (cur!=0) ans = max(ans, sum2[cur]);

        for (int nxt: next[cur])
        {
            if (nxt==parent) continue;
            arr1.push_back({sum1[nxt], nxt});
            arr2.push_back({sum2[nxt], nxt});
            dfs2(nxt, cur, price);
        }
        sort(arr1.rbegin(), arr1.rend()); //who is the max sum1
        sort(arr2.rbegin(), arr2.rend()); //who is the max sum2

        if (arr1.size() >= 2)
        {
            if (arr1[0].second!=arr2[0].second)
                ans = max(ans, arr1[0].first + arr2[0].first + price[cur]);
            else
                ans = max(ans, max(arr1[0].first + arr2[1].first, arr1[1].first + arr2[0].first) + price[cur]);
        }

        ret = max(ret, ans);
    }
};


// Find a maximum path, for which one end is leaf, and the other is not.