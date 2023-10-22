> The kth element of n sorted list

    XXXXXX
    YYYY
    ...
    ZZZZZZZZ

> if we use heap

- heappush: logN
- Time: logN\*ttl_nodes

> The kth element of two sorted arrays

- if we take k/2 elements from each list
  x x x0 x x x
  y y y y0 y y y y y y

- assume x0 < y0
  => there are k-1 elements < y0

- in next iteration: take (k-k/2)
  x x x
  y y y y0 y y y y y
