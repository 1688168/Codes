# <p style="text-align: center"> <span style="color:Orange"> Patterns</span> </p>

> How to traverse all subset of a bit

```python
# how to traverse all subset of a bit
subset=state
while subset > 0:
    # to something on the subset
    subset=(subset-1)&state
```

> N VS Time complexity

```yaml
N    o(N)
1e6  O(N)
1e5  Nlog(N)
1e3  O(N^2)


# when you see 1e4:
1e4: O(kN)
-> if given a string and all in lowercase
-> highly likely the k is 26 lower chars
```

> When buildung graph, if output has requirements on order (lexical order, etc), we have to use defaultdict(list) instead of defaultdict(set)

> Sort string list in reversed order

```yaml
tickets.sort(reverse=True)
```

# [`Idioms`]

> For interval problems starting from Sort the intervals by beginning or ending
> How to detect cycle in graph

### **3 passes**

- [2565]

### **BFS**

- Topology Sort

### **DFS**

- [207]: see sample code on DFS/BFS
- visited=1 and visited=2 where visited=2 is the current search path that is visited
- On current search path, mark visited=2, but on backtrack, mark visited=1

> How to Find Prev/Next Smaller/Greater

```yaml
Monotoic Stack
```

```python
# calc prev smaller
prev_smaller=[-1]*N
stk=[]

nums.reverse()
for ii, nn in enumerate(nums):
    while stk and nn < nums[stk[-1]]:
        prev_smaller[stk[-1]]=N-ii-1
        stk.pop()
    stk.append(ii)

prev_smaller.reverse()
nums.reverse()

```

> How to find how many elements before current that is smaller/greater than current?

```yaml
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

```yaml
- group[n%k].add(n)
- sort
```

- You can Sort as order doesn't matter in subset
- You can group and aggregate [2638] and aggregate by group

> How to define sort key

```yaml
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

# [`Arrangement with Stride`]

1. simulation (PQ) - if the question is asking print out the actual arrangement
2. greedy

- [0621]

# [`Binary Index Tree`]

- https://www.cnblogs.com/grandyang/p/4985506.html

# [`Binary Search`]

```yaml
- Find Min/Max of some condition.  Guess the Min/Max see if we can satisfy the condition
- Count some condition, use binary search to find the range for counting
```

- [0004]: Binary search for median in two sorted Array
- [0033]: rotated array: Binary Search on sorted-rotated array with unique numbers
- [0153]: find min in rotated array without duplicate
- [0154]: find min in sorted-rotated array with duplicate numbers
- [0240]: 2D binary search element
- [0081]: rotated array with duplicate
- [0373]: <span style="color:red">**pair-sum:**</span> kth-smallest pair sum from two sorted array (<span style="color:red">**pair sum can be constructed as sorted matrix**</span>)
- [0373] - (719, 1918, 2040)
- [0378]: kth-smallest value in sorted matrix
- [0668]: <span style="color:red">**pair-product:**</span>kth-smallest value in sorted matrix. Binary Search on two dimentional table (multiplication table)
- [0719]: <span style="color:red">**pair-diff:**</span> Pairs of an array (so you can sort, since we need to make pairs), find kth smallest pair distance
- [1918]: kth smallest subarray sum
- [2040]: <span style="color:red">**pair-product:**</span> kth smallest product of two sorted array
  - [1918]
- [2439]: is feasible for a max num in an array

  - What is the min-max value after some operations? -> guess the number and check feasible
    > Binary Search on Pairs

- [0373]: <span style="color:red">**pair-sum:**</span> kth-smallest pair sum from two sorted array (<span style="color:red">**pair sum can be constructed as sorted matrix**</span>)
- [0668]: <span style="color:red">**pair-product:**</span>kth-smallest value in sorted matrix. Binary Search on two dimentional table (multiplication table)
- [0719]: <span style="color:red">**pair-diff:**</span> Pairs of an array (so you can sort, since we need to make pairs), find kth smallest pair distance
- [1918]: kth smallest subarray sum
- [2040]: <span style="color:red">**pair-product:**</span> kth smallest product of two sorted array

