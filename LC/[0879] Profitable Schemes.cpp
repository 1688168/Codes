class Solution {
    int dp[105][105][105];
    int M = 1e9+7;
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
        
        dp[0][0][0] = 1;//do nothing to achieve nothing is also one scheme
        
        int m=group.size();
        group.insert(group.begin(), 0);
        profit.insert(profit.begin(), 0);
     
        for(int ii=0; ii<m; ++ii){//iith scheme
            for(int jj=0; jj<=n; ++jj){ //jj members
                for(int kk=0; kk<=minProfit; ++kk){ //kk profit
                    // dp[ii+1][jj][kk] += dp[ii][jj][kk]; //skipping current
                    dp[ii+1][jj][kk] =  (dp[ii+1][jj][kk]+dp[ii][jj][kk])%M; //by skipping, (current iteration ii has apready been populated by ii-1 iteration)

                    if(jj+group[ii+1] <= n) //not exceeding max ppl
                        dp[ii+1][jj+group[ii+1]][min(minProfit,kk+profit[ii+1])] =
                         (dp[ii+1][jj+group[ii+1]][min(minProfit,kk+profit[ii+1])]+dp[ii][jj][kk])%M;
                    // dp[ii+1][jj][kk] %= M;

                    // if(jj+group[ii+1] <= n)
                    //      dp[ii+1][jj+group[ii+1]][min(minProfit,kk+profit[ii+1])] %=M;
                }

            }
        }
        int ret=0;
        for(int jj=0; jj<=n; ++jj)
            ret = (ret+dp[m][jj][minProfit])%M;

        return ret;
    }
};

// x x x x x ii
// * dp[ii][person][profit]: from the first ii projects, how many of schemes s.t. we just use person and earn profit
// * dp[ii][person][profit] = dp[ii-1][person][profit]        //skip
//                          + dp[ii-1][person-x][profit-y]  //take current

// T: 100*100*(100*100)

// //redefine DP as flollows
// @iith crime, how many schemes s.t we earn at least minProfit by using person
// dp[ii][person][minProfit] = sum{dp[ii][person][p]} where p = minprofit, minProfit+1, ...
// T: 100*100*100

// dp[ii][person][profit] => 
//   dp[ii+1][person][profit] += dp[ii][person][profit]
//   dp[ii+1][person+x][min(profit,profit+y)] += dp[ii][person][profit]

// return sum{dp[m][jj][minProfit]} where j=0,1,2,...n