# <center><b><span style="color:orange">DP I</span></b></center>

> # <b><span style="color:purple">Type I definition (no constrain)</span></b>
1. Given an int/string array, optimize something 
2. current state(s) (the optimized answer) can be derived from previous state(s)
3. Or currents (optimal) state can be derived from previous states

> # <b><span style="color:purple">Type I definition (with constrain)</span></b>
* House robber -> you can make a decision on current state (pick/skip) based on previous state
* partition the state into two pick/skip states whenver you need to make a decision

> # <b><span style="color:purple">The Pattern</span></b>
1. define the base case
2. define the current state(s)
3. identify what are the requried prevous state(s) to derive current state(s)
4. for DP I, we do NOT need to record "ALL STATES", but just the require previous state(s)  -- (DP II, needs to record all states)
5. think about DFS

> # <b><span style="color:purple">Examples</span></b>

* [0070] - climing stairs
  * depends on prev and prevprev
* [0123] - buy sell stock III
  * 
* [0509] - Fibonacci Number
  * depends on prev and prevprev