> Binary Search - Two dimentional
> Binary Search by Value

# [`Binary Index Tree (BIT)`]

```yaml
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

```yaml
- When dealing with subsequence and order doesn't matter (only care about max/min-1498), we can sort
- consider adding dummy at beginning/ending of the array
- you can loop by the array or loop by all letters (the diff btn num vs string)
- or when dealing with string, you might want to loop lower-case chars instead by index of string
```

```yaml
- Pattern: looking for some metrics of all sub-arrays, sub-sequences
- All sub-arrays is O(N^2)
- We should pre-calc info for each element and bring down the time complexity

>> example matrics:
- min*sub-arr-sum (H)

```

```yaml
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

# [`Divide and Conquer`]

```yaml
 # divide & conquer: what is the clue?
  - asking to calc something that is relating to how many is smaller than self before/after
  - accumulate some statistics (cost based on some cost function, count per some criteria)
  - The statistics has to do with each element's relationship with other elements in the array
  - when dealing with statistics with respect to relations - divide and conquery

# Divide & Conquer framework:
  - partition the original and merging two sorted list while accumulating the statistids
  - binary search before merging two sorted list
  - operating on two lists: original and sorted
  - merge two sorted list

A: [x x x x x x x] //break the original array into two (divide)
B: [Y Y Y Y]
C: [Z Z Z]

1. recursively equally partition the original array
2. solve the problem in each subarray
3. before returning to previous stack, sort the subarray
4. solve the problem with two solved-subarray (leverage binary search per previous sort)

# Time: N*logN*logN
```

- [0315]: count right smaller than self
  - Given an list, count right smaller than self
  - > Reverse the list and count left smaller than self
  - > return reverse of the result
- [0327]: Given a list, count range sum in [lower, upper]
  - convert the list to presum (also a list)
  - sum[ii:jj] in [lower, upper]
  - > lower <= presum[jj]-presum[ii-1] <= upper
  - > presum[ii-1] >= presum[jj]- upper
  - > presum[ii-1] <= presum[jj] - lower
  - > traverse left and two binary search the right to count the range
  - Number of (ii, jj) pairs that satisfies some range sum criteria
- [0493]: count pairs where 2bj > ai
  - This is almost the same as 315 but change the right smaller to 2Xright smaller
  - Number of (ii, jj) pairs that satisfies some relationship
- [1649]: count total cost where cost = min(smaller, greater)
  - first find left smaller
  - after we have the list of left smaller, right bigger=len-equal-smaller
  - cost = min(left smaller, right bigger) and accumulate the total cost

# [`Design`]

```yaml
- [0146]
* [0155]
- [0355]: Design Twitter
  - push or pull model
* [0380]
* [0381]
* [0432]
* [0460]
* [0535]
* [0588]
* [0622]
* [0631]
* [0642]
* [0895]
* [1146]
- [1172]
- [1268]
- [1352]:
  - product of last k (how to handle zero)
- [1381]:
  - increment all (range addition)
- [1622]:
  - 逆源 (inverse)
  - API for addAll and multiplication
- [1670]
- [2166]
- [2296]
```

# [`DFS`]

```yaml
- memo (lru_cache) is the best friend of DFS
```

```yaml
# The Island counts, The 3 Island count variation
- [0200]
  - count islands surround by water/sea -> marking (1)<land> as visited and count
  - islands can reach edge
- [1020]
  - Count enclosed "Cells"
  sol1. fill all edge 1s as zero. count number of 1s
  sol2. accumulate DFS counts

- [1254]
  - Islands cannot reach edge
  - count islands where must be surrounded by water (edge doesn't count) -> all 4 directions cannot reach water or edge
```

