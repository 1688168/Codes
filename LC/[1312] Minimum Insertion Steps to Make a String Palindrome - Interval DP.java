class Solution {
    public int minInsertions(String s) {
        int N = s.length();

        //declare dp as 2D and initialize dp to maxInt
        var dp = IntStream.range(0, N)
                          .mapToObj(ii->IntStream.range(0, N)
                                                  .map(jj -> Integer.MAX_VALUE/2)
                                                  .toArray()
                          ).toArray(int[][]::new);

        for(int ii=0; ii<N; ++ii){
            for(int jj=0; jj<N; ++jj)if(ii==jj || ii+1 >= jj) dp[ii][jj]=0;    
        }

        for(int ll=2; ll<=N; ++ll){
            for(int ii=0; ii+ll-1<N; ++ii){
                int jj = ii+ll-1;
                if(s.charAt(ii)==s.charAt(jj)){
                    dp[ii][jj] = dp[ii+1][jj-1];
                }else{
                    dp[ii][jj] = 1+Math.min(dp[ii+1][jj], dp[ii][jj-1]);
                }
            }
        }


        return dp[0][N-1];
    }
}

/* Given a string -> min insertion required to make it palindrome
['Method I']
* - when editing a string into palindrome -> make s equal to s' where s' is the reversal of s
* --> this converts the problem into two string problem
* --> shortest-super-sequence is a palindrome on top of s and s' (with min add)
* --> LCS is a palindrome with min-remval
['Method II']
* interval DP.-> dp grows from both end.
* base case: dp[0][0]=0 (two empty string)
* dp[ii][ii] = 0 (single char is palindrome)
*/

