# $${\color{orange}Patterns, \space Data \space Structures}$$

### Top K and Quick Select/Heap
### Modified Binary Search
### Heap
### Trie
### Sliding Window
### Subarray
* [Count Subarray by Element]
### Subsequence
### Segment Tree
### DFS:
- all paths
### BFS:
`Shortest path from A to B`
- [127 Word Ladder I](https://github.com/1688168/Leetcode/blob/main/LC/%5B0127%5D%20Word%20Ladder.py "I")  

`Shortest path from A to B print all paths`  
- [126 Word Ladder II](https://github.com/1688168/Leetcode/blob/main/LC/%5B0126%5D%20Word%20Ladder%20II.py "II")  

### DP:
`Max Subarray`
- [Substring With Largest Variance](https://github.com/1688168/Leetcode/blob/main/LC/%5B2272%5D%20Substring%20With%20Largest%20Variance.md "Read Me")
- 2272

### Greedy:
### subarray:
`Count Subarray by element`  
- 828.Count-Unique-Characters-of-All-Substrings-of-a-Given-String 
- 907.Sum-of-Subarray-Minimums 
- 1498.Number-of-Subsequences-That-Satisfy-the-Given-Sum-Condition 
- 1856.Maximum-Subarray-Min-Product 
- 2104.Sum-of-Subarray-Ranges 
- 2262.Total-Appeal-of-A-String 
- 2281.Sum-of-Total-Strength-of-Wizards
- 2302.Count-Subarrays-With-Score-Less-Than-K 
- 2444.Count-Subarrays-With-Fixed-Bounds 

### sweep line or Intervals [扫描线]
- How many Airplanes on the sky at any moment?

## idea:
- break the intervals (st, ed) to (st, 1), (ed, -1)
- add all (st, 1), (ed, -1) to an subArrayRanges
- sort the array in increasing Order by time of (time, val)
- accumulate val and check the max sum of val along the way.

## Examples:
- max meetings at any time
- can one person attend all meetings? => is there any more than one meeting at the same time
- min number of conf rooms required -> max concurrent meetings at any time
- merge intervals
- insert interval
- remove interval


### some patterns:
- prev/next max/min
- subsum

### Problem Sets:
- Buy Sell Stock
- Basic Calculator
- Word Break
- Jump Game
- Course Schedule
