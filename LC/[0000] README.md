# Path in a Tree

2538
2421
2246
124
2049
687
1522\*
543
2467

# Binary Search

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
[2702]

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

[0075] (sort color)(dutch national flag)
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

# Sliding Window

[1151]
532.K-diff-Pairs-in-an-Array (H-)
611.Valid-Triangle-Number (M+)
930.Binary-Subarrays-With-Sum (M+)
1004.Max-Consecutive-Ones-III (M)
1052.Grumpy-Bookstore-Owner (M)
1358.Number-of-Substrings-Containing-All-Three-Characters (M)
1838.Frequency-of-the-Most-Frequent-Element (H-)
395.Longest-Substring-with-At-Least-K-Repeating-Characters (H)
1763.Longest-Nice-Substring (H)
2009.Minimum-Number-of-Operations-to-Make-Array-Continuous (M+)
2024.Maximize-the-Confusion-of-an-Exam (M)
424.Longest-Repeating-Character-Replacement (H-)
2106.Maximum-Fruits-Harvested-After-at-Most-K-Steps (H)
2401.Longest-Nice-Subarray (H-)
2411.Smallest-Subarrays-With-Maximum-Bitwise-OR (H-)
2516.Take-K-of-Each-Character-From-Left-and-Right (M+)
2564.Substring-XOR-Queries (H-)
2730.Find-the-Longest-Semi-Repetitive-Substring (M+)
2747.Count-Zero-Request-Servers (H-)
2831.Find-the-Longest-Equal-Subarray (M)
Sliding window : Distinct Characters
076.Minimum-Window-Substring (M+)
003.Longest-Substring-Without-Repeating-Character (E+)
159.Longest-Substring-with-At-Most-Two-Distinct-Characters(H-)
340.Longest-Substring-with-At-Most-K-Distinct-Characters (H)
992.Subarrays-with-K-Different-Integers (H-)
2461.Maximum-Sum-of-Distinct-Subarrays-With-Length-K (M)
2537.Count-the-Number-of-Good-Subarrays (M+)
Two pointers for two sequences
986.Interval-List-Intersections (M)
1229.Meeting-Scheduler (M+)
1537.Get-the-Maximum-Score (H-)
1577.Number-of-Ways-Where-Square-of-Number-Is-Equal-to-Product-of-Two-Numbers (H-)
1775.Equal-Sum-Arrays-With-Minimum-Number-of-Operations (M+)
1868.Product-of-Two-Run-Length-Encoded-Arrays (M+)
2098.Subsequence-of-Size-K-With-the-Largest-Even-Sum (M+)

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