- [2597]: can you try 2638 by DFS?

```yaml
- Counting: for each element, you can either take or no-take based on some condition.  when reaching the end, we return 1
```

```yaml
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

# [`DP`][`Dynamic Programming`]

> Type I (Basic): Single Array Find Max/Min of something with a sub-array

- O(N): one loop
- Space O(1) passible: dp[ii]
- only depends on dp[ii-1]
- prev state (dp[ii-1]), could be two consequted elements (276-paint fence)
- when using space O(1) strategy, be careful setup tmp variable to avoid states interfering each other

```
- template:
    Kadane: dp[ii]=max(nums[ii], dp[ii-1]+nums[ii])
         -> one previous state
  house robber: dp[ii] = dp_rob/dp_no_rob
         -> two previous state
  buy/sell stock III: bought1, sold1, bought2, sold2
         -> 4 previous state

- only need one state variable for DP type I
- use tmp vars for state transition
```

```yaml
dp[ii][jj]:   iith round, state jj
dp[ii][jj] = dp[ii-1][jj]+something
- Today's state can be derived from Yesterday's states
```

```yaml
- [0053]: Kadane                       -> max subarray sum a list of number
                                       * two states: dlp[ii-1] > nums[ii] or not
                                       * prev state = dp[ii-1] (max subarray sum ending @ ii-1)
                                       * condition, dp[ii-1]+nums[ii] > nums[ii] ?
- [0123]:
    Best Time Buy Sell Stock III       -> max profit buy/sell stock twice in timeseries
                                       * 4 states bought1, sold1, bought2, sold2
                                       * current 4 states depends on prev 4 states

- [0198]: House Robber I               -> max profit robing a row of house
                                       * 2 states, rob, no rob
- [0213]: House Robber II              -> max profit robing a ring of house
                                       * two states (rob, no_rob)
                                       * two scenarios
                                         1. rob first + no_rob_second + no_rob_last)
                                         2. no_rob_first
                                       * return the max(scenario1, scenario2)
- [0256]: Paint House                  -> min cost painting a row of house
                                       * two states: cannnot be same color as prev house
                                       * k-1 choice of colors
- [0276]: Paint Fence                  -> number of ways to achive something
                                       * states is two elements in a row (same, diff)

- [0309]
- [0376]
- [0487]
- [1186]
- [1289]
```

```yaml
# Number of subsets from an array with some constrains
- [0198]: max profit from an array s.t. you cannot rob two consequtive houses
- [2222]: two kinds of buildings, need to select 3 buildings s.t. no two consequtive buildings are with same types
  - jj is the num of buildings currently we are selecting (0, 1, 2, 3)
  - current_building_type
  - current_building_idx
- [2638]: after grouping, no subset with pair of numbers with abs(diff)=k
```

> To-do or Not-to-do (State Design)

- you can exercise one strategy (buy/sell stock) => states=(tke, ntk)

- [487]
- [1186]

> Type II (Basic enhanced): Time Series 2

```yaml
- O(N^2): two loops, ii, and jj < ii
- today's state can be derived from one of the JJ where jj < ii
- how to leverage stk to find jj?
  - 2297, 2355: leverage monotonic stack to find dp[jj] and reduce time to o(N)
```

```yaml
- [0300]: Longest Increasing Subsequence -> subsequence (order matters)
  - Best NlogN
  - [0673] -> subsequence count
  - prev state @ jj where nums[jj] < nums[ii]
