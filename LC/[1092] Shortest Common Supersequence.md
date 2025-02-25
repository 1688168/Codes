
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
 

# <center><b><span style="color:orange">1092</span></b></center>

> # <b><span style="color:purple">Analysis</span></b>
* what would be the length of the string satisfy the ask?
* N=1000 -> 2D
* two series/strings -> DP III


> ### <span style='color:green'>Bruteforce<span>
1. len(res) >=max(len(s1), len(s2))
2. two pointers find chars in s2 but cannot be matched in s2: O(N1+N2))

```
abcd
cef

-> ef


```

> ### <span style='color:green'>DP III<span>
* N1, N2 <= 1000
* dp[ii][jj] = the length of shortest common supersequence for s1[:ii+1] and s2[:jj+1]

xxxxxxxx a
yyyy b
zzzzzzzzzzzz a|b 

if s[ii]==s[jj]:
  dp[ii][jj] = dp[ii-1][jj-1]+1
else:
  dp[ii][jj] = min(dp[ii-1][jj], dp[ii][jj-1])+1

* to trace back path, consider "frog leap" question

> ### <span style='color:green'>LCS strategy<span>

> ### <span style='color:green'>Greedy<span>

