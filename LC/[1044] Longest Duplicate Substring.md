"""

- find longest duplicate substring.

1. dp:
   dp[ii][jj]: two string - ending on ii, and ending on jj. if they are equal
   = dp[ii-1][jj-1] if s[ii]==s[jj] else
   [x x x] i x x x
   x x x [x x x] j
   ans = max(dp[ii][jj]) where ii=0, ..., n, j=0, ... n

- O(N^2), but here we have 10^5 -> N^2 won't work
- 10^5 => nlogn
- log -> Binary
- given a window, do we have duplicate ? Yes -> increase window size. No -> reduce window size
  => this still TLE.
- inserting long string into Hash is slow.

# Rolling Hash.

- hash a sting into hash, number into hash is much easier than string
  use 26 based rolling Hash

a[k-1]*26^(k-1) + a[k-2]*26^(k-2) + ... + a[0]\*26^0 % M
we need to take Mod as this number could be very big.
select a prime number for M: power(10, 9)+7

- to avoid collision: 二哈算法: str1 => keyA, keyB. str2 => keyC, KeyD (reduce the collision rate)

In this question, this selection of parameter works for all test cases (so far):

- base = 26
- m=(1<<32)

# binary search:

while left < right:
mid = left + (right-left)//2 ===> right - (right-left)//2 ===> to avoid infinite loop
if(ok){
-> mid is a solution
-> left = mid <<< avoid infinite loop. try left=0, right=1 => left is always zero
-> right = mid-1 #for all that is not working, do not include in the next search scope
}
"""

> Rolling Hash

xx[abcd]exxxx
xxx[abcd]exxx

a=1
b=2
...

abcd=1234

bcde
1234 => 234 => 2345

each time we hash for a new string, we only need to process the begin and ending char

a[k-1]*26^(k-1) + a[k-2]*26^(k-2) + ... + a[0]\*26^0

> how to avoid the collesion?

1. double hash (二哈哈希)
