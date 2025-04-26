class Solution {
    int dp[105][105][25];
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) {
        //whenever current status is derived from previous stats, we need to insert dummy. for ii-1
        houses.insert(houses.begin(), 0);
        cost.insert(cost.begin(), {{}});//c++, insert 2D vector dummy

        for(int ii=0; ii<=m; ++ii){
            for(int jj=0; jj<=target; ++jj){
                for(int kk=0; kk<=n; ++kk){
                    dp[ii][jj][kk] = INT_MAX/2;
                }
            }
        }
        
        //this doesn't seem required, without this also works
        for(int kk=0; kk<=n; ++kk) dp[0][0][kk] = 0;

        //this is very tricky.  consider only 1 house, 1 neighborhood. the value is determined
        //initialize dp when we only have 1 house and 1 neighborhood
        if (houses[1]!=0) //when 1 house, 1 neighborhood and painted
        {
            dp[1][1][houses[1]] = 0;//already painted 1st house (all other colors are invalid, stay as INT_MAX/2)
        }
        else
        {
            for (int k=1; k<=n; k++)//not painted, populate all colors
                dp[1][1][k] = cost[1][k-1];
        }
        
        for(int ii=2; ii<=m; ++ii){//for each house (starting from 1, remember 0 is the dummy)
            //each house could be painted or not-painted, so we branch the condition here
            if(houses[ii]!=0){//the house is already painted -> no additional cost for current
                for(int jj=1; jj<= target; ++jj){//also 1 indexed to match the dummy we insrted
                    int kk = houses[ii];//current color
                    //current min cost is min_cost @ ii-1
                    for(int pkk=1; pkk<=n; ++pkk){
                        if(pkk != kk){ //previous house has diff color -> diff neighborhood
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj-1][pkk]);
                        }else{//previous house has same color -> sam,e neighborhood
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj][pkk]);
                        }
                    }
                }
            }else{//the house is not painted yet -> need to pay aditional pcost for current house
                for(int jj=1; jj<= target; ++jj){//also 1 indexed to match the dummy we insrted
                    vector<pair<int,int>> tmp; //{cost, color}
        
                    for(int pkk=1; pkk<=n; ++pkk){
                        tmp.push_back({dp[ii-1][jj-1][pkk], pkk});
                    }

                    sort(tmp.begin(), tmp.end());
                    for(int kk=1; kk<=n; ++kk){//consider ii and ii-1 same color or diff color both case

                        dp[ii][jj][kk] = dp[ii-1][jj][kk]+cost[ii][kk-1];//when ii and ii-1 same color

                        //when ii and ii-1 in diff color
                        if(tmp[0].second != kk){//prev min house in diff color
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], tmp[0].first + cost[ii][kk-1]);
                        }else{
                            dp[ii][jj][kk] = min(dp[ii][jj][kk], tmp[1].first + cost[ii][kk-1]);
                        }
                    }
                }    
            }
        }    

        int ret = INT_MAX/2;
        for(int kk=1; kk<=n; ++kk) ret = min(ret, dp[m][target][kk]);

        return ret != INT_MAX/2? ret: -1;
    }
};