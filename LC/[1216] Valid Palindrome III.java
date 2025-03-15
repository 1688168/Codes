class Solution {
    public boolean isValidPalindrome(String s, int k) {
        /* -> min delete to make a string palindrome
        * * a string is a palindrome if it equals to its own reversal
        * * min delete to make a string palindrome is equivalent to min delete to make 
        * * a string equal to it's own reversal  -> LCS
        */
        // create s2 which is s's reversal
        String s2 = new StringBuilder(s).reverse().toString();//java reversing a string
        int N = s.length();

        s = "#" + s;
        s2 = "#" + s2;

        // find min delete to make s equal to s2 -> LCS (longest common subsequence)
        //declare dp: 2D int array with 0
        var dp = IntStream.range(0, N+1)
                          .mapToObj(ii -> IntStream.range(0, N+1)
                                                   .map(jj -> 0).toArray()
                          ).toArray(int[][]::new);

        for (int ii=1; ii<=N; ++ii){
            for(int jj=1; jj<=N; ++jj){
                if(s.charAt(ii)==s2.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1]+1;
                }else{
                    dp[ii][jj] = Math.max(dp[ii-1][jj], dp[ii][jj-1]);
                }              
            }
        }

        // return if min delete <= k
        return N-dp[N][N] <= k;

    }
}