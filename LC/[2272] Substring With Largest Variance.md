### Problem:

- Variance: max(char_freq)-min(char_freq)
  => find max(Variance) of all substring

### Constrains

```
+ 1 <= s.length <= 10^4
+ s consists of lowercase English letters.
```

### Observation:

- All substring is O(N^2), given N=10^4 (> 10^3), we need to consider if we
  can do log(N) or better.
- All lower case chars -> can we try all lower case combinations?
  -> 26*26*N = 256N

## Ideas 1: (converting to 1, 0, -1 array and apply Max subarray sum - Kadane)

- Variance of (a, b)
  => create subarray and set a=1, b=-1, and others as 0, then sum
  of such subarray is the variance.
- Convert original string to 1, 0, -1 array.
- max subarray sum -> Kadane's Algorithm.

### Steps:

- for all chars in the given string, find all pairs of chars.
- for each pair of chars, construct the (1,0, -1) array
- here each pair is 26*25/2*1=325,
  Kadane's algorithm is O(N)
  => O(325N) = 3250000
- Bruteforce: 10^4^2 = 100000000

# DP: 26*26*N

- For each pair (a,b) of chars in the substring
- let a=1, b=-1, others=0
- since the answer need to contain two chars.
- define dp0: max subarray sum ending @ ii where nums[ii]=1 and the subarray does NOT containing b
  dp1: max subarray sum ending @ ii where nums[ii]=1 and the subarray does containing b

  if nums[ii]==a
  update both
  else:
  output result and reset dp0

# DP: 26N:

- only process those with 1, -1
