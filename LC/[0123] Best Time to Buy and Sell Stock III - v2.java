class Solution {
    public int maxProfit(int[] prices) {
        int N = prices.length;
        int b1 = Integer.MIN_VALUE;
        int s1 = 0;//why zero. the initial state of best profit should always be 0
        int b2 = Integer.MIN_VALUE;
        int s2 = 0;//why zero. the initial state of best profit should always be 0
        
        for(int ii=0; ii<N; ++ii){
            s2 = Math.max(s2, b2+prices[ii]);//please notice this is in reversed order to ensure prev value is not updated until no longer required
            b2 = Math.max(b2, s1-prices[ii]);
            s1 = Math.max(s1, b1+prices[ii]);
            b1 = Math.max(b1, -prices[ii]);

        }

        return s2;
    }
}