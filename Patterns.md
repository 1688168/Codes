$${\color{orange}Patterns, \space Data \space Structures}$$

> When buildung graph, if output has requirements on order (lexical order, etc), we have to use defaultdict(list) instead of defaultdict(set)

> Sort string list in reversed order

```
tickets.sort(reverse=True)
```

# [`Idioms`]

> For interval problems starting from Sort the intervals by beginning or ending
> How to detect cycle in graph

### **BFS**

- Topology Sort

### **DFS**

- [207]: see sample code on DFS/BFS
- visited=1 and visited=2 where visited=2 is the current search path that is visited
- On current search path, mark visited=2, but on backtrack, mark visited=1

> How to Find Prev/Next Smaller/Greater

```
Monotoic Stack
```

> How to find how many elements before current that is smaller/greater than current?

```
- [2519]
- use Heap top K
- use bisect, insert
```

> How to get all subsets/combination

- [0078]

> Subsets
> Subarrayies

- Max subarray sum -> Kadane
- When finding max something of all subarraies, we might only need to consider the whole array as any subarray won't qualify

> How to group numbers with some distance k

```
- group[n%k].add(n)
- sort
```

- You can Sort as order doesn't matter in subset
- You can group and aggregate [2638] and aggregate by group

> How to define sort key

```
[937]
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
```

> When you see topK question for pairs (multiplication table, etc) -> Sorted Matrix Binary Search

> DFS VS BFS

- [126]: if we use BFS to carry the path, we will have to hold paths in queue for all nodes in same level. We only hold 1 path for DFS until we reach the end or fail. so from memory perspective, DFS is surpior
- BFS: shortest distance

> when you see anything that is represented in lower case english letters, think of can we try all 26 letters on same calc

# [`Binary Search`]

```
- Find Min/Max of some condition.  Guess the Min/Max see if we can satisfy the condition
- Count some condition, use binary search to find the range for counting
```

- [240]
- [373] - (719, 1918, 2040)
- [378] - (240)
- [668]
- [2040]

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

# [`BFS`]

- beware of the local_visited concept, we cannot add visited until all nodes same level are processed complete
- [0235] BST
- [0236] BT
- [1123] LCA on lowest leaves (same as 1676)
- [1644] LCA on P, q that might not existing
- [1650] LCA with pointer to parent
- [1676] LCA on a set (same as 1123)

- [1740]
- [2096]
- [2439]
- [2519]
- [2528] Maximize the Minimum Powered City

- [2702]

# [`Count Subarray by Element`]

```
- When dealing with subsequence and order doesn't matter (only care about max/min-1498), we can sort
- consider adding dummy at beginning/ending of the array
- you can loop by the array or loop by all letters (the diff btn num vs string)
- or when dealing with string, you might want to loop lower-case chars instead by index of string
```

```
- Pattern: looking for some metrics of all sub-arrays, sub-sequences
- All sub-arrays is O(N^2)
- We should pre-calc info for each element and bring down the time complexity

>> example matrics:
- min*sub-arr-sum (H)

```

```
### when calculating the metrics
- Monotonic stack to help find prev-smaller/greater, next-smaller/greater
- consider each ii as max/min (going both direciton) or ending
- use presum to find subarray sum
- use Kadane to findout max subarray sum

```

- [828] H: count distinct chars in subarray (duplicates are ignored)
- [1498] M:

  - Sub-Sequence: Sortable -> only care about max/min, order doesn't matter
  - when dealing with max-min relationship
    a. ii is min, find max (two pointers) -> O(N)
    b. ii is max. min is all from the right
  - Try ii be the min or max to solve

- [2262] H: count unique chars in subarray (duplicates counted as 1)
- [2281] H: Sum of Total Strength of Wizards
  - Strength: min(in subarray) \* sum(subarray)
- [2302] H: Count Subarrays With Score Less Than K
  - Score: subarray_sum\*subarray_length < K
- [2681] H : Power-of-Heroes
  - sum of all (sub-sequence-max)^2\*subsequence-min
  - Whenever grouping by subsequence, we can sort as the original order no longer matter
  - Whenever we are looking for Nlog(N) time, we can sort
  - max/min of group (subset) -> sort
  -

# [`Design`]

- [0146]
- [0155]
- [0355]
- [0380]
- [0381]
- [0432]
- [0460]
- [0535]
- [0588]
- [0622]
- [0631]
- [0642]
- [0895]
- [1146]
- [1172]
- [1268]
- [1352]
- [1381]
- [1622]
- [1670]
- [2166]
- [2296]

# [`DFS`]

```
- memo (lru_cache) is the best friend of DFS
```

- [2597]: can you try 2638 by DFS?

```
- Counting: for each element, you can either take or no-take based on some condition.  when reaching the end, we return 1
```

```
- dp[ii] = dp[jj]+something: how do find jj?
- monotonic stack (Prev/Next Smaller/Greater)
- topK strategy (Binary Search insert, Heap)
- BruteForce (O(N^2))
```

# [`DFS-Search in an Array`]

- [301]
- [473]
- [491]
- [698]
- [996]
- [1307]

# [`DP`]

> Type I (Basic): Single Array Find Max/Min of something with a sub-array

```
dp[ii][jj]:   iith round, state jj
dp[ii][jj] = dp[ii-1][jj]+something
- Today's state can be derived from Yesterday's states
```

- Kadane
- [123]
- [198]: House Robber
- [213]
- [256]
- [309]
- [376]
- [1289]

> To-do or Not-to-do (State Design)

- you can exercise one strategy (buy/sell stock) => states=(tke, ntk)

- [487]
- [1186]

> Type II (Basic enhanced): Time Series 2