[2297 - M - Jump Game VIII](https://github.com/1688168/Leetcode/blob/main/LC/%5B2297%5DJumpGameVIII.py) - https://www.youtube.com/watch?v=II7tWDuY7yE

- DP + monotonic stack
- [1944] https://www.youtube.com/watch?v=oV-HvcHogyk
- [2282] https://www.youtube.com/watch?v=AgC28b_0ekM

  264.Ugly-Number-II (H-)
  313.Super-Ugly-Number (H-)
  091.Decode-Ways (M)
  639.Decode-Ways-II (H)
  634.Find-the-Derangement-of-An-Array (H)
  823.Binary-Trees-With-Factors (M+)
  221.Maximal-Square (H-)
  1277.Count-Square-Submatrices-with-All-Ones (M+)
  600.Non-negative-Integers-without-Consecutive-Ones (H)
  656.Coin-Path (H-)
  818.Race-Car (H)
  377.Combination-Sum-IV (M)
  837.New-21-Game (H-)
  887.Super-Egg-Drop (H)
  1884.Egg-Drop-With-2-Eggs-and-N-Floors (H-)
  920.Number-of-Music-Playlists (H)
  940.Distinct-Subsequences-II (H)
  1987.Number-of-Unique-Good-Subsequences (H)
  446.Arithmetic-Slices-II-Subsequence (H-)
  1027.Longest-Arithmetic-Sequence (M+)
  1269.Number-of-Ways-to-Stay-in-the-Same-Place-After-Some-Steps (M+)
  1316.Distinct-Echo-Substrings (M+)
  1420.Build-Array-Where-You-Can-Find-The-Maximum-Exactly-K-Comparisons (H-) 1444. Number of Ways of Cutting a Pizza (TBD)
  1531.String-Compression-II (H+)
  1575.Count-All-Possible-Routes (M+)
  1621.Number-of-Sets-of-K-Non-Overlapping-Line-Segments (H)
  1639.Number-of-Ways-to-Form-a-Target-String-Given-a-Dictionary (H-)
  1692.Count-Ways-to-Distribute-Candies (H-)
  1787.Make-the-XOR-of-All-Segments-Equal-to-Zero (H)
  1872.Stone-Game-VIII (H-)
  1900.The-Earliest-and-Latest-Rounds-Where-Players-Compete (H)
  1937.Maximum-Number-of-Points-with-Cost (H-)
  1955.Count-Number-of-Special-Subsequences (H-)
  2088.Count-Fertile-Pyramids-in-a-Land (H-)
  2140.Solving-Questions-With-Brainpower (H)
  2189.Number-of-Ways-to-Build-House-of-Cards (H-)
  2218.Maximum-Value-of-K-Coins-From-Piles (H-)
  2222.Number-of-Ways-to-Select-Buildings (M+)
  2312.Selling-Pieces-of-Wood (M+)
  2338.Count-the-Number-of-Ideal-Arrays (H)
  2431.Maximize-Total-Tastiness-of-Purchased-Fruits (M+)
  2484.Count-Palindromic-Subsequences (H-)
  2713.Maximum-Strictly-Inreasing-Cells-in-a-Matrix (H-)
  2787.Ways-to-Express-an-Integer-as-Sum-of-Powers (M+)
  2809.Minimum-Time-to-Make-Array-Sum-At-Most-x (H)
  2826.Sorting-Three-Groups (M)

基本型 I
198.House-Robber (E)
213.House-Robber-II (M+)
2597.The-Number-of-Beautiful-Subsets (H)
2638.Count-the-Number-of-K-Free-Subsets (M+)
2320.Count-Number-of-Ways-to-Place-Houses (M+)
1388.Pizza-With-3n-Slices (H-)
276.Paint-Fence (H-)
265.Paint-House-II (H)
1473.Paint-House-III (H-)
376.Wiggle-Subsequence (H-)
123.Best-Time-to-Buy-and-Sell-Stock-III (M+)
188.Best-Time-to-Buy-and-Sell-Stock-IV (H)
309.Best-Time-to-Buy-and-Sell-Stock-with-Cooldown (H-)
714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee (M+)
514.Freedom-Trail (H-)
740.Delete-and-Earn (H-)
552.Student-Attendance-Record-II (H)
801.Minimum-Swaps-To-Make-Sequences-Increasing (M)
1223.Dice-Roll-Simulation (H-)
1262.Greatest-Sum-Divisible-by-Three (M+)
1363.Largest-Multiple-of-Three (H)
1419.Minimum-Number-of-Frogs-Croaking (M)
1548.The-Most-Similar-Path-in-a-Graph (M+)
1746.Maximum-Subarray-Sum-After-One-Operation (M+)
1824.Minimum-Sideway-Jumps (M)
1839.Longest-Substring-Of-All-Vowels-in-Order (M)
1883.Minimum-Skips-to-Arrive-at-Meeting-On-Time (H)
2036.Maximum-Alternating-Subarray-Sum (M+)
2143.Choose-Numbers-From-Two-Arrays-in-Range (H)
2318.Number-of-Distinct-Roll-Sequences (H-)
2361.Minimum-Costs-Using-the-Train-Line (M+)
2786.Visit-Array-Positions-to-Maximize-Score (M)
基本型 II
368.Largest-Divisible-Subset (M+)
300.Longest-Increasing-Subsequence (M+)
673.Number-of-Longest-Increasing-Subsequence (M+)
960.Delete-Columns-to-Make-Sorted-III (H-)
983.Minimum-Cost-For-Tickets (H-)
1043.Partition-Array-for-Maximum-Sum(M+)
1105.Filling-Bookcase-Shelves (H-)
1959.minimum-total-space-wasted-with-k-resizing-operations (H-)
2052.Minimum-Cost-to-Separate-Sentence-Into-Rows (H-)
1416.Restore-The-Array (M+)
1546.Maximum-Number-of-Non-Overlapping-Subarrays-With-Sum-Equals-Target (M+)
1626.Best-Team-With-No-Conflicts (M)
1691.Maximum-Height-by-Stacking-Cuboids (H)
2188.Minimum-Time-to-Finish-the-Race (H-)
2209.Minimum-White-Tiles-After-Covering-With-Carpets (M+)
2430.Maximum-Deletions-on-a-String (M+)
2464.Minimum-Subarrays-in-a-Valid-Split (M)
2522.Partition-String-Into-Substrings-With-Values-at-Most-K (M+)
Interval
1235.Maximum-Profit-in-Job-Scheduling (H-)
1751.Maximum-Number-of-Events-That-Can-Be-Attended-II (H)
2008.Maximum-Earnings-From-Taxi (M+)
2830.Maximize-the-Profit-as-the-Salesman (M)
走迷宫型
120.Triangle (E)
174.Dungeon-Game (H-)
741.Cherry-Pickup (H-)
1463.Cherry-Pickup-II (M)
576.Out-of-Boundary-Paths (H)
931.Minimum-Falling-Path-Sum (M)
1289.Minimum-Falling-Path-Sum-II (M+)
1301.Number-of-Paths-with-Max-Score (M+)
1594.Maximum-Non-Negative-Product-in-a-Matrix (M)
2267.Check-if-There-Is-a-Valid-Parentheses-String-Path (H-)
2435.Paths-in-Matrix-Whose-Sum-Is-Divisible-by-K (M)
背包型
322.Coin-Change (M)
416.Partition-Equal-Subset-Sum (M+)
518.Coin-Change-2 (H-)
474.Ones-and-Zeroes (H-)
494.Target-Sum (M+)
805.Split-Array-With-Same-Average (H)
879.Profitable-Schemes (M+)
956.Tallest-Billboard (H)
1049.Last-Stone-Weight-II (H-)
1449.Form-Largest-Integer-With-Digits-That-Add-up-to-Target (H-)
1981.Minimize-the-Difference-Between-Target-and-Chosen-Elements (M+)
2291.Maximum-Profit-From-Trading-Stocks (M)
2518.Number-of-Great-Partitions (H-)
2585.Number-of-Ways-to-Earn-Points (M)
键盘型
650.2-Keys-Keyboard (M+)
651.4-Keys-Keyboard (M+)
935.Knight-Dialer (M)
1320.Minimum-Distance-to-Type-a-Word-Using-Two-Fingers (H)
To Do or Not To Do
487.Max-Consecutive-Ones-II (H-)
1186.Maximum-Subarray-Sum-with-One-Deletion (H-)
1187.Make-Array-Strictly-Increasing (H-)
1909.Remove-One-Element-to-Make-the-Array-Strictly-Increasing (H-)
区间型 I
132.Palindrome-Partitioning-II (H-)
410.Split-Array-Largest-Sum (H)
813.Largest-Sum-of-Averages (H-)
1278.Palindrome-Partitioning-III (H)
1335.Minimum-Difficulty-of-a-Job-Schedule (M+)
1478.Allocate-Mailboxes (H)
1977.Number-of-Ways-to-Separate-Numbers (H)
2463.Minimum-Total-Distance-Traveled (M+)
2472.Maximum-Number-of-Non-overlapping-Palindrome-Substrings (M+)
2478.Number-of-Beautiful-Partitions (H-)
2547.Minimum-Cost-to-Split-an-Array (M)
区间型 II
131.Palindrome-Partitioning (M+)
312.Burst-Balloons (H-)
375.Guess-Number-Higher-or-Lower-II (H)
471.Encode-String-with-Shortest-Length (H)
516.Longest-Palindromic-Subsequence (H-)
546.Remove-Boxes (H+)
664.Strange-Printer (H)
730.Count-Different-Palindromic-Subsequences (H)
1000.Minimum-Cost-to-Merge-Stones (H)
1130.Minimum-Cost-Tree-From-Leaf-Values (M+)
1246.Palindrome-Removal (H)
1039.Minimum-Score-Triangulation-of-Polygon (H)
1547.Minimum-Cost-to-Cut-a-Stick (M)
1682.Longest-Palindromic-Subsequence-II (H)
1690.Stone-Game-VII (H-)
1745.Palindrome-Partitioning-IV (M)
1770.Maximum-Score-from-Performing-Multiplication-Operations (H-)
双序列型
010.Regular-Expression-Matching (H)
044.Wildcard-Matching (H-)
097.Interleaving-String (H-)
072.Edit-Distance (H-)
115.Distinct-Subsequences (H-)
583.Delete-Operation-for-Two-Strings (M+)
712.Minimum-ASCII-Delete-Sum-for-Two-Strings (M+)
718.Maximum-Length-of-Repeated-Subarray (M)
727.Minimum-Window-Subsequence (H-)
1035.Uncrossed-Lines (M)
1092.Shortest-Common-Supersequence (H-)
1143.Longest-Common-Subsequence (M)
1216.Valid-Palindrome-III (M+)
1312.Minimum-Insertion-Steps-to-Make-a-String-Palindrome (M+)
1458.Max-Dot-Product-of-Two-Subsequences (M)
1771.Maximize-Palindrome-Length-From-Subsequences (H)
状态压缩 DP
465.Optimal-Account-Balancing (H)
691.Stickers-to-Spell-Word (H)
1125.Smallest-Sufficient-Team (H)
1349.Maximum-Students-Taking-Exam (H)
1411.Number-of-Ways-to-Paint-N×3-Grid (M)
1434.Number-of-Ways-to-Wear-Different-Hats-to-Each-Other (H-)
1659.Maximize-Grid-Happiness (H)
1681.Minimum-Incompatibility (H)
1723.Find-Minimum-Time-to-Finish-All-Jobs (H-)
1799.Maximize-Score-After-N-Operations (H-)
1931.Painting-a-Grid-With-Three-Different-Colors (M+)
1994.The-Number-of-Good-Subsets (H)
2184.Number-of-Ways-to-Build-Sturdy-Brick-Wall (H-)
2403.Minimum-Time-to-Kill-All-Monsters (M+)
2572.Count-the-Number-of-Square-Free-Subsets (H-)
枚举集合的子集
1494.Parallel-Courses-II (H)
1655.Distribute-Repeating-Integers (H)
1986.Minimum-Number-of-Work-Sessions-to-Finish-the-Tasks (M+)
2152.Minimum-Number-of-Lines-to-Cover-Points (H-)
带权二分图
1066.Campus-Bikes-II (H+)
1595.Minimum-Cost-to-Connect-Two-Groups-of-Points (H)
1879.Minimum-XOR-Sum-of-Two-Arrays (H)
1947.Maximum-Compatibility-Score-Sum (H)
2172.Maximum-AND-Sum-of-Array (H)
TSP
943.Find-the-Shortest-Superstring (H+)
2247.Maximum-Cost-of-Trip-With-K-Highways (H)
Catalan
096.Unique-Binary-Search-Trees (M+)
1259.Handshakes-That-Don't-Cross (M+)
Permutation
629.K-Inverse-Pairs-Array (H)
903.Valid-Permutations-for-DI-Sequence (H)
1866.Number-of-Ways-to-Rearrange-Sticks-With-K-Sticks-Visible (H)
Infer future from current
2044.Count-Number-of-Maximum-Bitwise-OR-Subsets (M)
2742.Painting-the-Walls (H)
maximum subarray
053.Maximum-Subarray (E+)
152.Maximum-Product-Subarray (M+)
2272.Substring-With-Largest-Variance (H-)
2321.Maximum-Score-Of-Spliced-Array (H-)

Time-Series
[0198] M : House Robber
[0123] : Best Time to Buy and Sell Stock III
[0213] : House Robber II
[0487]
[1186]
[1289]

# Design

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

# BFS

1591
1203
1857
2392
2204*
2115
802
310
2050
1136*
1462
210
207

# DFS

351*
2328
329
2305
1723
2313*
834
2322
2277\*

# Greedy

2055
524
1055*
792
2263*
2311
2332
2242
2350
2234
2333
2233
1405
984
621
358\*
1054
2335
1953
767

# Segment Tree

# Stack

[0032]

503
255*
496
1063*
85
84
145
94
144
636
456
173
1096
1087*
1106
1381
439*
726
591
385
772\*
227
224
42
856
844
1019
173
341
232
768
1209
1190
225
155

# Heap

[2519] - <215>: binary search, sortedcontainers

# Graph

# Quick Select

[0215] Kth-Largest-Element-in-an-Array (M)
[0324] Wiggle-Sort-II (H)
[0347] Top-K-Frequent-Elements (M+)
[0973] K-Closest-Points-to-Origin (M)

# Top K elements

1. sort: NlogN
2. Heap/PQ: Nlogk
3. Binary Search: Nlog C
4. Quick select: AVG O(N)

[215]
