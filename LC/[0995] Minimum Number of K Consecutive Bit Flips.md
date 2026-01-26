# Minimum Number of K Consecutive Bit Flips
## Task
* Min num of k-bit flips
  
## Hints
* Interval operation -> sweepline
* Min/Max 
  * DP
  * Greedy
  * Binary Search
  
## Analysis
* N=10^5
* k=10^5

> `Bruteforce`
> Can we partially solve the problem and get partial credit?
* How to rule out those has no solution:
  * if you have a 1 that is covered by two k-interval that has zeros

> Can we exhaust and sort for best solution? what's the cost?
* How to exhaust all outcomes?
  * any zero as starting point recursive left and right
  * T: k!
  * S: k depth where k is number of zeros

* Heuristic: go from the end of array and identify those you must flip
