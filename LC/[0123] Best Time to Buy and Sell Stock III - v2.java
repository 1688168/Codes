import java.util.Arrays;

class Solution {
    public int maxProfit(int[] prices) {
        int bought1 = Integer.MIN_VALUE;
        int sold1 = 0;
        int bought2 = Integer.MIN_VALUE;
        int sold2 = 0;

        for (int price : prices) {
            bought1 = Math.max(bought1, -price);
            sold1 = Math.max(sold1, price + bought1);
            bought2 = Math.max(bought2, sold1 - price);
            sold2 = Math.max(sold2, price + bought2);
        }

        return sold2; // Maximum profit with at most two transactions
    }
}