1. sort the whole array: NlogN
2. PQ: rolling K Max element: NlogK
3. Binary Search by Value: O(NlogC)
   Guess T: if contNum(>=t) >= k => adjust bigger
   < k => adjust smaller
   Binary Search => the largest t s.t. satisfy condition
   array => the kth largest element is the larget t s.t. satisfy condition

   => the binary search result is in the array

4. Quick Select: avg O(N), worst O(N^2)


| Approach | Time | Extra space | How it works |
|---|---|---|---|
| Sort | `O(n log n)` | Depends on the sorting algorithm | Sort ascending and return `nums[n - k]`. |
| Min-heap of size `k` | `O(n log(k + 1))` worst case | `O(k)` | Keep the `k` largest elements seen so far. The root is the answer. |
| Max-heap of all elements | `O(n + k log n)` worst case | `O(1)` with iterative, in-place heap operations, `O(n)` if copied | Heapify in `O(n)`, then pop `k` times. |
| Randomized Quickselect | `O(n)` expected, `O(n²)` worst case | `O(1)` with iterative, in-place partitioning | Partition around a pivot and continue on the side containing index `n - k`. |
| Binary search on values | `O(n log(R + 1))` | `O(1)` | Find the largest value `x` for which at least `k` elements are `≥ x`. |

`n` is the array length, and `R = max(nums) - min(nums) + 1` is the size of the integer value range.