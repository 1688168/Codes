* paint house I [0256]: 3 colors non-consecutive, min cost -> same as rob house
* paint house II [0265]: k colors non-consecutive, min cost -> same as rob house
* paint house III [1473]: k colors, target neighborhood num, non-consecutive neighborhood color.

> paint house III:

* dp[ii][jj][kk]: min cost, when we paint the first ii houses. with jj neighborhood and iith house is with color=kk

for each ii://for each house
    //is painted
    if(houses[ii]!= 0){//the house is painted
        for(int jj = 1; jj<=target; ++jj){
            int kk = houses[ii]; //the house is painted and the color is the value in house array
            for(int k=1; k<=n; +kk){
                if(k!=kk){//previous house in diff neighborhood
                    dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj-1][kk-1]); //current house is painted, no additional cost incurred
                }else{////previous house in same neighborhood (also same color)
                    dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj][kk-1])
                }
             

            }
            

        }

    }
    else{//house is NOT painted
        for(int jj=1; jj<=target; ++jj){//current house can be any color
            for(int kk=1; kk<=n; ++kk){//kk is current color
                for(int k=1; k<=n; ++k>){//k is prev house color
                    if(kk!=k){//diff neighborhood
                        dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj-1][kk]+cost[ii][kk-1])
                    }else{//same neighborhood
                        dp[ii][jj][kk] = min(dp[ii][jj][kk], dp[ii-1][jj][kk]+cost[ii][kk-1])  
                    }
                }

            }
        }
    }
