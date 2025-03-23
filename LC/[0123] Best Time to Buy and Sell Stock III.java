class Solution {
    public int maxProfit(int[] prices) {
        int N = prices.length;
        int bought1 = Integer.MIN_VALUE/2;
        int sold1 = Integer.MIN_VALUE/2;
        int bought2 = Integer.MIN_VALUE/2;
        int sold2 = Integer.MIN_VALUE/2;

        for(int ii=0; ii<N; ++ii){
            if(ii==0) {//day1
                bought1= Math.max(bought1, -prices[ii]);
                continue;
            }

            int _bought1 = bought1;
            int _sold1 = sold1;
            int _bought2 = bought2;
            int _sold2 = sold2;

            //the day after day1  
            bought1= Math.max(_bought1, -prices[ii]); 
            sold1 = Math.max(_sold1, prices[ii] + _bought1);
            bought2 = Math.max(_bought2, _sold1 - prices[ii]);
            sold2 = Math.max(_sold2, prices[ii] + _bought2);
        }

        //return Math.max(0, Math.max(sold1, sold2));
        //[java][stream][max][initialize int array]
        //return Arrays.stream(new int[]{0, sold1, sold2}).max().getAsInt();
        return IntStream.of(0, sold1, sold2).max().getAsInt();//[java][max]
    }
}
/*
** Analysis:
* N=10^5
* given an array
* maxProfit: optimize something on a single array
* constrains: two transactions
* -> bruteforce: 4^n
* -> binarysearch: given a target (32). achievable?
* -> greedy:
* -> DP:
* dp[ii] - the max profit on day ii
* dp[ii] - didNothing, bought1, sold1, bought2, sold2
* return max(sold2)
*/