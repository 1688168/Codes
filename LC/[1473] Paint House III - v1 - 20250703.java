class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        int ans = Integer.MAX_VALUE/2;
        
        //define dp
        //dp[ii][jj][kk]: min cost @house ii, neighborhood jj, color kk
        var dp = new int[m][target+1][n+1];

        for(int ii=0; ii<m; ++ii){
            for(int jj=0; jj<=target; ++jj){
                for(int kk=0; kk<=n; ++kk){
                    dp[ii][jj][kk] = Integer.MAX_VALUE/2;
                }
            }
        }

        //initialize dp
        //when nothing -> no cost
        dp[0][0][0]=0; 
        //when ii = 0 
        //-- when jj=0: no neighborhood
        //for(int kk=1; kk<=n; ++kk) dp[0][0][kk]=0;//cost is zero if no neighborhood

        //-- when jj=1: 1 neighborhood
        //--- house is painted
        if(houses[0] > 0){
            dp[0][1][houses[0]]=0;
        }else{
            for(int kk=1; kk<=n; ++kk){
                dp[0][1][kk] = cost[0][kk-1];
            }
        }

        for(int ii=1; ii<m; ++ii){//iith house
            for(int jj=1; jj<=target; ++jj){//jjth neighborhood
                int ckk=houses[ii];
                boolean isPainted = ckk > 0;
            
                if(isPainted){
                    for(int pkk=1; pkk<=n; ++pkk){
                        if(pkk==ckk){//same neighborhood
                            dp[ii][jj][ckk] = Math.min(dp[ii][jj][ckk], dp[ii-1][jj][pkk]);
                        }else{
                            dp[ii][jj][ckk] =  Math.min(dp[ii][jj][ckk], dp[ii-1][jj-1][pkk]);
                        }
                    }
                }else{
                    for(int kk=1; kk<=n; ++kk){//color kk
                        for(int pkk = 1; pkk<=n; ++pkk){
                            if(pkk==kk){
                                dp[ii][jj][kk] = Math.min(dp[ii][jj][kk], dp[ii-1][jj][pkk]+cost[ii][kk-1]);
                            }else{
                                dp[ii][jj][kk] = Math.min(dp[ii][jj][kk], dp[ii-1][jj-1][pkk]+cost[ii][kk-1]);
                            }
                        }
                    }
                }
            }
        }


        //if ans is inf/2 -> return -1
        for(int kk=1; kk<=n; ++kk){
            ans = Math.min(ans, dp[m-1][target][kk]);
        }

        return ans == Integer.MAX_VALUE/2?-1: ans;
    }
}


// * m: num of houses in a row
// * n: num of colors
// * some house already painted -> do not paint again
// * neighborhood: same color continuous houses
// -> min cost with target neighborhoods
// -> -1 if not possible

// * dp[ii][jj][kk]: min cost @ house ii, color jj, with kk neighborhood
// * dp[ii][jj][kk] = if painted
//                    else
//                       if same neighborhood
//                       else:
//                         try all color VS previous
// -> min(dp[M-1][jj][kk])
                      