class Solution {
    unordered_map<int, int> parent;
    unordered_map<int, int> size;
    unordered_map<int, vector<int>> rows;
    unordered_map<int, vector<int>> cols;

    static const int BASE = 10001;

public:
    int removeStones(vector<vector<int>>& stones) {
        for (auto& stone : stones) {
            int r = stone[0];
            int c = stone[1];
            int id = getId(r, c);

            parent[id] = id;
            size[id] = 1;

            rows[r].push_back(id);
            cols[c].push_back(id);
        }

        for (auto& [r, ids] : rows) {
            unionGroup(ids);
        }

        for (auto& [c, ids] : cols) {
            unionGroup(ids);
        }

        unordered_set<int> roots;
        for (auto& stone : stones) {
            roots.insert(find(getId(stone[0], stone[1])));
        }

        return stones.size() - roots.size();
    }

private:
    int getId(int r, int c) {
        return r * BASE + c;
    }

    void unionGroup(vector<int>& ids) {
        int first = ids[0];

        for (int i = 1; i < ids.size(); i++) {
            unite(first, ids[i]);
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unite(int a, int b) {
        int pa = find(a);
        int pb = find(b);

        if (pa == pb) return;

        if (size[pa] < size[pb]) {
            swap(pa, pb);
        }

        parent[pb] = pa;
        size[pa] += size[pb];
    }
};