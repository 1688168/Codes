# <center><b><span style="color:orange">Jump Game V</span></b></center>

> # <b><span style="color:purple">DFS - O(N)</span></b>



> # <b><span style="color:purple">DP Solution - NlogN</span></b>
* Dynamic programming is trying to find a current state, and via a tranformation function, we can move to next state.
* The current state could be prev index (house robber) or one of the previous index (Longest increasing subsequence), or an interval.
* in this problem, we can start from any index. (order doesn't matter -> sort)
* after sorting, what's the initial state we should choose? lowest bar or highest bar?
* from lowest bar, we have initial jump value as it cannot jump to anywhere.  so lowest bar jump count is 1.  from which, can we move on to 2nd lowest bar and so on so forth.
* where do we start? Since we can start from anywhere
* Does order matter? -> NO, if we can start from anywhere, what's the easiest starting point and we can make progress on top of that?
* DP is from previous state to next state.
* the lowest index cannot going anywere. -> max jump is 1
* if we know answer for lower bars -> we can solve higher bars

1. sort, so we go from low bar to high bar -> NlogN
2. from low to high -> N