> Naive solution (two pointer)+Greedy
* Time: S*(M+N) --> similar to DP solution
* find a starting point, always look for 1st next char in order to achieve min len

> Finite state machine strategy+Greedy

* preprocess next[ii][ch]: look right from position i, the nearest index of ch
* Time: S*N + (26*N)
  where next will take 26N, and we will do S*N look (S should be much smaller than M)
* building state-machine: 
  * current state is built on top of previous state.
  * considering next: next[ii][ch] = next[ii+1][ch] and consider if s1[ii+1]
  * consider what's the known initial state and build next state from there.  the known initial state could be from s1[0] or s1[-1]
> DP III - two series counting/optimization
* Time - M*N