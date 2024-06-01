class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int cost0=0, cost1=0, cost2=0;
        int N=costs.size();
        for(int ii=0; ii<N; ++ii){
            int cost0_tmp=cost0, cost1_tmp=cost1, cost2_tmp=cost2;

            if(ii==0){
                cost0=costs[ii][0];
                cost1=costs[ii][1];
                cost2=costs[ii][2];
            }else{
                cost0=min(cost1_tmp, cost2_tmp)+costs[ii][0];
                cost1=min(cost0_tmp, cost2_tmp)+costs[ii][1];
                cost2=min(cost0_tmp, cost1_tmp)+costs[ii][2];
            }
        }

        return min(min(cost0, cost1), cost2);
        
    }
};