```
- today's state can be derived from one of the JJ where jj < ii
```

- [300]: Longest Increasing Subsequence
- [368]
- [1105]

> Type III: Two sequences

- [72]
- [97]
- [115]
- [727]
- [1092]
- [1143]: Longest Common Subsequences

> LCS/SCS Variation

- [583]
- [712]
- [1035]
- [1216]
- [1312]

> Type IV: Type I Intervals

- [410]
- [813]
- [1278]
- [1335]

> Type V: Type II Intervals

- [312]
- [375]
- [516]
- [1246]

> Type VI: backpack

- [474]
- [494]
- [879]
- [956]
- [1049]

> Compress state

- [691]
- [1125]
- [1349]

> Homework

- [903] Type I
- [983] Type II
- [546] Type III
- [518] Backpack
- [943] state compression
- [887] Give up

> DP MISC

- [1000]: combining Type I and Type II intervals
- [2355]

- [2297 - M - Jump Game VIII](https://github.com/1688168/Leetcode/blob/main/LC/%5B2297%5D%20JumpGameVIII.py) - [Video](https://www.youtube.com/watch?v=II7tWDuY7yE) - (DP), (Monotonic Stack)

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

# [`Indexing Sort`]

> array with N~ elements, with element values from 1~N~.
> Find missing num, duplicated num

```
# some trics
* if not indexing from 0, insert a dummy starting element

# condition of swap
while ii != nums[ii] and nums[ii] < N and nums[ii] != nums[nums[ii]]:
a. element not matching it's own index
b. element value is not out-of-bound so we can swap
c. element value is not equal to the destination value or no point of swapping
```

# [`Intervals`]

> 1. 50%: Sweep line
> 2. 40%: Greedy
> 3. 10%: DP
>
> - typically need to sort
> - the initial (cs, ce)=(-math.inf, -math.inf) or intervals[0]?

- [56]
- [57]
- [495]
- [763]
- [2345] (Google)

## Two Directions:

### Greedy:

1. Sweep Line
   - when you do not need to select anything in the range.
   - count something on a specific moment
2. Sort
   - Sort by starting point => The minimum number of intervals to cover the whole range
   - Sort by ending point => The Maximum number of intervals that are non-overlapping

- If we can use Greedy, it typically is more efficient than DP

### DP:

# [`Monotonic Stack`]

```
- for each index, require increasing pattern before or after the anchor
- the increasing or decreasing pattern could be subarray or subsequence
- frequently relating to pre-smaller, prev-greater
-
```

=> PrevSmaller, NextSmaller, PrevGreater, NextGreater

- [42]
- [0084] Use monotonic stack to calculate largest rectangle
- [0496]
- [0503]
- [2297] - Jump Game VIII:
- [2334]
- [2866] Use monotonic stack to calculate Peak shape area

> [42][84][2334]

- Histogram: consider each bar as the highest number in the array (prev_smaller_equal, next_smaller)

# [`Parenthesis`]

```
- Stack
- Greedy
```

- [32]
- [301]
- [021]
- [1249]
- [1541]
- [1963]
- [678]
- [2116]

# [`Parse Expression`]

- [224] basic Calculator

# [`Quick Select`]

- [0215] Kth-Largest-Element-in-an-Array (M)
- [0324] Wiggle-Sort-II (H)
- [0347] Top-K-Frequent-Elements (M+)
- [0973] K-Closest-Points-to-Origin (M)

# [`Sliding Window`]`

[1151]

```
> grouping all something together
> -> when all something are together, there is a window

> counting something
> -> if something is zeros and ones, sum(nums) is the number of ones
```

- [0907] H :

> Monotonic Stack: sum of subarray min
> -> for each element as min, how many subarray this min can be?

- [1856] M

- [2104] M : sum of subarray range  
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

# [`Subset, Subarray, Subsequence`]

- Subsequence -> DP (Longest increasing subsequence, Longest Common Subsequence)
- Subarray -> Monotonic Stack, presum, presum2
- Subset -> you can group and sort

# [`Sweep Line`]

- When we use Sweep Line, we only consider sets of starting points and ending points, we do NOT know which starting point matching with which ending point.

# [`Top K elements`]

1. sort: NlogN
2. Heap/PQ: Nlogk
3. Binary Search: Nlog C
4. Quick select: AVG O(N)

```
### When we see top K
1. sort
2. heap
3. quick-sort
4. Binary Search with count

### When we see pair
1. sorted matrix strategy
```

- [215]

# [`Topology Sort`]

- [0207]
- [1591] Strange Printer

# [`Trie`]

- [0139]

```
- DFS by set lookup
> Space: O(N*k): N words with duplicated prefix
-- Time:

- DFS by Trie word search
> Space: o(N*j): N words but compressed
- DP: O(N)
```

- [0140]
- [0212]

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

- [0075] (sort color)(dutch national flag)
- [1151]
- [2762] M

# [`Union Find`]

- [990]

# Series

# [`Buy Sell Stock`]

# [`Calculator`]

# [`Course Schedule`]

# [`Jump Game`]

- [55]
- [45]
- [1306]
- [1345]
- [1340]
- [1696]
- [1871]
- [2297] - Jump Game VIII - (DP + Monotonic Stack) (1944, 2282, )

# [`Concatenated Word`]

# [`Word Search`]

# [`Word Break`]

- [139]
- [140]
- [472]

# [[`Word Ladder`]](https://github.com/1688168/Leetcode/blob/main/LC/%5B0126%5D%20Word%20Ladder%20II.md)

- [126]: Word Ladder II
  - From BeginWord to EndWord all, output all valid path
- [127]: Word Ladder I
  - Is existing from BeginWord to EndWord
