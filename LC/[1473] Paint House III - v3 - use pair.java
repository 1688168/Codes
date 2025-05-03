class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        //dp[ii][jj[kk]: the min cost to paint ii houses, jj neighborhood and last house is with color=kk
        //ii could be painted or not-painted
        //jj need to be @ target neighborhood
        //find min of last color
        int[][][] dp = new int[m+1][target+1][n+1];

        //insert dummy for houses and cost representing 0 house, 0 neighborhood
        int[] tmpArr = new int[m+1];
        //arraycopy(originalArr, srcStartingIdx, newArr, targetStartingIdx, copyLengh);
        System.arraycopy(houses, 0, tmpArr, 1, m);//[java][insert][array][copy]
        houses=tmpArr;

        int[][] cost2 = new int[m+1][n+1];
        for(int ii=0; ii<m; ++ii){
            System.arraycopy(cost[ii], 0, cost2[ii+1], 1, n);
        }

        cost=cost2;

        //initialize dp for know base states
        //default to max int
        for(int ii=0; ii<=m; ++ii){
            for(int jj=0; jj<=target; ++jj){
                for(int kk=0; kk<=n; ++kk){
                    dp[ii][jj][kk] = Integer.MAX_VALUE/2;
                }
            }
        }
        //when no house, no neighborhood -> no cost, others invalid
        for(int kk=0; kk<=n; ++kk){
            dp[0][0][kk]=0;
        }
    
        //when 1 house painted vs not painted
        if(houses[1] !=0){//first house is painted
            dp[1][1][houses[1]] = 0;//when one house is painted, it has 1 neighborhood at least and cost is 0 as already painted
        }else{
            for(int kk=1; kk<=n; ++kk){
                dp[1][1][kk] = cost[1][kk];
            }
        }

        //populate dp
        for(int ii=2; ii<=m; ++ii){//from 2nd house. as 1st house is special handled above
            if(houses[ii] !=0){//the house is painted no additional cost incurring
                int kk = houses[ii];//the current color
                for(int jj=1; jj<=target; ++jj){
                    for(int pkk=1; pkk<=n; ++pkk){
                        if(pkk==kk){//same color, same neighborhood
                            dp[ii][jj][kk] = Math.min(dp[ii][jj][kk], dp[ii-1][jj][pkk]);
                        }else{//diff color, diff neighborhood
                            dp[ii][jj][kk] = Math.min(dp[ii][jj][kk], dp[ii-1][jj-1][pkk]);
                        }
                    }
                }
            }else{//the house is not painted 
                for(int jj=1; jj<=target; ++jj){ 
                    //carry tmp as ii-1 min cost @ each color
                    Pair<Integer, Integer>[] tmp = new Pair[n+1];//color 1~n, 0 is dummy
                    for(int pkk=0; pkk<=n; ++pkk){
                        tmp[pkk] = new Pair<Integer, Integer>(dp[ii-1][jj-1][pkk], pkk);
                    }
                    tmp[0] = new Pair<Integer, Integer>(Integer.MAX_VALUE/2, 0);
                    Arrays.sort(tmp, Comparator.comparingInt(p -> p.getKey()));

                    // for(int kkk=0; kkk<=n; ++kkk) System.out.println("kkk: " + tmp[kkk].getKey() + ":" + tmp[kkk].getValue());
                    //an array n color of array of 2 (cost, idx)
                    // int[][] tmp= new int[n+1][2];
                    // for(int pkk=0; pkk<=n; ++pkk){
                    //     tmp[pkk][0] = dp[ii-1][jj-1][pkk];
                    //     tmp[pkk][1] = pkk;
                    // }

                    // tmp[0][0] = Integer.MAX_VALUE/2;
                    // tmp[0][1] = 0;
                    // Arrays.sort(tmp, Comparator.comparingInt(p -> p[0]));

                    for(int kk=1; kk<=n; ++kk){

                        dp[ii][jj][kk] = dp[ii-1][jj][kk]+cost[ii][kk];//when ii and ii-1 same color

                        if(kk == tmp[0].getValue()){//if same color, cannot, use 2nd min
                            dp[ii][jj][kk] = Math.min(dp[ii][jj][kk], tmp[1].getKey()+cost[ii][kk]);
                        }else{//diff color, diff neighborhood
                            dp[ii][jj][kk] = Math.min(dp[ii][jj][kk], tmp[0].getKey()+cost[ii][kk]);
                        }
                        
                    }
                }
            }
        }

        int ret=Integer.MAX_VALUE/2;
        for(int kk=1; kk<=n; ++kk){
            ret = Math.min(ret, dp[m][target][kk]);
        }
        return ret==Integer.MAX_VALUE/2?-1:ret;
    }
}
/*
* m house
* n colors
* target neighborhood
-> min cost to paint m houses, target neighborhood, and each house has n colors to select
*/