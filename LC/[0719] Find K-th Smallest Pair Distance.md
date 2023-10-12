### When we see top K
1. sort
2. heap
3. quick-sort
4. Binary Search with count

### When we see pair
1. sorted matrix strategy
   
### High level coding structure
```
1. sort the array: O(nlogn)
2. define the distance range from the sorted array: O(N)
3. Binary Search within the defined range in step2 (O(32))
4. given a mid (the kth smallest distance)
   n1 n2 n3 ... nk
   all numbers from n1 ~ n1+mid are with distance <= mid
   bisect to find the right hand number index and count how many distances <= mid

5 if count >= k -> guessed too high
          else  -> guessed too low
```


