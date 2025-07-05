class Solution {
    public long minCost(int n, int[][] cost) {//see the return value, they already hint you need to use long
        int left = n/2-1;
        int right = left+1;
        long MAX_VAL = Long.MAX_VALUE/2;//int(Math.power(10, 5)* Math.power(10, 5));
        //dp[ll][rr]: current min cost with left color ll, right color rr
        var dp = new long[3][3];
        for(int c1=0; c1<3; ++c1){//initialize all combination to max int
            for(int c2=0; c2<3; ++c2){
                dp[c1][c2]=MAX_VAL;
            }
        }
        //center 
        for(int c1=0; c1<3; ++c1){
            for(int c2=0; c2<3; ++c2){
                if(c1==c2) continue;
                dp[c1][c2]=Math.min(dp[c1][c2], cost[left][c1]+cost[right][c2]);
            }
        }
        --left;
        ++right;
        while(left >=0 && right < n){//from center to both ends
            //clone the dp
            
            var tmp_dp = new long[3][3];
            for(int ii=0; ii<3; ++ii) tmp_dp[ii] = dp[ii].clone();//copy as previous states
            for(int ii=0; ii<3; ++ii){//reset current states
                for(int jj=0; jj<3; ++jj){
                    dp[ii][jj] = MAX_VAL;
                }
            }

            for(int c1=0; c1<3; ++c1){//for each color to consider @ current house from center
                for(int c2=0; c2<3; ++c2){
                    if(c1==c2) {
                        dp[c1][c2] = MAX_VAL;
                        continue; //equi-distance is skipped
                    }
                    List<Integer> left_list = new ArrayList<>(); //collect prev color candidates
                    List<Integer> right_list = new ArrayList<>();
                    for(int pc =0; pc<3; ++pc){//pc: previous color
                        if(pc!=c1) left_list.add(pc);//left pc cannot be same as current left color
                        if(pc!=c2) right_list.add(pc);//right pc cannot be same as current right color
                        
                    }

                    for(var lpc: left_list){//left prev color
                        for(var rpc: right_list){//right prev color                         
                            dp[c1][c2] = Math.min(dp[c1][c2], tmp_dp[lpc][rpc]+cost[left][c1]+cost[right][c2]);
                        }
                    }  
                }
            }
            --left;
            ++right;
        }
        long ans=MAX_VAL;
        for(int ii=0; ii<3; ++ii){
            for(int jj=0; jj<3; ++jj){
                ans=Math.min(ans, dp[ii][jj]);
            }
        }
        return ans;

    }
}