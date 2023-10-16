### Objectives:

- Given a string, count sum of unique chars of all substrings.

### Observations:

- All substring (subarray) is N^2
- We are given the following constrains:

```diff
+Constraints:
  !1 <= s.length <= 10^5 (>>> solution need to be N(logN) or lower)
  !s consists of uppercase English letters only. (>>> consider all 26 chars)
```

- Per constrains, we cannot consider O(N^2) bruteforce solution

### Pattern:

- each time we try to accumulate some "metrics" from all subarrays
  a. can we bruteforce? all subarrays is O(N^2). if N is < 100 Yes, otherwise No
  b. can we pre-calculate some lookup info and calculate contribution of each array
  elements to the observed metric.

### Idea:

- Consider contribution of each char to the "unique char count"  
  ex: arr[a x x x x ii x x x x x b]  
  -> how many counts arr[ii] can contribute to the total unique char count?  
  ** arr[ii] contributes to count for all subarrays btn [a, b]  
   where arr[a]=arr[ii] << prev arr[ii]  
   arr[b]=arr[ii] << next arr[ii]  
   a could be -1 (dummy start)  
   a could be N (dummy end)  
  ** number of subarrays btn [a,b] = (ii-a)\*(b-ii)  
  ** precalculate [a, b] for each char in the string. --- A  
  ** traverse A in prev step and accumulate (ii-a)(b-ii)
