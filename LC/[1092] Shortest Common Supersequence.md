> Problem statement
1. find a min str s.t. both s, t are subsequence of str.
2. need to output the min string -> need to output DP path
3. 

> analysis
* two series: s, t
* trying to find min/max of something that both s, t are associated with
* N=1000 (double loop)

> DP
* dp[ii][jj]: min len of str that s[:ii+1] and t[:jj+1] are both subsequence of
* dp[ii][jj] = 

z z z z z z z z a

x x x x x a
y y y y y y a


if s[ii]==t[jj]
    dp[ii][jj] = dp[ii-1][jj-1]+1
else
    dp[ii][jj] = min(dp[ii-1][jj], dp[ii][jj-1]) + 1
 
