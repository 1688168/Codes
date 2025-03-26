class Solution {
    private int helper(int ii, int state, int maxProfit, int[] prices){
        int N = prices.length;
        if(ii>=N || state >= 4) return maxProfit;
        if(state==0) return Math.max(helper(ii+1, state, maxProfit, prices), helper(ii+1, 1, maxProfit-prices[ii], prices));

        if(state==1) return Math.max(helper(ii+1, state, maxProfit, prices), helper(ii+1, 2, 
maxProfit+prices[ii], prices));

        if(state==2) return Math.max(helper(ii+1, state, maxProfit, prices), helper(ii+1, 3, maxProfit-prices[ii], prices));

        if(state==3) return Math.max(helper(ii+1, state, maxProfit, prices), helper(ii+1, 4, maxProfit+prices[ii], prices));

        return maxProfit;

    }
    public int maxProfit(int[] prices) {
        return helper(0, 0, 0, prices);
    }
}