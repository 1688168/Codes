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