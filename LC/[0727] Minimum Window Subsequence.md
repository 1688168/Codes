> Naive solution (two pointer)+Greedy
* Time: S*(M+N) --> similar to DP solution
* find a starting point, always look for 1st next char in order to achieve min len

> Finite state machine strategy+Greedy

* preprocess next[ii][ch]: look right from position i, the nearest index of ch
* Time: S*N + (26*N)
  where next will take 26N, and we will do S*N look (S should be much smaller than M)


```cpp


```



> DP III - two series counting/optimization
* Time - M*N