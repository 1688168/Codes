# <center><b><span style="color:orange">Jump Game V</span></b></center>

> # <b><span style="color:purple">DFS - O(N)</span></b>



> # <b><span style="color:purple">DP Solution - NlogN</span></b>
* where do we start? Since we can start from anywhere
* Does order matter? -> NO, if we can start from anywhere, what's the easiest starting point and we can make progress on top of that?
* DP is from previous state to next state.
* the lowest index cannot going anywere. -> max jump is 1
* if we know answer for lower bars -> we can solve higher bars

1. sort, so we go from low bar to high bar -> NlogN
2. from low to high -> N