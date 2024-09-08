class Solution {
    public int lastStoneWeightII(int[] A) {
       //java default boolean is false?
       boolean[] dp = new boolean[1501]; //30*100/2 (total_sum/2)
       dp[0] = true;//initialize dp[0] as true: do nothing is achievable
       /*
        * dp[ii]: if smaller subset sum to ii is possible?
        * where ii is the smaller subset sum
       */
       int sumA = 0;
       for (int a : A) {//for each stone
           sumA += a;//this is for pruning, no need to try anything beyound the total sum so far
           
           //consider each potential sum see if achievable for each stone
           //notice here we start from total/2 and ending @ a (avoided array out of bound)
           for (int i = Math.min(1500, sumA); i >= a; --i)//nice pruning
               dp[i] |= dp[i - a]; //dp[ii] was achievable or is achievable after adding new stone from "ii-a" state
       }
       for (int i = sumA / 2; i >= 0; --i)//the potential smaller sum
           if (dp[i]) return sumA - i - i;//return the smallest sum that is true
       return 0;
   }
}