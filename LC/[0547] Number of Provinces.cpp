class Solution {
    unordered_map<int, int> Father;
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int N = isConnected.size();
        for(int ii=0; ii<N; ++ii){
            Father[ii] = ii;    
        }

        for(int ii=0; ii<N; ++ii){
            for(int jj=0; jj<N; ++jj){
                if(ii!=jj && isConnected[ii][jj]==1){
                    if(FindFather(ii) !=FindFather(jj)){
                        Union(ii, jj);
                    }
                }
            }
        }

        unordered_set<int> Set;
        for(int ii=0; ii<N; ++ii){
            Set.insert(FindFather(ii));
        }

        return Set.size();
    }

    int FindFather(int x){
        if(Father[x] != x)
            Father[x]= FindFather(Father[x]);
        return Father[x];
    }

    void Union(int x, int y){
        x = Father[x];
        y = Father[y];
        Father[x]=y;
    }
};