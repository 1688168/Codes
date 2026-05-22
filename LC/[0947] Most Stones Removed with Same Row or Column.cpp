class Solution {
    unordered_map<int, int> Parent;
    unordered_map<int, vector<int>> MapX;
    unordered_map<int, vector<int>> MapY;
    int N = 10000;
public:
    int removeStones(vector<vector<int>>& stones) {
        for(auto x: stones){
            int ii=x[0];
            int jj=x[1];
            int gid = ii*N+jj;
            Parent[gid] = gid;
            MapX[ii].push_back(gid);
            MapY[jj].push_back(gid);
        }

        for(auto x: MapX){
            int id0 = x.second[0];
            for(int ii=1; ii<x.second.size(); ++ii){
                int id = x.second[ii];
                if(Find(id0) != Find(id)){
                    Union(id0, id);
                }
            }
        }

        for(auto x: MapY){
            int id0 = x.second[0];
            for(int ii=1; ii<x.second.size(); ++ii){
                int id = x.second[ii];
                if(Find(id0) != Find(id)){
                    Union(id0, id);
                }
            }
        }

        unordered_set<int> Set;
        for(auto x: stones){
            int id = x[0]*N+x[1];
            int id0=Find(id);
            Set.insert(id0);
        }

        return stones.size() - Set.size();
    }

    int Find(int x){
        if(Parent[x] != x) Parent[x] = Find(Parent[x]);
        return Parent[x];
    }

    void Union(int a, int b){
        int pa = Find(a);
        int pb = Find(b);
        if(pa < pb)
            Parent[pb] = pa;
        else    
            Parent[pa] = pb;
    }
};