- [368]: Largest Divisible subset        -> subset (order doesn't matter)
  - nums[ii]%nums[jj]==0
- [1105]: Filling Bookcase Shelves       -> minimize the max of all the subarrays
  - prev state (prev level of book-shelf) is prev, book for first book @ current_level.
  - try jj < ii until we exceed max width
  - ii-1 is the jj
  - find the min(ttl_height) for each prev jj
- [2297]:
  - dp[ii]=min(dp[jj]+costs[ii])
  - where jj is prev higher or lower
  - if we traverse backward from ii looking for min dp[jj] -> O(N^2)
  - leverage monotonic stack to maintian prev_higher, perv_lower
- [2355]: O(N^2) but leverage monotonic stack to reduce to O(N)
  - Max books you can take from a bookshelf
  - find hte prev that is not as expected
  - dp[ii] = dp[jj] + arithmatic_sum (jj is the prev smaller than expected)

```

> Type III: Two sequences

```yaml
- Longest Common Subsequences
- Shortest Common Supersequence
- Edit Distance

-> dp[ii][jj]: s[1:iii], t[1:jj]
   dp[ii][jj] = from dp[ii-1][jj], dp[ii][jj-1], dp[ii-1][jj-1]
-> return dp[-1][-1]
```

- [72]: \*Edit Distance
- [97]: Interleaving String
- [115]: Distinct Subsequences
- [727]: Minimum Window Subsequence
- [1092]: \*Shortest Common Supersequences
  - How to trace back the optimal solution (display path)
- [1143]: \*Longest Common Subsequences
  - [0583]: \*delete to make the same
  - [0072]: \*edit s1 into s2

> > LCS/SCS Variation

- [583]: Delete Operation for two strings
- [712]: Minimum ASCII Delete Sum for Two Strings
- [1035]: \*Uncrossed Lines (LCS)
- [1216]: Valid Palindrome III
- [1312]: Minimum Insertion Steps to Make a String Palindrome

> Type IV: Type I Intervals

- [0410]: Split Array Largest Sum
- [0813]: Largest Sum of Averages
- [1278]: Palindrome Partitioning III
- [1335]: Minimum Difficulty of a Job Schedule

> Type V: Type II Intervals

- [312]: Burst Balloons
- [375]: Guess Number Higher or Lower II
- [516]: Longest Palindromic Subsequence
- [1246]: Palindrome Removal

> Type VI: Knapsack

[[背包九讲] - Article)](https://www.cnblogs.com/jbelial/articles/2116074.html)  
[[背包九讲] - video I](https://www.youtube.com/watch?v=nleY0-eexps)
[[背包九讲] - video II](https://www.youtube.com/watch?v=0Jp4p0uO7Dw)

```yaml
1. 01 背包问题（选或不选）
2. 完全背包问题 （同物可选无限次）
3. 多重背包问题 （每个物品有不同限制）
4. 混合背包问题
5. 二维费用背包问题 （体积加重量限制）
6. 分组背包问题 （每组物品只能选一件）
7. 背包问题求方案数 （通常问max profit, min cost.  这里问方案数）
8. 求背包方案 （print the path)
9. 有依赖的背包问题 （each item has dependency/prerequisite）
```

````yaml
# review of [0494: target sum] VS [2518: num of great partition]
> classic knapsack
```python
'''
* given list of items
  - w[ii]= weight of item ii
  - value[ii] = value of item ii
  - capacity is the max allowed ttl weight
=> max value we can carry
'''

  """
  Given:
  a. capacity
  b. list of items s.t.
      b1. weights[ii]
      b2. values[ii]
  => max value one can carry

  capacity   0   1   2   ...   Capacity
  0
  n1
  n2
  n3
  .
  .
  .

  dp[ii][jj]: the max value one can carry upto item ii and capacity jj
  """
def find_max_knapsack_profit(capacity, weights, values):
    weights=[0]+weights
    values = [0]+values
    M=len(weights)
    N=capacity+1
    dp=[[0]*N for _ in range(M)]

    for ii in range(1, M):
        for w in range(1, N):
            #not taking

            ntk = dp[ii-1][w]

            #taking
            tke=0
            if w-weights[ii]>=0:
                tke= dp[ii-1][w-weights[ii]]+values[ii]

            dp[ii][w]=max(ntk, tke)

    return dp[-1][-1]


