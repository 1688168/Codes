1. sort the whole array: NlogN
2. PQ: rolling K Max element: NlogK
3. Binary Search by Value: O(N \* logC)
   Guess T: if contNum(>=t) >= k => adjust bigger
   < k => adjust smaller
   Binary Search => the largest t s.t. satisfy condition
   array => the kth largest element is the larget t s.t. satisfy condition

   => the binary search result is in the array

4. Quick Select
