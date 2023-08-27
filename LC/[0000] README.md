# Two Pointers

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

[2762] M

# Max/Min of a sliding window

-> max value in sliding window

1. use deque <span style="color:red">(recording the index of the element, not the value)</span>
2. each time expand the window, pop the deque until the new window element is smaller than the last element in deque
3. each time shrinking the window,
4. the max is the first element in the deque <span style="color:red"> use the index to retrieve value from original array<span>

# Binary Index Tree (BIT)

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

![Alt text](image.png)

[0307] M

# Count Subarray by Element

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

# Monotonic Stack

=> PrevSmaller, NextSmaller, PrevGreater, NextGreater
[0496]
[0503]

# Count Subarray by Element

```
- Pattern: looking for some metrics of all sub-arrays
- All sub-arrays is O(N^2)
- We should pre-calc info for each element and bring down the time complexity
```
[1498]
[2302]
[2681] H : Power-of-Heroes

- sum of all (sub-sequence-max)^2\*subsequence-min
- Whenever grouping by subsequence, we can sort as the original order no longer matter
- Whenever we are looking for Nlog(N) time, we can sort
- All combination: O(N^2)  
  -> In order to meet nO(logn), we need to calc something for a set of group to reduce time-complexity



# DP

Time-Series
[0198] M : House Robber
[0123] : Best Time to Buy and Sell Stock III
[0213] : House Robber II
[0487]
[1186]
[1289]