````

- list of nums
- constrain: ttl capacity
- action: add or ignore
  => max value
  capacity 0 1 2 ... capacity
  0
  n1
  n2
  .
  .

> 494:

- list of nums
- constrain: expression value
- actions: add to ttl or substrack to ttl
  => count number of ways sum to target
  target sum 0 1 2 ...target_sum+offset
  0
  n1
  n2
  .
  .
  .

> 2518:

- list of nums
- constrain: group
- actions: add or ignore (ignore goes to group 2)
  => number of ways both group sum > k
- ttl ways count: power(2, k)
- when ttl_sum < 2\*k --> return 0 (unable to partition to two groups both sum greater than k)
  --> here we have ttl > 2k, ie. when group1_sum < k --> group2_sum will be > k
- valid ways count: ttl_count - group1_invalid_count\*2

required_k 0, 1, 2,..., k-1 (we don't need k as we will use ttl to sustrace invalids)
0
n1
n2
.
.
.

- when we have two symmetric groups. and know the ttl outcome space (ttl count), think of use ttl to substrack invalids to derive valid counts.

````

- [0474]: Ones and Zeroes
- [0494]: Target Sum
  - [2518]
- [0879]: Profitable Schemes
- [0956]: Tallest Billboard
- [1049]: Last Stone Weight II
  * 穷举法 （exhaustive method)

> Type I and Type II Interval DP

- [1000]: Minimum Cost to Merge Stones (most difficult DP)

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

> Greedy mental model

```yaml
- not search, not exhaustive method, not DP, only by heuristic performing a optimized strategy from ii=0~n-1
- always choose the local optimal solution and reach the global optimal solution
- current sub-optimal solution cannot become global optimal solution with future decisions

1. Guess a solution (might or might not be the optimized solution)
2. try to adjust the guessed solution (applying some kind of greedy strategy) and observe if a greedy strategy can solve the problem

````

> Greedy classics

- Huffman
- Dijkstra (shortest distance) - min steps to reach goal
- Prim (MST)
- Kruskal

> Greedy: min steps/stops to reach goal

```yaml
- Can you reach the goal? (on each move, move to a spot that you can reach the furthest - a local optimal solution)
- min refuel to reach the goal? (on each refuel, choose the refueling stop that provides the most fuel)
- fixed resource with options, how far can you go?
```

- [0134]: can you reach the end?

  - failure condition
  - greedy, find the first positive start (since unique solution, we cannot end at postive -> ending @ zero)

- [0871]: min refueling stops

> Greedy-distribution given constrains

```yaml
- Give a list of array and some limited resource and constrains.  Distribute the resources without violating the constrains to optimize some objectives
- Start from analyze the objective function see if we can come up with some greedy heuristic for the optimization
```

- [0135]:
- [1840]:
  - two passes, the 2nd pass does not break first pass
- [2233]:
- [2234]:

  > Greedy-arrangment

```yaml

- given a list of task (each task represented by a char)
  given a string with duplicate chars
- Given a K such that each char (task) need to have the gap/idle in order to process same task again
  """
  ex: Given: A A B C C D D D ..
  """
