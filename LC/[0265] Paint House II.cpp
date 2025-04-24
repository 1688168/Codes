class Solution {
    public:
        int minCostII(vector<vector<int>>& costs) {
            int N = costs.size(); //num of houses
            if(N==0) return 0;
            int K = costs[0].size(); //num of paint colors
            auto dp = vector<vector<int>> (N, vector<int>(K, 0));
    
            for(int jj=0; jj<K; ++jj) dp[0][jj] = costs[0][jj];
    
            for(int ii=1; ii<N; ++ii){
                //we need min and 2nd min
                vector<pair<int, int>> tmp;
    
                for(int jj=0; jj<K; ++jj) tmp.push_back({dp[ii-1][jj], jj});
                sort(tmp.begin(), tmp.end());
    
                for(int jj=0; jj<K; ++jj){
                    if(jj==tmp[0].second) 
                        dp[ii][jj] = tmp[1].first+costs[ii][jj];
                    else
                        dp[ii][jj] = tmp[0].first+costs[ii][jj];
    
                }
            }
    
            int ret = INT_MAX;
            for(int jj=0; jj<K; ++jj){
                ret = min(ret, dp[N-1][jj]);
            }
    
            return ret;
            
        }
    };