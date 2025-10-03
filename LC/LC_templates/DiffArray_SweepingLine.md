# <center><b><span style="color:orange">Diff Array, Sweeping Line</span></b></center>

> # <b><span style="color:purple">Pattern</span></b>
* you will be givne list of (start, end).  We will model those timestamps into (start, 1), (end, -1) as events
* To sort the events, we can leverage Java-treeMap to maintain order
* asking Interval Merge: when sum==0 -> we complete interval merge
* asking count of Interval intersect -> each new event, we update max so far
