class Solution {
    public long minCost(int n, int[][] cost) {
        //partition the houses to p1 and p2
        //find min cost of P1 like paint house I
        //find min cost of P2 considering P1
        int nn = n/2;

        var dp = new int[nn][3];
        //when ii=0: the first house
        for(int jj=0; jj<3; ++jj) dp[0][jj]= cost[0][jj];
        for(int ii=1; ii<n; ++ii){//for each house
            for(int kk=0; kk<3; ++kk){
                for(int pkk=0; pkk<3; ++pkk){
                    if(kk==pkk) continue;
                    dp[ii][kk] = Math.min(dp[kk], dp[ii-1][pkk] + cost[ii][kk]);
                }
            }
        }

        int p1 = Arrays.stream(dp[n-1]).min();

        var dp2 = new int[nn][3];
        //handle first house in p2
        dp2[n][0] = Math.min(dp[n-1][1], dp[n-1][2]);
        dp2[n][1] = Math.min(dp[n-1][0], dp[n-1][2]);
        dp2[n][2] = Math.min(dp[n-1][0], dp[n-1][1]);

        for(int ii=nn+1; ii<n; ++ii){//for each house in p2
            int eii = n-ii-1;
            for(int kk=0; kk<3; ++kk){
                dp2[ii][kk]
                
            }
        }
    }
}

// * n: even integer - 10^5 - num of houses
// * cost: size=nX3 (3 colors)
// * no adjacent houses of same color
// * no equidistant of houses of same color
// -> min cost to paint all houses
// -----
// x x x o o o

// p1: -> paint house II (3 colors, no adjacent house same color min cost)
// p2: -> paint house IV (3 colors, no adjacent h ouse same color and cannot be same color as equidistance houses in P1)
