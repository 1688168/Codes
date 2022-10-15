### Problem:
* Variance: max(char_freq)-min(char_freq)
=> find max(Variance) of all substring

```diff
+ constrains
+ 1 <= s.length <= 10^4
+ s consists of lowercase English letters.
```
### Observation:
* All substring is O(N^2), given N=10^4 (> 10^3), we need to consider if we
  can do log(N) or better.
* All lower case chars -> can we try all lower case combinations?
                       -> 26*26*N = 256N

## Ideas 1: (converting to 1, 0, -1 array and apply Max subarray sum - Kadane)
* Variance of (a, b)
  => create subarray and set a=1, b=-1, and others as 0, then sum
  of such subarray is the variance.
* Convert original string to 1, 0, -1 array.
* max subarray sum -> Kadane's Algorithm.

### Steps:
* for all chars in the given string, find all pairs of chars.
* for each pair of chars, construct the (1,0, -1) array
* here each pair is 26*25/2*1=325,
  Kadane's algorithm is O(N)
  => O(325N)         =   3250000
* Bruteforce: 10^4^2 = 100000000

## Ideas 2: (Instead of physically construct 1,0, -1 array and using Kadane Alg, why not just calc)
