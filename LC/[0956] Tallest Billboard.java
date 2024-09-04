class Solution {
    public int tallestBillboard(int[] rods) {
        int N = rods.length;
        int offset=5000;
        int[] dp = new int[offset*2+5];//rods=[0, N], diff=[-5k, 5k]
     
        //initialize int array to a specific value
        dp=Arrays.stream(dp).map(x -> -1).toArray();
       
        //initialize DP
        dp[0+offset]=0;//start from maz height as zero when we have nothing

        //int [] dp_old = new int[offset*2+5];
        for(int ii=0; ii<N; ++ii){//this is contribution model, so in range [0, N-1] - all rods
            //clone the old dp
            //IntStream.range(0, N+1).map(idx -> dp_old[idx]=dp[idx]);
            int[] dp_old = dp.clone(); //Java how to copy array
            int ll=rods[ii];

            for(int jj=-offset; jj<offset; ++jj){//we don't need to contribute in end last use case
                if(dp_old[jj+offset]==-1) continue; //new rod can only be added on top of valid current state
                //can new rod contribute to left?
                if(jj+ll < offset){//no need to consider last jj for contribution (nothing after it)
                    dp[jj+ll+offset] = Math.max(dp[jj+ll+offset],dp_old[jj+offset] + ll);
                }
                
                //can new rod add to right?
                if(jj-ll >= -offset)
                    dp[jj-ll+offset] = Math.max(dp[jj-ll+offset], dp_old[jj+offset]);
            }
        }

        return dp[0+offset];//max height for diff=0
    }
}