- if gap=1 -> special handling O(N) calc
- if we do not present the path, we can do O(N), just calc
- Can you finish all? (when len(mxq) < k and mxq[0][0] < 1)
- Min cycle required to complete if allowing idle? (when len(tmp)==0 + k else + N)
- max cycle we can do until we cannot honor the rule? (1953)
```

- [0042]: trapping rain water
- [0045]: Jump Game II: min steps to reaach the end
- [0055]: Jump Game: can you reach the end
- [0134]:
  - Gas station - condition of no solution - sum(gas)-sum(cost) < 0
- [0135]
- [0358] (arrangement) - not allowing idle

  - VS [0621]: allow idle
  - k is flexible
  - if cannot complete, return "" => how do you identify failure condition
  - how do you identify last round?

- [0435] interval, remove the one ending the longest when overlapping
- [0621] (arrangement): if cannot honor gap, fill with idle
  - VS [0358]: not allowing idle
  - k is flexible
  - if cannot complete, allow idle
  - How do you identify last round?
- [0767] (arrangement): chars
  - VS [1054]
  - VS [1953] do not need to output path, only calc
  - need to output
  - k=1 -> special odd/even solution
  - return "" if not possible -> how do you check if not possible?
- [0871] min refueling top
- [0881]
- [0995]: if already in place, just skip to avoid redo
- [1029]
- [1054] (arrangement): ints
  - VS [0767]
  - k=1 -> spacial odd/even solution
  - guarantee has answer
- [1642]:
  - use option 1 by default and replace with option 2 when needed
- [1723]: This is a DP (assigning N tasks to K workders). place here for comparison
- [1840]
- [1846]
- [1953] (arrangement)

  - VS [0621]: k is flexible
  - k=1
  - how far you can go without breaking rules?
  - when do we start to break?
  -

  ```yaml
  We can only apply this strategy when

  1. k=1
  2. do not need to output the path
  ```

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

```yaml
# some trics
* if not indexing from 0, insert a dummy starting element

# condition of swap
while ii != nums[ii] and nums[ii] < N and nums[ii] != nums[nums[ii]]:
a. element not matching it's own index
b. element value is not out-of-bound so we can swap
c. element value is not equal to the destination value or no point of swapping
```

# [`Intervals`]

> when do you sort by beginning point

- -> the min number of intervals to cover the whole range

> when do you sort by ending point

- -> relating to overlap
- -> the max number of non-overlapping intervals

  > 1. 50%: Sweep line
  > 2. 40%: Greedy
  > 3. 10%: DP
  >
  > - typically need to sort
  > - the initial (cs, ce)=(-math.inf, -math.inf) or intervals[0]?

- [0056] merge interval
- [0057] insert inverval
- [0435] min remove so no overlap
- [0986] intersect of interval from two sorted list of intervals
- [0621]
- [0252] Meeting-Rooms: can attent all meetings?
- [0253] Meeting-Rooms-II: min meeting room required
- [0370] Range-Addition: sweep line
- [0495]
- [0759] Employee-Free-Time (M+)
- [0763]
- [0798] Smallest-Rotation-with-Highest-Score (H)
- [0995] Minimum-Number-of-K-Consecutive-Bit-Flips (H-)
- [1024] min to cover range. same as 1326
- [1326] min to cover range. same as 1024
- [2345] (Google)
- [2589] (start, end, duration), merge all overlapping intervals and return cnt

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

```yaml
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

# [`Parentheses`]

```yaml
- Stack
- Greedy
```

- [0022]: generate parentheses
- [0032]: longest valid parentheses substring
- [0301]: all valid strings by removing minimum # of Parentheses
- [0921]: num of minimum remove to make valid parentheses
- [1249]: any valid strings by removing minimum num of paren

- [021]
- [1541]
- [1963]
- [678]
- [2116]

# [`Parse Expression`][`String Parsing`]

- [0394]
- [0224] basic Calculator

# [`Quick Select`]

> when you search for number, we can use quick-select. otherwise, try binary search

- [0215] Kth-Largest-Element-in-an-Array (M)
- [0324] Wiggle-Sort-II (H)
- [0347] Top-K-Frequent-Elements (M+)
- [0973] K-Closest-Points-to-Origin (M)

# [`Segment Tree`]

```yaml
- find range sum
- `binary index tree` is subset of `segment tree`
- less coding for `binary index tree`, otherwise, `segment tree` can cover
```

- [0307] Basic
- [0370]

# [`Sliding Window`]`

[1151]

