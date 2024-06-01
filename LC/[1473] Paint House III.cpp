class Solution {
    /*
    DP: min(cost) of
        + m houses
        + target blocks
        + n colors
    */
    int dp[105][105][25];//100 house, target neighbors, n colors
public:
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int m, int n, int target) 
    {
        houses.insert(houses.begin(), 0); //whenever you need to ref to prev row
        cost.insert(cost.begin(), {0});

        for (int i=0; i<=m; i++) //initialize DP
            for (int j=0; j<=target; j++)
                for (int k=0; k<=n; k++)
                    dp[i][j][k] = INT_MAX/2;//min cost so initialize inf

        if (houses[1]!=0) //houses[0] is dummy
        {
            dp[1][1][houses[1]] = 0;//already painted (all others are invalid)
        }
        else
        {
            for (int k=1; k<=n; k++)//not painted, populate all colors
                dp[1][1][k] = cost[1][k-1];
        }

        //for each house
        for (int i=2; i<=m; i++)//remember ii=0 is dummy, ii=1 is pre-processed
        {
            if (houses[i]!=0)//current house is painted
            {       
                for (int j=1; j<=target; j++)
                {
                    int k = houses[i];                    
                    for (int kk=1; kk<=n; kk++) //prev house color
                    {
                        if (kk==k)//if current color same as prev house color (same block)
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][kk]);
                        else//current color not same as prev color
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][kk]); //(diff block)
                    }
                }
            }
            else//current house need to be painted
            {
                //for each block
                for (int j=1; j<=target; j++)
                    for (int k=1; k<=n; k++)//for each color
                    {
                        for (int kk=1; kk<=n; kk++)//for each previous color
                        {
                            if (kk==k)//if prev color same as current color
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][kk] + cost[i][k-1]);//same block
                            else
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][kk] + cost[i][k-1]);//diff block
                        }
                    }                
            }    
        }

        int ret = INT_MAX/2;
        for (int k=1; k<=n; k++)//for each color
            ret = min(ret, dp[m][target][k]);//last house, last block, each color
        if (ret==INT_MAX/2)
            return -1;
        else
            return ret;
    }
};