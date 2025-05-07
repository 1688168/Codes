class Solution {
    public int minSpaceWastedKResizing(int[] nums, int k) {
        //min waste given an array and cost formula
        //for each ii, try all the valid size (color)
        //1473 color is given, 1959, valid size is all the max upto ii <<<<< 
        //1473 try all the colors -> this is a type I DP
        //1959 try all valid size -> this is an interval DP. last interval on top of prior interval

        int N = nums.length;

        //declare/define DP
        //1473 we use 3D dp cuz the number of color is given
        //1959, we do not know how many resize (actually, could be N)
        int[][] dp = new int[N][k+1]; //dp[ii][jj]: min waste upto ii with jj resize

        //initialize dp
        //default to MAX as we are minimize the waste
        for(int ii=0; ii<N; ++ii){
            for(int jj=0; jj<=k; ++jj)
                dp[ii][jj]= Integer.MAX_VALUE/2;
        }

        //when jj=0 -- we have jj start from 1 -> no reset -> min waste is have sz=mx in the interval 
        int mx=0;
        int ttl=0;
        for(int ii=0; ii<N; ++ii){
            mx=Math.max(mx, nums[ii]);
            ttl += nums[ii];
            dp[ii][0] = mx*(ii+1)-ttl;
        }

        dp[0][0]=0;
        //populate dp
        for(int ii=1; ii<N; ++ii){//for each item in array
            for(int jj=1; jj<=Math.min(ii, k); ++jj){ //for each resize count, cannot reset more than available ii
                mx=0;
                ttl=0;
                for(int st=ii; st>=1; --st){
                    ttl += nums[st];
                    mx=Math.max(mx, nums[st]);
                    dp[ii][jj] = Math.min(dp[ii][jj], dp[st-1][jj-1] + mx*(ii-st+1)-ttl);
                }
            }
        }

        int ret=Integer.MAX_VALUE/2;

        for(int jj=0; jj<=k; ++jj) ret = Math.min(ret, dp[N-1][jj]);

        return ret;
    }
}
