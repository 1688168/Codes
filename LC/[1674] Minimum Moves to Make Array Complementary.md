# 1674. Minimum Moves to Make Array Complementary

## Problem Statements
* nums: even length n
* limit: replace with 1...limit (inclusive)
* min moves required to make nums complementary
* define operation

## Analysis
* N: 10^5 -> nlonn
* what is the ultimate pair sum -> x: [2, 2*10^5] --- range of x 
* if we know x, how many moves requires to make pairs sum to x
* range arithmatic -> sweep line
ex: 
- 1, 2, 4, 3
- limit=4


## Ideas
* greedy
* dp
* 



## Follow up questions
* time: max(O(N), O(C))
* space: O(C)
* what if C=10^9
* diff is sparce, no need to create space for zeros (most are zero)
* only need to traverse turning point