```yaml
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

# [`Stack`]

```yaml
* Validate stack
* Validate Parentheses
* validate a sequence of something
* match start, end on a single CPU
* match parenthesis
* match adjacent chars
* simulating a text cursor moving back and forth, append, delete
```

- [0946]

# [`Subset, Subarray, Subsequence`]

- Subsequence -> DP (Longest increasing subsequence, Longest Common Subsequence)
- Subarray -> Monotonic Stack, presum, presum2
- Subset -> you can group and sort

- [0039]

# [`Sweep Line`]

- When we use Sweep Line, we only consider sets of starting points and ending points, we do NOT know which starting point matching with which ending point.

- [0995]

# [`TopK elements`]

1. sort: NlogN
2. Heap/PQ: Nlogk
3. Binary Search: 32N
4. Quick select: AVG O(N)
5. bucket_sort (for top k freq)

> The kth smallest element of an unsorted array
> The medium of two sorted array

```yaml
### When we see pair
1. sorted matrix strategy
```

- [215]: be careful top k largest VS top K smallest

# [`Topology Sort`]

- [0207]
- [1591] Strange Printer

# [`Trie`]

```yaml
- something relating to searching words
- something relating to building dictionary
```

- [0139]
- [0642]:
  - search char input one-by-one -> need to record current and reset when we receive '#'
  - output need to sort per (freq, lexical order)
- [1268]:
  - search word is given, and output sort lexically only

```yaml
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

```yaml
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

# [`Union Find`][`并查集`]

```yaml
* grouping connected nodes
```

- [0547]\*
- [0684]\*
- [0990]
- [0924]
- [1202]
- [0952]
- [0947]
- [0721]
- [0685]

-[0128]

# Series

# [`Buy Sell Stock`]

- [0121] I: buy sell once
  - max of current - prev_min
  - find the global max diff
- [0122] II: buy sell unlimited with 1 share
  - accumulate all postive diff
- [0123] III: buy sell twice
- [0188] IV: buy sell k times

# [`basic Calculator`]

- [0224] basic calculator I: num+paren
- [0227] basic calculator II: +-\*/ (no paren)
- [0772] basic calculator III: +-\*/ with paren
- [0770] basic calculator IV: +-\*/ with paren, with e

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

# [`Optimization`]

1. Binary Searcy by Value (with count)
2. Dynamic programming
3. Greedy

# [`Word Search`]

- [0079]: given a word and a grid, return true/false if the word is in the grid
  - backtrack -> no memo
- [0212]
-

# [`Word Break`]

- [139]: Word Break I: given a word, can it be composed by a given dictionary
- [140] Word Break II: set/Trie is your friend
- [472] Concatenated Words

# [`Concatenated Word`]

- [0472]

# [[`Word Ladder`]](https://github.com/1688168/Leetcode/blob/main/LC/%5B0126%5D%20Word%20Ladder%20II.md)

- [126]: Word Ladder II: From BeginWord to EndWord all, output all valid path
  - BFS to find the shortest distance
  - DFS with backtrack to find all valid path that is with shortest distance (word searh with defined length)
- [127]: Word Ladder I: Is existing from BeginWord to EndWord
  - BFS find the shortest distance

# [[`Complete All Tasks`]]()

- [1723]
  -> Given N tasks, K workers => find min threshold time each worker can work to complete all tasks

- [1986]
  -> Given N tasks, 1 worker, session_time => find min num of sesstions to complete all tasks  
  --> Given N tasks, sessiton_time (threshold) => min num of workers you need to work concurrently to complete all tasks

- [2589]
  -> Given a CPU and a list of tasks, where each task is (start, end, duration) and CPU can process unlimited tasks in parallel => find min uptime  
  -> Given a list of intervals (start, end, duration) where duration can be partitioned. => merge all durations and count num of non-overlapping durations (intervals) after merge  
   ** [2589] Strategy 1: range of (start, end) is given  
   ** [2589] Strategy 2: range of (start, end) is unknown
