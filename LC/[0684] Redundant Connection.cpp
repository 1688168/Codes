class Solution {
    unordered_map<int, int> parent;

public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for (auto& edge : edges) {
            int a = edge[0];
            int b = edge[1];

            if (!parent.count(a)) parent[a] = a;
            if (!parent.count(b)) parent[b] = b;

            if (find(a) == find(b)) {
                return edge;
            }

            unite(a, b);
        }

        return {};
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unite(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) return;

        if (x < y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }
};