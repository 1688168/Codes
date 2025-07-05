class Solution {
    public long minCost(int n, int[][] cost) {
        int left = n/2-1;
        int right = left+1;
        //dp[ll][rr]: current min cost with left color ll, right color rr
        var dp = new int[3][3];
        for(int c1=0; c1<3; ++c1){//initialize all combination to max int
            for(int c2=0; c2<3; ++c2){
                dp[c1][c2]=Integer.MAX_VALUE/2;
            }
        }
        //center 
        for(int c1=0; c1<3; ++c1){
            for(int c2=0; c2<3; ++c2){
                if(c1==c2) continue;
                dp[c1][c2]=Math.min(dp[c1][c2], cost[left][c1]+cost[right][c2]);
            }
        }
        left -= 1;
        right += 1;
        while(left >=0 && right < n){
            //clone the dp
            
            var tmp_dp = new int[3][3];
            for(int ii=0; ii<3; ++ii) tmp_dp[ii] = dp[ii].clone();

            for(int c1=0; c1<3; ++c1){//for each color to consider @ current house from center
                for(int c2=0; c2<3; ++c2){
                    if(c1==c2) {
                        dp[c1][c2] = Integer.MAX_VALUE/2;
                        continue; //equi-distance is skipped
                    }
                    List<Integer> left_list = new ArrayList<>();
                    List<Integer> right_list = new ArrayList<>();
                    for(int cc =0; cc<3; ++cc){
                        if(cc!=c1) left_list.add(cc);
                        if(cc!=c2) right_list.add(cc);
                        
                    }

                    for(int ii=0; ii<3; ++ii){
                        for(int jj=0; jj<3; ++jj){
                            dp[ii][jj] = Integer.MAX_VALUE/2;
                        }
                    }

                    for(var lc: left_list){
                        for(var rc: right_list){
                            if(lc==rc){
                                continue;
                            }

                            dp[lc][rc] = Math.min(dp[c1][c2], tmp_dp[lc][rc]+cost[left][c1]+cost[right][c2]);

                        }
                    }  
                }
            }
            --left;
            ++right;
        }
        int ans=Integer.MAX_VALUE/2;
        for(int ii=0; ii<3; ++ii){
            for(int jj=0; jj<3; ++jj){
                ans=Math.min(ans, dp[ii][jj]);
            }
        }
        return ans;

    }
}