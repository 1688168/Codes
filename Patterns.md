n# $${\color{orange}Patterns, \space Data \space Structures}$$

# [`BFS`]

# [`Binary Search`]

```
- Find Min/Max of some condition.  Guess the Min/Max see if we can satisfy the condition
- Count some condition, use binary search to find the range for counting
```

[0235] BST
[0236] BT
[1123] LCA on lowest leaves (same as 1676)
[1644] LCA on P, q that might not existing
[1650] LCA with pointer to parent
[1676] LCA on a set (same as 1123)

[1740]
[2096]
[2439]
[2519]
[2528] Maximize the Minimum Powered City

```
-
```

[2702]

# [`Binary Index Tree (BIT)`]

```
* asking for range sum from an array
* "Binary index tree" can always solve "Segment Tree" problems
* The reason we are still larning "Segment Tree" is the required coding is less than "Binary index tree"
* Notice the BIT is 1 indexed
* The supported interface:
-> initialization
-> sumRange
-> updateDelta``
```

[0307] M

# [`Count Subarray by Element`]

```
- Pattern: looking for some metrics of all sub-arrays
- All sub-arrays is O(N^2)
- We should pre-calc info for each element and bring down the time complexity

>> example matrics:
- min*sub-arr-sum (H)

```

[1498]  
[2281] H: Sum of Total Strength of Wizards

- Strength: min(in subarray) \* sum(subarray)

[2302] H: Count Subarrays With Score Less Than K

- Score: subarray_sum\*subarray_length < K

[2681] H : Power-of-Heroes

- sum of all (sub-sequence-max)^2\*subsequence-min
- Whenever grouping by subsequence, we can sort as the original order no longer matter
- Whenever we are looking for Nlog(N) time, we can sort
- All combination: O(N^2)  
  -> In order to meet nO(logn), we need to calc something for a set of group to reduce time-complexity

# [`Design`]

[0146]
[0155]
[0355]
[0380]
[0381]
[0432]
[0460]
[0535]
[0588]
[0622]
[0631]
[0642]
[0895]
[1146]
[1172]
[1268]
[1352]
[1381]
[1622]
[1670]
[2166]
[2296]

# [`DFS`]
- [2597]: can you try 2638 by DFS?
```
- Counting: for each element, you can either take or no-take based on some condition.  when reaching the end, we return 1
```

# [`DP`](https://github.com/1688168/Leetcode/template/DP.md)

[2297 - M - Jump Game VIII](https://github.com/1688168/Leetcode/blob/main/LC/%5B2297%5D%20JumpGameVIII.py) - [Video](https://www.youtube.com/watch?v=II7tWDuY7yE) - (DP), (Monotonic Stack)

- [1944] [Video](https://www.youtube.com/watch?v=oV-HvcHogyk)
- [2282] [Video](https://www.youtube.com/watch?v=AgC28b_0ekM)

# [`Greedy`]

# [`Heap`]

[2519] - <215>: binary search, sortedcontainers

# [`Max/Min of a sliding window`]

-> max value in sliding window

1. use deque <span style="color:red">(recording the index of the element, not the value)</span>
2. each time expand the window, pop the deque until the new window element is smaller than the last element in deque
3. each time shrinking the window,
4. the max is the first element in the deque <span style="color:red"> use the index to retrieve value from original array<span>

# [`Monotonic Stack`]

=> PrevSmaller, NextSmaller, PrevGreater, NextGreater
[0496]
[0503]

# [`Quick Select`]

[0215] Kth-Largest-Element-in-an-Array (M)
[0324] Wiggle-Sort-II (H)
[0347] Top-K-Frequent-Elements (M+)
[0973] K-Closest-Points-to-Origin (M)

# [`Sliding Window`]`

[1151]

```
Given an integer array
-> Define something for a subarray
-> Calc something for all subarrays

Ideas:
-> finding all subarrays and calc something -> O(N)
-> for each element as min/max -> find the max subarray that holds true
```

[0907] H :

> Monotonic Stack: sum of subarray min
> -> for each element as min, how many subarray this min can be?

[1856] M

[2104] M : sum of subarray range  
-> Define something as range: max-min of subarray  
-> Calc sum of all ranges

Observation 1:  
-> sum((max-min) of all subarrays)  
-> sum(max of all subarrays)-sum(min of all subarrays)

Observation 2:  
-> Min/Max of subarry  
-> Similar to Min/Max of Sliding Window  
-> Monotonic stack

Strategy:

> sum(max of all subarrays)

- precalc pre-larger and next-larger
- for each element as Max, we can find the valid window that the element is max
- (A): num of subarray of the "valid window" is left-length\*right-length
- (B): sum of subarray with that element as max: A \* element_value
- accumulate "B" for all elements -> we have sum(max of all subarrays)
- do the similar thing for min

# [`Top K elements`]

1. sort: NlogN
2. Heap/PQ: Nlogk
3. Binary Search: Nlog C
4. Quick select: AVG O(N)

[215]

# [`Topology Sort`]

[0207]  
[1591] Strange Printer


# [`Trie`]
[0139]  
```
- DFS by set lookup
> Space: O(N*k): N words with duplicated prefix
-- Time: 

- DFS by Trie word search
> Space: o(N*j): N words but compressed
- DP: O(N)
```
[0140]  
[0212]    


# [`Two Pointers`]

```
> template:
1. Givn an integer array.
2. Define qualification of a subarray
3. Calculate total number of qualifed subarrays in the original array

> key steps:
a. expand the window until it is disqualified (how to check the qualification?)
b. calculate/accumulate the required statistics
c. move (slide) the window

> Time: O(N)
```

[0075] (sort color)(dutch national flag)
[2762] M

# [`Union Find`]
