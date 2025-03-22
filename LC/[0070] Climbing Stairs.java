class Solution {
    public int climbStairs(int n) {

        //sanity check
        if(n<=2) return n;

        //define dp
        //dp[ii]: number of ways to reach stair ii

        //declare dp
        var dp = new int[n+1];

        //initialize dp
        dp[0]=1;
        dp[1]=1;
        dp[2]=2;

        for(int ii=3; ii<=n; ++ii) dp[ii]=dp[ii-1]+dp[ii-2];
        
        return dp[n];
    }
}

/*
Analysis:
    * N=45 

Bruteforce:
    * 2^45

DP:
    * if we know all the previous states
    * dp[ii] = dp[ii-1] + dp[ii-2]

*/