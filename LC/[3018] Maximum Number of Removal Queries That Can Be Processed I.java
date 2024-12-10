      /* 
       */
      class Solution {
        public int maximumProcessableQueries(int[] nums, int[] queries) {
            int N = nums.length;//java take array size
            int M = queries.length;
            int[][] dp = new int[1005][1005];//java initialize two dimentional array
            dp[0][N-1]=0;//this is known
    
            //type V DP template
            for(int len=N-1; len>=1; --len){//try each len from large interval to smaller as we know the initial status only @ max interval
                for(int ii=0; ii+len-1<N; ++ii){ //each staring idx of the interval
                    int jj = ii+len-1;//ending index
                    //current (smaller) state is from previous (bigger) state
                    /* case I: can we reach current state by eliminate nums[ii] in the interval
                    */
                    if(ii-1>=0){//we can derive current state from ii-1   
                        int kk = dp[ii-1][jj]; 
                        if(kk<M && queries[kk] <= nums[ii-1])
                            dp[ii][jj] = Math.max(dp[ii][jj], dp[ii-1][jj]+1);
                        else
                            dp[ii][jj] = Math.max(dp[ii][jj], dp[ii-1][jj]);
                    }
    
                    // case II: can we reach current state by eliminate nums[jj] in the interval
                    if(jj+1 < N){//we can derive current state from jj+1   
                        int kk = dp[ii][jj+1];//current state??   
                        if(kk<M && queries[kk] <= nums[jj+1])
                            dp[ii][jj] = Math.max(dp[ii][jj], 1+dp[ii][jj+1]);
                        else
                            dp[ii][jj] = Math.max(dp[ii][jj], dp[ii][jj+1]);       
                     }
                }
            }
    
            int ans=0;
            //can we eliminate the last char?
            for(int ii=0; ii<N; ++ii){
                int kk = dp[ii][ii];
                ans = Math.max(ans, kk<M && queries[kk] <= nums[ii] ? kk+1: kk);
            }
            return ans;
        }
    }