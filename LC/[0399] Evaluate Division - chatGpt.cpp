class Solution {
    unordered_map<string, vector<pair<string, double>>> Map;
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        Map.clear();
        for(int ii=0; ii<equations.size(); ++ii){
            Map[equations[ii][0]].push_back({equations[ii][1], values[ii]}); //a->[(b, v1),(c, v2), ...]
            Map[equations[ii][1]].push_back({equations[ii][0], 1.0/values[ii]});
        }           
        vector<double> results;
        for(int ii=0; ii<queries.size(); ++ii){
            if(Map.find(queries[ii][0])==Map.end() || Map.find(queries[ii][1])==Map.end()){
                results.push_back(-1);
                continue;
            }
            unordered_set<string> visited({queries[ii][0]});
            results.push_back(DFS(queries[ii][0], queries[ii][1], visited));
        }
        return results;
    }

    double DFS(string & A, string & B, unordered_set<string>&visited){

        if(A==B) return 1.0;
        for(int ii=0; ii<Map[A].size(); ++ii){
            string C = Map[A][ii].first;
            //if(B==C) return Map[A][ii].second;
            if(visited.find(C)!=visited.end()) continue;
            visited.insert(C);
            double val1 = Map[A][ii].second;
            double val2 = DFS(C, B, visited);
            //visited.erase(C); --> this is not required.
            if(val2!=-1.0) return val1*val2;
        }
        return -1.0;
    }
};