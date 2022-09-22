### Leetcode

### Top K and Quick Select/Heap
### Modified Binary Search
### Heap
### Trie
### Sliding Window
### Subarray
### Subsequence
### Segment Tree
### DFS:
- all paths
### BFS:
- Shortest path from A to B
- Shortest path from A to B print all paths

[Word Ladder](https://github.com/1688168/Leetcode/blob/main/%5B0126%5D%20Word%20Ladder.md "Read Me")
- [127 Word Ladder I](https://github.com/1688168/Leetcode/blob/main/%5B0126%5D%20Word%20Ladder.py "I")
- [126 Word Ladder II](https://github.com/1688168/Leetcode/blob/main/%5B0127%5D%20Word%20Ladder%20II.py "II")

### DP:
### Greedy:

### sweep line or Intervals
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
- sliding window maximum
- prev/next max/min

### Problem Sets:
- Buy Sell Stock
- Basic Calculator
- Word Break
- Jump Game
- Course Schedule
